#  widget - это имя, присваиваемое компоненту пользовательского интерфейса,
#  с которым пользователь может взаимодействовать 
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (    
    QDialog # это базовый класс диалогового окна
)

from PyQt5.uic import loadUi # загрузка интерфейса, созданного в Qt Creator

import sqlite3

class Zakazchik(QDialog):
    def __init__(self):        
        super(Zakazchik, self).__init__()
    #    loadUi("welcomescreen.ui",self) # загружаем интерфейс.
    #    self.back_Zakazchik.clicked.connect(self.knopka_Zakazchik) 
        print("sgaclusa")