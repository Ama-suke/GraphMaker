# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

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
    QTabWidget, QVBoxLayout, QWidget, QFileDialog)
import csv
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class Ui_GraphMaker(object):
    def setupUi(self, GraphMaker):
        if not GraphMaker.objectName():
            GraphMaker.setObjectName(u"GraphMaker")
        GraphMaker.resize(900, 550)
        self.actionLoadTable = QAction(GraphMaker)
        self.actionLoadTable.setObjectName(u"actionLoadTable") 
        self.actionSaveTable = QAction(GraphMaker)
        self.actionSaveTable.setObjectName(u"actionSaveTable")
        self.actionLoadSetting = QAction(GraphMaker)
        self.actionLoadSetting.setObjectName(u"actionLoadSetting")
        self.actionSaveSetting = QAction(GraphMaker)
        self.actionSaveSetting.setObjectName(u"actionSaveSetting")
        self.actionUserManual = QAction(GraphMaker)
        self.actionUserManual.setObjectName(u"actionUserManual")
        self.centralwidget = QWidget(GraphMaker)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMaximumSize(QSize(400, 16777215))
        font = QFont()
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabDataSelector = QWidget()
        self.tabDataSelector.setObjectName(u"tabDataSelector")
        self.horizontalLayout_14 = QHBoxLayout(self.tabDataSelector)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.listDataList = QListWidget(self.tabDataSelector)
        QListWidgetItem(self.listDataList)
        self.listDataList.setObjectName(u"listDataList")
        self.listDataList.setMinimumSize(QSize(170, 0))
        self.listDataList.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_14.addWidget(self.listDataList)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalSpacer_4 = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_9.addItem(self.verticalSpacer_4)

        self.buttonAddXAxis = QPushButton(self.tabDataSelector)
        self.buttonAddXAxis.setObjectName(u"buttonAddXAxis")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonAddXAxis.sizePolicy().hasHeightForWidth())
        self.buttonAddXAxis.setSizePolicy(sizePolicy)
        self.buttonAddXAxis.setMaximumSize(QSize(30, 20))

        self.verticalLayout_9.addWidget(self.buttonAddXAxis)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_3)

        self.buttonAddYAxis = QPushButton(self.tabDataSelector)
        self.buttonAddYAxis.setObjectName(u"buttonAddYAxis")
        sizePolicy.setHeightForWidth(self.buttonAddYAxis.sizePolicy().hasHeightForWidth())
        self.buttonAddYAxis.setSizePolicy(sizePolicy)
        self.buttonAddYAxis.setMaximumSize(QSize(30, 20))

        self.verticalLayout_9.addWidget(self.buttonAddYAxis)

        self.buttonRemoveYAxis = QPushButton(self.tabDataSelector)
        self.buttonRemoveYAxis.setObjectName(u"buttonRemoveYAxis")
        sizePolicy.setHeightForWidth(self.buttonRemoveYAxis.sizePolicy().hasHeightForWidth())
        self.buttonRemoveYAxis.setSizePolicy(sizePolicy)
        self.buttonRemoveYAxis.setMaximumSize(QSize(30, 20))

        self.verticalLayout_9.addWidget(self.buttonRemoveYAxis)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_5)


        self.horizontalLayout_14.addLayout(self.verticalLayout_9)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_10 = QLabel(self.tabDataSelector)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_3.addWidget(self.label_10)

        self.listXAxisData = QListWidget(self.tabDataSelector)
        self.listXAxisData.setObjectName(u"listXAxisData")
        sizePolicy.setHeightForWidth(self.listXAxisData.sizePolicy().hasHeightForWidth())
        self.listXAxisData.setSizePolicy(sizePolicy)
        self.listXAxisData.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout_3.addWidget(self.listXAxisData)

        self.label_9 = QLabel(self.tabDataSelector)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_3.addWidget(self.label_9)

        self.listYAxisData = QListWidget(self.tabDataSelector)
        self.listYAxisData.setObjectName(u"listYAxisData")
        self.listYAxisData.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_3.addWidget(self.listYAxisData)


        self.horizontalLayout_14.addLayout(self.verticalLayout_3)

        self.tabWidget.addTab(self.tabDataSelector, "")
        self.tabAxis = QWidget()
        self.tabAxis.setObjectName(u"tabAxis")
        self.verticalLayout_4 = QVBoxLayout(self.tabAxis)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox = QGroupBox(self.tabAxis)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(90, 0))

        self.horizontalLayout_3.addWidget(self.label)

        self.lineEditXAxisText = QLineEdit(self.groupBox)
        self.lineEditXAxisText.setObjectName(u"lineEditXAxisText")

        self.horizontalLayout_3.addWidget(self.lineEditXAxisText)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(90, 0))

        self.horizontalLayout_2.addWidget(self.label_2)

        self.sliderXAxisFontSize = QSlider(self.groupBox)
        self.sliderXAxisFontSize.setObjectName(u"sliderXAxisFontSize")
        self.sliderXAxisFontSize.setOrientation(Qt.Horizontal)

        self.horizontalLayout_2.addWidget(self.sliderXAxisFontSize)

        self.spinBoxXAxisFontSize = QSpinBox(self.groupBox)
        self.spinBoxXAxisFontSize.setObjectName(u"spinBoxXAxisFontSize")

        self.horizontalLayout_2.addWidget(self.spinBoxXAxisFontSize)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.checkBoxXAxisMinLimit = QCheckBox(self.groupBox)
        self.checkBoxXAxisMinLimit.setObjectName(u"checkBoxXAxisMinLimit")
        self.checkBoxXAxisMinLimit.setMinimumSize(QSize(90, 0))

        self.horizontalLayout_4.addWidget(self.checkBoxXAxisMinLimit)

        self.sliderXAxisMinLimit = QSlider(self.groupBox)
        self.sliderXAxisMinLimit.setObjectName(u"sliderXAxisMinLimit")
        self.sliderXAxisMinLimit.setOrientation(Qt.Horizontal)

        self.horizontalLayout_4.addWidget(self.sliderXAxisMinLimit)

        self.spinBoxXAxisMinLimit = QDoubleSpinBox(self.groupBox)
        self.spinBoxXAxisMinLimit.setObjectName(u"spinBoxXAxisMinLimit")

        self.horizontalLayout_4.addWidget(self.spinBoxXAxisMinLimit)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.checkBoxXAxisMaxLimit = QCheckBox(self.groupBox)
        self.checkBoxXAxisMaxLimit.setObjectName(u"checkBoxXAxisMaxLimit")
        self.checkBoxXAxisMaxLimit.setMinimumSize(QSize(90, 0))

        self.horizontalLayout_5.addWidget(self.checkBoxXAxisMaxLimit)

        self.sliderXAxiMaxLimit = QSlider(self.groupBox)
        self.sliderXAxiMaxLimit.setObjectName(u"sliderXAxiMaxLimit")
        self.sliderXAxiMaxLimit.setOrientation(Qt.Horizontal)

        self.horizontalLayout_5.addWidget(self.sliderXAxiMaxLimit)

        self.SpinBoxXAxisMaxLimit = QDoubleSpinBox(self.groupBox)
        self.SpinBoxXAxisMaxLimit.setObjectName(u"SpinBoxXAxisMaxLimit")

        self.horizontalLayout_5.addWidget(self.SpinBoxXAxisMaxLimit)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)


        self.verticalLayout_4.addWidget(self.groupBox)

        self.groupBox_3 = QGroupBox(self.tabAxis)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QSize(90, 0))

        self.horizontalLayout_6.addWidget(self.label_4)

        self.lineEditYAxisText = QLineEdit(self.groupBox_3)
        self.lineEditYAxisText.setObjectName(u"lineEditYAxisText")

        self.horizontalLayout_6.addWidget(self.lineEditYAxisText)


        self.verticalLayout_7.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(90, 0))

        self.horizontalLayout_7.addWidget(self.label_5)

        self.sliderYAxisFontSize = QSlider(self.groupBox_3)
        self.sliderYAxisFontSize.setObjectName(u"sliderYAxisFontSize")
        self.sliderYAxisFontSize.setOrientation(Qt.Horizontal)

        self.horizontalLayout_7.addWidget(self.sliderYAxisFontSize)

        self.spinBoxYAxisFontSize = QSpinBox(self.groupBox_3)
        self.spinBoxYAxisFontSize.setObjectName(u"spinBoxYAxisFontSize")

        self.horizontalLayout_7.addWidget(self.spinBoxYAxisFontSize)


        self.verticalLayout_7.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.checkBoxYAxisMinLimit = QCheckBox(self.groupBox_3)
        self.checkBoxYAxisMinLimit.setObjectName(u"checkBoxYAxisMinLimit")
        self.checkBoxYAxisMinLimit.setMinimumSize(QSize(90, 0))

        self.horizontalLayout_8.addWidget(self.checkBoxYAxisMinLimit)

        self.sliderYAxisMinLimit = QSlider(self.groupBox_3)
        self.sliderYAxisMinLimit.setObjectName(u"sliderYAxisMinLimit")
        self.sliderYAxisMinLimit.setOrientation(Qt.Horizontal)

        self.horizontalLayout_8.addWidget(self.sliderYAxisMinLimit)

        self.spinBoxYAxisMinLimit = QDoubleSpinBox(self.groupBox_3)
        self.spinBoxYAxisMinLimit.setObjectName(u"spinBoxYAxisMinLimit")

        self.horizontalLayout_8.addWidget(self.spinBoxYAxisMinLimit)


        self.verticalLayout_7.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.checkBoxYAxisMaxLimit = QCheckBox(self.groupBox_3)
        self.checkBoxYAxisMaxLimit.setObjectName(u"checkBoxYAxisMaxLimit")
        self.checkBoxYAxisMaxLimit.setMinimumSize(QSize(90, 0))

        self.horizontalLayout_9.addWidget(self.checkBoxYAxisMaxLimit)

        self.sliderYAxisMaxLimit = QSlider(self.groupBox_3)
        self.sliderYAxisMaxLimit.setObjectName(u"sliderYAxisMaxLimit")
        self.sliderYAxisMaxLimit.setOrientation(Qt.Horizontal)

        self.horizontalLayout_9.addWidget(self.sliderYAxisMaxLimit)

        self.spinBoxYAxisMaxLimit = QDoubleSpinBox(self.groupBox_3)
        self.spinBoxYAxisMaxLimit.setObjectName(u"spinBoxYAxisMaxLimit")

        self.horizontalLayout_9.addWidget(self.spinBoxYAxisMaxLimit)


        self.verticalLayout_7.addLayout(self.horizontalLayout_9)


        self.verticalLayout_4.addWidget(self.groupBox_3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.tabWidget.addTab(self.tabAxis, "")
        self.tabPlot = QWidget()
        self.tabPlot.setObjectName(u"tabPlot")
        self.verticalLayout_8 = QVBoxLayout(self.tabPlot)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.groupBox_2 = QGroupBox(self.tabPlot)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFont(font)
        self.verticalLayout = QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QSize(80, 0))
        self.label_6.setFont(font)

        self.horizontalLayout_11.addWidget(self.label_6)

        self.sliderLineWidth = QSlider(self.groupBox_2)
        self.sliderLineWidth.setObjectName(u"sliderLineWidth")
        self.sliderLineWidth.setFont(font)
        self.sliderLineWidth.setOrientation(Qt.Horizontal)

        self.horizontalLayout_11.addWidget(self.sliderLineWidth)

        self.spinBoxLineWidth = QSpinBox(self.groupBox_2)
        self.spinBoxLineWidth.setObjectName(u"spinBoxLineWidth")
        self.spinBoxLineWidth.setFont(font)

        self.horizontalLayout_11.addWidget(self.spinBoxLineWidth)


        self.verticalLayout.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMinimumSize(QSize(80, 0))
        self.label_7.setFont(font)

        self.horizontalLayout_12.addWidget(self.label_7)

        self.comboBoxLineColorLine = QComboBox(self.groupBox_2)
        self.comboBoxLineColorLine.setObjectName(u"comboBoxLineColorLine")
        self.comboBoxLineColorLine.setFont(font)

        self.horizontalLayout_12.addWidget(self.comboBoxLineColorLine)

        self.paletteLineColor = QWidget(self.groupBox_2)
        self.paletteLineColor.setObjectName(u"paletteLineColor")
        sizePolicy.setHeightForWidth(self.paletteLineColor.sizePolicy().hasHeightForWidth())
        self.paletteLineColor.setSizePolicy(sizePolicy)
        self.paletteLineColor.setMinimumSize(QSize(20, 0))

        self.horizontalLayout_12.addWidget(self.paletteLineColor)


        self.verticalLayout.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMinimumSize(QSize(80, 0))
        self.label_8.setFont(font)

        self.horizontalLayout_13.addWidget(self.label_8)

        self.comboBoxLineStileLine = QComboBox(self.groupBox_2)
        self.comboBoxLineStileLine.setObjectName(u"comboBoxLineStileLine")
        self.comboBoxLineStileLine.setFont(font)

        self.horizontalLayout_13.addWidget(self.comboBoxLineStileLine)

        self.comboBoxLineStile = QComboBox(self.groupBox_2)
        self.comboBoxLineStile.setObjectName(u"comboBoxLineStile")
        self.comboBoxLineStile.setFont(font)

        self.horizontalLayout_13.addWidget(self.comboBoxLineStile)


        self.verticalLayout.addLayout(self.horizontalLayout_13)


        self.verticalLayout_8.addWidget(self.groupBox_2)

        self.groupBox_4 = QGroupBox(self.tabPlot)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setFont(font)
        self.verticalLayout_10 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_11 = QLabel(self.groupBox_4)
        self.label_11.setObjectName(u"label_11")
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMinimumSize(QSize(80, 0))
        self.label_11.setFont(font)

        self.horizontalLayout_15.addWidget(self.label_11)

        self.sliderLegendFontSize = QSlider(self.groupBox_4)
        self.sliderLegendFontSize.setObjectName(u"sliderLegendFontSize")
        self.sliderLegendFontSize.setFont(font)
        self.sliderLegendFontSize.setOrientation(Qt.Horizontal)

        self.horizontalLayout_15.addWidget(self.sliderLegendFontSize)

        self.spinBoxLegendFontSize = QSpinBox(self.groupBox_4)
        self.spinBoxLegendFontSize.setObjectName(u"spinBoxLegendFontSize")
        self.spinBoxLegendFontSize.setFont(font)

        self.horizontalLayout_15.addWidget(self.spinBoxLegendFontSize)


        self.verticalLayout_10.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_12 = QLabel(self.groupBox_4)
        self.label_12.setObjectName(u"label_12")
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setMinimumSize(QSize(80, 0))
        self.label_12.setFont(font)

        self.horizontalLayout_16.addWidget(self.label_12)

        self.sliderLegendXPosition = QSlider(self.groupBox_4)
        self.sliderLegendXPosition.setObjectName(u"sliderLegendXPosition")
        self.sliderLegendXPosition.setFont(font)
        self.sliderLegendXPosition.setOrientation(Qt.Horizontal)

        self.horizontalLayout_16.addWidget(self.sliderLegendXPosition)

        self.BoxLegendXPosition = QSpinBox(self.groupBox_4)
        self.BoxLegendXPosition.setObjectName(u"BoxLegendXPosition")
        self.BoxLegendXPosition.setFont(font)

        self.horizontalLayout_16.addWidget(self.BoxLegendXPosition)


        self.verticalLayout_10.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_13 = QLabel(self.groupBox_4)
        self.label_13.setObjectName(u"label_13")
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setMinimumSize(QSize(80, 0))
        self.label_13.setFont(font)

        self.horizontalLayout_17.addWidget(self.label_13)

        self.sliderLegendYPosition = QSlider(self.groupBox_4)
        self.sliderLegendYPosition.setObjectName(u"sliderLegendYPosition")
        self.sliderLegendYPosition.setFont(font)
        self.sliderLegendYPosition.setOrientation(Qt.Horizontal)

        self.horizontalLayout_17.addWidget(self.sliderLegendYPosition)

        self.spinBoxLegendYPosition = QSpinBox(self.groupBox_4)
        self.spinBoxLegendYPosition.setObjectName(u"spinBoxLegendYPosition")
        self.spinBoxLegendYPosition.setFont(font)

        self.horizontalLayout_17.addWidget(self.spinBoxLegendYPosition)


        self.verticalLayout_10.addLayout(self.horizontalLayout_17)


        self.verticalLayout_8.addWidget(self.groupBox_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer)

        self.tabWidget.addTab(self.tabPlot, "")

        self.verticalLayout_2.addWidget(self.tabWidget)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.groupBox_5 = QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setFont(font)
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.FigurePlotPreview = plt.figure()
        self.figureCanvasPlotPreview = FigureCanvas(plt.figure())
        self.figureCanvasPlotPreview.setObjectName(u"figureCanvasPlotPreview")
        self.figureCanvasPlotPreview.setFont(font)
        self.axis = self.FigurePlotPreview.add_subplot(1,1,1) # axを持っておく

        self.verticalLayout_11.addWidget(self.figureCanvasPlotPreview)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer)

        self.pushButtonPlotPreview = QPushButton(self.groupBox_5)
        self.pushButtonPlotPreview.setObjectName(u"pushButtonPlotPreview")
        self.pushButtonPlotPreview.setFont(font)

        self.horizontalLayout_10.addWidget(self.pushButtonPlotPreview)

        self.pushButtonPlotExport = QPushButton(self.groupBox_5)
        self.pushButtonPlotExport.setObjectName(u"pushButton")
        self.pushButtonPlotExport.setFont(font)

        self.horizontalLayout_10.addWidget(self.pushButtonPlotExport)


        self.verticalLayout_11.addLayout(self.horizontalLayout_10)


        self.horizontalLayout.addWidget(self.groupBox_5)

        GraphMaker.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(GraphMaker)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 20))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        GraphMaker.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(GraphMaker)
        self.statusbar.setObjectName(u"statusbar")
        GraphMaker.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionLoadTable)
        self.menuFile.addAction(self.actionSaveTable)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionLoadSetting)
        self.menuFile.addAction(self.actionSaveSetting)
        self.menuHelp.addAction(self.actionUserManual)

        self.retranslateUi(GraphMaker)

        self.tabWidget.setCurrentIndex(0)

        # callbacks
        self.actionLoadTable.triggered.connect(self.clickedActionLoadTable) 
        self.actionSaveTable.triggered.connect(self.clickedActionSaveTable)
        self.actionLoadSetting.triggered.connect(self.clickedActionLoadSetting)
        self.actionSaveSetting.triggered.connect(self.clickedActionSaveSetting)
        self.actionUserManual.triggered.connect(self.clickedActionUserManual)
        self.buttonAddXAxis.clicked.connect(self.clickedButtonAddXAxis)
        self.buttonAddYAxis.clicked.connect(self.clickedButtonAddYAxis)
        self.buttonRemoveYAxis.clicked.connect(self.clickedButtonRemoveYAxis)
        self.listDataList.doubleClicked.connect(self.doubleClickedListDataList)
        self.listXAxisData.doubleClicked.connect(self.doubleClickedListXAxisData)
        self.listYAxisData.doubleClicked.connect(self.doubleClickedListYAxisData)
        self.pushButtonPlotPreview.clicked.connect(self.clickedPushButtonPlotPreview)
        self.pushButtonPlotExport.clicked.connect(self.clickedPushButtonPlotExport)

        self.dataList_ = {}


        QMetaObject.connectSlotsByName(GraphMaker)
    # setupUi

    def retranslateUi(self, GraphMaker):
        GraphMaker.setWindowTitle(QCoreApplication.translate("GraphMaker", u"GraphMaker", None))
        self.actionLoadTable.setText(QCoreApplication.translate("GraphMaker", u"Load table", None))
        self.actionSaveTable.setText(QCoreApplication.translate("GraphMaker", u"Save table", None))
        self.actionLoadSetting.setText(QCoreApplication.translate("GraphMaker", u"Load setting", None))
        self.actionSaveSetting.setText(QCoreApplication.translate("GraphMaker", u"Save setting", None))
        self.actionUserManual.setText(QCoreApplication.translate("GraphMaker", u"User manual", None))

        __sortingEnabled = self.listDataList.isSortingEnabled()
        self.listDataList.setSortingEnabled(False)
        ___qlistwidgetitem = self.listDataList.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("GraphMaker", u"No data", None));
        self.listDataList.setSortingEnabled(__sortingEnabled)

        self.buttonAddXAxis.setText(QCoreApplication.translate("GraphMaker", u"\u2192", None))
        self.buttonAddYAxis.setText(QCoreApplication.translate("GraphMaker", u"\u2192", None))
        self.buttonRemoveYAxis.setText(QCoreApplication.translate("GraphMaker", u"\u2190", None))
        self.label_10.setText(QCoreApplication.translate("GraphMaker", u"X axis", None))
        self.label_9.setText(QCoreApplication.translate("GraphMaker", u"Y axis", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabDataSelector), QCoreApplication.translate("GraphMaker", u"Data Selector", None))
        self.groupBox.setTitle(QCoreApplication.translate("GraphMaker", u"X axis", None))
        self.label.setText(QCoreApplication.translate("GraphMaker", u"Text:", None))
        self.label_2.setText(QCoreApplication.translate("GraphMaker", u"Font size:", None))
        self.checkBoxXAxisMinLimit.setText(QCoreApplication.translate("GraphMaker", u"Min limit:", None))
        self.checkBoxXAxisMaxLimit.setText(QCoreApplication.translate("GraphMaker", u"Max limit:", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("GraphMaker", u"Y axis", None))
        self.label_4.setText(QCoreApplication.translate("GraphMaker", u"Text:", None))
        self.label_5.setText(QCoreApplication.translate("GraphMaker", u"Font size:", None))
        self.checkBoxYAxisMinLimit.setText(QCoreApplication.translate("GraphMaker", u"Min limit:", None))
        self.checkBoxYAxisMaxLimit.setText(QCoreApplication.translate("GraphMaker", u"Max limit:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabAxis), QCoreApplication.translate("GraphMaker", u"Axis", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("GraphMaker", u"Line", None))
        self.label_6.setText(QCoreApplication.translate("GraphMaker", u"Width:", None))
        self.label_7.setText(QCoreApplication.translate("GraphMaker", u"Color:", None))
        self.label_8.setText(QCoreApplication.translate("GraphMaker", u"Stile:", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("GraphMaker", u"Legend", None))
        self.label_11.setText(QCoreApplication.translate("GraphMaker", u"Font size:", None))
        self.label_12.setText(QCoreApplication.translate("GraphMaker", u"X position:", None))
        self.label_13.setText(QCoreApplication.translate("GraphMaker", u"Y position:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabPlot), QCoreApplication.translate("GraphMaker", u"Plot", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("GraphMaker", u"Preview", None))
        self.pushButtonPlotPreview.setText(QCoreApplication.translate("GraphMaker", u"Preview", None))
        self.pushButtonPlotExport.setText(QCoreApplication.translate("GraphMaker", u"Export", None))
        self.menuFile.setTitle(QCoreApplication.translate("GraphMaker", u"File(F)", None))
        self.menuEdit.setTitle(QCoreApplication.translate("GraphMaker", u"Edit(E)", None))
        self.menuHelp.setTitle(QCoreApplication.translate("GraphMaker", u"Help(H)", None))
    # retranslateUi

    def clickedActionLoadTable(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(None, "Select File", "", "CSV Files (*.csv);;Bag Files (*.bag)")
        if file_path == '':
            return
        
        if file_path.endswith('.csv'):
            self.loadCsvData(file_path)

        elif file_path.endswith('.bag'):
            self.loadRosBagData(file_path)
    # clickedActionLoadTable

    def loadCsvData(self, file_path):
        headers = []
        dataList = []
        with open(file_path, 'r') as file:
            csv_reader = csv.reader(file)
            headers = next(csv_reader)
            for row in csv_reader:
                dataList.append(row)

        existingItems = [self.listDataList.item(i).text() for i in range(self.listDataList.count())]
        newHeaders = [f"{item}/{i+1}" if item in existingItems else item for i, item in enumerate(headers)]
        if self.listDataList.item(0).text() == "No data":
            self.listDataList.clear()
        self.listDataList.addItems(newHeaders)

        for i in range(len(newHeaders)):
            self.dataList_[newHeaders[i]] = [float(data[i]) for data in dataList]

        self.listDataList.setCurrentRow(0)
    # loadCsvData

    def loadRosBagData(self, file_path):
        pass
    # loadRosBagData

    def clickedActionSaveTable(self):
        pass
    # clickedActionSaveTable

    def clickedActionLoadSetting(self):
        pass
    # clickedActionLoadSetting

    def clickedActionSaveSetting(self):
        pass
    # clickedActionSaveSetting

    def clickedActionUserManual(self):
        pass
    # clickedActionUserManual

    def clickedButtonAddXAxis(self):
        if self.listDataList.currentItem() is None:
            return
        text = self.listDataList.currentItem().text()
        self.addTextToList(self.listXAxisData, text, clear=True)
    # clickedButtonAddXAxis

    def clickedButtonAddYAxis(self):
        if self.listDataList.currentItem() is None:
            return
        text = self.listDataList.currentItem().text()
        self.addTextToList(self.listYAxisData, text)
    # clickedButtonAddYAxis

    def clickedButtonRemoveYAxis(self):
        if self.listYAxisData.currentItem() is None:
            return
        text = self.listYAxisData.currentItem().text()
        self.removeTextFromList(self.listYAxisData, text)
    # clickedButtonRemoveYAxis

    def doubleClickedListDataList(self):
        if self.listXAxisData.count() == 0:
            self.clickedButtonAddXAxis()
        else:
            self.clickedButtonAddYAxis()
    # doubleClickedListDataList

    def doubleClickedListXAxisData(self):
        self.removeTextFromList(self.listXAxisData, self.listXAxisData.currentItem().text())
    # doubleClickedListXAxisData

    def doubleClickedListYAxisData(self):
        self.clickedButtonRemoveYAxis()
    # doubleClickedListYAxisData

    def clickedPushButtonPlotPreview(self):
        self.plotGraph()
    # clickedPushButtonPlotPreview

    def clickedPushButtonPlotExport(self):
        self.exportGraph()
    # clickedPushButtonPlotExport

    def plotGraph(self):
        plt.cla()
        if self.listXAxisData.count() == 0 or self.listYAxisData.count() == 0:
            return
        
        x_data = self.dataList_[self.listXAxisData.item(0).text()]
        for i in range(0, self.listYAxisData.count()):
            y_data = self.dataList_[self.listYAxisData.item(i).text()]
            print(x_data)
            print(y_data)
            print(self.listYAxisData.count())

            plt.plot(x_data, y_data)
        plt.xlabel("X Axis")
        plt.ylabel("Y Axis")

        self.figureCanvasPlotPreview.draw()
    # plotGraph

    def exportGraph(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getSaveFileName(None, "Save File", "", "PNG Files (*.png);;PDF Files (*.pdf)")
        if file_path == '':
            return
        
        plt.savefig(file_path)
        

    def addTextToList(self, list: QListWidget, text: str, clear: bool = False):
        if clear:
            list.clear()
        list.addItem(text)

        self.plotGraph()
    # addTextToList

    def removeTextFromList(self, list: QListWidget, text: str):
        for i in range(list.count()):
            if list.item(i).text() == text:
                list.takeItem(i)
                break

        self.plotGraph()
    # removeTextFromList