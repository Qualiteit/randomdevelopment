import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import *
from PyQt5 import uic
import requests

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('basic.ui', self)
        self.show()



response = requests.get('http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=2680454F00E6FAE51F4AD8CE0F477AB8&steamid=76561198124741242&format=json')

data = response.json()

print(data['response']['game_count'])
game_count = data['response']['game_count']


app = QApplication(sys.argv)

window = Ui()
window.show()

app.exec_()