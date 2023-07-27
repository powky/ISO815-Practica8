from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(400, 300)
        Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.regBtn = QtWidgets.QPushButton(Frame)
        self.regBtn.setGeometry(QtCore.QRect(130, 230, 113, 32))
        self.regBtn.setObjectName("regBtn")
        self.facturaTxt = QtWidgets.QTextEdit(Frame)
        self.facturaTxt.setGeometry(QtCore.QRect(30, 50, 131, 31))
        self.facturaTxt.setObjectName("facturaTxt")
        self.condTxt = QtWidgets.QTextEdit(Frame)
        self.condTxt.setGeometry(QtCore.QRect(210, 50, 131, 31))
        self.condTxt.setObjectName("condTxt")
        self.idTxt = QtWidgets.QTextEdit(Frame)
        self.idTxt.setGeometry(QtCore.QRect(30, 110, 131, 31))
        self.idTxt.setObjectName("idTxt")
        self.dateTxt = QtWidgets.QTextEdit(Frame)
        self.dateTxt.setGeometry(QtCore.QRect(210, 110, 131, 31))
        self.dateTxt.setObjectName("dateTxt")
        self.montoTxt = QtWidgets.QTextEdit(Frame)
        self.montoTxt.setGeometry(QtCore.QRect(30, 170, 131, 31))
        self.montoTxt.setObjectName("montoTxt")
        self.stsTxt = QtWidgets.QTextEdit(Frame)
        self.stsTxt.setGeometry(QtCore.QRect(210, 170, 131, 31))
        self.stsTxt.setObjectName("stsTxt")
        self.facturaLbl = QtWidgets.QLabel(Frame)
        self.facturaLbl.setGeometry(QtCore.QRect(30, 30, 60, 16))
        self.facturaLbl.setObjectName("facturaLbl")
        self.condLbl = QtWidgets.QLabel(Frame)
        self.condLbl.setGeometry(QtCore.QRect(210, 30, 91, 16))
        self.condLbl.setObjectName("condLbl")
        self.idLbl = QtWidgets.QLabel(Frame)
        self.idLbl.setGeometry(QtCore.QRect(30, 90, 91, 16))
        self.idLbl.setObjectName("idLbl")
        self.dateLbl = QtWidgets.QLabel(Frame)
        self.dateLbl.setGeometry(QtCore.QRect(210, 90, 91, 16))
        self.dateLbl.setObjectName("dateLbl")
        self.montoLbl = QtWidgets.QLabel(Frame)
        self.montoLbl.setGeometry(QtCore.QRect(30, 150, 91, 16))
        self.montoLbl.setObjectName("montoLbl")
        self.stsLbl = QtWidgets.QLabel(Frame)
        self.stsLbl.setGeometry(QtCore.QRect(210, 150, 91, 16))
        self.stsLbl.setObjectName("stsLbl")
        self.regBtn.clicked.connect(self.register_data)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Registrar facturas - Ian F A00100600"))
        self.regBtn.setText(_translate("Frame", "Registrar"))
        self.facturaLbl.setText(_translate("Frame", "# factura"))
        self.condLbl.setText(_translate("Frame", "Condición"))
        self.idLbl.setText(_translate("Frame", "ID cliente"))
        self.dateLbl.setText(_translate("Frame", "Fecha"))
        self.montoLbl.setText(_translate("Frame", "Monto"))
        self.stsLbl.setText(_translate("Frame", "Estado"))

    def register_data(self):
        factura = int(self.facturaTxt.toPlainText())
        condicion = self.condTxt.toPlainText()
        cliente = self.idTxt.toPlainText()
        fecha = self.dateTxt.toPlainText()
        monto = float(self.montoTxt.toPlainText())
        estado = self.stsTxt.toPlainText()

        try:
            result = subprocess.check_output(['python3', 'insert.py', str(factura), condicion, cliente, fecha, str(monto), estado], stderr=subprocess.STDOUT)

            QtWidgets.QMessageBox.information(None, "Éxito", "Información guardada exitosamente.")
            self.facturaTxt.clear()
            self.condTxt.clear()
            self.idTxt.clear()
            self.dateTxt.clear()
            self.montoTxt.clear()
            self.stsTxt.clear()

        except subprocess.CalledProcessError as e:
            QtWidgets.QMessageBox.critical(None, "Error", "Ocurrió un error: {}".format(e.output.decode()))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())
