# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGraphicsView,
    QHBoxLayout, QLabel, QPushButton, QScrollBar,
    QSizePolicy, QSpacerItem, QStackedWidget, QToolBox,
    QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1029, 600)
        Widget.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"")
        self.horizontalLayout = QHBoxLayout(Widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.left_container = QFrame(Widget)
        self.left_container.setObjectName(u"left_container")
        self.left_container.setMaximumSize(QSize(200, 16777215))
        self.left_container.setStyleSheet(u"*{\n"
"	border:none;\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.left_container.setFrameShape(QFrame.StyledPanel)
        self.left_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.left_container)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_3 = QFrame(self.left_container)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.left_container)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"border-color: rgb(249, 240, 107);\n"
"gridline-color: rgb(249, 240, 107);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.toolBox = QToolBox(self.frame_4)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setStyleSheet(u"QToolBox::tab{\n"
"	color: rgb(0, 0, 0);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(194,232,255);\n"
"	text-align:left;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(0, 0, 0);\n"
"	border-top-left-radius: 15px;\n"
"	background-color: rgb(192, 191, 188);\n"
"}")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 80, 429))
        self.verticalLayout_4 = QVBoxLayout(self.page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.button_home = QPushButton(self.page)
        self.button_home.setObjectName(u"button_home")

        self.verticalLayout_4.addWidget(self.button_home)

        self.butto_contato = QPushButton(self.page)
        self.butto_contato.setObjectName(u"butto_contato")

        self.verticalLayout_4.addWidget(self.butto_contato)

        self.button_sobre = QPushButton(self.page)
        self.button_sobre.setObjectName(u"button_sobre")

        self.verticalLayout_4.addWidget(self.button_sobre)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.toolBox.addItem(self.page, u"Page 1")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 123, 429))
        self.verticalLayout_5 = QVBoxLayout(self.page_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.text_account = QLabel(self.page_2)
        self.text_account.setObjectName(u"text_account")

        self.verticalLayout_5.addWidget(self.text_account)

        self.button_gerenciar = QPushButton(self.page_2)
        self.button_gerenciar.setObjectName(u"button_gerenciar")

        self.verticalLayout_5.addWidget(self.button_gerenciar)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.toolBox.addItem(self.page_2, u"Page 2")

        self.verticalLayout_3.addWidget(self.toolBox)


        self.verticalLayout_2.addWidget(self.frame_4)


        self.horizontalLayout.addWidget(self.left_container)

        self.right_container = QFrame(Widget)
        self.right_container.setObjectName(u"right_container")
        self.right_container.setStyleSheet(u"*{\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.right_container.setFrameShape(QFrame.StyledPanel)
        self.right_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.right_container)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Header = QFrame(self.right_container)
        self.Header.setObjectName(u"Header")
        self.Header.setStyleSheet(u"*{\n"
"	background-color: rgb(249, 240, 107);\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.Header.setFrameShape(QFrame.StyledPanel)
        self.Header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Header)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_toggle = QPushButton(self.Header)
        self.btn_toggle.setObjectName(u"btn_toggle")

        self.horizontalLayout_2.addWidget(self.btn_toggle)

        self.label = QLabel(self.Header)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.Header)

        self.MainFrame = QFrame(self.right_container)
        self.MainFrame.setObjectName(u"MainFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MainFrame.sizePolicy().hasHeightForWidth())
        self.MainFrame.setSizePolicy(sizePolicy)
        self.MainFrame.setFrameShape(QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QFrame.Raised)
        self.vboxLayout = QVBoxLayout(self.MainFrame)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.Pages = QStackedWidget(self.MainFrame)
        self.Pages.setObjectName(u"Pages")
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.horizontalLayout_5 = QHBoxLayout(self.pg_home)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.Logo = QLabel(self.pg_home)
        self.Logo.setObjectName(u"Logo")
        self.Logo.setTextFormat(Qt.RichText)
        self.Logo.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.Logo)

        self.label_5 = QLabel(self.pg_home)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setPointSize(8)
        self.label_5.setFont(font)
        self.label_5.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.label_5)

        self.Pages.addWidget(self.pg_home)
        self.pg_contatos = QWidget()
        self.pg_contatos.setObjectName(u"pg_contatos")
        self.verticalLayout_6 = QVBoxLayout(self.pg_contatos)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame = QFrame(self.pg_contatos)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_7.addWidget(self.label_4)


        self.verticalLayout_6.addWidget(self.frame)

        self.frame_2 = QFrame(self.pg_contatos)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_8.addWidget(self.label_6)

        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_8.addWidget(self.label_7)

        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_8.addWidget(self.label_8)

        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_8.addWidget(self.label_9)


        self.verticalLayout_6.addWidget(self.frame_2)

        self.Pages.addWidget(self.pg_contatos)
        self.pg_sobre = QWidget()
        self.pg_sobre.setObjectName(u"pg_sobre")
        self.verticalLayout_9 = QVBoxLayout(self.pg_sobre)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_5 = QFrame(self.pg_sobre)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_10 = QLabel(self.frame_5)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_10.addWidget(self.label_10)


        self.verticalLayout_9.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.pg_sobre)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy2)
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_6)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_11 = QLabel(self.frame_6)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_11.addWidget(self.label_11)

        self.label_12 = QLabel(self.frame_6)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_11.addWidget(self.label_12)


        self.verticalLayout_9.addWidget(self.frame_6)

        self.Pages.addWidget(self.pg_sobre)
        self.pg_gerenciamento = QWidget()
        self.pg_gerenciamento.setObjectName(u"pg_gerenciamento")
        self.verticalLayout_12 = QVBoxLayout(self.pg_gerenciamento)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalScrollBar = QScrollBar(self.pg_gerenciamento)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        self.horizontalScrollBar.setOrientation(Qt.Horizontal)

        self.verticalLayout_12.addWidget(self.horizontalScrollBar)

        self.frame_7 = QFrame(self.pg_gerenciamento)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_8)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.graphicsView = QGraphicsView(self.frame_8)
        self.graphicsView.setObjectName(u"graphicsView")

        self.verticalLayout_14.addWidget(self.graphicsView)

        self.label_13 = QLabel(self.frame_8)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_14.addWidget(self.label_13)

        self.pushButton = QPushButton(self.frame_8)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"background-color: rgb(249, 240, 107);\n"
