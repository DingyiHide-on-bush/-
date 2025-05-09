import sys, efforts
import matplotlib
import numpy as np
matplotlib.use("Qt5Agg")


from PyQt6.QtWidgets import QApplication,  QVBoxLayout,QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


#副本

class MyMplCanvas(FigureCanvas):
    """FigureCanvas的最终的父类其实是QWidget。"""

    def __init__(self, parent=None, width=2, height=2, dpi=100):

        # 配置中文显示
        plt.rcParams['font.family'] = ['SimHei']  # 用来正常显示中文标签
        plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
        plt.gca().set_aspect('equal')
        self.fig = Figure(figsize=(width, height), dpi=dpi)  # 新建一个figure
        self.axes = self.fig.add_subplot(111)  # 建立一个子图，如果要建立复合图，可以在这里修改
 
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)
        self.axes.grid(True)
        FigureCanvas.updateGeometry(self)  



    def nurbs_plot(self, ax, ay, wn, kn, degree):
        #画nurbs曲线
        weigh=wn#权重会被自动归一化处理（总和为1，占比不变）
        knot=kn#节点矢量元素个数=阶数+控制点数+1，其内元素从0不严格单增至1
        an=[];
        
        for i in range(len(ax)):
            an=an+[[ax[i], ay[i]]]
    
        plts=efforts.nurbs(an,weigh, knot, degree)
        t=plts[:, 0]
        s=plts[:, 1]
        
        self.axes.plot(t, s, color='blue')
        an=np.array(an)
        self.axes.scatter(an[:, 0], an[:, 1], color='red', marker='*')
        self.axes.grid(True)
        self.draw()
        return plts
        
    def clear(self):
        self.axes.cla()
        
    def plots(self, points):
        #画  总曲线 输入二维数组或列表
        if type(points)==np.ndarray:
            pass
        elif type(points)==list:
            points=np.array(points)
        if len(points[0, :].tolist()) != 2:
            points=points.T
        #转为列是维度的2维数组
        
        x=points[:, 0]
        y=points[:, 1]
        self.axes.plot(x, y)
        self.axes.grid(True)
        self.draw()
    def scatters(self, point):
        #画点
        x=point[0].tolist()
        y=point[1].tolist()
        self.axes.scatter(x, y)
        self.axes.grid(True)
        self.draw()



    
class MatplotlibWidget(QWidget):
    def __init__(self, parent=None):
        super(MatplotlibWidget, self).__init__(parent)
        self.initUi()

    def initUi(self):
        self.layout = QVBoxLayout(self)
        self.mpl = MyMplCanvas(self, width=3, height=3, dpi=100)
        self.mpl_ntb = NavigationToolbar(self.mpl, self)  # 添加完整的 toolbar
        self.layout.addWidget(self.mpl)
        self.layout.addWidget(self.mpl_ntb)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MatplotlibWidget()
    ui.mpl.start_static_plot()  # 测试静态图效果
    # ui.mpl.start_dynamic_plot() # 测试动态图效果
    ui.show()
    sys.exit(app.exec_()) 
