# Form implementation generated from reading ui file 'D:\mycodes\eric\controler_suck_and_press.ui'
#
# Created by: PyQt6 UI code generator 6.5.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(597, 189)
        self.layoutWidget = QtWidgets.QWidget(parent=Form)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 20, 592, 42))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Adobe Myungjo Std M")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.spinBox_x_2 = QtWidgets.QSpinBox(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_x_2.sizePolicy().hasHeightForWidth())
        self.spinBox_x_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Adobe Myungjo Std M")
        font.setPointSize(20)
        self.spinBox_x_2.setFont(font)
        self.spinBox_x_2.setMinimum(1)
        self.spinBox_x_2.setObjectName("spinBox_x_2")
        self.horizontalLayout_5.addWidget(self.spinBox_x_2)
        self.label_5 = QtWidgets.QLabel(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Adobe Myungjo Std M")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.doubleSpinBox_w = QtWidgets.QDoubleSpinBox(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox_w.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_w.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Adobe Myungjo Std M")
        font.setPointSize(20)
        self.doubleSpinBox_w.setFont(font)
        self.doubleSpinBox_w.setObjectName("doubleSpinBox_w")
        self.horizontalLayout_5.addWidget(self.doubleSpinBox_w)
        self.pushButton_2 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 130, 51, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setObjectName("pushButton_2")
        self.layoutWidget1 = QtWidgets.QWidget(parent=Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 70, 592, 61))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(parent=self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Adobe Myungjo Std M")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.doubleSpinBox_x = QtWidgets.QDoubleSpinBox(parent=self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox_x.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_x.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Adobe Myungjo Std M")
        font.setPointSize(20)
        self.doubleSpinBox_x.setFont(font)
        self.doubleSpinBox_x.setMinimum(-99999.0)
        self.doubleSpinBox_x.setMaximum(99999.0)
        self.doubleSpinBox_x.setSingleStep(1.0)
        self.doubleSpinBox_x.setProperty("value", 20.0)
        self.doubleSpinBox_x.setObjectName("doubleSpinBox_x")
        self.horizontalLayout_3.addWidget(self.doubleSpinBox_x)
        self.doubleSpinBox_y = QtWidgets.QDoubleSpinBox(parent=self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox_y.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_y.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Adobe Myungjo Std M")
        font.setPointSize(20)
        self.doubleSpinBox_y.setFont(font)
        self.doubleSpinBox_y.setMinimum(-99999.0)
        self.doubleSpinBox_y.setMaximum(99999.0)
        self.doubleSpinBox_y.setProperty("value", -13.0)
        self.doubleSpinBox_y.setObjectName("doubleSpinBox_y")
        self.horizontalLayout_3.addWidget(self.doubleSpinBox_y)
        self.pushButton_4 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 130, 51, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(Form)
        self.pushButton_2.clicked.connect(Form.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "控制器-吸力面与压力面"))
        self.label_4.setText(_translate("Form", "控制点位置"))
        self.label_5.setText(_translate("Form", "控制点权重"))
        self.pushButton_2.setText(_translate("Form", "关闭"))
        self.label.setText(_translate("Form", "控制点坐标"))
        self.pushButton_4.setText(_translate("Form", "绘制"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
