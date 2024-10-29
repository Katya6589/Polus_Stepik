#  widget - это имя, присваиваемое компоненту пользовательского интерфейса,
#  с которым пользователь может взаимодействовать 
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QApplication, # это то, что поддерживает работоспособность приложения Qt, выполняя его основной цикл событий
)

import sys # взаимодействие с интерпретатором

from PyQt5.QtGui import QPixmap, QIcon # для работы с изображениями и загрузки иконок

from pages.WelcomeScreen import WelcomeScreen # файл из папки pages

# запуcк приложения
app = QApplication(sys.argv)

# позволяте менять страницы в окне
welcome = WelcomeScreen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)

# загружаем иконку
icon = QIcon()
icon.addPixmap(QPixmap("media/logo.png"), QIcon.Normal, QIcon.Off) #не пишем в путь Autorizaciya/ тк они в одной папке
widget.setWindowIcon(icon) 
widget.show()

# запускаем приложение
try:
    sys.exit(app.exec_())
except:
    print("You close application")