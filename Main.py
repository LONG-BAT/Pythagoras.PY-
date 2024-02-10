from PySide6.QtWidgets import QApplication
import sys
from Pythagcalc import box

if __name__ == "__main__":    
    app = QApplication(sys.argv)  
    pyt = box()   
    pyt.setWindowTitle("Pythagoras Theorem Calculator") 
    pyt.show()   
    app.exec()