"color: rgb(0, 0, 0);")

        self.verticalLayout_14.addWidget(self.pushButton)

        self.checkBox = QCheckBox(self.frame_8)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout_14.addWidget(self.checkBox)


        self.horizontalLayout_6.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_9)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.graphicsView_2 = QGraphicsView(self.frame_9)
        self.graphicsView_2.setObjectName(u"graphicsView_2")

        self.verticalLayout_15.addWidget(self.graphicsView_2)

        self.label_14 = QLabel(self.frame_9)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_15.addWidget(self.label_14)

        self.pushButton_2 = QPushButton(self.frame_9)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(249, 240, 107);")

        self.verticalLayout_15.addWidget(self.pushButton_2)

        self.checkBox_2 = QCheckBox(self.frame_9)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.verticalLayout_15.addWidget(self.checkBox_2)


        self.horizontalLayout_6.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame_7)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_10)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.graphicsView_3 = QGraphicsView(self.frame_10)
        self.graphicsView_3.setObjectName(u"graphicsView_3")

        self.verticalLayout_13.addWidget(self.graphicsView_3)

        self.label_15 = QLabel(self.frame_10)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_13.addWidget(self.label_15)

        self.pushButton_3 = QPushButton(self.frame_10)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(249, 240, 107);")

        self.verticalLayout_13.addWidget(self.pushButton_3)

        self.checkBox_3 = QCheckBox(self.frame_10)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.verticalLayout_13.addWidget(self.checkBox_3)


        self.horizontalLayout_6.addWidget(self.frame_10)


        self.verticalLayout_12.addWidget(self.frame_7)

        self.Pages.addWidget(self.pg_gerenciamento)

        self.vboxLayout.addWidget(self.Pages)


        self.verticalLayout.addWidget(self.MainFrame)

        self.Footer = QFrame(self.right_container)
        self.Footer.setObjectName(u"Footer")
        self.Footer.setFrameShape(QFrame.StyledPanel)
        self.Footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.Footer)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.Footer)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"*{\n"
