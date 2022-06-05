import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QToolTip
#icon eklemek için eklenen kütüphane
from PyQt5.QtGui import QIcon

#pencere oluşturuyoruz
def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    #uygulama başlığı
    win.setWindowTitle("First Application")
    #açılış konumu belirtme
    win.setGeometry(200,200,500,500)
    #icon değiştirme
    win.setWindowIcon(QIcon('anasayfa.png'))
    #pencere üzerine geldiğimizde maasun bulunduğuyerde yazı çıkartan tool tip
    win.setToolTip("My Tool Tip")
    #pencerenin başlatılması
    win.show()
    #çarpı tuşuna bastığımızda ekranın kapanması için
    sys.exit(app.exec_())


window()
