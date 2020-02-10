import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from open_file import *
import pandas as pd
from Heatmap_97MN import *
import numpy as np


class heatmap_figure(QWidget):

    ''' global variable in heatmap_figure '''

    def __init__(self):
        super().__init__()
        self.filename = None
        self.cmap = 'Reds'
        self.vmin = 720
        self.vmax = 820
        self.hist_to_heatmap = True
        self.top_y_axis = 25
        self.range_x_axis = (720, 820)
        self.interval_bin = 5
        self.bins = np.arange(self.vmin, self.vmax, self.interval_bin)
        self.setupUI()

    def setupUI(self):

        self.setGeometry(600, 100, 1200, 800)
        self.setWindowTitle("Heatmap & Histogram for needle")
        self.setWindowIcon(QIcon('PyQt5/images/edit.png'))

        self.label_title = QLabel()
        self.label_title.setText("By Wonjun")

        ''' PushButton collection '''
        self.pushButton = QPushButton("open the file")
        self.histoButton = QPushButton("convert to heatmap-histogram")
        self.pushButton1 = QPushButton("save the Heatmap")
        self.pushButton2 = QPushButton("save the Histogram")

        ''' 색깔 변환을 위한 콤보 박스 라벨 '''
        self.label_color = QLabel()
        self.label_color.setText("Color Change for heatmap")

        ''' combobox collection '''
        self.combobox_color = QComboBox()
        self.combobox_color.addItem("Reds")
        self.combobox_color.addItem("Greens")
        self.combobox_color.addItem("Greys")
        self.combobox_color.addItem("Oranges")
        self.combobox_color.addItem("Blues")

        ''' lineedit label 모음 '''
        self.label_minimum = QLabel()
        self.label_minimum.setText("Minimum value for heatmap/histogram")
        self.label_maximum = QLabel()
        self.label_maximum.setText("Maximum value for heatmap/histogram")

        ''' lineedit collection '''
        self.min_spinbox = QSpinBox()
        self.min_spinbox.setMinimum(200)
        self.min_spinbox.setMaximum(800)
        self.max_spinbox = QSpinBox()
        self.max_spinbox.setMaximum(900)
        self.max_spinbox.setMinimum(300)

        ''' 빈 넘버 라벨 '''
        self.label_slider = QLabel()
        self.label_slider.setText("Interval")

        self.label_interval = QLabel()
        self.label_interval.setText(f"{self.interval_bin}")

        ''' 히스토그램 bin을 조절하기 위한 slider'''
        self.slider_bins = QSlider(Qt.Horizontal)
        self.slider_bins.setTickPosition(QSlider.TicksBelow)
        self.slider_bins.setRange(1, 20)
        self.slider_bins.setTickInterval(1)
        self.slider_bins.setSingleStep(1)
        self.slider_bins.setValue(self.interval_bin)

        ''' 통계 결과 창에 대한 라벨 '''
        self.label_result = QLabel()
        self.label_result.setText("Statistical Result")

        ''' result textbrowser '''
        self.result_text = QTextBrowser()

        ''' Action 모음 '''
        self.pushButton.clicked.connect(self.pushButtonClicked)
        self.histoButton.clicked.connect(self.plottinghistogram)
        self.combobox_color.activated[str].connect(
            self.combobox_color_activated)
        self.min_spinbox.valueChanged.connect(
            self.lineedit_minvalue_textchanged)
        self.max_spinbox.valueChanged.connect(
            self.lineedit_maxvalue_textchanged)
        self.slider_bins.valueChanged[int].connect(self.setbins_histogram)

        ''' heatmap 그려주기 위한 모음. '''
        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig)

        ''' left Layout 구성하기 '''
        leftLayout = QVBoxLayout()
        leftLayout.addWidget(self.canvas)

        ''' 작은 right layout 구성하기 '''
        rightLayout_small = QHBoxLayout()
        rightLayout_small.addWidget(self.pushButton1)
        rightLayout_small.addWidget(self.pushButton2)

        rightLayout_bins = QHBoxLayout()
        rightLayout_bins.addWidget(self.label_slider)
        rightLayout_bins.addWidget(self.label_interval)

        ''' Right Layout 구성하기 '''
        rightLayout = QVBoxLayout()
        rightLayout.addWidget(self.label_title)
        rightLayout.addWidget(self.pushButton)
        rightLayout.addWidget(self.histoButton)
        rightLayout.addLayout(rightLayout_small)
        rightLayout.addStretch(0.5)

        rightLayout.addWidget(self.label_color)
        rightLayout.addWidget(self.combobox_color)
        rightLayout.addWidget(self.label_minimum)
        rightLayout.addWidget(self.min_spinbox)
        rightLayout.addWidget(self.label_maximum)
        rightLayout.addWidget(self.max_spinbox)
        rightLayout.addStretch(0.5)

        rightLayout.addLayout(rightLayout_bins)
        rightLayout.addWidget(self.slider_bins)
        rightLayout.addWidget(self.label_result)
        rightLayout.addWidget(self.result_text)
        rightLayout.addStretch(1)

        layout = QHBoxLayout()
        layout.addLayout(leftLayout)
        layout.addLayout(rightLayout)
        layout.setStretchFactor(leftLayout, 1)
        layout.setStretchFactor(rightLayout, 0)

        self.setLayout(layout)

    def pushButtonClicked(self):
        self.hist_to_heatmap = True
        self.openfile = fileoptions()
        filename = self.openfile.openFileNameDialog()

        if filename:

            self.filename = filename
            self.plottingheatmap()

    def combobox_color_activated(self, text):

        cmap = text
        self.cmap = cmap

        if self.filename == None:
            print("no file selected(1)")

        elif self.filename and self.hist_to_heatmap:
            self.plottingheatmap()

        elif self.filename and self.hist_to_heatmap == False:
            pass

    def lineedit_minvalue_textchanged(self):
        vminvalue = self.min_spinbox.value()

        if self.hist_to_heatmap:

            if vminvalue >= 200:
                self.vmin = vminvalue
                self.plottingheatmap()

        elif self.hist_to_heatmap == False and self.label_interval.text() == f"{self.interval_bin}":

            if vminvalue >= 200:
                self.interval_bin = self.slider_bins.value()
                self.bins = np.arange(self.vmin, self.vmax, self.interval_bin)
                self.vmin = vminvalue
                self.hist_to_heatmap = True
                self.plottinghistogram()

        else:
            print("정수가 아닙니다.(1)")

    def lineedit_maxvalue_textchanged(self):
        vmaxvalue = self.max_spinbox.value()

        if self.hist_to_heatmap:
            if vmaxvalue > self.vmin:
                self.vmax = vmaxvalue
                self.plottingheatmap()
            # self.max_lineEdit.clear()

        elif self.hist_to_heatmap == False and self.label_interval.text() == f"{self.interval_bin}":
            if vmaxvalue > self.vmin:
                self.interval_bin = self.slider_bins.value()
                self.bins = np.arange(self.vmin, self.vmax, self.interval_bin)
                self.vmax = vmaxvalue
                self.hist_to_heatmap = True
                self.plottinghistogram()
                print(f"second {self.hist_to_heatmap}")

        else:
            print("정수가 아닙니다.(2)")

    def plottingheatmap(self):

        if self.filename == None:
            print("no file selected(2)")

        else:
            figure_heatmap, height_ind_needle = makingheatmap(self.filename)
            print("good job")
            ax = self.fig.add_subplot(1, 1, 1)
            im = ax.imshow(figure_heatmap,
                           cmap=self.cmap, vmin=self.vmin, vmax=self.vmax)

            cbar = self.fig.colorbar(im)
            cbar.ax.set_ylabel("height(units:um)", rotation=-90, va="bottom")

            annotate_heatmap(im, valfmt="{x:.1f}")

            self.canvas.draw()
            self.fig.clear()
            self.result_text.setText(
                f"총 갯수: {height_ind_needle.describe()[0]:.0f} 개\n평균: {height_ind_needle.describe()[1]:.2f} um\n표준편차: {height_ind_needle.describe()[2]:.2f}\n최소높이: {height_ind_needle.describe()[3]:.2f} um\n최대높이: {height_ind_needle.describe()[-1]:.2f} um")

    def setbins_histogram(self, value_slider):

        if self.filename == None:
            print("no file selected(3)")

        elif self.filename and self.hist_to_heatmap == False:

            self.interval_bin = value_slider

            if self.interval_bin > 0:
                self.bins = np.arange(self.vmin, self.vmax, self.interval_bin)

            # self.max_lineEdit
            self.label_interval.setText(str(value_slider))
            self.hist_to_heatmap = True

            self.plottinghistogram()

    def plottinghistogram(self):

        if self.filename == None:
            print("no file selected(3)")

        elif self.filename and self.hist_to_heatmap:

            _, height_ind_needle = makingheatmap(self.filename)
            self.interval_bin = self.slider_bins.value()
            self.bins = np.arange(self.vmin, self.vmax, self.interval_bin)
            ax = self.fig.add_subplot(1, 1, 1)

            ax.set(ylim=[0, self.top_y_axis],
                   title="Histogram", ylabel='amount')

            ax.hist(height_ind_needle,
                    bins=self.bins, range=(self.vmin, self.vmax))

            self.canvas.draw()
            self.hist_to_heatmap = False
            #print("뭐가 문제야!!")
            self.fig.clear()

        elif self.filename and self.hist_to_heatmap == False:

            self.plottingheatmap()
            self.hist_to_heatmap = True
#            self.result_text.setText(
#                f"총 갯수: {height_ind_needle.describe()[0]}\n평균: {height_ind_needle.describe()[1]}\n표준편차: {height_ind_needle.describe()[2]}\n최소높이: {height_ind_needle.describe()[3]}\n최대높이: {height_ind_needle.describe()[-1]}")