"	\n"
"	background-color: rgb(249, 240, 107);\n"
"	color: rgb(0, 0, 0);\n"
"}")

        self.horizontalLayout_3.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.Footer)


        self.horizontalLayout.addWidget(self.right_container)


        self.retranslateUi(Widget)

        self.toolBox.setCurrentIndex(1)
        self.Pages.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"Blink", None))
        self.button_home.setText(QCoreApplication.translate("Widget", u"Home", None))
        self.butto_contato.setText(QCoreApplication.translate("Widget", u"Contatos", None))
        self.button_sobre.setText(QCoreApplication.translate("Widget", u"Sobre", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("Widget", u"Page 1", None))
        self.text_account.setText(QCoreApplication.translate("Widget", u"Conta:", None))
        self.button_gerenciar.setText(QCoreApplication.translate("Widget", u"Gerenciamento", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("Widget", u"Page 2", None))
        self.btn_toggle.setText(QCoreApplication.translate("Widget", u"PushButton", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Blink inova\u00e7\u00f5es", None))
        self.Logo.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p align=\"center\"><img src=\":/imgs/QrcFiles/_icons/mcqueen lighting icon\"/><span style=\" vertical-align:super;\"><br/></span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"<html><head/><body><h1 style=\" margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:xx-large; font-weight:700;\">Bem-vindo \u00e0 Blink - Gerenciamento de Energia</span></h1><p>Conectamos voc\u00ea ao futuro sustent\u00e1vel com solu\u00e7\u00f5es inteligentes e eficientes para o<br/>gerenciamento de energia. Nossos servi\u00e7os incluem:</p><ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Efici\u00eancia Energ\u00e9tica</span>: Consultoria personalizada para otimizar o uso de<br/>energia em sua casa ou empresa.</li><li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Monitoramento Inteligente</span>: Acompanhe "
                        "o consumo de energia em<br/>tempo real e tome decis\u00f5es informadas.</li><li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Energias Renov\u00e1veis</span>: Explore fontes limpas como solar e e\u00f3lica.</li><li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Armazenamento de Energia</span>: Solu\u00e7\u00f5es eficientes para uso residencial e<br/>comercial.</li></ol><p>Junte-se \u00e0 Blink e fa\u00e7a parte da revolu\u00e7\u00e3o energ\u00e9tica!</p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt;\">Contatos</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p align=\"center\"><img src=\":/imgs/QrcFiles/_icons/icons8-whatsapp-48.png\"/><a href=\"https://api.whatsapp.com/send?phone=5511931004219&amp;text=Ol%C3%A1%2C%20meu%20amigo!\"><span style=\" font-size:24pt; vertical-align:super;\">Ivan Mendon\u00e7a</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p align=\"center\"><img src=\":/imgs/QrcFiles/_icons/icons8-instagram-48.png\"/><a href=\"https://www.instagram.com/diagramadevann/\"><span style=\" font-size:24pt; vertical-align:super;\">BlinkEnergia</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p align=\"center\"><img src=\":/imgs/QrcFiles/_icons/icons8-linkedin-48.png\"/><a href=\"https://www.linkedin.com/in/ivanaguiarm/\"><span style=\" font-size:24pt; vertical-align:super;\">Blink Energia</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p align=\"center\"><img src=\":/imgs/QrcFiles/_icons/icons8-twitterx-48.png\"/><span style=\" font-size:24pt; vertical-align:super;\">BlinkEnergia</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:700;\">Sobre...</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">A </span><span style=\" font-size:10pt; font-weight:700;\">Blink Empresas</span><span style=\" font-size:10pt;\"> é especializada em soluções de gerenciamento e controle de energia elétrica para empresas. <br/>Oferecemos serviços como monitoramento de consumo, otimização de demanda, e eficiência energética.<br/> Nossa equipe de especialistas trabalha para garantir que sua empresa tenha um uso inteligente e sustentável<br/> da energia elétrica, reduzindo custos e impacto ambiental.</span></p><p align=\"center\"><span style=\" font-size:10pt;\">Se você deseja saber mais detalhes ou tem alguma necessidade específica, não hesite<br/> em entrar em contato conosco! </span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p align=\"center\"><img src=\":/imgs/QrcFiles/_icons/PostAmbScience_EG35-590x275.png\"/></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p align=\"center\">Item 1</p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"Ativar", None))
        self.checkBox.setText(QCoreApplication.translate("Widget", u"CheckBox", None))
        self.label_14.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p align=\"center\">Item 2</p></body></html>", None))
        self.pushButton_2.setText(QCoreApplication.translate("Widget", u"Ativar", None))
        self.checkBox_2.setText(QCoreApplication.translate("Widget", u"CheckBox", None))
        self.label_15.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p align=\"center\">Item 3</p></body></html>", None))
        self.pushButton_3.setText(QCoreApplication.translate("Widget", u"Ativar", None))
        self.checkBox_3.setText(QCoreApplication.translate("Widget", u"CheckBox", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Blink", None))
    # retranslateUi

