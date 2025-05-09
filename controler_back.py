# -*- coding: utf-8 -*-

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
        self.set()
        p={}#导出p
        if self.checkBox.isChecked()==False:
            p['后缘端点横坐标']=str(self.doubleSpinBox_x.value())
            p['后缘端点纵坐标']=str(self.doubleSpinBox_y.value())
            p['后缘圆心横坐标']=str(self.circle_x.value())
            p['后缘圆心纵坐标']=str(self.circle_y.value())
            p['后缘圆弧度数']=str(self.circle_x_2.value())
            
            self.set()
            
        else:
            #固定斜率后，将会根据两点的横坐标和斜率以及圆心位置来求出其他参数
            p['后缘端点横坐标']=str(self.doubleSpinBox_x.value())
            p['后缘端点纵坐标']=str(self.doubleSpinBox_y.value())
            p['后缘圆心横坐标']=str(self.circle_x.value())
            n=self.k*(self.circle_x.value()-self.doubleSpinBox_x.value())+self.doubleSpinBox_y.value()
            self.circle_y.setValue(n)
            p['后缘圆心纵坐标']=str(n)
            p['后缘圆弧度数']=str(self.circle_x_2.value())
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

