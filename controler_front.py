# -*- coding: utf-8 -*-

"""
Module implementing Form.
"""

from PyQt6.QtCore import pyqtSlot
from PyQt6.QtWidgets import QDialog
from PyQt6.QtCore import *
from Ui_controler_front import Ui_Form
import math


class Form(QDialog, Ui_Form):
    Signal_model =pyqtSignal(dict)
    Signal_model2 =pyqtSignal(dict)
    def __init__(self, parent=None):

        super().__init__(parent)
        self.setupUi(self)
        self.checkBox.setChecked(True)
        self.k=0
    def set(self):
        self.k=(self.doubleSpinBox_y.value()-self.circle_y.value())/(self.doubleSpinBox_x.value()-self.circle_x.value())
        self.textBrowser.setText(str(math.degrees(math.atan(self.k))))
    
    def get(self):
        p={}#导出p
        
        
        if self.checkBox.isChecked()==False:
            p['前缘端点横坐标']=str(self.doubleSpinBox_x.value())
            p['前缘端点纵坐标']=str(self.doubleSpinBox_y.value())
            p['前缘圆心横坐标']=str(self.circle_x.value())
            p['前缘圆心纵坐标']=str(self.circle_y.value())
            p['前缘圆弧度数']=str(self.circle_x_2.value())
            
            self.set()
        else:
            
            #固定斜率
            p['前缘端点横坐标']=str(self.doubleSpinBox_x.value())
            p['前缘端点纵坐标']=str(self.doubleSpinBox_y.value())
            p['前缘圆心横坐标']=str(self.circle_x.value())
            m=self.k*(self.circle_x.value()-self.doubleSpinBox_x.value())+self.doubleSpinBox_y.value()
            self.circle_y.setValue(m)
            p['前缘圆心纵坐标']=str(m)
            p['前缘圆弧度数']=str(self.circle_x_2.value())
        return p
        

    @pyqtSlot()
    def on_pushButton_3_clicked(self):
        #导出
        p=self.get()
        self.Signal_model.emit(p)

    @pyqtSlot()
    def on_pushButton_4_clicked(self):
        #绘制
        p=self.get()
        self.Signal_model2.emit(p)
