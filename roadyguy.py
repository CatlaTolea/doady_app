# Form implementation generated from reading ui file 'roadyguy.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets

from roady import Roady


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.departure_city_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.departure_city_label.setGeometry(QtCore.QRect(20, 30, 81, 41))
        self.departure_city_label.setObjectName("departure_city_label")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(130, 40, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.Destination_city = QtWidgets.QLabel(parent=self.centralwidget)
        self.Destination_city.setGeometry(QtCore.QRect(290, 40, 81, 31))
        self.Destination_city.setObjectName("Destination_city")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(400, 40, 113, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gas_comboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.gas_comboBox.setGeometry(QtCore.QRect(40, 120, 71, 31))
        self.gas_comboBox.setObjectName("gas_comboBox")
        self.gas_comboBox.addItem("")
        self.gas_comboBox.addItem("")
        self.fuel_usage = QtWidgets.QLabel(parent=self.centralwidget)
        self.fuel_usage.setGeometry(QtCore.QRect(40, 190, 49, 16))
        self.fuel_usage.setObjectName("fuel_usage")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(110, 180, 113, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.number_of_persons = QtWidgets.QLabel(parent=self.centralwidget)
        self.number_of_persons.setGeometry(QtCore.QRect(40, 240, 49, 16))
        self.number_of_persons.setObjectName("number_of_persons")
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(110, 240, 113, 22))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.calculate_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.calculate_button.clicked.connect(self.calculate_btn)
        self.calculate_button.setGeometry(QtCore.QRect(330, 210, 75, 24))
        self.calculate_button.setObjectName("calculate_button")
        self.add_return_radio_button = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.add_return_radio_button.setGeometry(QtCore.QRect(250, 120, 89, 20))
        self.add_return_radio_button.setObjectName("add_return_radio_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.departure_city_label.setText(_translate("MainWindow", "Departure City"))
        self.Destination_city.setText(_translate("MainWindow", "Destination City"))
        self.gas_comboBox.setItemText(0, _translate("MainWindow", "Benzina"))
        self.gas_comboBox.setItemText(1, _translate("MainWindow", "Diesel"))
        self.fuel_usage.setText(_translate("MainWindow", "Consum"))
        self.number_of_persons.setText(_translate("MainWindow", "Persons"))
        self.calculate_button.setText(_translate("MainWindow", "Calculate"))
        self.add_return_radio_button.setText(_translate("MainWindow", "dus-intors"))


    def calculate_btn(self):
        departure_city = self.lineEdit.text()
        destination_city = self.lineEdit_2.text()
        number_of_persons = self.lineEdit_4.text()
        fuel_type = self.gas_comboBox.currentText()
        fuel_usage = self.lineEdit_3.text()
        print(departure_city, destination_city, number_of_persons, fuel_type,fuel_usage)
        roady = Roady(departure_city, destination_city, int(number_of_persons),
                      float(fuel_usage), fuel_type)

        print(roady.calculate_prie_per_person())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
