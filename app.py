import sys
from PyQt5 import QtCore
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QApplication, QGridLayout, QPushButton
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget

app = QApplication(sys.argv)


window = QWidget()
window.setWindowTitle('Monitoring Application')
window.setGeometry(100, 100, 900, 600)
#window.setFixedSize(800,600)
window.setStyleSheet('background-color: #161219; font-family: Roboto')
#window.move(2700, 200)
widgets = {
    "title":[],
    "laser":[],
    "laser_value":[],
    "altra_sonic":[],
    "altra_sonic_value":[],
    "bin":[],
    "bin_value":[],
    "o_btn":[],
    "r_btn":[],
    "g_btn":[],
    "msg_status":[],
    "full":[],
    "full_value":[],
    "empty":[],
    "empty_value":[],
    "back_btn":[]
    
}
grid = QGridLayout()
def clear_widgets():
    ''' hide all existing widgets and erase
        them from the global dictionary'''
    for widget in widgets:
        if widgets[widget] != []:
            widgets[widget][-1].hide()
        for i in range(0, len(widgets[widget])):
            widgets[widget].pop()

def home():
    clear_widgets()
    title = QLabel('<h2>Monitoring Application</h2>')
    title.setAlignment(QtCore.Qt.AlignCenter)
    title.setStyleSheet(
        "margin: 10px;"+
        "color: '#BA55D3';"
    )
    widgets["title"].append(title)

    laser = QPushButton('laser satus')
    
    laser.setStyleSheet(
        '''
        *{margin: 10px;
        color: 'black';
        font-size: 25px;
        background-color: #BA55D3;
        border: 1px solid #BA55D3;
        border-radius: 5px;
        padding: 10px;}
        *:hover{background-color:'#FFB6C1';}
        '''
  
    )
    widgets["laser"].append(laser)
    laser.clicked.connect(sensor_details)
    laser_value = QLabel('<h4>50%</h4>')
    laser_value.setAlignment(QtCore.Qt.AlignCenter)
    laser_value.style()
    laser_value.setStyleSheet(
    '''
        margin: 10px;
        color: 'black';
        font-size: 20px;
        background-color: #BA55D3;
        max-width: 50px;
        max-height:50px;
        border: 1px solid #BA55D3;
        border-radius:25px;
        padding: 0px;
        '''
    )
    widgets["laser_value"].append(laser_value)

    altra_sonic = QPushButton('altra_sonic satus')

    altra_sonic.setStyleSheet(
    '''
        *{margin: 10px;
        color: 'black';
        font-size: 25px;
        background-color: #BA55D3;
        border: 1px solid #BA55D3;
        border-radius: 5px;
        padding: 10px;}
        *:hover{background-color:'#FFB6C1';}
        '''
    )
    widgets["altra_sonic"].append(altra_sonic)
    altra_sonic.clicked.connect(sensor_details)

    altra_sonic_value = QLabel('<h4> 50% </h4>')
    altra_sonic_value.setAlignment(QtCore.Qt.AlignCenter)
    altra_sonic_value.setStyleSheet(
    '''
        margin: 10px;
        color: 'black';
        font-size: 20px;
        background-color: #BA55D3;
        max-width: 50px;
        max-height:50px;
        border: 1px solid #BA55D3;
        border-radius:25px;
        padding: 0px;
        
        '''
    )
    widgets["altra_sonic_value"].append(altra_sonic_value)


    bin = QLabel('<h2>BIN STATUS </h2>')
    bin.setAlignment(QtCore.Qt.AlignCenter)
    bin.setStyleSheet(
    "margin: 10px;"+
    "color: '#BA55D3';"
    )
    widgets["bin"].append(bin)

    bin_value = QLabel('<h3>50% </h3>')
    bin_value.setAlignment(QtCore.Qt.AlignCenter)
    bin_value.setStyleSheet(
    "margin: 10px;"+
    "color: '#BA55D3';"
    )
    widgets["bin_value"].append(bin_value)

    o_btn = QLabel('')
    o_btn.setAlignment(QtCore.Qt.AlignCenter)
    o_btn.setStyleSheet(
        '''
        margin: 10px;
        color: 'black';
        font-size: 20px;
        background-color: #f0d500;
        max-width: 50px;
        max-height:50px;
        border: 1px solid #f0d500;
        border-radius:25px;
        padding: 0px;
        '''
        )
    widgets["o_btn"].append(o_btn)

    r_btn = QLabel('')
    r_btn.setAlignment(QtCore.Qt.AlignCenter)
    r_btn.setStyleSheet(
        '''
        margin: 10px;
        color: 'black';
        font-size: 20px;
        background-color:rgba(243,32,19,0.1);
        max-width: 50px;
        max-height:50px;
        border: 1px solid transparent;
        border-radius:25px;
        padding: 0px;
        opacity: 0.5;
        '''
        )
    widgets["r_btn"].append(r_btn)

    g_btn = QLabel('')
    g_btn.setAlignment(QtCore.Qt.AlignCenter)
    g_btn.setStyleSheet(
        '''
        margin: 10px;
        color: 'black';
        font-size: 20px;
        background-color:rgba(35,209,12,0.1);
        max-width: 50px;
        max-height:50px;
        border: 1px solid transparent;
        border-radius:25px;
        padding: 0px;
        '''
        )
    widgets["g_btn"].append(g_btn)

    msg_status = QLabel('<h2>The bin status is normal!!</h2>')
    msg_status.setAlignment(QtCore.Qt.AlignCenter)
    msg_status.setStyleSheet(
         '''
            margin: 10px;
            border-radius: 45px;
            background-color: '#BA55D3';
            margin: 10px;
            color: 'black';
            font-size: 20px;
           
        '''
        )
    widgets["msg_status"].append(msg_status)

    grid.addWidget(widgets["title"][-1], 0, 0,1,5)
    grid.addWidget(widgets["laser"][-1], 1, 1, 1, 1)
    grid.addWidget(widgets["laser_value"][-1], 1, 3,1,1)
    grid.addWidget(widgets["altra_sonic"][-1], 2, 1, 1, 1)
    grid.addWidget(widgets["altra_sonic_value"][-1], 2, 3,1,1)
    grid.addWidget(widgets["bin"][-1], 3, 1,1,3)
    grid.addWidget(widgets["bin_value"][-1],4, 1,1,3)
    grid.addWidget(widgets["r_btn"][-1],1, 5,1,1)
    grid.addWidget(widgets["o_btn"][-1],2, 5,1,1)
    grid.addWidget(widgets["g_btn"][-1],3, 5,1,1)
    grid.addWidget(widgets["msg_status"][-1],6, 1,1,3)

