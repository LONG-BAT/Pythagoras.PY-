from PySide6.QtWidgets import QLineEdit, QMainWindow, QFormLayout, QWidget, QPushButton, QLabel
import math
class box(QMainWindow):
    def __init__(self):
        super().__init__()       
        label = QLabel()
        def textin(text):
            try: 
                leg1int = float(text)
                label.setText("")
            except:
                print("Error Invalid Char")
                error = "Error: Invalid Char"
                label.setText(error)
            def sq(leg1int):
                return leg1int * leg1int   
            global leg
            leg = sq(leg1int)
            print(leg)     
        lineedit = QLineEdit()
        lineedit.setMaxLength(10)
        lineedit.setPlaceholderText("Leg 1(a)")
        lineedit.textChanged.connect(textin)
        def textin2(text):
            try: 
                leg1int2 = float(text)
                label.setText("")
            except:
                print("Error Invalid Char")
                error = "Error: Invalid Char"
                label.setText(error)
            def sq(leg1int2):
                return leg1int2 * leg1int2   
            global leg2
            leg2 = sq(leg1int2)
            print(leg2)   
        lineedit2 = QLineEdit()
        lineedit2.setMaxLength(10)
        lineedit2.setPlaceholderText("Leg 2(b)")
        lineedit2.textChanged.connect(textin2)      
        def button_clicked():            
            try:               
                x = math.sqrt(leg + leg2)  
            except:
                label.setText("Error: Invalid char")
            print(x)
            x = str(x)
            p = "C="+x
            label.setText(p)      
        button = QPushButton("Solve")
        button.clicked.connect(button_clicked)
        layout = QFormLayout()
        cwidget = QWidget()    
        layout.addWidget(lineedit)
        layout.addWidget(lineedit2)
        layout.addWidget(button)
        layout.addWidget(label)
        cwidget.setLayout(layout)
        self.setCentralWidget(cwidget)

        