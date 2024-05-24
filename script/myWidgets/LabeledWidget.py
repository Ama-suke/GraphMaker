from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QLineEdit, QSizePolicy, QSlider, QSpinBox, QDoubleSpinBox, QCheckBox, QComboBox
from PySide6.QtCore import QSize, Qt
import numpy as np

# 継承の使い方が下手すぎ。マネしないでね

# namespace
class my_widget:
    class LabeledWidget(QWidget):
        LABEL_WIDTH = 90
        
        def __init__(self, widgets: QHBoxLayout, parent=None, hasCheckBox=False, hasSelectBox=False):
            super().__init__(parent)
            self.hasCheckBox_ = hasCheckBox
            self.hasSelectBox_ = hasSelectBox
            self.layout_ = QHBoxLayout()
            self.setupObject(widgets)

            # callback
            self.fCheckedCallback_ = None
            self.fSelectBoxCallback_ = None

            # data
            self.dataDict_ = {}

        def setupObject(self, widgets: QHBoxLayout):
            # objects
            if self.hasCheckBox_:
                self.label_ = QCheckBox(self)
            else:
                self.label_ = QLabel(self)
            self.layoutWidget_ = widgets

            if self.hasSelectBox_:
                self.selectBox_ = QComboBox(self)
            else:
                self.selectBox_ = None
            
            # label setting
            sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, self.label_.sizePolicy().verticalPolicy())
            self.label_.setSizePolicy(sizePolicy)
            self.label_.setMinimumSize(QSize(self.LABEL_WIDTH, 0))

            # layout
            self.layout_.addWidget(self.label_)
            if self.hasSelectBox_:
                self.layout_.addWidget(self.selectBox_)
            self.layout_.addLayout(self.layoutWidget_)

            # signal
            if self.hasCheckBox_: 
                self.label_.stateChanged.connect(self.checkBoxCheckedCallback_)
            if self.hasSelectBox_:  
                self.selectBox_.currentIndexChanged.connect(self.selectBoxChangedCallback_)

        def setLabelText(self, text: str):
            self.label_.setText(text)

        def setData(self, key: str, data):
            self.dataDict_[key] = data
            # keyがセレクトボックスと一致する場合はデータを反映
            if self.hasSelectBox_ and key == self.selectBox_.currentText():
                self.setWidgetItem(data)

        def setWidgetItem(self, data):
            pass

        def getLabel(self):
            return self.label_
        
        def getLayout(self):
            return self.layout_
        
        def setChecked(self, checked: bool):
            self.label_.setChecked(checked)
        
        def isChecked(self):
            return self.label_.isChecked()
        
        def getDataDict(self):
            return self.dataDict_
        
        def getDataList(self):
            return list(self.dataDict_.values())
        
        def setCheckedCallback(self, fCheckedCallback):
            self.fCheckedCallback_ = fCheckedCallback

        def addSelectBoxItem(self, text: str):
            self.selectBox_.addItem(text)
            self.dataDict_[text] = None

        def removeSelectBoxItem(self, text: str):
            self.selectBox_.removeItem(self.selectBox_.findText(text))
            self.dataDict_.pop(text, None)

        def clearSelectBox(self):
            self.selectBox_.clear()
            self.dataDict_.clear()

        def getCurrentSelectBoxIndex(self):
            return self.selectBox_.currentIndex()
        
        def getCurrentSelectBoxText(self):
            return self.selectBox_.currentText()

        def setSelectBoxCallback(self, fSelectBoxCallback):
            self.fSelectBoxCallback_ = fSelectBoxCallback

        # private:
        def checkBoxCheckedCallback_(self):
            if self.fCheckedCallback_ is not None:
                self.fCheckedCallback_(self.isChecked())

        def selectBoxChangedCallback_(self, index):
            if self.hasCheckBox_ and not self.label_.isChecked():
                # チェックボックスがチェックされていないときはコールバックを呼ばない
                return

            if self.fSelectBoxCallback_ is not None:
                self.fSelectBoxCallback_(index)
        
    class LabeledLineEdit(LabeledWidget):
        def __init__(self, parent=None, hasCheckBox=False, hasSelectBox=False):
            self.layoutLineEdit_ = QHBoxLayout()
            super().__init__(self.layoutLineEdit_, parent, hasCheckBox, hasSelectBox)

            # objects
            self.lineEdit_ = QLineEdit()

            # layout
            self.layoutLineEdit_.addWidget(self.lineEdit_)

            # signal
            self.lineEdit_.textChanged.connect(self.textChangedCallback_)

            # callback
            self.fTextChangedCallback_ = None

        def addSelectBoxItem(self, text: str):
            super().addSelectBoxItem(text)
            self.dataDict_[text] = ""
        
        def setText(self, text: str):
            self.lineEdit_.setText(text)

        def setWidgetItem(self, data):
            self.setText(data)
        
        def getText(self):
            return self.lineEdit_.text()
        
        def getLineEdit(self):
            return self.lineEdit_
        
        def setTextChangedCallback(self, fTextChangedCallback):
            self.fTextChangedCallback_ = fTextChangedCallback

        # private:
        def selectBoxChangedCallback_(self, index):
            if self.hasSelectBox_ and self.selectBox_.currentText() in self.dataDict_:
                curData = self.dataDict_[self.selectBox_.currentText()]
                self.lineEdit_.setText(curData)

            super().selectBoxChangedCallback_(index)

        def textChangedCallback_(self, text):
            if self.hasSelectBox_ and self.selectBox_.currentText() in self.dataDict_:
                self.dataDict_[self.selectBox_.currentText()] = text

            if self.hasCheckBox_ and not self.label_.isChecked():
                # チェックボックスがチェックされていないときはコールバックを呼ばない
                return

            if self.fTextChangedCallback_ is not None:
                self.fTextChangedCallback_(text)
        
    class LabeledSlider(LabeledWidget):
        SLIDER_RESOLUTION = 1000
        SLIDER_DECIMALS = 5

        def __init__(self, parent=None, hasCheckBox=False, hasSelectBox=False, isDouble=False):
            self.layoutSlider_ = QHBoxLayout()
            super().__init__(self.layoutSlider_, parent, hasCheckBox, hasSelectBox)
            self.isDouble_ = isDouble

            # objects
            self.slider_ = QSlider(parent)
            self.slider_.setOrientation(Qt.Horizontal)
            if isDouble:
                self.spinBox_ = QDoubleSpinBox(parent)
                self.spinBox_.setDecimals(self.SLIDER_DECIMALS)    # 小数点桁数
                self.sliderGain_ = 10 ** self.SLIDER_DECIMALS
            else:
                self.spinBox_ = QSpinBox(parent)
                self.sliderGain_ = 1

            # layout
            self.layoutSlider_.addWidget(self.slider_)
            self.layoutSlider_.addWidget(self.spinBox_)

            # signal
            self.slider_.valueChanged.connect(self.sliderChangedCallback_)
            self.spinBox_.valueChanged.connect(self.spinBoxChangedCallback_)

            # callback
            self.fValueChangeCallback_ = None

        def addSelectBoxItem(self, text: str):
            super().addSelectBoxItem(text)
            self.dataDict_[text] = 0
        
        def setValue(self, value):
            self.spinBox_.setValue(value)

        def setWidgetItem(self, data):
            self.setValue(data)
        
        def getValue(self):
            return self.spinBox_.value()
        
        def setRange(self, min, max):
            self.slider_.setRange(min * self.sliderGain_, max * self.sliderGain_)
            self.spinBox_.setRange(min, max)
            self.slider_.setSingleStep((max - min) / self.SLIDER_RESOLUTION * self.sliderGain_)
            if self.isDouble_:
                self.spinBox_.setSingleStep((max - min) / self.SLIDER_RESOLUTION)

        def setValueChangeCallback(self, fValueChangeCallback):
            self.fValueChangeCallback_ = fValueChangeCallback
        
        # private:
        def selectBoxChangedCallback_(self, index):
            if self.hasSelectBox_ and self.selectBox_.currentText() in self.dataDict_:
                curData = self.dataDict_[self.selectBox_.currentText()]
                self.setValue(curData)

            super().selectBoxChangedCallback_(index)

        def sliderChangedCallback_(self, value):
            self.spinBox_.setValue(value / self.sliderGain_)

        def spinBoxChangedCallback_(self, value):
            self.slider_.setValue(value * self.sliderGain_)
            if self.hasSelectBox_ and self.selectBox_.currentText() in self.dataDict_:
                self.dataDict_[self.selectBox_.currentText()] = value

            if self.hasCheckBox_ and not self.label_.isChecked():
                # チェックボックスがチェックされていないときはコールバックを呼ばない
                return
            
            if self.fValueChangeCallback_ is not None:
                self.fValueChangeCallback_(value)

    class LabeledComboBox(LabeledWidget):
        def __init__(self, parent=None, hasCheckBox=False, hasSelectBox=False):
            self.layoutComboBox_ = QHBoxLayout()
            super().__init__(self.layoutComboBox_, parent, hasCheckBox, hasSelectBox)

            # objects
            self.comboBox_ = QComboBox(parent)

            # layout
            self.layoutComboBox_.addWidget(self.comboBox_)

            # signal
            self.comboBox_.currentIndexChanged.connect(self.comboBoxChangedCallback_)

            # callback
            self.fComboBoxCallback_ = None

        def addSelectBoxItem(self, text: str):
            super().addSelectBoxItem(text)
            self.dataDict_[text] = 0

        def addComboBoxItem(self, text: str):
            self.comboBox_.addItem(text)

        def removeComboBoxItem(self, text: str):
            self.comboBox_.removeItem(self.comboBox_.findText(text))

        def clearComboBox(self):
            self.comboBox_.clear()

        def setCurrentComboBoxIndex(self, index):
            self.comboBox_.setCurrentIndex(index)

        def setCurrentComboBoxText(self, text):
            self.comboBox_.setCurrentText(text)

        def setWidgetItem(self, data):
            self.setCurrentComboBoxIndex(data)

        def getCurrentComboBoxIndex(self):
            return self.comboBox_.currentIndex()
        
        def getCurrentComboBoxText(self):
            return self.comboBox_.currentText()
        
        def getComboBoxText(self, index):
            return self.comboBox_.itemText(index)
        
        def setComboBoxCallback(self, fComboBoxCallback):
            self.fComboBoxCallback_ = fComboBoxCallback

        # private:
        def selectBoxChangedCallback_(self, index):
            if self.hasSelectBox_ and self.selectBox_.currentText() in self.dataDict_:
                curData = self.dataDict_[self.selectBox_.currentText()]
                self.comboBox_.setCurrentIndex(curData)

            super().selectBoxChangedCallback_(index)

        def comboBoxChangedCallback_(self, index):
            if self.hasSelectBox_ and self.selectBox_.currentText() in self.dataDict_:
                self.dataDict_[self.selectBox_.currentText()] = index

            if self.hasCheckBox_ and not self.label_.isChecked():
                # チェックボックスがチェックされていないときはコールバックを呼ばない
                return

            if self.fComboBoxCallback_ is not None:
                self.fComboBoxCallback_(index)

    class LabeledColorSelector(LabeledWidget):
        def __init__(self, parent=None, hasCheckBox=False, hasSelectBox=False):
            self.layoutColorSelector_ = QHBoxLayout()
            super().__init__(self.layoutColorSelector_, parent, hasCheckBox, hasSelectBox)

            # objects
            self.colorComboBox_ = QComboBox(parent)
            self.colorViewer_ = QLabel(parent)
            self.colorViewer_.setFixedSize(20, 20)

            # layout
            self.layoutColorSelector_.addWidget(self.colorComboBox_)
            self.layoutColorSelector_.addWidget(self.colorViewer_)

            # signal
            self.colorComboBox_.currentIndexChanged.connect(self.colorChangedCallback_)

            # callback
            self.fColorChangedCallback_ = None

            self.initializeColorList_()

        def addSelectBoxItem(self, text: str):
            super().addSelectBoxItem(text)
            self.dataDict_[text] = "Black"

        def setColor(self, color: str):
            self.colorComboBox_.setCurrentIndex(self.colorComboBox_.findText(color))

        def setWidgetItem(self, data):
            self.setColor(data)
        
        def getColor(self):
            return self.colorComboBox_.currentText()

        def setColorChangedCallback(self, fColorChangedCallback):
            self.fColorChangedCallback_ = fColorChangedCallback

        # private:
        def initializeColorList_(self):
            self.colorComboBox_.addItem("Black")
            self.colorComboBox_.addItem("Red")
            self.colorComboBox_.addItem("Green")
            self.colorComboBox_.addItem("Blue")
            self.colorComboBox_.addItem("Yellow")
            self.colorComboBox_.addItem("Cyan")
            self.colorComboBox_.addItem("Magenta")
            self.colorComboBox_.addItem("White")
            self.colorComboBox_.addItem("Orange")
            self.colorComboBox_.addItem("Purple")

            self.colorComboBox_.setCurrentIndex(0)

        def selectBoxChangedCallback_(self, index):
            if self.hasSelectBox_ and self.selectBox_.currentText() in self.dataDict_:
                curData = self.dataDict_[self.selectBox_.currentText()]
                self.setColor(curData)

            super().selectBoxChangedCallback_(index)

        def colorChangedCallback_(self, index):
            self.colorViewer_.setStyleSheet("background-color: " + self.colorComboBox_.currentText())
            if self.hasSelectBox_ and self.selectBox_.currentText() in self.dataDict_:
                self.dataDict_[self.selectBox_.currentText()] = self.colorComboBox_.currentText()

            if self.hasCheckBox_ and not self.label_.isChecked():
                # チェックボックスがチェックされていないときはコールバックを呼ばない
                return

            if self.fColorChangedCallback_ is not None:
                self.fColorChangedCallback_(self.colorComboBox_.currentText())