def sensor_details():
    clear_widgets()
    full = QLabel('<h3>fullness ratio</h3>')
    full.setAlignment(QtCore.Qt.AlignCenter)
    full.setStyleSheet(
         '''
            margin: 10px 0;
            border-radius: 10px;
            background-color: '#BA55D3';
            padding: 10px 0;
            color: 'black';
            font-size: 20px;
            min-width:300px;
           
        '''
        )
    widgets["full"].append(full)

    full_value = QLabel('<h5>50%</h5>')
    full_value.setAlignment(QtCore.Qt.AlignCenter)
    full_value.style()
    full_value.setStyleSheet(
    '''
        margin: 0 0 0 200px;
        color: 'black';
        font-size: 20px;
        background-color: #BA55D3;
        max-width: 50px;
        max-height:50px;
        border: 1px solid #BA55D3;
        border-radius:25px;
        padding: 0px;
        '''
    )
    widgets["full_value"].append(full_value)

    empty = QLabel('<h3>void ratio</h3>')
    empty.setAlignment(QtCore.Qt.AlignCenter)
    empty.setStyleSheet(
         '''
            margin: 10px 0;
            border-radius: 10px;
            background-color: '#BA55D3';
            padding: 10px 0;
            color: 'black';
            font-size: 20px;
            min-width:300px;
           
        '''
        )
    widgets["empty"].append(empty)

    empty_value = QLabel('<h4>50%</h4>')
    empty_value.setAlignment(QtCore.Qt.AlignCenter)
    empty_value.style()
    empty_value.setStyleSheet(
     '''
        margin: 0 0 0 200px;
        color: 'black';
        font-size: 20px;
        background-color: #BA55D3;
        max-width: 50px;
        max-height:50px;
        border: 1px solid #BA55D3;
        border-radius:25px;
        padding: 0px;
        '''
    )
    widgets["empty_value"].append(empty_value)


    back_btn = QPushButton('back')
    back_btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    back_btn.setStyleSheet(
        "*{border-radius: 10px;" +
        "color: 'black';" +
        "background-color: '#BA55D3';"+
        "max-width: 100px;"+
        "max-height: 50px;"+
        "padding: 10px 20px;"
        "font-size: 25px;}"+
        "*:hover{background-color:'#FFB6C1';}"
    )
    widgets["back_btn"].append(back_btn)
    back_btn.clicked.connect(home)

    grid.addWidget(widgets["full"][-1], 0, 0,1,5)
    grid.addWidget(widgets["full_value"][-1], 0, 5,1,5)
    grid.addWidget(widgets["empty"][-1], 1, 0,1,5)
    grid.addWidget(widgets["empty_value"][-1], 1, 5,1,5)
    grid.addWidget(widgets["back_btn"][-1], 3, 3,1,5)



home()





# 4. Show your application's GUI
window.setLayout(grid)
window.show()

# 5. Run your application's event loop (or main loop)
sys.exit(app.exec())
