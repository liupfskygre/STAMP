# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'profileBarPlot.ui'
#
# Created: Thu Aug 11 10:42:25 2011
#      by: PyQt4 UI code generator 4.8.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ProfileBarPlotDialog(object):
    def setupUi(self, ProfileBarPlotDialog):
        ProfileBarPlotDialog.setObjectName(_fromUtf8("ProfileBarPlotDialog"))
        ProfileBarPlotDialog.resize(418, 277)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ProfileBarPlotDialog.sizePolicy().hasHeightForWidth())
        ProfileBarPlotDialog.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../../icons/programIcon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ProfileBarPlotDialog.setWindowIcon(icon)
        self.verticalLayout_5 = QtGui.QVBoxLayout(ProfileBarPlotDialog)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lblFieldToPlot = QtGui.QLabel(ProfileBarPlotDialog)
        self.lblFieldToPlot.setObjectName(_fromUtf8("lblFieldToPlot"))
        self.horizontalLayout.addWidget(self.lblFieldToPlot)
        self.cboFieldToPlot = QtGui.QComboBox(ProfileBarPlotDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cboFieldToPlot.sizePolicy().hasHeightForWidth())
        self.cboFieldToPlot.setSizePolicy(sizePolicy)
        self.cboFieldToPlot.setObjectName(_fromUtf8("cboFieldToPlot"))
        self.cboFieldToPlot.addItem(_fromUtf8(""))
        self.cboFieldToPlot.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.cboFieldToPlot)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.groupBox_3 = QtGui.QGroupBox(ProfileBarPlotDialog)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.spinFigColWidth = QtGui.QDoubleSpinBox(self.groupBox_3)
        self.spinFigColWidth.setDecimals(2)
        self.spinFigColWidth.setMinimum(0.01)
        self.spinFigColWidth.setMaximum(10.0)
        self.spinFigColWidth.setSingleStep(0.01)
        self.spinFigColWidth.setProperty(_fromUtf8("value"), 0.5)
        self.spinFigColWidth.setObjectName(_fromUtf8("spinFigColWidth"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.spinFigColWidth)
        self.lblFigureHeight = QtGui.QLabel(self.groupBox_3)
        self.lblFigureHeight.setObjectName(_fromUtf8("lblFigureHeight"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.lblFigureHeight)
        self.spinFigHeight = QtGui.QDoubleSpinBox(self.groupBox_3)
        self.spinFigHeight.setMinimum(0.1)
        self.spinFigHeight.setMaximum(20.0)
        self.spinFigHeight.setSingleStep(0.05)
        self.spinFigHeight.setProperty(_fromUtf8("value"), 6.0)
        self.spinFigHeight.setObjectName(_fromUtf8("spinFigHeight"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.spinFigHeight)
        self.lblFigureWidth = QtGui.QLabel(self.groupBox_3)
        self.lblFigureWidth.setObjectName(_fromUtf8("lblFigureWidth"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.lblFigureWidth)
        self.label_3 = QtGui.QLabel(self.groupBox_3)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_3)
        self.spinBarWidth = QtGui.QSpinBox(self.groupBox_3)
        self.spinBarWidth.setMaximum(100)
        self.spinBarWidth.setSingleStep(5)
        self.spinBarWidth.setProperty(_fromUtf8("value"), 80)
        self.spinBarWidth.setObjectName(_fromUtf8("spinBarWidth"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.spinBarWidth)
        self.verticalLayout_6.addLayout(self.formLayout_2)
        self.horizontalLayout_6.addWidget(self.groupBox_3)
        self.groupBox_4 = QtGui.QGroupBox(ProfileBarPlotDialog)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.chkShowCIs = QtGui.QCheckBox(self.groupBox_4)
        self.chkShowCIs.setChecked(True)
        self.chkShowCIs.setObjectName(_fromUtf8("chkShowCIs"))
        self.verticalLayout_3.addWidget(self.chkShowCIs)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.groupBox_4)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.spinEndCapSize = QtGui.QSpinBox(self.groupBox_4)
        self.spinEndCapSize.setMaximum(100)
        self.spinEndCapSize.setObjectName(_fromUtf8("spinEndCapSize"))
        self.horizontalLayout_2.addWidget(self.spinEndCapSize)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout_6.addWidget(self.groupBox_4)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.groupBox_5 = QtGui.QGroupBox(ProfileBarPlotDialog)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.chkShowPvalue = QtGui.QCheckBox(self.groupBox_5)
        self.chkShowPvalue.setChecked(True)
        self.chkShowPvalue.setObjectName(_fromUtf8("chkShowPvalue"))
        self.horizontalLayout_4.addWidget(self.chkShowPvalue)
        self.spinPvalueThreshold = QtGui.QDoubleSpinBox(self.groupBox_5)
        self.spinPvalueThreshold.setDecimals(4)
        self.spinPvalueThreshold.setMaximum(1.0)
        self.spinPvalueThreshold.setSingleStep(0.0001)
        self.spinPvalueThreshold.setProperty(_fromUtf8("value"), 0.05)
        self.spinPvalueThreshold.setObjectName(_fromUtf8("spinPvalueThreshold"))
        self.horizontalLayout_4.addWidget(self.spinPvalueThreshold)
        spacerItem1 = QtGui.QSpacerItem(1, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout_4.addWidget(self.groupBox_5)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_2 = QtGui.QLabel(ProfileBarPlotDialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.spinFeaturesToShow = QtGui.QSpinBox(ProfileBarPlotDialog)
        self.spinFeaturesToShow.setMinimum(1)
        self.spinFeaturesToShow.setMaximum(1000)
        self.spinFeaturesToShow.setProperty(_fromUtf8("value"), 50)
        self.spinFeaturesToShow.setObjectName(_fromUtf8("spinFeaturesToShow"))
        self.horizontalLayout_3.addWidget(self.spinFeaturesToShow)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_7.addLayout(self.verticalLayout_4)
        self.groupBox = QtGui.QGroupBox(ProfileBarPlotDialog)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.radioLegendPosNone = QtGui.QRadioButton(self.groupBox)
        self.radioLegendPosNone.setObjectName(_fromUtf8("radioLegendPosNone"))
        self.verticalLayout.addWidget(self.radioLegendPosNone)
        self.radioLegendPosBest = QtGui.QRadioButton(self.groupBox)
        self.radioLegendPosBest.setChecked(True)
        self.radioLegendPosBest.setObjectName(_fromUtf8("radioLegendPosBest"))
        self.verticalLayout.addWidget(self.radioLegendPosBest)
        self.radioLegendPosUpperRight = QtGui.QRadioButton(self.groupBox)
        self.radioLegendPosUpperRight.setObjectName(_fromUtf8("radioLegendPosUpperRight"))
        self.verticalLayout.addWidget(self.radioLegendPosUpperRight)
        self.radioLegendPosCentreRight = QtGui.QRadioButton(self.groupBox)
        self.radioLegendPosCentreRight.setObjectName(_fromUtf8("radioLegendPosCentreRight"))
        self.verticalLayout.addWidget(self.radioLegendPosCentreRight)
        self.radioLegendPosLowerRight = QtGui.QRadioButton(self.groupBox)
        self.radioLegendPosLowerRight.setObjectName(_fromUtf8("radioLegendPosLowerRight"))
        self.verticalLayout.addWidget(self.radioLegendPosLowerRight)
        self.radioLegendPosUpperLeft = QtGui.QRadioButton(self.groupBox)
        self.radioLegendPosUpperLeft.setObjectName(_fromUtf8("radioLegendPosUpperLeft"))
        self.verticalLayout.addWidget(self.radioLegendPosUpperLeft)
        self.radioLegendPosCentreLeft = QtGui.QRadioButton(self.groupBox)
        self.radioLegendPosCentreLeft.setObjectName(_fromUtf8("radioLegendPosCentreLeft"))
        self.verticalLayout.addWidget(self.radioLegendPosCentreLeft)
        self.radioLegendPosLowerLeft = QtGui.QRadioButton(self.groupBox)
        self.radioLegendPosLowerLeft.setChecked(False)
        self.radioLegendPosLowerLeft.setObjectName(_fromUtf8("radioLegendPosLowerLeft"))
        self.verticalLayout.addWidget(self.radioLegendPosLowerLeft)
        spacerItem3 = QtGui.QSpacerItem(20, 5, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout_7.addWidget(self.groupBox)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem4 = QtGui.QSpacerItem(100, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.buttonBox = QtGui.QDialogButtonBox(ProfileBarPlotDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout_5.addWidget(self.buttonBox)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.retranslateUi(ProfileBarPlotDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ProfileBarPlotDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ProfileBarPlotDialog.reject)
        QtCore.QObject.connect(self.chkShowCIs, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.spinEndCapSize.setEnabled)
        QtCore.QObject.connect(self.chkShowPvalue, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.spinPvalueThreshold.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(ProfileBarPlotDialog)

    def retranslateUi(self, ProfileBarPlotDialog):
        ProfileBarPlotDialog.setWindowTitle(QtGui.QApplication.translate("ProfileBarPlotDialog", "Profile bar plot", None, QtGui.QApplication.UnicodeUTF8))
        self.lblFieldToPlot.setText(QtGui.QApplication.translate("ProfileBarPlotDialog", "Field to plot:", None, QtGui.QApplication.UnicodeUTF8))
        self.cboFieldToPlot.setItemText(0, QtGui.QApplication.translate("ProfileBarPlotDialog", "Number of sequences", None, QtGui.QApplication.UnicodeUTF8))
        self.cboFieldToPlot.setItemText(1, QtGui.QApplication.translate("ProfileBarPlotDialog", "Proportion of sequences (%)", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("ProfileBarPlotDialog", "Figure size", None, QtGui.QApplication.UnicodeUTF8))
        self.lblFigureHeight.setText(QtGui.QApplication.translate("ProfileBarPlotDialog", "Height:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblFigureWidth.setText(QtGui.QApplication.translate("ProfileBarPlotDialog", "Column width:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ProfileBarPlotDialog", "Bar width (%):", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("ProfileBarPlotDialog", "Confidence Intervals", None, QtGui.QApplication.UnicodeUTF8))
        self.chkShowCIs.setText(QtGui.QApplication.translate("ProfileBarPlotDialog", "Show CIs", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ProfileBarPlotDialog", "End cap size:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_5.setTitle(QtGui.QApplication.translate("ProfileBarPlotDialog", "Mark significant features", None, QtGui.QApplication.UnicodeUTF8))
        self.chkShowPvalue.setText(QtGui.QApplication.translate("ProfileBarPlotDialog", "Mark features with a p-value <=", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ProfileBarPlotDialog", "Maximum # features to show:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("ProfileBarPlotDialog", "Legend position", None, QtGui.QApplication.UnicodeUTF8))
        self.radioLegendPosNone.setText(QtGui.QApplication.translate("ProfileBarPlotDialog", "None", None, QtGui.QApplication.UnicodeUTF8))
        self.radioLegendPosBest.setText(QtGui.QApplication.translate("ProfileBarPlotDialog", "Best", None, QtGui.QApplication.UnicodeUTF8))
        self.radioLegendPosUpperRight.setText(QtGui.QApplication.translate("ProfileBarPlotDialog", "Upper right", None, QtGui.QApplication.UnicodeUTF8))
        self.radioLegendPosCentreRight.setText(QtGui.QApplication.translate("ProfileBarPlotDialog", "Centre right", None, QtGui.QApplication.UnicodeUTF8))
        self.radioLegendPosLowerRight.setText(QtGui.QApplication.translate("ProfileBarPlotDialog", "Lower right", None, QtGui.QApplication.UnicodeUTF8))
        self.radioLegendPosUpperLeft.setText(QtGui.QApplication.translate("ProfileBarPlotDialog", "Upper left", None, QtGui.QApplication.UnicodeUTF8))
        self.radioLegendPosCentreLeft.setText(QtGui.QApplication.translate("ProfileBarPlotDialog", "Centre left", None, QtGui.QApplication.UnicodeUTF8))
        self.radioLegendPosLowerLeft.setText(QtGui.QApplication.translate("ProfileBarPlotDialog", "Lower left", None, QtGui.QApplication.UnicodeUTF8))

