# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/jérôme/Desktop/Freescale/freescale-cup-dan-jerome/Python/GUI Qt/Plot2D.ui'
#
# Created: Mon Feb  2 22:16:04 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_plot2D(object):
    def setupUi(self, plot2D):
        plot2D.setObjectName(_fromUtf8("plot2D"))
        plot2D.resize(377, 379)
        self.gridLayout = QtGui.QGridLayout(plot2D)
        self.gridLayout.setSpacing(4)
        self.gridLayout.setContentsMargins(2, 2, 2, 4)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.btn_clr = QtGui.QPushButton(plot2D)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_clr.sizePolicy().hasHeightForWidth())
        self.btn_clr.setSizePolicy(sizePolicy)
        self.btn_clr.setMinimumSize(QtCore.QSize(30, 0))
        self.btn_clr.setMaximumSize(QtCore.QSize(40, 16777215))
        self.btn_clr.setObjectName(_fromUtf8("btn_clr"))
        self.gridLayout.addWidget(self.btn_clr, 3, 3, 1, 1)
        self.btn_plotsel = QtGui.QPushButton(plot2D)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_plotsel.sizePolicy().hasHeightForWidth())
        self.btn_plotsel.setSizePolicy(sizePolicy)
        self.btn_plotsel.setMinimumSize(QtCore.QSize(100, 0))
        self.btn_plotsel.setObjectName(_fromUtf8("btn_plotsel"))
        self.gridLayout.addWidget(self.btn_plotsel, 1, 0, 3, 1)
        self.lst_plotvar = QtGui.QListView(plot2D)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lst_plotvar.sizePolicy().hasHeightForWidth())
        self.lst_plotvar.setSizePolicy(sizePolicy)
        self.lst_plotvar.setMaximumSize(QtCore.QSize(16777215, 60))
        self.lst_plotvar.setFrameShape(QtGui.QFrame.Box)
        self.lst_plotvar.setFrameShadow(QtGui.QFrame.Sunken)
        self.lst_plotvar.setLineWidth(1)
        self.lst_plotvar.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.lst_plotvar.setObjectName(_fromUtf8("lst_plotvar"))
        self.gridLayout.addWidget(self.lst_plotvar, 1, 1, 3, 1)
        self.lbl_valuesel = QtGui.QLabel(plot2D)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_valuesel.sizePolicy().hasHeightForWidth())
        self.lbl_valuesel.setSizePolicy(sizePolicy)
        self.lbl_valuesel.setMinimumSize(QtCore.QSize(20, 0))
        self.lbl_valuesel.setMaximumSize(QtCore.QSize(40, 16777215))
        self.lbl_valuesel.setBaseSize(QtCore.QSize(30, 0))
        self.lbl_valuesel.setFrameShape(QtGui.QFrame.Box)
        self.lbl_valuesel.setFrameShadow(QtGui.QFrame.Sunken)
        self.lbl_valuesel.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_valuesel.setObjectName(_fromUtf8("lbl_valuesel"))
        self.gridLayout.addWidget(self.lbl_valuesel, 1, 3, 1, 1)
        self.lbl_varsel = QtGui.QLabel(plot2D)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_varsel.sizePolicy().hasHeightForWidth())
        self.lbl_varsel.setSizePolicy(sizePolicy)
        self.lbl_varsel.setFrameShape(QtGui.QFrame.Box)
        self.lbl_varsel.setFrameShadow(QtGui.QFrame.Sunken)
        self.lbl_varsel.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_varsel.setMargin(3)
        self.lbl_varsel.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.lbl_varsel.setObjectName(_fromUtf8("lbl_varsel"))
        self.gridLayout.addWidget(self.lbl_varsel, 1, 2, 1, 1)
        self.btn_remvar = QtGui.QPushButton(plot2D)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_remvar.sizePolicy().hasHeightForWidth())
        self.btn_remvar.setSizePolicy(sizePolicy)
        self.btn_remvar.setMinimumSize(QtCore.QSize(0, 28))
        self.btn_remvar.setObjectName(_fromUtf8("btn_remvar"))
        self.gridLayout.addWidget(self.btn_remvar, 3, 2, 1, 1)
        self.frame_plot = QtGui.QFrame(plot2D)
        self.frame_plot.setFrameShape(QtGui.QFrame.Box)
        self.frame_plot.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_plot.setLineWidth(2)
        self.frame_plot.setObjectName(_fromUtf8("frame_plot"))
        self.gridLayout_2 = QtGui.QGridLayout(self.frame_plot)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.matplotlibwidget = MatplotlibWidget(self.frame_plot)
        self.matplotlibwidget.setObjectName(_fromUtf8("matplotlibwidget"))
        self.gridLayout_2.addWidget(self.matplotlibwidget, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_plot, 0, 0, 1, 4)
        spacerItem = QtGui.QSpacerItem(20, 3, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 2, 2, 1, 2)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setRowStretch(0, 1)

        self.retranslateUi(plot2D)
        QtCore.QMetaObject.connectSlotsByName(plot2D)

    def retranslateUi(self, plot2D):
        plot2D.setWindowTitle(_translate("plot2D", "Plot", None))
        self.btn_clr.setText(_translate("plot2D", "Clear", None))
        self.btn_plotsel.setText(_translate("plot2D", "PLOT SELECTION", None))
        self.lbl_valuesel.setText(_translate("plot2D", "0", None))
        self.lbl_varsel.setText(_translate("plot2D", "No variable", None))
        self.btn_remvar.setText(_translate("plot2D", "REMOVE VAR", None))

from matplotlibwidget import MatplotlibWidget
