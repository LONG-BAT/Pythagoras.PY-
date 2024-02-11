from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon, QPixmap

import sys
from Pythagcalc import box

if __name__ == "__main__":    
    app = QApplication(sys.argv) 
    pixmap = QPixmap("./be.ico")
    icon = QIcon(pixmap)
    app.setStyle('Breeze')
    app.setWindowIcon(icon)
    pyt = box()   
    pyt.setWindowTitle("Pythagoras Theorem Calculator") 
    pyt.setGeometry(100,100,400,150)
    pyt.show()   
    app.exec()
