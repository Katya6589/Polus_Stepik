#  widget - это имя, присваиваемое компоненту пользовательского интерфейса,
#  с которым пользователь может взаимодействовать 
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (    
    QDialog # это базовый класс диалогового окна
)

from PyQt5.uic import loadUi # загрузка интерфейса, созданного в Qt Creator

import sqlite3

class Operator(QDialog):
    def __init__(self):        
        super(Operator, self).__init__()
        print("sgaclusa")