# -*- coding: utf-8 -*-

from PyQt6.QtCore import pyqtSlot
from PyQt6.QtWidgets import QDialog
import numpy as np
from Ui_pass0 import Ui_Form


class Form(QDialog, Ui_Form):
    sw0=np.array([])
    sw0_suc=np.array([])
    sw0_pre=np.array([])

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        
    @pyqtSlot()
    def on_pushButton_clicked(self):
        self.pass0.mpl.plots(self.sw0)
        self.pass0.mpl.draw()

    @pyqtSlot()
    def on_pushButton_3_clicked(self):
        # 吸力面
        self.pass0.mpl.plots(self.sw0_suc)
        self.pass0.mpl.draw()

    @pyqtSlot()
    def on_pushButton_4_clicked(self):
        # 压力面
        self.pass0.mpl.plots(self.sw0_pre)
        self.pass0.mpl.draw()

    @pyqtSlot()
    def on_pushButton_5_clicked(self):
        # 清除
        self.pass0.mpl.clear()
        self.pass0.mpl.draw()
