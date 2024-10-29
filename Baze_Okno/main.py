#  widget - это имя, присваиваемое компоненту пользовательского интерфейса,
#  с которым пользователь может взаимодействовать 
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QApplication, # это то, что поддерживает работоспособность приложения Qt, выполняя его основной цикл событий
    QDialog # это базовый класс диалогового окна
)
from PyQt5.uic import loadUi # загрузка интерфейса, созданного в Qt Creator
import sys # взаимодействие с интерпретатором
from PyQt5.QtGui import QPixmap, QIcon # для работы с изображениями и загрузки иконок
import sqlite3

# Окно приветствия
class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("Baze_Okno/dialog_Stepik.ui",self) # загружаем интерфейс
        self.PasswordField.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pushButton.clicked.connect(self.Bxod)

    def Bxod(self):
        print(2)
        user = self.SigningField.text() # получени написанных данных с формы (Text())
        password = self.PasswordField.text()
        
        if user == "" or password == "":
            self.ErrorFiled.setText("Заполните все поля")
        else:
            try:
                conn = sqlite3.connect("Baze_Okno/uchet.db")
                cur = conn.cursor()

                user_info = [user, password]
                cur.execute('SELECT typeID FROM users WHERE login=(?) and password=(?)', user_info) 
                typeUser = cur.fetchone()
                print(typeUser[0])                      

                conn.commit()
                conn.close()

                if typeUser[0] == 1:
                    master = MasterScreen()
                    widget.addWidget(master)
                    widget.setCurrentIndex(widget.currentIndex()+1)
                else:
                    self.ErrorField.setText("Войдите под менеджером")
            except:
                print("Проблемы с БД")
                self.ErrorField.setText("Проблемы с БД")

        
class MasterScreen(QDialog):
    def __init__(self):
        super(MasterScreen, self).__init__()
        loadUi("Baze_Okno/master.ui",self)


# main       
# запуcк приложения
app = QApplication(sys.argv)

# позволяте менять страницы в окне
welcome = WelcomeScreen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)

# загружаем иконку
icon = QIcon()
icon.addPixmap(QPixmap("книга.png"), QIcon.Normal, QIcon.Off)
widget.setWindowIcon(icon) 
widget.show()

                # запускаем приложение
try:
    sys.exit(app.exec_())
except:
    print("You close application")