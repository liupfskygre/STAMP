# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BoxPlot.ui'
#
# Created: Fri Apr 22 14:29:57 2011
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_BoxPlotDialog(object):
    def setupUi(self, BoxPlotDialog):
        BoxPlotDialog.setObjectName("BoxPlotDialog")
        BoxPlotDialog.resize(282, 204)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(BoxPlotDialog.sizePolicy().hasHeightForWidth())
        BoxPlotDialog.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../icons/programIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        BoxPlotDialog.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(BoxPlotDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lblFieldToPlot = QtGui.QLabel(BoxPlotDialog)
        self.lblFieldToPlot.setObjectName("lblFieldToPlot")
        self.horizontalLayout.addWidget(self.lblFieldToPlot)
        self.cboFieldToPlot = QtGui.QComboBox(BoxPlotDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cboFieldToPlot.sizePolicy().hasHeightForWidth())
        self.cboFieldToPlot.setSizePolicy(sizePolicy)
        self.cboFieldToPlot.setObjectName("cboFieldToPlot")
        self.cboFieldToPlot.addItem("")
        self.cboFieldToPlot.addItem("")
        self.horizontalLayout.addWidget(self.cboFieldToPlot)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.groupBox_3 = QtGui.QGroupBox(BoxPlotDialog)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName("formLayout_2")
        self.spinFigWidth = QtGui.QDoubleSpinBox(self.groupBox_3)
        self.spinFigWidth.setDecimals(2)
        self.spinFigWidth.setMinimum(0.1)
        self.spinFigWidth.setMaximum(20.0)
        self.spinFigWidth.setSingleStep(0.05)
        self.spinFigWidth.setProperty("value", 6.0)
        self.spinFigWidth.setObjectName("spinFigWidth")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.spinFigWidth)
        self.lblFigureHeight = QtGui.QLabel(self.groupBox_3)
        self.lblFigureHeight.setObjectName("lblFigureHeight")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.lblFigureHeight)
        self.spinFigHeight = QtGui.QDoubleSpinBox(self.groupBox_3)
        self.spinFigHeight.setMinimum(0.1)
        self.spinFigHeight.setMaximum(20.0)
        self.spinFigHeight.setSingleStep(0.05)
        self.spinFigHeight.setProperty("value", 6.0)
        self.spinFigHeight.setObjectName("spinFigHeight")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.spinFigHeight)
        self.lblFigureWidth = QtGui.QLabel(self.groupBox_3)
        self.lblFigureWidth.setObjectName("lblFigureWidth")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.lblFigureWidth)
        self.verticalLayout_6.addLayout(self.formLayout_2)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.chkShowAverage = QtGui.QCheckBox(BoxPlotDialog)
        self.chkShowAverage.setChecked(True)
        self.chkShowAverage.setObjectName("chkShowAverage")
        self.verticalLayout.addWidget(self.chkShowAverage)
        self.chkShowPvalue = QtGui.QCheckBox(BoxPlotDialog)
        self.chkShowPvalue.setObjectName("chkShowPvalue")
        self.verticalLayout.addWidget(self.chkShowPvalue)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtGui.QSpacerItem(100, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.buttonBox = QtGui.QDialogButtonBox(BoxPlotDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout_5.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.retranslateUi(BoxPlotDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), BoxPlotDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), BoxPlotDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(BoxPlotDialog)

    def retranslateUi(self, BoxPlotDialog):
        BoxPlotDialog.setWindowTitle(QtGui.QApplication.translate("BoxPlotDialog", "Box plot", None, QtGui.QApplication.UnicodeUTF8))
        self.lblFieldToPlot.setText(QtGui.QApplication.translate("BoxPlotDialog", "Field to plot:", None, QtGui.QApplication.UnicodeUTF8))
        self.cboFieldToPlot.setItemText(0, QtGui.QApplication.translate("BoxPlotDialog", "Number of sequences", None, QtGui.QApplication.UnicodeUTF8))
        self.cboFieldToPlot.setItemText(1, QtGui.QApplication.translate("BoxPlotDialog", "Proportion of sequences (%)", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("BoxPlotDialog", "Figure size", None, QtGui.QApplication.UnicodeUTF8))
        self.lblFigureHeight.setText(QtGui.QApplication.translate("BoxPlotDialog", "Height:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblFigureWidth.setText(QtGui.QApplication.translate("BoxPlotDialog", "Width", None, QtGui.QApplication.UnicodeUTF8))
        self.chkShowAverage.setText(QtGui.QApplication.translate("BoxPlotDialog", "Show average of each group", None, QtGui.QApplication.UnicodeUTF8))
        self.chkShowPvalue.setText(QtGui.QApplication.translate("BoxPlotDialog", "Show p-value", None, QtGui.QApplication.UnicodeUTF8))

