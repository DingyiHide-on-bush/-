# Form implementation generated from reading ui file 'D:\mycodes\eric\main.ui'
#
# Created by: PyQt6 UI code generator 6.5.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1087, 792)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(parent=self.centralwidget)
        self.line.setGeometry(QtCore.QRect(860, 90, 21, 571))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.fig_main = MatplotlibWidget(parent=self.centralwidget)
        self.fig_main.setGeometry(QtCore.QRect(10, 100, 851, 561))
        self.fig_main.setObjectName("fig_main")
        self.layoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(2, 2, 1071, 83))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label.setMinimumSize(QtCore.QSize(0, 48))
        self.label.setMaximumSize(QtCore.QSize(16777215, 48))
        font = QtGui.QFont()
        font.setFamily("Adobe Myungjo Std M")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.textBrowser = QtWidgets.QTextBrowser(parent=self.layoutWidget)
        self.textBrowser.setMaximumSize(QtCore.QSize(16777215, 81))
        font = QtGui.QFont()
        font.setFamily("Adobe Myungjo Std M")
        font.setPointSize(12)
        self.textBrowser.setFont(font)
        self.textBrowser.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CursorShape.ForbiddenCursor))
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout.addWidget(self.textBrowser)
        self.spinBox = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(970, 100, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Adobe Myungjo Std M")
        font.setPointSize(20)
        self.spinBox.setFont(font)
        self.spinBox.setMinimum(1)
        self.spinBox.setProperty("value", 4)
        self.spinBox.setObjectName("spinBox")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(890, 110, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Myungjo Std M")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(880, 610, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Myungjo Std M")
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.textBrowser_2 = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(950, 610, 111, 41))
        self.textBrowser_2.setReadOnly(False)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(880, 560, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Myungjo Std M")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.textBrowser_3 = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(950, 560, 111, 41))
        self.textBrowser_3.setReadOnly(False)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(880, 510, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Myungjo Std M")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.textBrowser_4 = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.textBrowser_4.setGeometry(QtCore.QRect(950, 510, 111, 41))
        self.textBrowser_4.setReadOnly(False)
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.layoutWidget1 = QtWidgets.QWidget(parent=self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 670, 1061, 69))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.modify = QtWidgets.QHBoxLayout()
        self.modify.setObjectName("modify")
        self.leadingedge = QtWidgets.QCommandLinkButton(parent=self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        self.leadingedge.setFont(font)
        self.leadingedge.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.OpenHandCursor))
        self.leadingedge.setObjectName("leadingedge")
        self.modify.addWidget(self.leadingedge)
        self.trailingedge = QtWidgets.QCommandLinkButton(parent=self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        self.trailingedge.setFont(font)
        self.trailingedge.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.OpenHandCursor))
        self.trailingedge.setObjectName("trailingedge")
        self.modify.addWidget(self.trailingedge)
        self.suctionsurface = QtWidgets.QCommandLinkButton(parent=self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        self.suctionsurface.setFont(font)
        self.suctionsurface.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.OpenHandCursor))
        self.suctionsurface.setObjectName("suctionsurface")
        self.modify.addWidget(self.suctionsurface)
        self.pressuresurface = QtWidgets.QCommandLinkButton(parent=self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        self.pressuresurface.setFont(font)
        self.pressuresurface.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.OpenHandCursor))
        self.pressuresurface.setObjectName("pressuresurface")
        self.modify.addWidget(self.pressuresurface)
        self.horizontalLayout_3.addLayout(self.modify)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(parent=self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1087, 26))
        self.menubar.setObjectName("menubar")
        self.help = QtWidgets.QMenu(parent=self.menubar)
        self.help.setObjectName("help")
        self.save = QtWidgets.QMenu(parent=self.menubar)
        self.save.setObjectName("save")
        self.menu = QtWidgets.QMenu(parent=self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.action1 = QtGui.QAction(parent=MainWindow)
        self.action1.setObjectName("action1")
        self.actionsave_points_of_results = QtGui.QAction(parent=MainWindow)
        self.actionsave_points_of_results.setObjectName("actionsave_points_of_results")
        self.actionsave_the_modle = QtGui.QAction(parent=MainWindow)
        self.actionsave_the_modle.setObjectName("actionsave_the_modle")
        self.action1_2 = QtGui.QAction(parent=MainWindow)
        self.action1_2.setObjectName("action1_2")
        self.action11 = QtGui.QAction(parent=MainWindow)
        self.action11.setObjectName("action11")
        self.action33 = QtGui.QAction(parent=MainWindow)
        self.action33.setObjectName("action33")
        self.help.addAction(self.action33)
        self.save.addAction(self.actionsave_points_of_results)
        self.save.addAction(self.actionsave_the_modle)
        self.menu.addAction(self.action11)
        self.menubar.addAction(self.help.menuAction())
        self.menubar.addAction(self.save.menuAction())
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "一种通用二维叶型模型生成系统"))
        self.label.setText(_translate("MainWindow", "监视:"))
        self.label_2.setText(_translate("MainWindow", "样式"))
        self.label_3.setText(_translate("MainWindow", "备注"))
        self.label_4.setText(_translate("MainWindow", "入口宽度"))
        self.textBrowser_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">60</p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "喉部面积"))
        self.textBrowser_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.leadingedge.setText(_translate("MainWindow", "前缘"))
        self.trailingedge.setText(_translate("MainWindow", "后缘"))
        self.suctionsurface.setText(_translate("MainWindow", "吸力面"))
        self.pressuresurface.setText(_translate("MainWindow", "压力面"))
        self.pushButton.setText(_translate("MainWindow", "关闭"))
        self.pushButton_2.setText(_translate("MainWindow", "绘制"))
        self.pushButton_3.setText(_translate("MainWindow", "清除"))
        self.pushButton_5.setText(_translate("MainWindow", "通道宽度"))
        self.help.setTitle(_translate("MainWindow", "帮助"))
        self.save.setTitle(_translate("MainWindow", "保存"))
        self.menu.setTitle(_translate("MainWindow", "导入"))
        self.action1.setText(_translate("MainWindow", "样式beta"))
        self.actionsave_points_of_results.setText(_translate("MainWindow", "保存样本点"))
        self.actionsave_the_modle.setText(_translate("MainWindow", "保存样式(慎用)"))
        self.action1_2.setText(_translate("MainWindow", "未定"))
        self.action11.setText(_translate("MainWindow", "导入坐标点"))
        self.action33.setText(_translate("MainWindow", "点这里查看帮助"))
from MatplotlibWidget import MatplotlibWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
