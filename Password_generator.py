import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from win_main import Ui_Dialog
from win_two import Ui_DialogTwo
import random
import string


class MainWindow(QtWidgets.QWidget, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Генератор паролей')
        self.checkBox.setChecked(True)
        self.checkBox_2.setChecked(True)
        self.checkBox_3.setChecked(True)
        self.checkBox_4.setChecked(True)
        self.radioButton.setChecked(True)
        self.spinBox.setValue(15)
        self.pushButton.clicked.connect(self.generate_password)
        self.pushButton_2.clicked.connect(self.win_closed)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit.setFont(font)
        self.setFixedSize(431, 532)
        self.comboBox.addItems(('Русский', 'Английский'))
        self.comboBox.currentIndexChanged.connect(self.change_language)
        self.horizontalSlider.valueChanged.connect(self.slider_change_value)
    
    def is_cheked(self):
        check1 = self.checkBox.isChecked()
        check2 = self.checkBox_2.isChecked()
        check3 = self.checkBox_3.isChecked()
        check4 = self.checkBox_4.isChecked()
        return [check1, check2, check3, check4]
    
    def generate_password(self):
        quantity = self.horizontalSlider.value()
        letters_up = string.ascii_uppercase
        letters_low = string.ascii_lowercase
        letters_dig = string.digits
        letters_symb = string.punctuation
        lst_letters = [letters_low, letters_up, letters_dig, letters_symb]
        lst_is_checked = self.is_cheked()
        lst_checked_letters = [lst_letters[i] for i in range(4) if lst_is_checked[i]]
        lst = list(''.join(lst_checked_letters))
        len_password = self.spinBox.value()
        if len(lst) < len_password:
            self.radioButton_2.setChecked(True)
        if quantity == 1:
            if self.radioButton.isChecked():
                rand_letters = ''.join(random.sample(lst, k=len_password))
            if self.radioButton_2.isChecked():
                rand_letters = ''.join(random.choices(lst, k=len_password))
            self.lineEdit.setText(rand_letters)
        else:
            lst_temp = []
            count_quantity = 0
            while count_quantity < quantity:
                if self.radioButton.isChecked():
                    rand_letters = ''.join(random.sample(lst, k=len_password))
                if self.radioButton_2.isChecked():
                    rand_letters = ''.join(random.choices(lst, k=len_password))
                lst_temp.append(rand_letters)
                count_quantity += 1
            self.lineEdit.clear()
            self.window_two = WindowTwo(lst_temp, self.comboBox.currentIndex())
            self.window_two.show()
            self.hide()
    
    def change_language(self):
        language = self.comboBox.currentIndex()
        if language == 0:
            lst_values = ('Генератор паролей', 'Длина пароля', 'Язык', 'Выход', 'Алгоритм', 'Количество паролей:', ('Русский', 'Английский'), 'Список паролей')
        if language == 1:
            lst_values = ('Password generator', 'Password length', 'Language', 'Exit', 'Algorithm', 'Passwords quantity:', ('Russian', 'English'), 'Passwords list')
        self.set_translate(lst_values)
    
    def set_translate(self, values):
        self.setWindowTitle(values[0])
        self.label.setText(values[1])
        self.label_2.setText(values[2])
        self.pushButton_2.setText(values[3])
        self.label_3.setText(values[4])
        self.label_4.setText(values[5])
        for i in range(2):
            self.comboBox.setItemText(i, values[6][i])

    def slider_change_value(self):
        new_value = str(self.horizontalSlider.value())
        self.label_5.setText(new_value)
   
    def win_closed(self):
        self.close()

    def closeEvent(self, event):
        self.win_closed()

class WindowTwo(QtWidgets.QWidget, Ui_DialogTwo):
    def __init__(self, passwords, language):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(431, 532)
        for i in range(len(passwords)):
            self.textEdit.insertPlainText(f'{i+1} - {passwords[i]}\n')
        if language == 0:
            self.setWindowTitle(f'Список паролей - {len(passwords)} шт.')
        if language == 1:
            self.setWindowTitle(f'Password list - {len(passwords)} pcs.')
        self.pushButton.clicked.connect(self.win_closed)
        

    def win_closed(self):
        self.close()
        form.show()

    def closeEvent(self, event):
        self.win_closed()
    

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())