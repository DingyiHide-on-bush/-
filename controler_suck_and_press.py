# -*- coding: utf-8 -*-

"""
Module implementing Form.
"""
from PyQt6.QtCore import *
from PyQt6.QtCore import pyqtSlot
from PyQt6.QtWidgets import QDialog
import numpy as np
from Ui_controler_suck_and_press import Ui_Form


class Form(QDialog, Ui_Form):
    points=np.array([])
    controlx=[]
    controly=[]
    controlw=[]
    Signal_model =pyqtSignal(list)

    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    

    

    @pyqtSlot()
    def on_pushButton_4_clicked(self):
        #绘制  只有绘制后参数才会真正改变
        n=self.spinBox_x_2.value()
        self.controlx[n-1]=self.doubleSpinBox_x.value()
        self.controly[n-1]=self.doubleSpinBox_y.value()
        self.controlw[n]=self.doubleSpinBox_w.value()
        l1=[self.controlx]+[self.controly]+[self.controlw]
        self.Signal_model.emit(l1)
       
        
        
        

    @pyqtSlot(int)
    def on_spinBox_x_2_valueChanged(self, p0):
        n=p0
        self.doubleSpinBox_x.setValue(self.controlx[n-1])
        self.doubleSpinBox_y.setValue(self.controly[n-1])
        self.doubleSpinBox_w.setValue(self.controlw[n])

    
