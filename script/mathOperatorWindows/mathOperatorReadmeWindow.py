# mathOperatorReadmeWindow.py
# Author: hoshina
# Created: 2024/05/26
# brief: 数学演算機能の説明を表示するウィンドウ


from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QGraphicsView, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSlider, QSpacerItem, QSpinBox, QStatusBar,
    QTabWidget, QVBoxLayout, QWidget, QFileDialog, QStyle, QFrame,
    QTextEdit, QMessageBox, QDialog)

class MathOperatorReadmeWindow(QDialog):
    FONT = QFont()
    FONT.setPointSize(11)

    def __init__(self, parent=None):
        super().__init__(parent)

        # variable
        self.presetMap_ = {}
        self.currentPreset_ = ""
        self.isPresetSelected_ = False

        # setup
        self.setupUi_()
        self.initializePresets_()

    def isPresetSelected(self):
        return self.isPresetSelected_
    
    def getPreset(self):
        self.isPresetSelected_ = False
        return self.currentPreset_

    # private methods ---------------------------------------
    def setupUi_(self):
        self.setWindowTitle("Math Operator Readme")
        self.setGeometry(100, 100, 800, 400)
        windowIcon = QApplication.style().standardIcon(QStyle.SP_TitleBarMenuButton)
        self.setWindowIcon(windowIcon)
        self.setFont(self.FONT)

        self.layout_ = QHBoxLayout(self)

        # objects
        self.textEdit_ = QTextEdit()
        self.groupBoxPresets_ = QGroupBox()

        # layout
        self.layout_.addWidget(self.textEdit_)
        self.layout_.addWidget(self.groupBoxPresets_)

        # textEdit
        self.textEdit_.setObjectName("textEdit")
        self.textEdit_.setReadOnly(True)
        self.textEdit_.setPlainText("信号に対する数学演算を行う機能です。\n"
                                    "使える機能：\n"
                                    "・四則演算：+,- など通常通りに入力\n"
                                    "（例）u1 + u2：２つのデータを足す\n"
                                    "・数学関数：sin,exp などの基本関数\n"
                                    "（例）sin(u1)：１つ目のデータの正弦\n"
                                    "・データの切り取り：[start:stop:step]でデータを切り取る\n"
                                    "（例）u1[0:100]：最初から99番目までのデータを抽出\n"
                                    "・データを作る：range,linspace などでデータを作る\n"
                                    "（例）linspace(0,1,100)：0-1の範囲で等間隔に100個データを作成\n")
        
        # presets
        self.groupBoxPresets_.setTitle("Presets")
        self.groupBoxPresets_.setObjectName("groupBoxPresets")
        self.groupBoxPresets_.setFixedWidth(200)
        self.layoutPresets_ = QVBoxLayout()
        self.groupBoxPresets_.setLayout(self.layoutPresets_)
        self.listPresets_ = QListWidget()
        self.listPresets_.setObjectName("listPresets")
        self.lineEditPreset_ = QLineEdit()
        self.lineEditPreset_.setReadOnly(True)
        self.lineEditPreset_.setObjectName("lineEditPreset")

        self.layoutPresets_.addWidget(self.listPresets_)
        self.layoutPresets_.addWidget(self.lineEditPreset_)

        # event
        self.setupEvent_()

    def setupEvent_(self):
        self.listPresets_.itemClicked.connect(self.clickedListPreset_)
        self.listPresets_.itemDoubleClicked.connect(self.doubleClickedListPreset_)

    def initializePresets_(self):
        text = "time"
        self.presetMap_[text] = "linspace(0, 1, 100)"
        self.listPresets_.addItem(text)

        text = "derivative"
        self.presetMap_[text] = "u1[1:] - u1[:-1]"
        self.listPresets_.addItem(text)

        text = "integral"
        self.presetMap_[text] = "coming soon..."
        self.listPresets_.addItem(text)

        text = "fft amp"
        self.presetMap_[text] = "abs(fft.fft(u1)/(len(u1)/2))"
        self.listPresets_.addItem(text)

        text = "fft freq (u1 is time data)"
        self.presetMap_[text] = "fft.fftfreq(len(u1), d = u1[1] - u1[0])"
        self.listPresets_.addItem(text)

    # event handlers ----------------------------------
    def clickedListPreset_(self):
        item = self.listPresets_.currentItem()
        if item is None:
            return
        
        text = item.text()
        self.lineEditPreset_.setText(self.presetMap_[text])

    def doubleClickedListPreset_(self):
        item = self.listPresets_.currentItem()
        if item is None:
            return
        
        text = item.text()
        self.currentPreset_ = self.presetMap_[text]
        self.isPresetSelected_ = True
