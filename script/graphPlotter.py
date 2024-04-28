# graphPlotter.py
# Author: hoshina
# Created: 2024/04/14
# version: 0.0
# brief: グラフの描画を管理するクラス

import matplotlib.pyplot as plt
from switchedValue import SwitchedValue
import numpy as np

class GraphPlotter:   
    BIG_VALUE_ = 1e+10

    class Axis:
        DEFAULT_FONT_SIZE = 12

        class Limit:
            def __init__(self):
                self.min = SwitchedValue(0)
                self.max = SwitchedValue(0)
        
        def __init__(self):
            # parameters
            self.label = ""
            self.limit = self.Limit()
            self.fontSize = self.DEFAULT_FONT_SIZE
            # データから先頭のデータを引くかどうか
            self.enabledOffsetRejection = False

    class PlotParam:
        def __init__(self):
            self.colors = []
            self.lineStyles = []
            self.lineWidth = 1

    def __init__(self):
        # global settings
        # ここはプログラムから変更できないので直接書き換えてください
        plt.rcParams["font.family"] = "DejaVu Serif" # font

        self.fig_ = plt.figure()
        self.ax_ = self.fig_.add_subplot(111)

        # initialize the axis parameters
        self.xAxis_ = GraphPlotter.Axis()
        self.yAxis_ = GraphPlotter.Axis()

        # initialize the plot parameters
        self.plotParam_ = self.PlotParam()

        # initialize data
        self.dataList_ = []
        self.xDataIndexes_ = []
        self.yDataIndexes_ = []

        self.xDataRange_ = {"min": self.BIG_VALUE_, "max": -self.BIG_VALUE_}
        self.yDataRange_ = {"min": self.BIG_VALUE_, "max": -self.BIG_VALUE_}

    def getFigure(self):
        return self.fig_
    
    def getAxes(self):
        return self.ax_

    def plot(self):
        # reset the range
        self.resetRange_(self.xDataRange_)
        self.resetRange_(self.yDataRange_)

        # plot
        once = True
        while once:
            once = False
            if len(self.yDataIndexes_) == 0 or len(self.xDataIndexes_) == 0:
                self.ax_.plot([], [])
                break

            for i in range(len(self.yDataIndexes_)):
                yData = self.dataList_[self.yDataIndexes_[i]]
                if len(self.xDataIndexes_) == 1:
                    # x軸が1つの場合はデータを共有する
                    xData = self.dataList_[self.xDataIndexes_[0]]
                    self.ax_.plot(xData, yData)
                else:
                    xData = self.dataList_[self.xDataIndexes_[i]]
                    self.ax_.plot(xData, yData)
                self.updateRange_(self.xDataRange_, xData)
                self.updateRange_(self.yDataRange_, yData)

        # set the axis parameters
        self.ax_.set_xlabel(self.xAxis_.label, fontsize=self.xAxis_.fontSize)
        self.ax_.set_ylabel(self.yAxis_.label, fontsize=self.yAxis_.fontSize)
        if self.xAxis_.limit.min.enabled:
            self.ax_.set_xlim(left=self.xAxis_.limit.min.value)
        if self.xAxis_.limit.max.enabled:    
            self.ax_.set_xlim(right=self.xAxis_.limit.max.value)
        if self.yAxis_.limit.min.enabled:
            self.ax_.set_ylim(bottom=self.yAxis_.limit.min.value)
        if self.yAxis_.limit.max.enabled:
            self.ax_.set_ylim(top=self.yAxis_.limit.max.value)

        # resize plot
        self.fig_.tight_layout()

    def setData(self, dataList: list):
        self.dataList_ = dataList

    def addXDataIndex(self, index: int):
        self.xDataIndexes_.append(index)

    def removeXDataIndex(self, index: int):
        self.xDataIndexes_.remove(index)

    def setXDataIndex(self, index: int):
        self.xDataIndexes_ = [index]

    def addYDataIndex(self, index: int):
        self.yDataIndexes_.append(index)

    def removeYDataIndex(self, index: int):
        self.yDataIndexes_.remove(index)

    def setYDataIndex(self, index: int):
        self.yDataIndexes_ = [index]

    def setXAxisLabel(self, label: str):
        self.xAxis_.label = label

    def setYAxisLabel(self, label: str):
        self.yAxis_.label = label

    def setXAxisLimitValue(self, min: float, max: float):
        self.xAxis_.limit.min.value = min
        self.xAxis_.limit.max.value = max

    def setYAxisLimitValue(self, min: float, max: float):
        self.yAxis_.limit.min.value = min
        self.yAxis_.limit.max.value = max

    def setXAxisLimitEnabled(self, min: bool, max: bool):
        self.xAxis_.limit.min.enabled = min
        self.xAxis_.limit.max.enabled = max

    def setYAxisLimitEnabled(self, min: bool, max: bool):
        self.yAxis_.limit.min.enabled = min
        self.yAxis_.limit.max.enabled = max

    def setXAxisFontSize(self, size: int):
        self.xAxis_.fontSize = size

    def setYAxisFontSize(self, size: int):
        self.yAxis_.fontSize = size

    def getXDataRange(self):
        return self.xDataRange_
    
    def getYDataRange(self):
        return self.yDataRange_
    
    def clear(self):
        self.ax_.clear()
        self.dataList_ = []
        self.xDataIndexes_ = []
        self.yDataIndexes_ = []
        self.resetRange_(self.xDataRange_)
        self.resetRange_(self.yDataRange_)

    def show(self):
        plt.show()

    def save(self, filename: str):
        plt.savefig(filename)

    # private
    @staticmethod
    def updateRange_(range: dict, data: list):
        min = np.min(data)
        max = np.max(data)
        if min < range["min"]:
            range["min"] = min
        if max > range["max"]:
            range["max"] = max

    @staticmethod
    def resetRange_(range: dict):
        range["min"] = GraphPlotter.BIG_VALUE_
        range["max"] = -GraphPlotter.BIG_VALUE_