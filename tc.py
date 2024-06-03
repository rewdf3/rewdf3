class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(666, 560)
        ......
        # 定义的几个按钮
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(450, 480, 81, 31))
        self.pushButton.setStyleSheet("border:1px solid black")
        self.pushButton.setObjectName("pushButton")
        ......
        # 对应的按钮响应方法
        # 导入文件
        self.pushButton.clicked.connect(self.browse_image)
        # 开始预测
        self.pushButton_2.clicked.connect(self.predict_image)
