from contaPezziLogic import logicCounter
import sys
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow
from PyQt5 import QtWidgets
from contapezzi_ui import Ui_contaPezzi
import time
from PyQt5 import QtGui, QtCore
from const import CUSTOMER_NAME, RED_GRADIENT, GREEN_GRADIENT
from datetime import datetime
from const import DEBUG, IN_PIN, MSG_EXIT, MSG, MSG_WARN_NO_HOUR

if not DEBUG:
    import RPi.GPIO as GPIO

class PieceCounterGui(QMainWindow):
    def __init__(self):
        self.dateNow = datetime.now().strftime("%Y-%m-%d")
        self.datePassed = datetime.now().strftime("%Y-%m-%d")
        self.red_gradient = RED_GRADIENT
        self.green_gradient = GREEN_GRADIENT
        self.lista_orari = []
        self.logic = logicCounter(self)
        QMainWindow.__init__(self, parent=None)
        super(PieceCounterGui, self).__init__()
        self.ui = Ui_contaPezzi()
        self.ui.setupUi(self)

        self.ui.btnChiudi.clicked.connect(self.btn_esci_click)
        self.ui.actionEsci.triggered.connect(self.btn_esci_click)
        self.ui.lbCliente.setText(CUSTOMER_NAME)

        self.ui.btnTest.clicked.connect(self.count_piece)

        self.ui.btnImposta.clicked.connect(self.btn_sethours_click)

        # Timer declaration to control changing day. Fired every ten seconds
        self.timer_day_change = QtCore.QTimer(self)
        self.timer_day_change.timeout.connect(self.update_for_day_change)
        self.timer_day_change.start(10000)

        # This timer provide update of preview pieces till now. Fired every second but we can slow it.
        self.update_preview_tot = QtCore.QTimer(self)
        self.update_preview_tot.timeout.connect(self.update_preview_now)
        self.update_preview_tot.start(1000)
        self.internal_init()

        if not DEBUG:
            GPIO.cleanup()
            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)
            GPIO.setup(IN_PIN, GPIO.IN, GPIO.PUD_UP)
            self.read_timer = QtCore.QTimer(self)
            self.read_timer.timeout.connect(self.count_piece)
            self.read_timer.start(1)
            # Can't use... see below.
            # GPIO.add_event_detect(IN_PIN, GPIO.RISING, callback=self.count_piece, bouncetime=10)


    def internal_init(self):
        self.logic.prev_preview_pcs = 0
        self.daily_qty = self.logic.get_daily_qty()
        self.ui.lbPzGiorn.setText(str(self.daily_qty))
        self.ui.leNumPezzi.setText(str(self.daily_qty))
        self.logic.set_daily_qty()
        self.ui.lbData.setText(time.strftime("%d/%m/%Y"))
        self.ui.lbPzFatti.setText(str(self.logic.get_pieces_until_now()))
        self.draw_hours_and_qty()
        self.update_preview_now(True)

    def update_preview_now(self, do_anyway=False):
        tot_pcs_till_now = self.logic.get_preview_pcs_till_now(do_anyway)
        self.ui.lbPzPrevisti.setText(str(tot_pcs_till_now))
        if self.logic.get_pieces_until_now() < tot_pcs_till_now:
            self.ui.lbPzPrevisti.setStyleSheet(self.red_gradient)
        else:
            self.ui.lbPzPrevisti.setStyleSheet(self.green_gradient)

    def control_color_pcs_done(self, dict_passed):
        preview_pcs_hour = self.logic.get_preview_pieces_this_hour(dict_passed["HOUR_START"], dict_passed["HOUR_END"])
        done_pcs_hour = int(dict_passed["qty_hour"]);
        if done_pcs_hour < preview_pcs_hour:
            dict_passed["label_pcs_done"].setStyleSheet(self.red_gradient)
        else:
            dict_passed["label_pcs_done"].setStyleSheet(self.green_gradient)

    # Clearing QFrames
    def clear_qframe(self, qframe):
        for i in reversed(range(qframe.count())):
            # 0 is the title label
            if i > 0:
                qframe.itemAt(i).widget().deleteLater()

    def draw_hours_and_qty(self):
        self.clear_qframe(self.ui.vlOre)
        self.clear_qframe(self.ui.vlPrev)
        self.clear_qframe(self.ui.vlFatti)

        self.lista_orari = self.logic.get_hours()
        font = QtGui.QFont()
        font.setPointSize(24)
        for dict_orario in self.lista_orari:
            # N.B.: vl_ore it's the name of the layout of the object qfOre in QT Designer
            self.ui.lbTitoloOra = QtWidgets.QLabel(self.ui.qfOre)
            self.ui.lbTitoloOra.setText(dict_orario["ORARIO"])
            self.ui.lbTitoloOra.setFont(font)
            self.ui.vlOre.addWidget(self.ui.lbTitoloOra)

            # Label generation for preview pieces
            self.ui.lbQtyPerOra = QtWidgets.QLabel(self.ui.qfPrev)
            self.ui.lbQtyPerOra.setText(str(int(dict_orario["qty_expected"])))
            self.ui.lbQtyPerOra.setFont(font)
            self.ui.vlPrev.addWidget(self.ui.lbQtyPerOra)
            self.ui.lbQtyPerOra.setAlignment(QtCore.Qt.AlignCenter)

            # Label generation for done pieces.
            self.ui.vlFatti.addWidget(dict_orario["label_pcs_done"])
            dict_orario["label_pcs_done"].setFont(font)
            dict_orario["label_pcs_done"].setText(str(int(dict_orario["qty_hour"])))
            dict_orario["label_pcs_done"].setAlignment(QtCore.Qt.AlignCenter)
            self.control_color_pcs_done(dict_orario)


    def btn_sethours_click(self):
        self.logic.set_daily_qty(int(self.ui.leNumPezzi.text()))
        self.ui.lbPzGiorn.setText(str(self.logic.get_daily_qty()))

    def count_piece(self):
        if DEBUG or (not GPIO.input(IN_PIN)):
            if not self.logic.add_piece_in_hour():
                self.ui.lbError.setText(MSG_WARN_NO_HOUR)
            else:
                self.ui.lbPzFatti.setText(str(self.logic.get_pieces_until_now()))
                pcs_ts_hour = self.logic.get_pieces_this_hour()
                for dict_orario in self.lista_orari:
                    if dict_orario["ID"] == pcs_ts_hour[1]:
                        dict_orario["label_pcs_done"].setText(str(int(pcs_ts_hour[0])))
                        dict_orario["qty_hour"] = int(dict_orario["qty_hour"]) + 1
                        dict_to_pass = dict_orario

                # Can't use add_event_detect (like below) because of a total crash without error message or other
                # excuting some instruction inside control_color_pcs_done...
                # GPIO.add_event_detect(IN_PIN, GPIO.RISING, callback=self.count_piece, bouncetime=10)
                self.control_color_pcs_done(dict_to_pass)

                self.ui.lbError.setText("")
                if not DEBUG:
                    while not GPIO.input(IN_PIN):
                        time.sleep(0.05)

    def btn_esci_click(self):
        self.close()

    def closeEvent(self, event):
        s_msg = MSG_EXIT
        reply = QMessageBox.question(self, MSG, s_msg, QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def update_for_day_change(self):
        self.dateNow = datetime.now().strftime("%Y-%m-%d")
        if self.dateNow != self.datePassed:
            self.datePassed = datetime.now().strftime("%Y-%m-%d")
            self.internal_init()

app = QApplication(sys.argv)
ui = PieceCounterGui()
ui.showMaximized()
sys.exit(app.exec_())

