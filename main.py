import sys
import os
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from arayuz import *

WINDOW_SIZE = 0;
class MainWindow(QMainWindow):
    baglanKontrol = 4
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(":/images/images/nike_logo.png"))
        self.setWindowTitle("AtaNova Yer Kontrol İstasyonu")

        # Windows başlık barını kaldır.
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) 

        # Ana arka planı şeffaf olarak ayarla
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
      
        # Gölge Efekti Uygula
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 92, 157, 150))
        self.restore_or_maximize_window()
        # Merkezi widget'a gölge uygula
        self.ui.centralwidget.setGraphicsEffect(self.shadow)

        # ÜST SEKME BUTONLARI
        # 
        # Ekranı küçük
        self.ui.minimizeButton.clicked.connect(lambda: self.showMinimized())
        # Pencereyi Kapat
        self.ui.closeButton.clicked.connect(lambda: self.close())
        # Ekranı Büyüt
        self.ui.restoreButton.clicked.connect(lambda: self.restore_or_maximize_window())
        # Bağlan
        self.ui.baglan.clicked.connect(lambda: self.baglan())
        # ###############################################


        # ###############################################
        # Move window on mouse drag event on the tittle bar
        # ###############################################
        def moveWindow(e):
            # Detect if the window is  normal size
            # ###############################################  
            if self.isMaximized() == False: #Not maximized
                # Move window only when window is normal size  
                # ###############################################
                #if left mouse button is clicked (Only accept left mouse button clicks)
                if e.buttons() == Qt.LeftButton:  
                    #Move window 
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()
            # ###############################################

        
        # ###############################################
        # Add click event/Mouse move event/drag event to the top header to move the window
        # ###############################################
        self.ui.main_header.mouseMoveEvent = moveWindow
        # ###############################################




        ########################################################################
        # STACKED PAGES (DEFAUT /CURRENT PAGE)/////////////////
        #Set the page that will be visible by default when the app is opened 
        self.ui.stackedWidget.setCurrentWidget(self.ui.home_page)
        # ###############################################
        # //////////////////////////////////////



        #################################################################################
        # Window Size grip
        #################################################################################
        QSizeGrip(self.ui.size_grip)
        #################################################################################
        # Window Size grip
        #################################################################################





        # ############################################
        # Show window
        self.show()
        # ###############################################




    # EKRANI BÜYÜT
    def restore_or_maximize_window(self):
        global WINDOW_SIZE #Boyutun büyütülmediğini göstermek için varsayılan değer sıfırdır.
        win_status = WINDOW_SIZE

        if win_status == 0:
        	# Eğer pencere tam ekran değilse
        	WINDOW_SIZE = 1 #Pencerenin ekranı kapladığını göstermek için değeri güncelle
        	self.showMaximized()

        	# Pencere büyütüldüğünde düğme simgesini güncelle
        	self.ui.restoreButton.setIcon(QtGui.QIcon(u":/icons/icons/cil-window-restore.png"))
        else:
        	# Pencere varsayılan boyutundaysa
            WINDOW_SIZE = 0 #Pencerenin küçültüldüğünü/normal boyuta ayarlandığını göstermek için değeri güncelleyin (800'e 400'dür)
            self.showNormal()

            # Pencere simge durumuna küçültüldüğünde güncelle düğmesi simgesi
            self.ui.restoreButton.setIcon(QtGui.QIcon(u":/icons/icons/cil-window-maximize.png"))#Show maximize icon


    def baglan(self):
        if self.baglanKontrol%2 == 0:
            print(self.ui.comboBox.currentText());
            print(self.ui.baudrate.currentText());
            self.ui.baglan.setStyleSheet("color: #ffffff;background-color: #c0392b;font-size: 14px;font-weight: bold;border: 0;padding: 10px;margin-right: 10px;")
            self.ui.baglan.setText("BAĞLANTIYI KES")
            self.baglanKontrol = self.baglanKontrol + 1
        else:
            self.ui.baglan.setStyleSheet("color: #ffffff;background-color: #27ae60;font-size: 14px;font-weight: bold;border: 0;padding: 10px;margin-right: 10px;")
            self.ui.baglan.setText("BAĞLAN")
            self.baglanKontrol = self.baglanKontrol + 1


# UYGULAMAYI ÇALIŞTIR
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
else:
	print(__name__, "hh")


