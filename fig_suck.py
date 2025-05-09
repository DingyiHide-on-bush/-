# -*- coding: utf-8 -*-
from PyQt6.QtCore import pyqtSlot
from PyQt6.QtWidgets import QApplication, QDialog
from PyQt6.QtCore import *
import tkinter.messagebox
import efforts
from Ui_fig_suck import Ui_Form
import numpy as np



    
class Form(QDialog, Ui_Form):
    """
    Class documentation goes here.
    """
    points=np.array([])
    points0=np.array([])
    Signal_draw =pyqtSignal(list)
    Signal_model =pyqtSignal(dict)
    model={}
    point1x=''
    point1y=''
    point2x=''
    point2y=''
    k1=0
    k2=0

    def __init__(self, parent=None):
        
        super(Form, self).__init__(parent)
        self.setupUi(self)
        
        self.pushButton_5.clicked.connect(self.controler)
        
    def controler(self):
        from controler_suck_and_press import Form as Form0
        form=Form0(self)
        #传输控制点坐标和权
        
        form.controlx=efforts.choose(self.text_x.toPlainText())
        form.controly=efforts.choose(self.text_y.toPlainText())
        form.controlw=efforts.choose(self.text_w.toPlainText())
        form.spinBox_x_2.setMaximum(len(form.controlx))
        form.on_spinBox_x_2_valueChanged(1)
        
        form.Signal_model.connect(self.get)
        form.show()
    def get(self, p):
       
        #p=[controlx,controly,controlw]
        self.text_x.setText('，'.join(list(map(str, p[0]))))
        self.text_y.setText('，'.join(list(map(str, p[1]))))
        self.text_w.setText('，'.join(list(map(str, p[2]))))
        self.on_pushButton_clicked()#自动绘制

        
        
   

        
    
    def check(self, ax, ay, wn, kn, degree):
    #检查数据是否规范
        ax=len(ax)
        ay=len(ay)
        wn=len(wn)
        kn=len(kn)
    
        if ax==ay and ax==wn and kn==-degree+ax-1 and ax-1 >=degree and ax !=0:
            pass
            return 1
        else:
            msg='''请检查数据是否违背以下规范:
            1.横纵坐标以及权重元素个数一致
            2.节点元素=控制点数-1-阶数
            3.控制点数>=阶数+1
            '''
            tkinter.messagebox.showerror(title='WARNING', message=msg) 

    @pyqtSlot()
    def on_pushButton_clicked(self):
        #绘制
   
        
        ax=self.point1x+'，'+self.text_x.toPlainText()+'，'+self.point2x
        ay=self.point1y+'，'+self.text_y.toPlainText()+'，'+self.point2y
        wn=self.text_w.toPlainText()
        kn=self.text_k.toPlainText()
        degree=int(self.spinBox.value())
        
        if ax=='' or ay=='' or wn=='' or kn=='':
            tkinter.messagebox.showerror(title='WARNING', message='请输入数据') 
        else:
   
            ax=efforts.choose(ax)
            ay=efforts.choose(ay)
            wn=efforts.choose(wn)
            kn=efforts.choose(kn)
            if self.check(ax, ay, wn, kn, degree)==1:
                
                ay[1]=ay[0]+self.k1*(ax[1]-ax[0])
                ay[-2]=ay[-1]+self.k2*(ax[-2]-ax[-1])  #为什么要反号？
                
                #校正model
                ay0=ay[1:-1]
                self.model['吸力面控制点纵坐标']='，'.join(list(map(str, ay0)))
                
                self.points=self.fig1.mpl.nurbs_plot(ax, ay, wn, kn, degree)
                if self.points0.size>0:
                    self.fig1.mpl.plots(self.points0)
                self.Signal_draw.emit(self.points.tolist())
                self.fig1.setVisible(True)

    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        #清除
        self.fig1.mpl.clear()
        self.fig1.mpl.draw()

    @pyqtSlot()
    def on_pushButton_3_clicked(self):
        #还原
        self.text_x.setText(self.model['吸力面控制点横坐标'])
        self.text_y.setText(self.model['吸力面控制点纵坐标'])
        self.text_w.setText(self.model['吸力面控制点权重'])
        self.text_k.setText(self.model['吸力面节点矢量'])
        self.spinBox.setValue(int(self.model['吸力面阶数']))
        m='('+self.point1x+'，'+self.point1y+')('+self.point2x+','+self.point2y+')'
        self.textBrowser_2.setText(m)

    @pyqtSlot()
    def on_pushButton_4_clicked(self):
        #导出
        dic_mod={'吸力面控制点横坐标':self.text_x.toPlainText(), \
                '吸力面控制点纵坐标':self.text_y.toPlainText(),\
                '吸力面控制点权重':self.text_w.toPlainText(),\
                '吸力面节点矢量':self.text_k.toPlainText(),\
                '吸力面阶数':str(self.spinBox.value())}
                

        self.Signal_model.emit(dic_mod)
        self.textBrowser_2.setText('导出当前面板方案成功')
        

    @pyqtSlot()
    def on_pushButton_7_clicked(self):
        # 绘制曲率
        p=self.points
        if p.any()!=False:
            cur=efforts.curve(p)

            #绘图-曲率半径
            from pass0 import Form
            form=Form(self)
            form.sw0=np.array(cur)
            form.on_pushButton_clicked()
            form.show()
       


        
        

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = Form()
    ui.show()
    sys.exit(app.exec())
        
