import sys
import binascii
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()
        filename=''
        output=''

    def setupUI(self):
        self.setGeometry(800, 300, 500, 500)
        self.setWindowTitle("Hello World")

        self.pushinput = QPushButton("File Open")
        self.pushinput.move(10, 10)
        self.pushinput.clicked.connect(self.pushinputClicked)

        self.pushoutput=QPushButton('Save File')
        self.pushoutput.move(10, 30)
        self.pushoutput.clicked.connect(self.pushoutputClicked)

        self.help=QPushButton('help')
        self.help.clicked.connect(self.pushhelpclicked)
        

        layout = QVBoxLayout()
        layout.addWidget(self.pushinput)
        layout.addWidget(self.pushoutput)
        layout.addWidget(self.help) 

        self.setLayout(layout)
    
    def pushhelpclicked(self):
        self.setWindowIcon(QIcon('help.png'))
        self.label=QLabel('open file ', self)


    def pushinputClicked(self):
        self.filename = QFileDialog.getOpenFileName(self)
        print(self.filename)
        f= open(MyWindow.filename, 'rb')
        content = f.read()
        content=str(binascii.hexlify(content)) 

    def pushoutputClicked(self):
        self.output=QFileDialog.getOpenFileName(self)
        
       

       
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()



if '504b0304' in MyWindow.content: #zip 파일
    sta=MyWindow.content.find('504b')
    fo=open(MyWindow.output+'zip','wb')
    c = binascii.unhexlify(MyWindow.content[sta:-1])
    fo.write(c)
    fo.close()

elif 'ffd8' in MyWindow.content: #jpg 파일
    sta=MyWindow.content.find('ffd8')
    MyWindow.content=MyWindow.content[sta:-1]
    if 'ffd9' in MyWindow.content:
        fin=MyWindow.content.find('ffd9')
        fo = open(MyWindow.output+'.jpg', 'wb')
        c=binascii.unhexlify(MyWindow.content[sta:fin+4])
        fo.write(c)
        fo.close()

elif '89504e470d0a1a0a' in MyWindow.content: #png 파일
    sta=MyWindow.content.find('89504e470d0a1a0a')
    MyWindow.content=MyWindow.content[sta-1]
    if '49454e44Ae42608289' in MyWindow.content:
        fin=MyWindow.content.find('49454e44Ae42608289')
        fo = open(MyWindow.output+'.png')
        fo.write(c)
        fo.close()

elif '424d' in MyWindow.content: #bmp 파일
    sta=MyWindow.content.find('424d')
    fo=open(MyWindow.output+'.bmp', 'wb')
    c=binascii.unhexlify(MyWindow.content[sta:-1])
    fo.write(c)
    fo.close()    
else:
    print("error")