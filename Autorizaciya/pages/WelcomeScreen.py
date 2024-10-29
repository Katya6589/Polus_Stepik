#  widget - это имя, присваиваемое компоненту пользовательского интерфейса,
#  с которым пользователь может взаимодействовать 
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (    
    QDialog # это базовый класс диалогового окна
)

from PyQt5.uic import loadUi # загрузка интерфейса, созданного в Qt Creator

import sqlite3

from pages.Zakazchik import Zakazchik
from pages.Master import Master
from pages.Operator import Operator
from pages.Manager import Manager

# Окно приветствия
class WelcomeScreen(QDialog):
    """
    Это класс окна приветствия.
    """
    def __init__(self):
        """
        Это конструктор класса
        """
        super(WelcomeScreen, self).__init__()
        loadUi("Autorizaciya/views/welcomescreen.ui",self) # загружаем интерфейс.
        self.PasswordField.setEchoMode(QtWidgets.QLineEdit.Password) # скрываем пароль
        self.SignInButton.clicked.connect(self.signupfunction) # нажати на кнопку и вызов функции
        self.back.clicked.connect(self.backs)
        self.back.hide()
        self.stackedWidget.currentChanged.connect(self.hiddenButton)

        
        
        # Подключение кнопок к методам переключения страниц с использованием lambda
        #self.SignInButton.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Zakazchik))

    def signupfunction(self): # создаем функцию регистрации

        
        user = self.LoginField.text() # создаем пользователя и получаем из поля ввода логина введенный текст
        password = self.PasswordField.text() # создаем пароль и получаем из поля ввода пароля введенный текст
        print(user, password) # выводит логин и пароль

        if len(user)==0 or len(password)==0: # если пользователь оставил пустые поля
            self.ErrorField.setText("Заполните все поля") # выводим ошибку в поле
        else:
            self.ErrorField.setText(" ") # выводим что все хорошо в поле

            conn = sqlite3.connect("uchet.db") # подключение к базе данных в () изменить на название своей БД
            cur = conn.cursor() # переменная для запросов

            cur.execute('SELECT typeID FROM users WHERE login=(?) and password=(?)', [user, password]) # получаем тип пользователя, логин и пароль которого был введен
            typeUser = cur.fetchone() # получает только один тип пользователя
            #print(typeUser[0]) # выводит тип пользователя без скобок      
            if typeUser == None:
                self.ErrorField.setText("Пользователь с такими данными не найден")
            elif typeUser[0] == 4:
                self.stackedWidget.setCurrentWidget(self.Zakazchik)
                self.lybaya = Zakazchik()
            elif typeUser[0] == 2:
                self.stackedWidget.setCurrentWidget(self.Master)
                self.lybaya = Master()
            elif typeUser[0] == 3:
                self.stackedWidget.setCurrentWidget(self.Operator)
                self.lybaya = Operator()
            elif typeUser[0] == 1:
                self.stackedWidget.setCurrentWidget(self.Manager)
                self.lybaya = Manager()


            conn.commit() # сохраняет в подключении запросы
            conn.close() # закрываем подключение

    def backs(self):
        self.stackedWidget.setCurrentWidget(self.Avtorisation)
        self.lybaya = WelcomeScreen()
        print("oke")
        

    def hiddenButton(self):
        if self.stackedWidget.currentWidget() == self.Avtorisation:  
            self.back.hide()
        else:
            self.back.show()

