from contaPezziLogic import logicCounter
import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QMainWindow
from PyQt5 import QtWidgets
from contapezzi_ui import Ui_contaPezzi
import time
from PyQt5 import QtGui, QtCore


Debug = True
if not Debug:
    import RPi.GPIO as GPIO


class PieceCounterGui(QMainWindow):
    def __init__(self):

        self.red_gradient = "background-color: qlineargradient(spread:pad, x1:0.505, y1:1, x2:0.505, y2:0, stop:0 " \
                            "rgba(174, 0, 5, 255), stop:1 rgba(255, 2, 0, 255));"
        self.green_gradient = "background-color: qlineargradient(spread:pad, x1:0.505, y1:1, x2:0.505, y2:0, stop:0 " \
                              "rgba(0, 174, 68, 255), stop:1 rgba(0, 255, 67, 255));"
        self.lista_orari = []
        self.logic = logicCounter(self)
        QMainWindow.__init__(self, parent=None)
        super(PieceCounterGui, self).__init__()
        self.ui = Ui_contaPezzi()
        self.ui.setupUi(self)

        self.daily_qty = self.logic.get_daily_qty()
        self.ui.lbPzGiorn.setText(str(self.daily_qty))
        self.ui.leNumPezzi.setText(str(self.daily_qty))
        self.logic.set_daily_qty()
        #self.draw_hours_and_qty()

        self.ui.btnChiudi.clicked.connect(self.btnEsciClick)
        self.ui.actionEsci.triggered.connect(self.btnEsciClick)
        self.ui.lbCliente.setText("VIST TECH")
        self.ui.lbData.setText(time.strftime("%d/%m/%Y"))

        self.ui.btnTest.clicked.connect(self.btn_test_click)

        self.ui.btnImposta.clicked.connect(self.btn_sethours_click)
        self.ui.lbPzFatti.setText(str(self.logic.get_pieces_until_now()))
        self.draw_hours_and_qty()
        #Timer declaration to control changing day. Fired every minute
        self.timer_day_change = QtCore.QTimer(self)
        self.timer_day_change.timeout.connect(self.update_for_day_change)
        self.timer_day_change.start(60000)

        #This timer provide update of preview pieces till now.
        self.update_preview_tot = QtCore.QTimer(self)
        self.update_preview_tot.timeout.connect(self.update_preview_now)
        self.update_preview_tot.start(1000)
        self.update_preview_now(True)

    def update_preview_now(self, do_anyway = False):
        tot_pcs_till_now = self.logic.get_preview_pcs_till_now(do_anyway)
        self.ui.lbPzPrevisti.setText(str(tot_pcs_till_now))
        if tot_pcs_till_now < self.daily_qty:
            self.ui.lbPzPrevisti.setStyleSheet(self.red_gradient)
        else:
            self.ui.lbPzPrevisti.setStyleSheet(self.green_gradient)

    def control_color_pcs_done(self, dict_passed):
        preview_pcs_hour = self.logic.get_preview_pieces_this_hour(dict_passed["HOUR_START"], dict_passed["HOUR_END"])
        done_pcs_hour = int(dict_passed["qty_hour"]);
        if (done_pcs_hour < preview_pcs_hour):
            dict_passed["label_pcs_done"].setStyleSheet(self.red_gradient)
        else:
            dict_passed["label_pcs_done"].setStyleSheet(self.green_gradient)

    def draw_hours_and_qty(self):
        self.lista_orari = self.logic.get_hours()
        font = QtGui.QFont()
        font.setPointSize(24)
        for dict_orario in self.lista_orari:
            self.ui.lbTitoloOra = QtWidgets.QLabel(self.ui.qfOre)
            self.ui.lbTitoloOra.setText(dict_orario["ORARIO"])
            self.ui.lbTitoloOra.setFont(font)
            self.ui.vlOre.addWidget(self.ui.lbTitoloOra)

            #Label generation for preview pieces
            #N.B.: vl_ore it's the name of the layout of the object qfOre in QT Designer
            self.ui.lbQtyPerOra = QtWidgets.QLabel(self.ui.qfOre)
            self.ui.lbQtyPerOra.setText(str(int(dict_orario["qty_expected"])))
            self.ui.lbQtyPerOra.setFont(font)
            self.ui.vlPrev.addWidget(self.ui.lbQtyPerOra)
            self.ui.lbQtyPerOra.setAlignment(QtCore.Qt.AlignCenter)

            #Label generation for done pieces.
            self.ui.vlFatti.addWidget(dict_orario["label_pcs_done"])
            dict_orario["label_pcs_done"].setFont(font)
            dict_orario["label_pcs_done"].setText(str(int(dict_orario["qty_hour"])))
            dict_orario["label_pcs_done"].setAlignment(QtCore.Qt.AlignCenter)
            self.control_color_pcs_done(dict_orario)


    def btn_sethours_click(self):
        self.logic.set_daily_qty(int(self.ui.leNumPezzi.text()))
        self.ui.lbPzGiorn.setText(str(self.logic.get_daily_qty()))


    def btn_test_click(self):
        if not self.logic.add_piece_in_hour():
            self.ui.lbError.setText("ATTENZIONE: Orari non trovati. Controllare la tabella")
        else:
            self.ui.lbPzFatti.setText(str(self.logic.get_pieces_until_now()))
            pcs_ts_hour = self.logic.get_pieces_this_hour()
            for dict_orario in self.lista_orari:
                if dict_orario["ID"] == pcs_ts_hour[1]:
                    dict_orario["label_pcs_done"].setText(str(int(pcs_ts_hour[0])))
                    dict_orario["qty_hour"] = int(dict_orario["qty_hour"]) + 1

            self.control_color_pcs_done(dict_orario)

            self.ui.lbError.setText("")

    def btnEsciClick(self):
        self.close()

    def closeEvent(self, event):
        s_msg = 'Vuoi veramente uscire dal programma ?'
        reply = QMessageBox.question(self, 'Messaggio:', s_msg, QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def update_for_day_change(self):
        print("Timer!")

app = QApplication(sys.argv)
ui = PieceCounterGui()
ui.showMaximized()
sys.exit(app.exec_())

