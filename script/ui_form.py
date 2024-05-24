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
    QTabWidget, QVBoxLayout, QWidget, QFileDialog, QStyle)
import csv
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from graphPlotter import GraphPlotter 
import json
from distutils.util import strtobool
from myWidgets.LabeledWidget import my_widget
import webbrowser


class Ui_GraphMaker(object):
    SLIDER_DOUBLE_RATIO = 1e5  # sliderの値をdoubleに変換するための倍率
    SPINBOX_Decimals = 5  # spinboxの小数点以下の桁数
    LINE_STILE_MAP = {"Solid": "-", "Dashed": "--", "Dotted": ":", "DashDot": "-."}
    PLOT_LEGEND_POSITION_LIST = ["best", "upper right", "upper left", "lower left", "lower right", "right", "center left", "center right", "lower center", "upper center", "center"]

    PLOT_ASPECT_RATIO = 1.414   # plotのアスペクト比　白銀比
    PLOT_AREA_HEIGHT = 300      # plotの高さ
    TAB_WIDGET_WIDTH = 400      # tab widgetの幅
    WINDOW_MARGIN = 200         # windowの余白

    def setupUi(self, GraphMaker):
        if not GraphMaker.objectName():
            GraphMaker.setObjectName(u"MainWindow")

        # settings
        GraphMaker.setWindowTitle(QCoreApplication.translate("GraphMaker", u"GraphMaker", None))
        windowWidth = self.TAB_WIDGET_WIDTH + self.PLOT_AREA_HEIGHT * self.PLOT_ASPECT_RATIO + self.WINDOW_MARGIN
        GraphMaker.setFixedSize(windowWidth, self.PLOT_AREA_HEIGHT + self.WINDOW_MARGIN)
        windowIcon = QApplication.style().standardIcon( QStyle.SP_TitleBarMenuButton)
        GraphMaker.setWindowIcon(windowIcon)
        font = QFont()
        font.setPointSize(12)
        # 初期設定のために最初に生成する
        self.plotter_ = GraphPlotter()
        
        # layout settings begin --------------------------------------------
        # @brief window内のウィジェットのレイアウトを設定を行う
        # @description 
        # 現在の階層に必要なオブジェクトを列挙して先にレイアウトを設定する
        # 各オブジェクトの実装は下に書く

        # main window
        # setting
        self.centralWidget = QWidget(GraphMaker)
        self.centralWidget.setObjectName(u"CentralWidget")
        self.horizontalLayout = QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setObjectName(u"HorizontalLayoutMain")

        # objects
        self.tabWidget = QTabWidget(self.centralWidget)
        self.groupBoxPreview = QGroupBox(self.centralWidget)

        # layout
        self.horizontalLayout.addWidget(self.tabWidget)
        self.horizontalLayout.addWidget(self.groupBoxPreview)

        # tab widget begin ------------------------------------------------
        # setting
        self.tabWidget.setObjectName(u"TabWidget")
        self.tabWidget.setMaximumSize(QSize(self.TAB_WIDGET_WIDTH, 16777215))
        self.tabWidget.setFont(font)
        self.tabWidget.setCurrentIndex(0)

        # objects
        self.tabDataSelector = QWidget()
        self.tabAxis = QWidget()
        self.tabPlot = QWidget()

        # layout
        self.tabWidget.addTab(self.tabDataSelector, "")
        self.tabWidget.addTab(self.tabAxis, "")
        self.tabWidget.addTab(self.tabPlot, "")

        # data selector tab begin -----------------------------------------
        # setting
        self.tabDataSelector.setObjectName(u"TabDataSelector")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabDataSelector), QCoreApplication.translate("GraphMaker", u"Data Selector", None))
        self.horizontalLayoutDataSelectorTab = QHBoxLayout(self.tabDataSelector)
        self.horizontalLayoutDataSelectorTab.setObjectName(u"HorizontalLayoutDataSelectorTab")

        # objects
        self.listDataList = QListWidget(self.tabDataSelector)
        self.verticalLayoutAddAxisButton = QVBoxLayout()
        self.verticalLayoutSelectedAxis = QVBoxLayout()

        # layout
        self.horizontalLayoutDataSelectorTab.addWidget(self.listDataList)
        self.horizontalLayoutDataSelectorTab.addLayout(self.verticalLayoutAddAxisButton)
        self.horizontalLayoutDataSelectorTab.addLayout(self.verticalLayoutSelectedAxis)

        # data list begin -------------------------------------------------
        # setting
        QListWidgetItem(self.listDataList)
        self.listDataList.setObjectName(u"ListDataList")
        self.listDataList.setMinimumSize(QSize(170, 0))
        self.listDataList.setMaximumSize(QSize(16777215, 16777215))
        __sortingEnabled = self.listDataList.isSortingEnabled()
        self.listDataList.setSortingEnabled(False)
        ___qlistwidgetitem = self.listDataList.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("GraphMaker", u"No data", None))
        self.listDataList.setSortingEnabled(__sortingEnabled)
        # objects
        # layout

        # callback
        self.listDataList.doubleClicked.connect(self.doubleClickedListDataList)
        # data list end ---------------------------------------------------
        
        # data selector buttons begin -------------------------------------
        # setting
        self.verticalLayoutAddAxisButton.setObjectName(u"VerticalLayoutAddAxisButton")

        # objects
        self.verticalSpacerAddAxisButtonTop = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        self.verticalSpacerAddAxisButtonMiddle = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.verticalSpacerAddAxisButtonBottom = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.buttonAddXAxis = QPushButton(self.tabDataSelector)
        self.buttonAddYAxis = QPushButton(self.tabDataSelector)
        self.buttonRemoveYAxis = QPushButton(self.tabDataSelector)

        # layout
        self.verticalLayoutAddAxisButton.addItem(self.verticalSpacerAddAxisButtonTop)
        self.verticalLayoutAddAxisButton.addWidget(self.buttonAddXAxis)
        self.verticalLayoutAddAxisButton.addItem(self.verticalSpacerAddAxisButtonMiddle)
        self.verticalLayoutAddAxisButton.addWidget(self.buttonAddYAxis)
        self.verticalLayoutAddAxisButton.addWidget(self.buttonRemoveYAxis)
        self.verticalLayoutAddAxisButton.addItem(self.verticalSpacerAddAxisButtonBottom)

        # size policy
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonAddXAxis.sizePolicy().hasHeightForWidth())
        # x axis add button
        self.buttonAddXAxis.setObjectName(u"ButtonAddXAxis")
        self.buttonAddXAxis.setSizePolicy(sizePolicy)
        self.buttonAddXAxis.setText(QCoreApplication.translate("GraphMaker", u"\u2192", None))
        self.buttonAddXAxis.setMaximumSize(QSize(30, 20))
        self.buttonAddXAxis.clicked.connect(self.clickedButtonAddXAxis)
        # y axis add button
        self.buttonAddYAxis.setObjectName(u"ButtonAddYAxis")
        self.buttonAddYAxis.setText(QCoreApplication.translate("GraphMaker", u"\u2192", None))
        sizePolicy.setHeightForWidth(self.buttonAddYAxis.sizePolicy().hasHeightForWidth())
        self.buttonAddYAxis.setSizePolicy(sizePolicy)
        self.buttonAddYAxis.setMaximumSize(QSize(30, 20))
        self.buttonAddYAxis.clicked.connect(self.clickedButtonAddYAxis)
        # y axis remove button
        self.buttonRemoveYAxis.setObjectName(u"ButtonRemoveYAxis")
        self.buttonRemoveYAxis.setText(QCoreApplication.translate("GraphMaker", u"\u2190", None))
        sizePolicy.setHeightForWidth(self.buttonRemoveYAxis.sizePolicy().hasHeightForWidth())
        self.buttonRemoveYAxis.setSizePolicy(sizePolicy)
        self.buttonRemoveYAxis.setMaximumSize(QSize(30, 20))
        self.buttonRemoveYAxis.clicked.connect(self.clickedButtonRemoveYAxis)
        # data selector buttons end ---------------------------------------

        # selected axis begin ---------------------------------------------
        # setting
        self.verticalLayoutSelectedAxis.setObjectName(u"VerticalLayoutSelectedAxis")

        # objects
        self.labelDataSelectorXAxis = QLabel(self.tabDataSelector)
        self.labelDataSelectorXAxis.setText(QCoreApplication.translate("GraphMaker", u"X axis", None))
        self.labelDataSelectorYAxis = QLabel(self.tabDataSelector)
        self.labelDataSelectorYAxis.setText(QCoreApplication.translate("GraphMaker", u"Y axis", None))
        self.listXAxisData = QListWidget(self.tabDataSelector)
        self.listYAxisData = QListWidget(self.tabDataSelector)

        # layout
        self.verticalLayoutSelectedAxis.addWidget(self.labelDataSelectorXAxis)
        self.verticalLayoutSelectedAxis.addWidget(self.listXAxisData)
        self.verticalLayoutSelectedAxis.addWidget(self.labelDataSelectorYAxis)
        self.verticalLayoutSelectedAxis.addWidget(self.listYAxisData)

        # x axis label
        self.labelDataSelectorXAxis.setObjectName(u"LabelDataSelectorXAxis")
        # x axis list
        self.listXAxisData.setObjectName(u"ListXAxisData")
        sizePolicy.setHeightForWidth(self.listXAxisData.sizePolicy().hasHeightForWidth())
        self.listXAxisData.setSizePolicy(sizePolicy)
        self.listXAxisData.setMaximumSize(QSize(16777215, 25))
        self.listXAxisData.doubleClicked.connect(self.doubleClickedListXAxisData)
        # y axis label
        self.labelDataSelectorYAxis.setObjectName(u"LabelDataSelectorYAxis")
        # y axis list
        self.listYAxisData.setObjectName(u"ListYAxisData")
        self.listYAxisData.setMaximumSize(QSize(16777215, 16777215))
        self.listYAxisData.doubleClicked.connect(self.doubleClickedListYAxisData)
        # selected axis end -----------------------------------------------
        # data selector tab end -------------------------------------------

        # axis tab begin --------------------------------------------------
        # setting
        self.tabAxis.setObjectName(u"TabAxis")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabAxis), QCoreApplication.translate("GraphMaker", u"Axis", None))
        self.verticalLayoutAxisTab = QVBoxLayout(self.tabAxis)
        self.verticalLayoutAxisTab.setObjectName(u"VerticalLayoutAxisTab")

        # objects
        self.groupBoxXAxis = QGroupBox(self.tabAxis)
        self.groupBoxYAxis = QGroupBox(self.tabAxis)
        self.verticalSpacerAxisTab = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        # layout
        self.verticalLayoutAxisTab.addWidget(self.groupBoxXAxis)
        self.verticalLayoutAxisTab.addWidget(self.groupBoxYAxis)
        self.verticalLayoutAxisTab.addItem(self.verticalSpacerAxisTab)

        # x axis begin ----------------------------------------------------
        # setting
        self.groupBoxXAxis.setObjectName(u"GroupBoxXAxis")
        self.groupBoxXAxis.setTitle(QCoreApplication.translate("GraphMaker", u"X axis", None))
        self.verticalLayoutXAxis = QVBoxLayout(self.groupBoxXAxis)
        self.verticalLayoutXAxis.setObjectName(u"VerticalLayoutXAxis")

        # objects
        # label
        self.lineEditXAxisLabel = my_widget.LabeledLineEdit(self.groupBoxXAxis, False, False)
        self.lineEditXAxisLabel.setObjectName(u"LineEditXAxisLabel")
        self.lineEditXAxisLabel.setLabelText(QCoreApplication.translate("GraphMaker", u"Label:", None))
        self.lineEditXAxisLabel.setTextChangedCallback(self.changedLineEditXAxisLabel)
        # font size
        self.sliderXAxisFontSize = my_widget.LabeledSlider(self.groupBoxXAxis, False, False, False)
        self.sliderXAxisFontSize.setObjectName(u"SliderXAxisFontSize")
        self.sliderXAxisFontSize.setLabelText(QCoreApplication.translate("GraphMaker", u"Font size:", None))
        self.sliderXAxisFontSize.setValue(GraphPlotter.DEFAULT_FONT_SIZE)
        self.sliderXAxisFontSize.setRange(1, 100)
        self.sliderXAxisFontSize.setValueChangeCallback(self.setXAxisFontSize)
        # min limit
        self.sliderXAxisMinLimit = my_widget.LabeledSlider(self.groupBoxXAxis, True, False, True)
        self.sliderXAxisMinLimit.setObjectName(u"SliderXAxisMinLimit")
        self.sliderXAxisMinLimit.setLabelText(QCoreApplication.translate("GraphMaker", u"Min limit:", None))
        self.sliderXAxisMinLimit.setRange(-1, 1)
        self.sliderXAxisMinLimit.setValueChangeCallback(self.changedSliderXAxisLimit)
        self.sliderXAxisMinLimit.setCheckedCallback(self.changedCheckBoxXAxisLimit)
        # max limit
        self.sliderXAxisMaxLimit = my_widget.LabeledSlider(self.groupBoxXAxis, True, False, True)
        self.sliderXAxisMaxLimit.setObjectName(u"SliderXAxisMaxLimit")
        self.sliderXAxisMaxLimit.setLabelText(QCoreApplication.translate("GraphMaker", u"Max limit:", None))
        self.sliderXAxisMaxLimit.setRange(-1, 1)
        self.sliderXAxisMaxLimit.setValueChangeCallback(self.changedSliderXAxisLimit)
        self.sliderXAxisMaxLimit.setCheckedCallback(self.changedCheckBoxXAxisLimit)

        # layout
        self.verticalLayoutXAxis.addLayout(self.lineEditXAxisLabel.getLayout())
        self.verticalLayoutXAxis.addLayout(self.sliderXAxisFontSize.getLayout())
        self.verticalLayoutXAxis.addLayout(self.sliderXAxisMinLimit.getLayout())
        self.verticalLayoutXAxis.addLayout(self.sliderXAxisMaxLimit.getLayout())
        # x axis end ------------------------------------------------------
        
        # y axis begin ----------------------------------------------------
        # setting
        self.groupBoxYAxis.setObjectName(u"GroupBoxYAxis")
        self.groupBoxYAxis.setTitle(QCoreApplication.translate("GraphMaker", u"Y axis", None))
        self.verticalLayoutYAxis = QVBoxLayout(self.groupBoxYAxis)
        self.verticalLayoutYAxis.setObjectName(u"VerticalLayoutYAxis")

        # objects
        # label
        self.lineEditYAxisLabel = my_widget.LabeledLineEdit(self.groupBoxYAxis)
        self.lineEditYAxisLabel.setObjectName(u"LineEditYAxisLabel")
        self.lineEditYAxisLabel.setLabelText(QCoreApplication.translate("GraphMaker", u"Label:", None))
        self.lineEditYAxisLabel.setTextChangedCallback(self.changedLineEditYAxisLabel)
        # font size
        self.sliderYAxisFontSize = my_widget.LabeledSlider  (self.groupBoxYAxis, False, False, False)
        self.sliderYAxisFontSize.setObjectName(u"SliderYAxisFontSize")
        self.sliderYAxisFontSize.setLabelText(QCoreApplication.translate("GraphMaker", u"Font size:", None))
        self.sliderYAxisFontSize.setValue(GraphPlotter.DEFAULT_FONT_SIZE)
        self.sliderYAxisFontSize.setRange(1, 100)
        self.sliderYAxisFontSize.setValueChangeCallback(self.setYAxisFontSize)
        # min limit
        self.sliderYAxisMinLimit = my_widget.LabeledSlider(self.groupBoxYAxis, True, False, True)
        self.sliderYAxisMinLimit.setObjectName(u"SliderYAxisMinLimit")
        self.sliderYAxisMinLimit.setLabelText(QCoreApplication.translate("GraphMaker", u"Min limit:", None))
        self.sliderYAxisMinLimit.setRange(-1, 1)
        self.sliderYAxisMinLimit.setValueChangeCallback(self.changedSliderYAxisLimit)
        self.sliderYAxisMinLimit.setCheckedCallback(self.changedCheckBoxYAxisLimit)
        # max limit
        self.sliderYAxisMaxLimit = my_widget.LabeledSlider(self.groupBoxYAxis, True, False, True)
        self.sliderYAxisMaxLimit.setObjectName(u"SliderYAxisMaxLimit")
        self.sliderYAxisMaxLimit.setLabelText(QCoreApplication.translate("GraphMaker", u"Max limit:", None))
        self.sliderYAxisMaxLimit.setRange(-1, 1)
        self.sliderYAxisMaxLimit.setValueChangeCallback(self.changedSliderYAxisLimit)
        self.sliderYAxisMaxLimit.setCheckedCallback(self.changedCheckBoxYAxisLimit)

        # layout
        self.verticalLayoutYAxis.addLayout(self.lineEditYAxisLabel.getLayout())
        self.verticalLayoutYAxis.addLayout(self.sliderYAxisFontSize.getLayout())
        self.verticalLayoutYAxis.addLayout(self.sliderYAxisMinLimit.getLayout())
        self.verticalLayoutYAxis.addLayout(self.sliderYAxisMaxLimit.getLayout())
        # y axis end ------------------------------------------------------
        # axis tab end ----------------------------------------------------

        # plot tab begin --------------------------------------------------
        # setting
        self.tabPlot.setObjectName(u"TabPlot")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabPlot), QCoreApplication.translate("GraphMaker", u"Plot", None))
        self.verticalLayoutPlotTab = QVBoxLayout(self.tabPlot)
        self.verticalLayoutPlotTab.setObjectName(u"VerticalLayoutPlotTab")

        # objects
        self.groupBoxLine = QGroupBox(self.tabPlot)
        self.groupBoxLegend = QGroupBox(self.tabPlot)
        self.groupBoxAxes = QGroupBox(self.tabPlot)
        self.verticalSpacerPlotTab = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding) 
        # layout
        self.verticalLayoutPlotTab.addWidget(self.groupBoxLine)
        self.verticalLayoutPlotTab.addWidget(self.groupBoxLegend)
        self.verticalLayoutPlotTab.addWidget(self.groupBoxAxes)
        self.verticalLayoutPlotTab.addItem(self.verticalSpacerPlotTab)

        # line begin ------------------------------------------------------
        # setting
        self.groupBoxLine.setObjectName(u"GroupBoxLine")
        self.groupBoxLine.setTitle(QCoreApplication.translate("GraphMaker", u"Line", None))
        self.groupBoxLine.setFont(font)
        self.verticalLayoutLine = QVBoxLayout(self.groupBoxLine)
        self.verticalLayoutLine.setObjectName(u"VerticalLayoutLine")
        
        # objects
        # line selection
        self.comboBoxLineSelection = my_widget.LabeledComboBox(self.groupBoxLine, False, False)
        self.comboBoxLineSelection.setObjectName(u"ComboBoxLineSelection")
        self.comboBoxLineSelection.setLabelText(QCoreApplication.translate("GraphMaker", u"Line:", None))
        self.comboBoxLineSelection.setComboBoxCallback(self.changedComboBoxLineSelection)
        # line width
        self.sliderLineWidth = my_widget.LabeledSlider(self.groupBoxLine, False, False, False)
        self.sliderLineWidth.setObjectName(u"SliderLineWidth")
        self.sliderLineWidth.setLabelText(QCoreApplication.translate("GraphMaker", u"Width:", None))
        self.sliderLineWidth.setRange(1, 10)
        self.sliderLineWidth.setValueChangeCallback(self.changedSliderLineWidth)
        self.sliderLineWidth.setValue(GraphPlotter.DEFAULT_LINE_WIDTH)
        # line color
        self.colorSelectorLineColor = my_widget.LabeledColorSelector(self.groupBoxLine, False, False)
        self.colorSelectorLineColor.setObjectName(u"ColorSelectorLineColor")
        self.colorSelectorLineColor.setLabelText(QCoreApplication.translate("GraphMaker", u"Color:", None))
        self.colorSelectorLineColor.setColorChangedCallback(self.changedComboBoxLineColor)
        # line stile
        self.comboBoxLineStile = my_widget.LabeledComboBox(self.groupBoxLine, False, False)
        self.comboBoxLineStile.setObjectName(u"ComboBoxLineStile")
        self.comboBoxLineStile.setLabelText(QCoreApplication.translate("GraphMaker", u"Stile:", None))
        self.comboBoxLineStile.setComboBoxCallback(self.changedComboBoxLineStile)
        # line stile items
        for key in self.LINE_STILE_MAP.keys():
            self.comboBoxLineStile.addComboBoxItem(QCoreApplication.translate("GraphMaker", key, None))
        
        # layout
        self.verticalLayoutLine.addLayout(self.comboBoxLineSelection.getLayout())
        self.verticalLayoutLine.addLayout(self.sliderLineWidth.getLayout())
        self.verticalLayoutLine.addLayout(self.colorSelectorLineColor.getLayout())
        self.verticalLayoutLine.addLayout(self.comboBoxLineStile.getLayout())
        # line end -------------------------------------------------------

        # legend begin ----------------------------------------------------
        # setting
        self.groupBoxLegend.setObjectName(u"GroupBoxLegend")
        self.groupBoxLegend.setTitle(QCoreApplication.translate("GraphMaker", u"Legend", None))
        self.groupBoxLegend.setFont(font)
        self.verticalLayoutLegend = QVBoxLayout(self.groupBoxLegend)
        self.verticalLayoutLegend.setObjectName(u"VerticalLayoutLegend")
        
        # objects
        # text
        self.lineEditLegendText = my_widget.LabeledLineEdit(self.groupBoxLegend, True, True)
        self.lineEditLegendText.setObjectName(u"LineEditLegendText")
        self.lineEditLegendText.setLabelText(QCoreApplication.translate("GraphMaker", u"Text:", None))
        self.lineEditLegendText.setCheckedCallback(self.changedCheckBoxLegendText)
        self.lineEditLegendText.setTextChangedCallback(self.changedLineEditLegendText)
        # font size
        self.sliderLegendFontSize = my_widget.LabeledSlider(self.groupBoxLegend, False, False, False)
        self.sliderLegendFontSize.setObjectName(u"SliderLegendFontSize")
        self.sliderLegendFontSize.setLabelText(QCoreApplication.translate("GraphMaker", u"Font size:", None))
        self.sliderLegendFontSize.setValue(GraphPlotter.DEFAULT_FONT_SIZE)
        self.sliderLegendFontSize.setRange(1, 100)
        self.sliderLegendFontSize.setValueChangeCallback(self.changedSliderLegendFontSize)
        # position
        self.comboBoxLegendPosition = my_widget.LabeledComboBox(self.groupBoxLegend, False, False)
        self.comboBoxLegendPosition.setObjectName(u"ComboBoxLegendPosition")
        self.comboBoxLegendPosition.setLabelText(QCoreApplication.translate("GraphMaker", u"Position:", None))
        self.comboBoxLegendPosition.setComboBoxCallback(self.changedComboBoxLegendPosition)
        for position in self.PLOT_LEGEND_POSITION_LIST:
            self.comboBoxLegendPosition.addComboBoxItem(QCoreApplication.translate("GraphMaker", position, None))
        
        # layout
        self.verticalLayoutLegend.addLayout(self.lineEditLegendText.getLayout())
        self.verticalLayoutLegend.addLayout(self.sliderLegendFontSize.getLayout())
        self.verticalLayoutLegend.addLayout(self.comboBoxLegendPosition.getLayout())
        # legend end ------------------------------------------------------

        # axes begin ------------------------------------------------------
        # setting
        self.groupBoxAxes.setObjectName(u"GroupBoxAxes")
        self.groupBoxAxes.setTitle(QCoreApplication.translate("GraphMaker", u"Axes", None))
        self.groupBoxAxes.setFont(font)
        self.verticalLayoutAxes = QVBoxLayout(self.groupBoxAxes)
        self.verticalLayoutAxes.setObjectName(u"VerticalLayoutAxes")
        
        # objects
        # grid
        self.checkBoxGrid = QCheckBox(self.groupBoxAxes)
        self.checkBoxGrid.setObjectName(u"CheckBoxGrid")
        self.checkBoxGrid.setText(QCoreApplication.translate("GraphMaker", u"Grid:", None))
        self.checkBoxGrid.stateChanged.connect(self.changedCheckBoxGrid)

        # layout
        self.verticalLayoutAxes.addWidget(self.checkBoxGrid)
        # axes end -------------------------------------------------------
        # plot tab end ----------------------------------------------------
        # tab widget end --------------------------------------------------

        # plot preview begin ----------------------------------------------
        # setting
        self.groupBoxPreview.setObjectName(u"GroupBoxPreview")
        self.groupBoxPreview.setTitle(QCoreApplication.translate("GraphMaker", u"Preview", None))
        self.groupBoxPreview.setFont(font)
        self.verticalLayoutPreview = QVBoxLayout(self.groupBoxPreview)
        self.verticalLayoutPreview.setObjectName(u"VerticalLayoutPreview")
        # objects
        self.figureCanvasPlotPreview = FigureCanvas(self.plotter_.getFigure())
        self.horizontalLayoutPreviewButton = QHBoxLayout()
        # layout
        self.verticalLayoutPreview.addWidget(self.figureCanvasPlotPreview)
        self.verticalLayoutPreview.addLayout(self.horizontalLayoutPreviewButton)

        # plotter begin --------------------------------------------------
        # setting
        self.figureCanvasPlotPreview.setObjectName(u"FigureCanvasPlotPreview")
        self.figureCanvasPlotPreview.setFont(font)
        self.figureCanvasPlotPreview.setMinimumSize(QSize(self.PLOT_AREA_HEIGHT * self.PLOT_ASPECT_RATIO, self.PLOT_AREA_HEIGHT))
        # objects
        # layout
        # plotter end ----------------------------------------------------

        # preview buttons begin -------------------------------------------
        # setting
        self.horizontalLayoutPreviewButton.setObjectName(u"HorizontalLayoutPreviewButton")

        # objects
        self.horizontalSpacerPreviewButton = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        # preview button
        self.pushButtonPlotPreview = QPushButton(self.groupBoxPreview)
        self.pushButtonPlotPreview.setObjectName(u"PushButtonPlotPreview")
        self.pushButtonPlotPreview.setText(QCoreApplication.translate("GraphMaker", u"Preview", None))
        self.pushButtonPlotPreview.setFont(font)
        self.pushButtonPlotPreview.clicked.connect(self.clickedPushButtonPlotPreview)
        # export button
        self.pushButtonPlotExport = QPushButton(self.groupBoxPreview)
        self.pushButtonPlotExport.setObjectName(u"PushButtonPlotExport")
        self.pushButtonPlotExport.setText(QCoreApplication.translate("GraphMaker", u"Export", None))
        self.pushButtonPlotExport.setFont(font)
        self.pushButtonPlotExport.clicked.connect(self.clickedPushButtonPlotExport)

        # layout
        self.horizontalLayoutPreviewButton.addItem(self.horizontalSpacerPreviewButton)
        self.horizontalLayoutPreviewButton.addWidget(self.pushButtonPlotPreview)
        self.horizontalLayoutPreviewButton.addWidget(self.pushButtonPlotExport)
        # preview buttons end ----------------------------------------------
        # plot preview end -----------------------------------------------
        # layout settings  end ---------------------------------------------

        # menu bar begin ----------------------------------------------------
        GraphMaker.setCentralWidget(self.centralWidget)
        self.menubar = QMenuBar(GraphMaker)
        self.menubar.setObjectName(u"Menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 20))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"MenuFile")
        self.menuFile.setTitle(QCoreApplication.translate("GraphMaker", u"File(F)", None))
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"MenuHelp")
        self.menuHelp.setTitle(QCoreApplication.translate("GraphMaker", u"Help(H)", None))
        GraphMaker.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(GraphMaker)
        self.statusbar.setObjectName(u"statusbar")
        GraphMaker.setStatusBar(self.statusbar)

        # actions begin -----------------------------------------------------
        self.actionLoadTable = QAction(GraphMaker)
        self.actionLoadTable.setObjectName(u"ActionLoadTable") 
        self.actionLoadTable.setText(QCoreApplication.translate("GraphMaker", u"Load table", None))
        self.actionClearTable = QAction(GraphMaker)
        self.actionClearTable.setObjectName(u"ActionClearTable")
        self.actionClearTable.setText(QCoreApplication.translate("GraphMaker", u"Clear table", None))
        self.actionLoadSetting = QAction(GraphMaker)
        self.actionLoadSetting.setObjectName(u"ActionLoadSetting")
        self.actionLoadSetting.setText(QCoreApplication.translate("GraphMaker", u"Load setting", None))
        self.actionSaveSetting = QAction(GraphMaker)
        self.actionSaveSetting.setObjectName(u"ActionSaveSetting")
        self.actionSaveSetting.setText(QCoreApplication.translate("GraphMaker", u"Save setting", None))
        self.actionReadMe = QAction(GraphMaker)
        self.actionReadMe.setObjectName(u"ActionReadMe")
        self.actionReadMe.setText(QCoreApplication.translate("GraphMaker", u"Readme", None))
        # callback
        self.actionLoadTable.triggered.connect(self.clickedActionLoadTable) 
        self.actionClearTable.triggered.connect(self.clickedActionClearTable)
        self.actionLoadSetting.triggered.connect(self.clickedActionLoadSetting)
        self.actionSaveSetting.triggered.connect(self.clickedActionSaveSetting)
        self.actionReadMe.triggered.connect(self.clickedActionReadMe)
        # actions end ------------------------------------------------------
        # add actions to menu
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionLoadTable)
        self.menuFile.addAction(self.actionClearTable)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionLoadSetting)
        self.menuFile.addAction(self.actionSaveSetting)
        self.menuHelp.addAction(self.actionReadMe)
        # menu bar end ------------------------------------------------------

        self.dataList_ = {}
        self.lineSettings_ = {}

        QMetaObject.connectSlotsByName(GraphMaker)
    # setupUi

    def clickedActionLoadTable(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(None, "Load Table", "", "CSV Files (*.csv);;Bag Files (*.bag)")
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

        # ヘッダーの追加
        existingItems = [self.listDataList.item(i).text() for i in range(self.listDataList.count())]
        newHeaders = [self.getNumberedNameIfDuplicated(header, existingItems) for header in headers]
        if self.listDataList.item(0).text() == "No data":
            self.listDataList.clear()
        self.listDataList.addItems(newHeaders)

        # データの追加
        for i in range(len(newHeaders)):
            self.dataList_[newHeaders[i]] = [float(data[i]) if data[i] != "" else 0 for data in dataList]
        self.plotter_.setData(list(self.dataList_.values()))

        self.listDataList.setCurrentRow(0)
    # loadCsvData

    def loadRosBagData(self, file_path):
        pass
    # loadRosBagData

    def getNumberedNameIfDuplicated(self, name: str, nameList: list):
        if name not in nameList:
            return name
        else:
            index = 1
            while f"{name}/{index}" in nameList:
                index += 1
            return f"{name}/{index}"

    def clickedActionClearTable(self):
        self.listDataList.clear()
        self.listXAxisData.clear()
        self.listYAxisData.clear()
        self.listDataList.addItem("No data")
        self.lineEditLegendText.clearSelectBox()
        self.comboBoxLineSelection.clearComboBox()
        self.dataList_ = {}
        
        self.plotter_.clear()
        self.plotGraph()
    # clickedActionClearTable

    def clickedActionLoadSetting(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(None, "Load Setting", "", "Setting Files (*.json)")
        if file_path == '':
            return
        pass

        with open(file_path, 'r') as file:
            settings = json.load(file)

        lines = self.sliderLineWidth.getDataDict().keys()

        # 軸ラベル
        self.lineEditXAxisLabel.setText(settings["xAxis"]["label"])
        self.lineEditYAxisLabel.setText(settings["yAxis"]["label"])
        # フォントサイズ
        self.sliderXAxisFontSize.setValue(int(settings["xAxis"]["fontSize"]))
        self.sliderYAxisFontSize.setValue(int(settings["yAxis"]["fontSize"]))
        # 軸制限
        self.sliderXAxisMinLimit.setChecked(strtobool(settings["xAxis"]["limit"]["min"]["enabled"]))
        self.sliderXAxisMaxLimit.setChecked(strtobool(settings["xAxis"]["limit"]["max"]["enabled"]))
        self.sliderYAxisMinLimit.setChecked(strtobool(settings["yAxis"]["limit"]["min"]["enabled"]))
        self.sliderYAxisMaxLimit.setChecked(strtobool(settings["yAxis"]["limit"]["max"]["enabled"]))
        self.sliderXAxisMinLimit.setValue(float(settings["xAxis"]["limit"]["min"]["value"]))
        self.sliderXAxisMaxLimit.setValue(float(settings["xAxis"]["limit"]["max"]["value"]))
        self.sliderYAxisMinLimit.setValue(float(settings["yAxis"]["limit"]["min"]["value"]))
        self.sliderYAxisMaxLimit.setValue(float(settings["yAxis"]["limit"]["max"]["value"]))

        # ライン
        index = 0
        curPlotLines = self.comboBoxLineSelection.getComboBoxItems()
        for line in curPlotLines:
            # ライン幅
            if settings["line"]["widths"][index] is not None:
                self.lineSettings_[line]["width"] = int(settings["line"]["widths"][index])
                
            # ラインカラー
            if settings["line"]["colors"][index] is not None:
                self.lineSettings_[line]["color"] = settings["line"]["colors"][index]

            # ラインスタイル
            if settings["line"]["stiles"][index] is not None:
                self.lineSettings_[line]["stile"] = settings["line"]["stiles"][index]
                
            index += 1
            self.comboBoxLineSelection.setCurrentComboBoxText(line)

        # 凡例
        self.lineEditLegendText.setChecked(strtobool(settings["legend"]["enabled"]))
        # 凡例テキスト
        index = 0
        for line in lines:
            if settings["legend"]["texts"][index] is not None:
                self.lineEditLegendText.setData(line, settings["legend"]["texts"][index])
            
            index += 1
        # プロットへの反映
        self.plotter_.setLegendTexts(settings["legend"]["texts"])
        # 凡例フォントサイズ
        self.sliderLegendFontSize.setValue(int(settings["legend"]["fontSize"]))
        # 凡例位置
        self.comboBoxLegendPosition.setCurrentComboBoxText(settings["legend"]["position"])

        # グリッド
        self.checkBoxGrid.setChecked(strtobool(settings["grid"]["enabled"]))

        self.plotGraph()
    # clickedActionLoadSetting

    def clickedActionSaveSetting(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getSaveFileName(None, "Save Setting", "", "Setting Files (*.json)")
        if file_path == '':
            return

        settings = {
            "xAxis": {
                "label": self.lineEditXAxisLabel.getText(),
                "fontSize": str(self.sliderXAxisFontSize.getValue()),
                "limit": {
                    "min": {
                        "enabled": str(self.sliderXAxisMinLimit.isChecked()),
                        "value": str(self.sliderXAxisMinLimit.getValue())
                    },
                    "max": {
                        "enabled": str(self.sliderXAxisMaxLimit.isChecked()),
                        "value": str(self.sliderXAxisMaxLimit.getValue())
                    }
                }
            },
            "yAxis": {
                "label": self.lineEditYAxisLabel.getText(),
                "fontSize": str(self.sliderYAxisFontSize.getValue()),
                "limit": {
                    "min": {
                        "enabled": str(self.sliderYAxisMinLimit.isChecked()),
                        "value": str(self.sliderYAxisMinLimit.getValue())
                    },
                    "max": {
                        "enabled": str(self.sliderYAxisMaxLimit.isChecked()),
                        "value": str(self.sliderYAxisMaxLimit.getValue())
                    }
                }
            },
            "line": {
                "widths": [str(setting["width"]) for setting in self.lineSettings_.values()],
                "colors": [setting["color"] for setting in self.lineSettings_.values()],
                "stiles": [setting["stile"] for setting in self.lineSettings_.values()]
            },
            "legend": {
                "enabled": str(self.lineEditLegendText.isChecked()),
                "texts": self.lineEditLegendText.getDataList(),
                "fontSize": str(self.sliderLegendFontSize.getValue()),
                "position": self.comboBoxLegendPosition.getCurrentComboBoxText()
            },
            "grid": {
                "enabled": str(self.checkBoxGrid.isChecked())
            }
        }

        with open(file_path, 'w') as file:
            json.dump(settings, file, indent=4)
    # clickedActionSaveSetting

    def clickedActionReadMe(self):
        # githubのreadmeを開く
        webbrowser.open("https://github.com/Ama-suke/GraphMaker/blob/main/readme.md")
    # clickedActionReadMe

    def clickedButtonAddXAxis(self):
        if self.listDataList.currentItem() is None:
            return
        
        text = self.listDataList.currentItem().text()
        if self.listXAxisData.findItems(text, Qt.MatchExactly):
            # リストにすでに存在する場合は追加しない
            return
        
        index = self.convertHeaderToIndex(text)
        self.plotter_.setXDataIndex(index)
        self.addTextToList(self.listXAxisData, text, clear=True)
    # clickedButtonAddXAxis

    def clickedButtonAddYAxis(self):
        if self.listDataList.currentItem() is None:
            return
        
        text = self.listDataList.currentItem().text()
        if self.listYAxisData.findItems(text, Qt.MatchExactly):
            # リストにすでに存在する場合は追加しない
            return

        # データの設定
        index = self.convertHeaderToIndex(text)
        self.plotter_.addYDataIndex(index)

        # レジェンド、ライン幅、ラインスタイルの初期設定
        self.lineEditLegendText.addSelectBoxItem(text)
        self.comboBoxLineSelection.addComboBoxItem(text)

        # デフォルト値を設定
        self.sliderLineWidth.setData(text, GraphPlotter.DEFAULT_LINE_WIDTH)
        self.colorSelectorLineColor.setData(text, GraphPlotter.DEFAULT_LINE_COLOR)
        self.comboBoxLineStile.setData(text, 0)
        if self.lineSettings_.get(text) is None:
            self.lineSettings_[text] = {
                "width": GraphPlotter.DEFAULT_LINE_WIDTH,
                "color": GraphPlotter.DEFAULT_LINE_COLOR,
                "stile": "Solid"
            }

        # プロットへの反映
        self.addTextToList(self.listYAxisData, text)
    # clickedButtonAddYAxis

    def clickedButtonRemoveYAxis(self):
        if self.listYAxisData.currentItem() is None:
            return
        
        text = self.listYAxisData.currentItem().text()
        if not self.listYAxisData.findItems(text, Qt.MatchExactly):
            # リストに存在しない場合は削除しない
            return
        
        index = self.convertHeaderToIndex(text)
        self.plotter_.removeYDataIndex(index)
        self.comboBoxLineSelection.removeComboBoxItem(text)
        self.lineEditLegendText.removeSelectBoxItem(text)
        self.removeTextFromList(self.listYAxisData, text)
    # clickedButtonRemoveYAxis

    def convertHeaderToIndex(self, header):
        return list(self.dataList_.keys()).index(header)

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

    def changedLineEditXAxisLabel(self, text: str):
        self.plotter_.setXAxisLabel(text)
        self.plotGraph()
    # changedLineEditXAxisText

    def changedLineEditYAxisLabel(self, text: str):
        self.plotter_.setYAxisLabel(text)
        self.plotGraph()
    # changedLineEditYAxisText

    def setXAxisFontSize(self, value):
        self.plotter_.setXAxisFontSize(value)
        self.plotGraph()
    # setXAxisFontSize

    def setYAxisFontSize(self, value):
        self.plotter_.setYAxisFontSize(value)
        self.plotGraph()
    # setYAxisFontSize

    def plotGraph(self):
        # set line settings
        settingList = [self.lineSettings_[key] for key in self.comboBoxLineSelection.getComboBoxItems()] 
        lineWidthList = [setting["width"] for setting in settingList]
        colorList = [setting["color"] for setting in settingList]
        stileList = [self.LINE_STILE_MAP[setting["stile"]] for setting in settingList]
        self.plotter_.setLineWidth(lineWidthList)
        self.plotter_.setLineColors(colorList)
        self.plotter_.setLineStiles(stileList)

        try:
            plt.cla()
            
            self.plotter_.plot()
            self.figureCanvasPlotPreview.draw()

            self.updatePlotDataRange()
        except:
            # ラインのスタイルなどが設定されていない場合
            pass
    # plotGraph

    def updatePlotDataRange(self):
        xDataRange = self.plotter_.getXDataRange()
        yDataRange = self.plotter_.getYDataRange()

        # 範囲を+-10%ずつ増やす
        xMin = xDataRange["min"] - (xDataRange["max"] - xDataRange["min"]) * 0.1
        xMax = xDataRange["max"] + (xDataRange["max"] - xDataRange["min"]) * 0.1
        yMin = yDataRange["min"] - (yDataRange["max"] - yDataRange["min"]) * 0.1
        yMax = yDataRange["max"] + (yDataRange["max"] - yDataRange["min"]) * 0.1

        # スライダとスピンボックスに反映
        # X軸 min
        self.sliderXAxisMinLimit.setRange(xMin, xMax)
        # X軸 max
        self.sliderXAxisMaxLimit.setRange(xMin, xMax)
        # Y軸 min
        self.sliderYAxisMinLimit.setRange(yMin, yMax)
        # Y軸 max
        self.sliderYAxisMaxLimit.setRange(yMin, yMax)
    # updatePlotDataRange

    def changedCheckBoxXAxisLimit(self, state):
        minEnabled = self.sliderXAxisMinLimit.isChecked()
        maxEnabled = self.sliderXAxisMaxLimit.isChecked()
        self.plotter_.setXAxisLimitEnabled(minEnabled, maxEnabled)

        self.updateXAxisLimitValue(True)
    # changedCheckBoxXAxisMinLimit

    def changedSliderXAxisLimit(self, value):
        minEnabled = self.sliderXAxisMinLimit.isChecked()
        maxEnabled = self.sliderXAxisMaxLimit.isChecked()

        self.updateXAxisLimitValue(minEnabled or maxEnabled)
    # changedSliderXAxisLimit

    def updateXAxisLimitValue(self, plotEnabled=True):
        minValue = self.sliderXAxisMinLimit.getValue()
        maxValue = self.sliderXAxisMaxLimit.getValue()
        self.plotter_.setXAxisLimitValue(minValue, maxValue)
        if plotEnabled:
            self.plotGraph()
    # updateXAxisLimitValue

    def changedCheckBoxYAxisLimit(self, state):
        minEnabled = self.sliderYAxisMinLimit.isChecked()
        maxEnabled = self.sliderYAxisMaxLimit.isChecked()
        self.plotter_.setYAxisLimitEnabled(minEnabled, maxEnabled)

        self.updateYAxisLimitValue(True)
    # changedCheckBoxYAxisLimit

    def changedSliderYAxisLimit(self, value):
        minEnabled = self.sliderYAxisMinLimit.isChecked()
        maxEnabled = self.sliderYAxisMaxLimit.isChecked()
        self.updateYAxisLimitValue(minEnabled or maxEnabled)
    # changedSliderXAxisLimit

    def updateYAxisLimitValue(self, plotEnabled=True):
        minValue = self.sliderYAxisMinLimit.getValue()
        maxValue = self.sliderYAxisMaxLimit.getValue()
        self.plotter_.setYAxisLimitValue(minValue, maxValue)

        if plotEnabled:
            self.plotGraph()
    # updateYAxisLimitValue

    def changedCheckBoxLegendText(self, state):
        self.plotter_.setLegendEnabled(self.lineEditLegendText.isChecked())
        self.plotGraph()
    # changedCheckBoxLegendText

    def changedLineEditLegendText(self, text: str):
        self.plotter_.setLegendTexts(self.lineEditLegendText.getDataList())
        self.plotGraph()
    # changedLineEditLegendText

    def changedSliderLegendFontSize(self, value):
        self.plotter_.setLegendFontSize(value)
        self.plotGraph()
    # changedSliderLegendFontSize

    def changedComboBoxLegendPosition(self, index):
        position = self.comboBoxLegendPosition.getCurrentComboBoxText() 
        self.plotter_.setLegendPosition(position)
        self.plotGraph()
    # changedComboBoxLegendPosition

    def changedComboBoxLineSelection(self, index):
        text = self.comboBoxLineSelection.getCurrentComboBoxText()

        self.sliderLineWidth.setValue(self.lineSettings_[text]["width"])
        self.colorSelectorLineColor.setColor(self.lineSettings_[text]["color"])
        self.comboBoxLineStile.setCurrentComboBoxText(self.lineSettings_[text]["stile"])

        self.plotGraph()

    def changedSliderLineWidth(self, value):
        text = self.comboBoxLineSelection.getCurrentComboBoxText()
        self.lineSettings_[text]["width"] = value
        self.plotGraph()
    # changedSliderLineWidth

    def changedComboBoxLineColor(self, color):
        text = self.comboBoxLineSelection.getCurrentComboBoxText()
        self.lineSettings_[text]["color"] = color
        self.plotGraph()
    # changedComboBoxLineColor

    def changedComboBoxLineStile(self, index):
        text = self.comboBoxLineSelection.getCurrentComboBoxText()
        self.lineSettings_[text]["stile"] = self.comboBoxLineStile.getComboBoxText(index)
        self.plotGraph()
    # changedComboBoxLineStile

    def changedCheckBoxGrid(self, state):
        self.plotter_.setGridEnabled(self.checkBoxGrid.isChecked())
        self.plotGraph()
    # changedCheckBoxGrid

    def exportGraph(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getSaveFileName(None, "Save Plot", "", "PNG Files (*.png);;PDF Files (*.pdf)")
        if file_path == '':
            return
        
        self.plotter_.save(file_path)
    # exportGraph
        
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