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
    #label oluşturma
    lbl_name=QtWidgets.QLabel(win)
    lbl_name.setText("Adınız:")
    lbl_name.move(50,30)

    lbl_surname=QtWidgets.QLabel(win)
    lbl_surname.setText("Soyadınız:")
    lbl_surname.move(50,70)

    #yazı yazma yeri
    txt_name=QtWidgets.QLineEdit(win)
    txt_name.move(150,30)
    txt_name.resize(200,32)
    txt_surname=QtWidgets.QLineEdit(win)
    txt_surname.move(150,70)
    txt_surname.resize(200,32)

    #buton
    btn_save=QtWidgets.QPushButton(win)
    btn_save.move(150,110)
    btn_save.setText("Kaydet")

    # tıklamaya bağlı çalıştıracak fonksiyon
    def clicken(self):
        print("Buton Tıklandı Name:"+txt_name.text()+"Surname :"+txt_surname.text())


    #buton tıklama
    btn_save.clicked.connect(clicken)




    #pencerenin başlatılması
    win.show()
    #çarpı tuşuna bastığımızda ekranın kapanması için
    sys.exit(app.exec_())


window()
