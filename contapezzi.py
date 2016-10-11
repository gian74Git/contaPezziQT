from contaPezziLogic import logicCounter
import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QMainWindow
from PyQt5 import QtWidgets
from contapezzi_ui import Ui_contaPezzi
import time
from PyQt5 import QtGui

Debug = True
if not Debug:
    import RPi.GPIO as GPIO


class PieceCounterGui(QMainWindow):
    def __init__(self):
        self.lista_orari = []
        self.logic = logicCounter(self)
        QMainWindow.__init__(self, parent=None)
        super(PieceCounterGui, self).__init__()
        self.ui = Ui_contaPezzi()
        self.ui.setupUi(self)

        self.ui.lbPzGiorn.setText(str(self.logic.get_daily_qty()))
        self.ui.leNumPezzi.setText(str(self.logic.get_daily_qty()))
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


    def draw_hours_and_qty(self):
        self.lista_orari = self.logic.get_hours()
        font = QtGui.QFont()
        font.setPointSize(24)
        for dict_orario in self.lista_orari:
            self.ui.lbTitoloOra = QtWidgets.QLabel(self.ui.qfOre)
            self.ui.lbTitoloOra.setText(dict_orario["ORARIO"])
            self.ui.lbTitoloOra.setFont(font)
            self.ui.vlOre.addWidget(self.ui.lbTitoloOra)

            #Generazione label per i pezzi previsti
            #N.B.: vl_ore è il nome del layout dell'oggetto qfOre in QT Designer
            self.ui.lbQtyPerOra = QtWidgets.QLabel(self.ui.qfOre)
            self.ui.lbQtyPerOra.setText(str(int(dict_orario["qty_expected"])))
            self.ui.lbQtyPerOra.setFont(font)
            #self.ui.lbQtyPerOra.upda
            self.ui.vlPrev.addWidget(self.ui.lbQtyPerOra)

            #Generazione label per i pezzi fatti.
            self.ui.vlFatti.addWidget(dict_orario["label_pcs_done"])
            dict_orario["label_pcs_done"].setFont(font)
            dict_orario["label_pcs_done"].setText(str(int(dict_orario["qty_hour"])))


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

app = QApplication(sys.argv)
ui = PieceCounterGui()
ui.showMaximized()
sys.exit(app.exec_())

