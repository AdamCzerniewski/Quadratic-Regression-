# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1293, 841)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 361, 211))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 30, 81, 17))
        self.label.setObjectName("label")
        self.tf_pointA_x = QtWidgets.QLineEdit(self.groupBox)
        self.tf_pointA_x.setGeometry(QtCore.QRect(90, 29, 31, 21))
        self.tf_pointA_x.setObjectName("tf_pointA_x")
        self.tf_pointA_y = QtWidgets.QLineEdit(self.groupBox)
        self.tf_pointA_y.setGeometry(QtCore.QRect(149, 29, 31, 21))
        self.tf_pointA_y.setObjectName("tf_pointA_y")
        self.tf_pointB_x = QtWidgets.QLineEdit(self.groupBox)
        self.tf_pointB_x.setGeometry(QtCore.QRect(90, 78, 31, 21))
        self.tf_pointB_x.setObjectName("tf_pointB_x")
        self.tf_pointB_y = QtWidgets.QLineEdit(self.groupBox)
        self.tf_pointB_y.setGeometry(QtCore.QRect(149, 78, 31, 21))
        self.tf_pointB_y.setObjectName("tf_pointB_y")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 78, 71, 17))
        self.label_2.setObjectName("label_2")
        self.tf_pointC_x = QtWidgets.QLineEdit(self.groupBox)
        self.tf_pointC_x.setGeometry(QtCore.QRect(90, 128, 31, 21))
        self.tf_pointC_x.setObjectName("tf_pointC_x")
        self.tf_pointC_y = QtWidgets.QLineEdit(self.groupBox)
        self.tf_pointC_y.setGeometry(QtCore.QRect(149, 128, 31, 21))
        self.tf_pointC_y.setObjectName("tf_pointC_y")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 128, 71, 17))
        self.label_3.setObjectName("label_3")
        self.btn_enterParams = QtWidgets.QPushButton(self.groupBox)
        self.btn_enterParams.setGeometry(QtCore.QRect(150, 170, 89, 25))
        self.btn_enterParams.setObjectName("btn_enterParams")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(130, 80, 16, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(190, 80, 16, 17))
        self.label_5.setObjectName("label_5")
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setGeometry(QtCore.QRect(130, 30, 16, 17))
        self.label_13.setObjectName("label_13")
        self.label_15 = QtWidgets.QLabel(self.groupBox)
        self.label_15.setGeometry(QtCore.QRect(190, 30, 16, 17))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.groupBox)
        self.label_16.setGeometry(QtCore.QRect(130, 130, 16, 17))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.groupBox)
        self.label_17.setGeometry(QtCore.QRect(190, 130, 16, 17))
        self.label_17.setObjectName("label_17")
        self.btn_clearParams = QtWidgets.QPushButton(self.groupBox)
        self.btn_clearParams.setGeometry(QtCore.QRect(260, 170, 89, 25))
        self.btn_clearParams.setObjectName("btn_clearParams")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(400, 10, 641, 461))
        self.groupBox_2.setObjectName("groupBox_2")
        self.wgt1 = PlotWidget(self.groupBox_2)
        self.wgt1.setGeometry(QtCore.QRect(10, 30, 621, 421))
        self.wgt1.setObjectName("wgt1")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 230, 361, 211))
        self.groupBox_3.setObjectName("groupBox_3")
        self.tf_matrix_sqrdx1 = QtWidgets.QLineEdit(self.groupBox_3)
        self.tf_matrix_sqrdx1.setGeometry(QtCore.QRect(30, 39, 31, 21))
        self.tf_matrix_sqrdx1.setObjectName("tf_matrix_sqrdx1")
        self.tf_matrix_sqrdx2 = QtWidgets.QLineEdit(self.groupBox_3)
        self.tf_matrix_sqrdx2.setGeometry(QtCore.QRect(30, 70, 31, 21))
        self.tf_matrix_sqrdx2.setObjectName("tf_matrix_sqrdx2")
        self.tf_matrix_sqrdx3 = QtWidgets.QLineEdit(self.groupBox_3)
        self.tf_matrix_sqrdx3.setGeometry(QtCore.QRect(30, 100, 31, 21))
        self.tf_matrix_sqrdx3.setObjectName("tf_matrix_sqrdx3")
        self.tf_matrix_x2 = QtWidgets.QLineEdit(self.groupBox_3)
        self.tf_matrix_x2.setGeometry(QtCore.QRect(70, 70, 31, 21))
        self.tf_matrix_x2.setObjectName("tf_matrix_x2")
        self.tf_matrix_x3 = QtWidgets.QLineEdit(self.groupBox_3)
        self.tf_matrix_x3.setGeometry(QtCore.QRect(70, 100, 31, 21))
        self.tf_matrix_x3.setObjectName("tf_matrix_x3")
        self.tf_matrix_x1 = QtWidgets.QLineEdit(self.groupBox_3)
        self.tf_matrix_x1.setGeometry(QtCore.QRect(70, 40, 31, 21))
        self.tf_matrix_x1.setObjectName("tf_matrix_x1")
        self.tf_matrix_c3 = QtWidgets.QLineEdit(self.groupBox_3)
        self.tf_matrix_c3.setGeometry(QtCore.QRect(110, 100, 31, 21))
        self.tf_matrix_c3.setObjectName("tf_matrix_c3")
        self.tf_matrix_c2 = QtWidgets.QLineEdit(self.groupBox_3)
        self.tf_matrix_c2.setGeometry(QtCore.QRect(110, 70, 31, 21))
        self.tf_matrix_c2.setObjectName("tf_matrix_c2")
        self.tf_matrix_c1 = QtWidgets.QLineEdit(self.groupBox_3)
        self.tf_matrix_c1.setGeometry(QtCore.QRect(110, 40, 31, 21))
        self.tf_matrix_c1.setObjectName("tf_matrix_c1")
        self.tf_matrix_y3 = QtWidgets.QLineEdit(self.groupBox_3)
        self.tf_matrix_y3.setGeometry(QtCore.QRect(150, 100, 31, 21))
        self.tf_matrix_y3.setObjectName("tf_matrix_y3")
        self.tf_matrix_y2 = QtWidgets.QLineEdit(self.groupBox_3)
        self.tf_matrix_y2.setGeometry(QtCore.QRect(150, 70, 31, 21))
        self.tf_matrix_y2.setObjectName("tf_matrix_y2")
        self.tf_matrix_y1 = QtWidgets.QLineEdit(self.groupBox_3)
        self.tf_matrix_y1.setGeometry(QtCore.QRect(150, 40, 31, 21))
        self.tf_matrix_y1.setObjectName("tf_matrix_y1")
        self.btn_enterMatrix = QtWidgets.QPushButton(self.groupBox_3)
        self.btn_enterMatrix.setGeometry(QtCore.QRect(150, 170, 89, 25))
        self.btn_enterMatrix.setObjectName("btn_enterMatrix")
        self.label_14 = QtWidgets.QLabel(self.groupBox_3)
        self.label_14.setGeometry(QtCore.QRect(0, -10, 31, 161))
        self.label_14.setObjectName("label_14")
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setGeometry(QtCore.QRect(183, 30, 67, 111))
        self.label_7.setObjectName("label_7")
        self.btn_clearMatrix = QtWidgets.QPushButton(self.groupBox_3)
        self.btn_clearMatrix.setGeometry(QtCore.QRect(260, 170, 89, 25))
        self.btn_clearMatrix.setObjectName("btn_clearMatrix")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 450, 361, 261))
        self.groupBox_4.setObjectName("groupBox_4")
        self.tf_RREF_val1 = QtWidgets.QLineEdit(self.groupBox_4)
        self.tf_RREF_val1.setGeometry(QtCore.QRect(150, 41, 31, 21))
        self.tf_RREF_val1.setReadOnly(True)
        self.tf_RREF_val1.setObjectName("tf_RREF_val1")
        self.tf_RREF_a1 = QtWidgets.QLineEdit(self.groupBox_4)
        self.tf_RREF_a1.setGeometry(QtCore.QRect(30, 40, 31, 21))
        self.tf_RREF_a1.setReadOnly(True)
        self.tf_RREF_a1.setObjectName("tf_RREF_a1")
        self.tf_RREF_c3 = QtWidgets.QLineEdit(self.groupBox_4)
        self.tf_RREF_c3.setGeometry(QtCore.QRect(110, 101, 31, 21))
        self.tf_RREF_c3.setReadOnly(True)
        self.tf_RREF_c3.setObjectName("tf_RREF_c3")
        self.tf_RREF_b3 = QtWidgets.QLineEdit(self.groupBox_4)
        self.tf_RREF_b3.setGeometry(QtCore.QRect(70, 101, 31, 21))
        self.tf_RREF_b3.setReadOnly(True)
        self.tf_RREF_b3.setObjectName("tf_RREF_b3")
        self.tf_RREF_a3 = QtWidgets.QLineEdit(self.groupBox_4)
        self.tf_RREF_a3.setGeometry(QtCore.QRect(30, 101, 31, 21))
        self.tf_RREF_a3.setReadOnly(True)
        self.tf_RREF_a3.setObjectName("tf_RREF_a3")
        self.tf_RREF_b1 = QtWidgets.QLineEdit(self.groupBox_4)
        self.tf_RREF_b1.setGeometry(QtCore.QRect(70, 41, 31, 21))
        self.tf_RREF_b1.setReadOnly(True)
        self.tf_RREF_b1.setObjectName("tf_RREF_b1")
        self.tf_RREF_a2 = QtWidgets.QLineEdit(self.groupBox_4)
        self.tf_RREF_a2.setGeometry(QtCore.QRect(30, 71, 31, 21))
        self.tf_RREF_a2.setReadOnly(True)
        self.tf_RREF_a2.setObjectName("tf_RREF_a2")
        self.tf_RREF_c2 = QtWidgets.QLineEdit(self.groupBox_4)
        self.tf_RREF_c2.setGeometry(QtCore.QRect(110, 71, 31, 21))
        self.tf_RREF_c2.setReadOnly(True)
        self.tf_RREF_c2.setObjectName("tf_RREF_c2")
        self.tf_RREF_val3 = QtWidgets.QLineEdit(self.groupBox_4)
        self.tf_RREF_val3.setGeometry(QtCore.QRect(150, 101, 31, 21))
        self.tf_RREF_val3.setReadOnly(True)
        self.tf_RREF_val3.setObjectName("tf_RREF_val3")
        self.tf_RREF_b2 = QtWidgets.QLineEdit(self.groupBox_4)
        self.tf_RREF_b2.setGeometry(QtCore.QRect(70, 71, 31, 21))
        self.tf_RREF_b2.setReadOnly(True)
        self.tf_RREF_b2.setObjectName("tf_RREF_b2")
        self.tf_RREF_c1 = QtWidgets.QLineEdit(self.groupBox_4)
        self.tf_RREF_c1.setGeometry(QtCore.QRect(110, 41, 31, 21))
        self.tf_RREF_c1.setReadOnly(True)
        self.tf_RREF_c1.setObjectName("tf_RREF_c1")
        self.tf_RREF_val2 = QtWidgets.QLineEdit(self.groupBox_4)
        self.tf_RREF_val2.setGeometry(QtCore.QRect(150, 71, 31, 21))
        self.tf_RREF_val2.setReadOnly(True)
        self.tf_RREF_val2.setObjectName("tf_RREF_val2")
        self.label_8 = QtWidgets.QLabel(self.groupBox_4)
        self.label_8.setGeometry(QtCore.QRect(20, 170, 71, 17))
        self.label_8.setObjectName("label_8")
        self.tf_equation = QtWidgets.QLineEdit(self.groupBox_4)
        self.tf_equation.setGeometry(QtCore.QRect(90, 170, 251, 21))
        self.tf_equation.setReadOnly(True)
        self.tf_equation.setObjectName("tf_equation")
        self.label_9 = QtWidgets.QLabel(self.groupBox_4)
        self.label_9.setGeometry(QtCore.QRect(270, 40, 31, 17))
        self.label_9.setObjectName("label_9")
        self.tf_a = QtWidgets.QLineEdit(self.groupBox_4)
        self.tf_a.setEnabled(True)
        self.tf_a.setGeometry(QtCore.QRect(300, 40, 41, 21))
        self.tf_a.setReadOnly(True)
        self.tf_a.setObjectName("tf_a")
        self.tf_b = QtWidgets.QLineEdit(self.groupBox_4)
        self.tf_b.setGeometry(QtCore.QRect(300, 70, 41, 21))
        self.tf_b.setReadOnly(True)
        self.tf_b.setObjectName("tf_b")
        self.tf_c = QtWidgets.QLineEdit(self.groupBox_4)
        self.tf_c.setGeometry(QtCore.QRect(300, 100, 41, 21))
        self.tf_c.setReadOnly(True)
        self.tf_c.setObjectName("tf_c")
        self.label_10 = QtWidgets.QLabel(self.groupBox_4)
        self.label_10.setGeometry(QtCore.QRect(270, 70, 31, 17))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox_4)
        self.label_11.setGeometry(QtCore.QRect(270, 100, 31, 17))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox_4)
        self.label_12.setGeometry(QtCore.QRect(0, -10, 31, 161))
        self.label_12.setObjectName("label_12")
        self.label_6 = QtWidgets.QLabel(self.groupBox_4)
        self.label_6.setGeometry(QtCore.QRect(183, 30, 67, 111))
        self.label_6.setObjectName("label_6")
        self.btn_clearRREF = QtWidgets.QPushButton(self.groupBox_4)
        self.btn_clearRREF.setGeometry(QtCore.QRect(260, 220, 89, 25))
        self.btn_clearRREF.setObjectName("btn_clearRREF")
        self.tf_messages = QtWidgets.QTextEdit(self.centralwidget)
        self.tf_messages.setGeometry(QtCore.QRect(400, 490, 361, 181))
        self.tf_messages.setReadOnly(True)
        self.tf_messages.setObjectName("tf_messages")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1293, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Quadratic Regression Calculator"))
        self.groupBox.setTitle(_translate("MainWindow", "Parameters"))
        self.label.setText(_translate("MainWindow", "Point A = (  "))
        self.label_2.setText(_translate("MainWindow", "Point B = (               "))
        self.label_3.setText(_translate("MainWindow", "Point C = (               "))
        self.btn_enterParams.setText(_translate("MainWindow", "Enter"))
        self.label_4.setText(_translate("MainWindow", ","))
        self.label_5.setText(_translate("MainWindow", ")"))
        self.label_13.setText(_translate("MainWindow", ","))
        self.label_15.setText(_translate("MainWindow", ")"))
        self.label_16.setText(_translate("MainWindow", ","))
        self.label_17.setText(_translate("MainWindow", ")"))
        self.btn_clearParams.setText(_translate("MainWindow", "Clear All"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Graph"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Matrix Format"))
        self.btn_enterMatrix.setText(_translate("MainWindow", "Enter"))
        self.label_14.setText(_translate("MainWindow", "<html>\n"
" <body>\n"
"  <img src = \"/home/coco/pyApps/pyQt5_images/left_parenthesis.png\">\n"
" </body>\n"
"</html>"))
        self.label_7.setText(_translate("MainWindow", "<html>\n"
" <body>\n"
"  <img src = \"/home/coco/pyApps/pyQt5_images/right_parenthesis.png\">\n"
" </body>\n"
"</html>"))
        self.btn_clearMatrix.setText(_translate("MainWindow", "Clear All"))
        self.groupBox_4.setTitle(_translate("MainWindow", "RREF"))
        self.label_8.setText(_translate("MainWindow", "Equation: "))
        self.label_9.setText(_translate("MainWindow", "a = "))
        self.label_10.setText(_translate("MainWindow", "b = "))
        self.label_11.setText(_translate("MainWindow", "c = "))
        self.label_12.setText(_translate("MainWindow", "<html>\n"
" <body>\n"
"  <img src = \"/home/coco/pyApps/pyQt5_images/left_parenthesis.png\">\n"
" </body>\n"
"</html>"))
        self.label_6.setText(_translate("MainWindow", "<html>\n"
" <body>\n"
"  <img src = \"/home/coco/pyApps/pyQt5_images/right_parenthesis.png\">\n"
" </body>\n"
"</html>"))
        self.btn_clearRREF.setText(_translate("MainWindow", "Clear All"))
        self.tf_messages.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Formula in use: <span style=\" font-weight:600;\">y = ax² + bx + c</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The &quot;Clear All&quot; button only clears out the data from the group box in which it resides</p></body></html>"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())