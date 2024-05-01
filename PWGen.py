from PyQt6 import QtCore, QtGui, QtWidgets
import random
import string
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(795, 507)
        MainWindow.setWindowFlags(QtCore.Qt.WindowType.Window)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 250, 781, 211))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit.setReadOnly(True)  # Add this line to make it non-editable
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 130, 781, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.spinBox = QtWidgets.QSpinBox(parent=self.horizontalLayoutWidget)
        self.spinBox.setMaximum(100)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout.addWidget(self.spinBox)
        self.label = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.spinBox_2 = QtWidgets.QSpinBox(parent=self.horizontalLayoutWidget)
        self.spinBox_2.setMaximum(100)
        self.spinBox_2.setObjectName("spinBox_2")
        self.horizontalLayout.addWidget(self.spinBox_2)
        self.label_2 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 781, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkBox_3 = QtWidgets.QCheckBox(parent=self.horizontalLayoutWidget_2)
        self.checkBox_3.setObjectName("checkBox_3")
        self.horizontalLayout_2.addWidget(self.checkBox_3)
        self.checkBox_2 = QtWidgets.QCheckBox(parent=self.horizontalLayoutWidget_2)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout_2.addWidget(self.checkBox_2)
        self.checkBox = QtWidgets.QCheckBox(parent=self.horizontalLayoutWidget_2)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_2.addWidget(self.checkBox)
        self.checkBox_4 = QtWidgets.QCheckBox(parent=self.horizontalLayoutWidget_2)
        self.checkBox_4.setObjectName("checkBox_4")
        self.horizontalLayout_2.addWidget(self.checkBox_4)
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 220, 781, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 470, 161, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(630, 470, 161, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.generate_passwords)
        self.pushButton_2.clicked.connect(self.save_to_file)
        self.pushButton_3.clicked.connect(QtWidgets.QApplication.instance().quit)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PassGen"))
        self.label.setText(_translate("MainWindow", "Количество"))
        self.label_2.setText(_translate("MainWindow", "Длина"))
        self.checkBox_3.setText(_translate("MainWindow", "0 - 9"))
        self.checkBox_2.setText(_translate("MainWindow", "a - z"))
        self.checkBox.setText(_translate("MainWindow", "A - Z"))
        self.checkBox_4.setText(_translate("MainWindow", "! @ ..."))
        self.pushButton.setText(_translate("MainWindow", "Сгенрировать"))
        self.pushButton_2.setText(_translate("MainWindow", "Сохранить в файл"))
        self.pushButton_3.setText(_translate("MainWindow", "Выход"))

    def generate_passwords(self):
        password_length = self.spinBox_2.value()
        password_count = self.spinBox.value()
        password_characters = ''

        if self.checkBox.isChecked():
            password_characters += string.ascii_uppercase
        if self.checkBox_2.isChecked():
            password_characters += string.ascii_lowercase
        if self.checkBox_3.isChecked():
            password_characters += string.digits
        if self.checkBox_4.isChecked():
            password_characters += string.punctuation

        if not password_characters:
            QtWidgets.QMessageBox.warning(self.centralwidget, "Warning", "Please select at least one character type.")
            return

        passwords = []
        for _ in range(password_count):
            password = ''.join(random.choice(password_characters) for _ in range(password_length))
            passwords.append(password)

        self.plainTextEdit.setPlainText('\n'.join(passwords))

    def save_to_file(self):
        file_path, _ = QtWidgets.QFileDialog.getSaveFileName(None, "Save Passwords", "", "Text Files (*.txt)")
        if file_path:
            try:
                with open(file_path, 'w') as file:
                    file.write(self.plainTextEdit.toPlainText())
            except Exception as e:
                QtWidgets.QMessageBox.warning(self.centralwidget, "Error", f"An error occurred: {e}")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())