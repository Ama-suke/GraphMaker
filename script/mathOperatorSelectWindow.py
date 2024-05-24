# mathOperatorSelectWindow.py
# Author: hoshina
# Created: 2024/05/08
# brief: データに対する演算子を選択するウィンドウ

from __future__ import annotations

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
from graphPlotter import GraphPlotter 
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from myWidgets.LabeledWidget import my_widget
import sys
from numpy import *

# include guard
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ui_form import Ui_GraphMaker

class MathOperatorOption:
    def __init__(self):
        self.dataName = ""
        self.data1Name = ""
        self.data2Name = ""
        self.mathOperatorStr = ""


class MathOperatorSelectWindow(QDialog):
    WINDOW_SIZE = QSize(1000, 500)
    
    FONT = QFont()
    FONT.setPointSize(12)

    def __init__(self, parent=None):
        super().__init__(parent)
    
        # variables
        self.plotter_ = GraphPlotter()
        self.dataDict_ = {}
        self.operatorOptions_ = []
        self.isError_ = False
        self.isValid_ = False
        self.resultOperatorOption_ = MathOperatorOption()
        self.resultDataDict_ = {}

        # initialize plotter
        self.plotter_.setXDataIndex(0)
        self.plotter_.setYDataIndex(1)
        self.plotter_.setLineColors(["Red"])
        self.plotter_.setLineStiles(["-"])
        self.plotter_.setLineWidth([1])

        self.setupUi()

    def setupUi(self):
        # settings
        self.setObjectName("MathOperatorSelectWindow")
        self.setWindowTitle("Math Operator Select")
        self.resize(MathOperatorSelectWindow.WINDOW_SIZE)
        windowIcon = QApplication.style().standardIcon(QStyle.SP_TitleBarMenuButton)
        self.setWindowIcon(windowIcon)

        # layout settings begin --------------------------------

        # main
        self.horizontalLayout_ = QHBoxLayout(self)
        self.horizontalLayout_.setObjectName("horizontalLayout")

        # objects
        self.groupBoxDataSelect_ = QGroupBox(self)
        self.groupBoxPreview_ = QGroupBox(self)
        
        # layout
        self.horizontalLayout_.addWidget(self.groupBoxDataSelect_)
        self.horizontalLayout_.addWidget(self.groupBoxPreview_)

        # Data select group begin -----------------------------
        # setting
        self.groupBoxDataSelect_.setObjectName("groupBoxDataSelect")
        self.groupBoxDataSelect_.setTitle("Data Select")
        self.groupBoxDataSelect_.setMinimumWidth(400)
        self.groupBoxDataSelect_.setFont(MathOperatorSelectWindow.FONT)
        self.horizontalLayoutDataSelect_ = QHBoxLayout(self.groupBoxDataSelect_)
        self.horizontalLayoutDataSelect_.setObjectName("verticalLayoutDataSelect")

        # objects
        self.listWidgetDataSelect_ = QListWidget(self.groupBoxDataSelect_)
        self.verticalLayoutDataSelect_ = QVBoxLayout(self.groupBoxDataSelect_)

        # layout
        self.horizontalLayoutDataSelect_.addWidget(self.listWidgetDataSelect_)
        self.horizontalLayoutDataSelect_.addLayout(self.verticalLayoutDataSelect_)

        # Data List begin -------------------------------
        # setting
        self.listWidgetDataSelect_.setObjectName("listWidgetDataSelect")
        self.listWidgetDataSelect_.setFont(MathOperatorSelectWindow.FONT)
        self.listWidgetDataSelect_.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.listWidgetDataSelect_.setMaximumSize(200, 16777215)
        # Data List end -------------------------------

        # Data setting begin -------------------------------
        # setting
        self.verticalLayoutDataSelect_.setObjectName("verticalLayoutDataSelect")

        # objects
        self.labelNewData_ = QLabel(self.groupBoxDataSelect_)
        self.lineEditNewData_ = QLineEdit(self.groupBoxDataSelect_)
        self.lineEditData1_ = my_widget.LabeledLineEdit(self.groupBoxDataSelect_, False, False)
        self.lineEditData2_ = my_widget.LabeledLineEdit(self.groupBoxDataSelect_, False, False)
        self.spacerSeparateLine_ = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.separateLineDataSelect_ = QFrame(self.groupBoxDataSelect_)
        self.labelMathOperator_ = QLabel(self.groupBoxDataSelect_)
        self.lineEditMathOperator_ = QLineEdit(self.groupBoxDataSelect_)
        self.labelConsoleLog_ = QLabel(self.groupBoxDataSelect_)
        self.textEditConsoleLog_ = QTextEdit(self.groupBoxDataSelect_)
        self.spacerDataSelect_ = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.horizontalLayoutDataSelectPushButton_ = QHBoxLayout()
        self.pushButtonAddData_ = QPushButton(self.groupBoxDataSelect_)

        # layout
        self.verticalLayoutDataSelect_.addWidget(self.labelNewData_)
        self.verticalLayoutDataSelect_.addWidget(self.lineEditNewData_)
        self.verticalLayoutDataSelect_.addItem(self.spacerSeparateLine_)
        self.verticalLayoutDataSelect_.addLayout(self.lineEditData1_.getLayout())
        self.verticalLayoutDataSelect_.addLayout(self.lineEditData2_.getLayout())
        self.verticalLayoutDataSelect_.addItem(self.spacerSeparateLine_)
        self.verticalLayoutDataSelect_.addWidget(self.separateLineDataSelect_)
        self.verticalLayoutDataSelect_.addItem(self.spacerSeparateLine_)
        self.verticalLayoutDataSelect_.addWidget(self.labelMathOperator_)
        self.verticalLayoutDataSelect_.addWidget(self.lineEditMathOperator_)
        self.verticalLayoutDataSelect_.addWidget(self.labelConsoleLog_)
        self.verticalLayoutDataSelect_.addWidget(self.textEditConsoleLog_)
        self.verticalLayoutDataSelect_.addItem(self.spacerDataSelect_)
        self.verticalLayoutDataSelect_.addLayout(self.horizontalLayoutDataSelectPushButton_)

        # objects settings
        self.labelNewData_.setObjectName("labelDataName")
        self.labelNewData_.setText("New Data:")
        self.labelNewData_.setFont(MathOperatorSelectWindow.FONT)
        self.lineEditNewData_.setObjectName("lineEditNewData")
        self.lineEditNewData_.setFont(MathOperatorSelectWindow.FONT)
        self.lineEditData1_.setObjectName("lineEditData1")
        self.lineEditData1_.setFont(MathOperatorSelectWindow.FONT)
        self.lineEditData1_.setLabelText("Data1 (u1):")
        self.lineEditData2_.setObjectName("lineEditData2")
        self.lineEditData2_.setFont(MathOperatorSelectWindow.FONT)
        self.lineEditData2_.setLabelText("Data2 (u2):")
        self.separateLineDataSelect_.setObjectName("separateLineDataSelect")
        self.separateLineDataSelect_.setFrameShape(QFrame.HLine)
        self.separateLineDataSelect_.setFrameShadow(QFrame.Sunken)
        self.labelMathOperator_.setObjectName("labelMathOperator")
        self.labelMathOperator_.setText("Math Operator:")
        self.labelMathOperator_.setFont(MathOperatorSelectWindow.FONT)
        self.lineEditMathOperator_.setObjectName("lineEditMathOperator")
        self.lineEditMathOperator_.setFont(MathOperatorSelectWindow.FONT)
        self.labelConsoleLog_.setObjectName("labelConsoleLog")
        self.labelConsoleLog_.setText("Console Log:")
        self.labelConsoleLog_.setFont(MathOperatorSelectWindow.FONT)
        self.textEditConsoleLog_.setObjectName("textEditConsoleLog")
        self.textEditConsoleLog_.setFont(MathOperatorSelectWindow.FONT)
        self.textEditConsoleLog_.setReadOnly(True)
        self.horizontalLayoutDataSelectPushButton_.setObjectName("horizontalLayoutDataSelectPushButton")
        self.horizontalLayoutDataSelectPushButton_.addItem(self.spacerDataSelect_)
        self.horizontalLayoutDataSelectPushButton_.addWidget(self.pushButtonAddData_)
        self.pushButtonAddData_.setObjectName("pushButtonAddData")
        self.pushButtonAddData_.setText("Add")
        # Data select group end -------------------------------

        # Preview group begin ---------------------------------
        # setting
        self.groupBoxPreview_.setObjectName("groupBoxPreview")
        self.groupBoxPreview_.setTitle("Preview")
        self.groupBoxPreview_.setFont(MathOperatorSelectWindow.FONT)
        self.verticalLayoutPreview_ = QVBoxLayout(self.groupBoxPreview_)
        self.verticalLayoutPreview_.setObjectName("verticalLayoutPreview")

        # objects
        self.figureCanvasPlotPreview_ = FigureCanvas(self.plotter_.getFigure())

        # layout
        self.verticalLayoutPreview_.addWidget(self.figureCanvasPlotPreview_)

        # objects settings
        self.figureCanvasPlotPreview_.setObjectName("figureCanvasPlotPreview")
        self.figureCanvasPlotPreview_.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.figureCanvasPlotPreview_.setMaximumSize(400, 16777215)
        # Preview group end -----------------------------------
        # layout settings end ----------------------------------

        # event handlers
        self.setupEvent()

    def setupEvent(self):
        # event handlers
        self.listWidgetDataSelect_.itemDoubleClicked.connect(self.doubleClickedDataList_)
        self.pushButtonAddData_.clicked.connect(self.clickedAddData_)
        self.lineEditNewData_.textChanged.connect(self.changedNewDataName_)
        self.lineEditData1_.setTextChangedCallback(self.changedData1_)
        self.lineEditData2_.setTextChangedCallback(self.changedData2_)
        self.lineEditMathOperator_.textChanged.connect(self.changedMathOperator_)

    def initializeUi(self):
        self.dataDict_ = {}
        self.resultDataDict_ = {}
        self.resultOperatorOption_ = MathOperatorOption()
        self.isError_ = False
        self.isValid_ = False
        self.listWidgetDataSelect_.clear()
        self.lineEditNewData_.setText("Math")
        self.lineEditData1_.setText("")
        self.lineEditData2_.setText("")
        self.lineEditMathOperator_.setText("u1 + u2")
        self.textEditConsoleLog_.setText("")

    def showWindow(self, dataDict: dict, operatorOptions: list):
        self.show() 

        self.initializeUi()

        # initialize
        # data
        self.dataDict_ = dataDict
        self.operatorOptions_ = operatorOptions
        
        # data list
        if self.dataDict_ is not None:
            for key in self.dataDict_.keys():
                self.listWidgetDataSelect_.addItem(key)

        # operator list
        if self.operatorOptions_ is not None:
            self.setMathOperatorFromList_("Math")

        self.diagnoseError_()
        
    def isMathOperatorValid(self, data1Name: str, data2Name: str, mathOperator: str):
        try:
            if data1Name in self.dataDict_.keys():
                data1List = self.dataDict_[data1Name]
                data1 = array(data1List)
            if data2Name in self.dataDict_.keys():
                data2List = self.dataDict_[data2Name]
                data2 = array(data2List)
            eval(mathOperator.replace("u1", "data1").replace("u2", "data2"))
            return True
        except:
            return False

    def getResults(self):
        return self.resultOperatorOption_, self.resultDataDict_
    
    def isValid(self):
        return self.isValid_
    
    # private methods ---------------------------------------
    def setMathOperatorFromList_(self, mathName: str):
        for operatorOption in self.operatorOptions_:
            if operatorOption.dataName == mathName:
                self.lineEditNewData_.setText(operatorOption.dataName)
                self.lineEditData1_.setText(operatorOption.data1Name)
                self.lineEditData2_.setText(operatorOption.data2Name)
                self.lineEditMathOperator_.setText(operatorOption.mathOperatorStr)
                break
    
    def plotGraph_(self):
        if self.isError_:
            self.plotter_.clearPlot()
            return

        result = self.computeMathOperator_(self.lineEditData1_.getText(), \
                                          self.lineEditData2_.getText(), \
                                          self.lineEditMathOperator_.text())
        if result is None:
            self.plotter_.clearPlot()
            return
        
        self.plotter_.clearPlot()

        xData = [i for i in range(len(result))]
        dataList = [xData, \
                    result]
        self.plotter_.setData(dataList)
        self.plotter_.plot()
        self.figureCanvasPlotPreview_.draw()

        self.resultOperatorOption_.dataName = self.lineEditNewData_.text()
        self.resultOperatorOption_.data1Name = self.lineEditData1_.getText()
        self.resultOperatorOption_.data2Name = self.lineEditData2_.getText()
        self.resultOperatorOption_.mathOperatorStr = self.lineEditMathOperator_.text()
    

    def computeMathOperator_(self, data1Name: str, data2Name: str, mathOperator: str):
        if data1Name in self.dataDict_.keys():
            data1List = self.dataDict_[data1Name]
            data1 = array(data1List)
        if data2Name in self.dataDict_.keys():
            data2List = self.dataDict_[data2Name]
            data2 = array(data2List)

        if self.isMathOperatorValid(data1Name, data2Name, mathOperator):
            result = eval(mathOperator.replace("u1", "data1").replace("u2", "data2"))
            return result
        else:
            return None

    def diagnoseError_(self):
        errorMessage = ""

        # check if new data name is empty
        if self.lineEditNewData_.text() == "":
            self.isError_ = True
            errorMessage += "New Data Name is empty.\n"

        # check if data1 and data2 are empty
        if self.lineEditData1_.getText() == "" and self.lineEditData2_.getText() == "":
            self.isError_ = True
            errorMessage += "Data1 and Data2 are empty.\n"

        # check if data1 is invalid
        data1Text = self.lineEditData1_.getText()
        if data1Text != "":
            if not data1Text in self.dataDict_.keys():
                self.isError_ = True
                errorMessage += "Data1 is invalid.\n"

        # check if data2 is invalid
        data2Text = self.lineEditData2_.getText()
        if data2Text != "":
            if not data2Text in self.dataDict_.keys():
                self.isError_ = True
                errorMessage += "Data2 is invalid.\n"

        # check if data1 and data2 have different length
        if self.lineEditData1_.getText() in self.dataDict_.keys() and\
              self.lineEditData2_.getText() in self.dataDict_.keys():
            data1Len = len(self.dataDict_[self.lineEditData1_.getText()])
            data2Len = len(self.dataDict_[self.lineEditData2_.getText()])
            if data1Len != data2Len:
                self.isError_ = True
                errorMessage += "Data1 and Data2 have different length.\n"

        # check if math operator is empty
        if self.lineEditMathOperator_.text() == "":
            self.isError_ = True
            errorMessage += "Math Operator is empty.\n"

        # check if math operator is invalid
        if not self.isMathOperatorValid(self.lineEditData1_.getText(), \
                                        self.lineEditData2_.getText(), \
                                        self.lineEditMathOperator_.text()):
            self.isError_ = True
            errorMessage += "Math Operator is invalid.\n"

        # no error
        if errorMessage == "":
            self.isError_ = False
            errorMessage = "Correct!"

        # display the error message
        self.textEditConsoleLog_.setText(errorMessage)

    # event handlers start ----------------------------------
    def doubleClickedDataList_(self):
        if self.lineEditData1_.getText() == "":
            self.lineEditData1_.setText(self.listWidgetDataSelect_.currentItem().text())

        elif self.lineEditData2_.getText() == "":
            self.lineEditData2_.setText(self.listWidgetDataSelect_.currentItem().text())

        self.diagnoseError_()
        self.plotGraph_()

    def changedNewDataName_(self, text: str):
        self.setMathOperatorFromList_(text)
        
        self.diagnoseError_()
        self.plotGraph_()

    def changedData1_(self, text: str):
        self.diagnoseError_()
        self.plotGraph_()

    def changedData2_(self, text: str):
        self.diagnoseError_()
        self.plotGraph_()

    def changedMathOperator_(self):
        self.diagnoseError_()
        self.plotGraph_()

    def clickedAddData_(self):
        if self.isError_:
            QMessageBox.critical(self, "Error", "An error occurred. Please fix it.")
            return
        
        if self.lineEditNewData_.text() in self.dataDict_.keys():
            if self.lineEditNewData_.text() in self.dataDict_.keys():
                reply = QMessageBox.question(self, 'Confirmation', 'Data with the same name already exists. Do you want to overwrite it?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if reply != QMessageBox.Yes:
                    return
        
        # add data
        data_name = self.lineEditNewData_.text()
        self.listWidgetDataSelect_.addItem(data_name)
        self.resultDataDict_[data_name] = list(\
            self.computeMathOperator_(self.lineEditData1_.getText(), \
                                     self.lineEditData2_.getText(), \
                                     self.lineEditMathOperator_.text()))
        
        self.isValid_ = True

        self.close()
    # event handlers end ------------------------------------
        


if __name__ == "__main__":
    app = QApplication([])
    window = MathOperatorSelectWindow(None)
    window.showWindow(None, None)
    sys.exit(app.exec())