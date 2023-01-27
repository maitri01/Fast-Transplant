# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'profilescreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from acdoscreen import Ui_acdowindow


class Ui_profilewindow(object):

    def nextacdo(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_acdowindow()
        self.ui.setupUi (self.window)
        #profilewindow.hide() 
        self.window.show()

    def backacdo(self):
        from homescreen import Ui_homewindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_homewindow()
        self.ui.setupUi (self.window)
        #profilewindow.hide()
        self.window.show()

    def setupUi(self, profilewindow):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        profilewindow.setWindowIcon(icon)
        profilewindow.setObjectName("profilewindow")
        profilewindow.resize(1920, 1080)
        self.NextProfile = QtWidgets.QPushButton(profilewindow)
        self.NextProfile.setGeometry(QtCore.QRect(790, 650, 121, 41))
        font = QtGui.QFont()
        font.setFamily("CentSchbkCyrill BT")
        font.setPointSize(16)
        self.NextProfile.setFont(font)
        self.NextProfile.setObjectName("NextProfile")
        self.NextProfile.clicked.connect(self.nextacdo)
        self.EnterdetailsProfile = QtWidgets.QLabel(profilewindow)
        self.EnterdetailsProfile.setGeometry(QtCore.QRect(180, 140, 301, 31))
        font = QtGui.QFont()
        font.setFamily("CentSchbkCyrill BT")
        font.setPointSize(24)
        self.EnterdetailsProfile.setFont(font)
        self.EnterdetailsProfile.setWordWrap(True)
        self.EnterdetailsProfile.setObjectName("EnterdetailsProfile")
        self.BackProfile = QtWidgets.QPushButton(profilewindow)
        self.BackProfile.setGeometry(QtCore.QRect(40, 40, 71, 41))
        font = QtGui.QFont()
        font.setFamily("CentSchbkCyrill BT")
        font.setPointSize(16)
        self.BackProfile.setFont(font)
        self.BackProfile.setAutoFillBackground(True)
        self.BackProfile.setObjectName("BackProfile")
        self.BackProfile.clicked.connect(self.backacdo)
        self.BackProfile.clicked.connect(profilewindow.close)
        self.groupBoxProfile = QtWidgets.QGroupBox(profilewindow)
        self.groupBoxProfile.setGeometry(QtCore.QRect(380, 250, 351, 251))
        font = QtGui.QFont()
        font.setFamily("CentSchbkCyrill BT")
        font.setPointSize(18)
        self.groupBoxProfile.setFont(font)
        self.groupBoxProfile.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.groupBoxProfile.setObjectName("groupBoxProfile")
        self.formLayoutWidget = QtWidgets.QWidget(self.groupBoxProfile)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 50, 311, 41))
        font = QtGui.QFont()
        font.setFamily("CentSchbkCyrill BT")
        font.setPointSize(18)
        self.formLayoutWidget.setFont(font)
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayoutProfile = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayoutProfile.setContentsMargins(0, 0, 0, 0)
        self.formLayoutProfile.setObjectName("formLayoutProfile")
        self.nameLineEditProfile = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("CentSchbkCyrill BT")
        font.setPointSize(18)
        self.nameLineEditProfile.setFont(font)
        self.nameLineEditProfile.setText("")
        self.nameLineEditProfile.setObjectName("nameLineEditProfile")
        self.formLayoutProfile.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nameLineEditProfile)
        self.nameLabelProfile = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("CentSchbkCyrill BT")
        font.setPointSize(18)
        self.nameLabelProfile.setFont(font)
        self.nameLabelProfile.setObjectName("nameLabelProfile")
        self.formLayoutProfile.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.nameLabelProfile)
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.groupBoxProfile)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(20, 120, 311, 41))
        font = QtGui.QFont()
        font.setFamily("CentSchbkCyrill BT")
        font.setPointSize(18)
        self.formLayoutWidget_2.setFont(font)
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2Profile = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2Profile.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2Profile.setObjectName("formLayout_2Profile")
        self.ageGroupLabelProfile = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("CentSchbkCyrill BT")
        font.setPointSize(18)
        self.ageGroupLabelProfile.setFont(font)
        self.ageGroupLabelProfile.setObjectName("ageGroupLabelProfile")
        self.formLayout_2Profile.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.ageGroupLabelProfile)
        self.ageGroupComboBoxProfile = QtWidgets.QComboBox(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("CentSchbkCyrill BT")
        font.setPointSize(18)
        self.ageGroupComboBoxProfile.setFont(font)
        self.ageGroupComboBoxProfile.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ageGroupComboBoxProfile.setMaxVisibleItems(5)
        self.ageGroupComboBoxProfile.setObjectName("ageGroupComboBoxProfile")
        self.ageGroupComboBoxProfile.addItem("")
        self.ageGroupComboBoxProfile.addItem("")
        self.ageGroupComboBoxProfile.addItem("")
        self.ageGroupComboBoxProfile.addItem("")
        self.ageGroupComboBoxProfile.addItem("")
        self.ageGroupComboBoxProfile.addItem("")
        self.ageGroupComboBoxProfile.addItem("")
        self.ageGroupComboBoxProfile.addItem("")
        self.ageGroupComboBoxProfile.addItem("")
        self.formLayout_2Profile.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.ageGroupComboBoxProfile)
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.groupBoxProfile)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(20, 190, 311, 41))
        font = QtGui.QFont()
        font.setFamily("CentSchbkCyrill BT")
        font.setPointSize(18)
        self.formLayoutWidget_3.setFont(font)
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_3Profile = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3Profile.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3Profile.setObjectName("formLayout_3Profile")
        self.nameLineEdit_2Profile = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        
        #validatorno = QtCore.QRegExp(r'[0-9]+')
        #self.nameLineEdit_2Profile.setValidator(validatorno)    
               
        font = QtGui.QFont()
        font.setFamily("CentSchbkCyrill BT")
        font.setPointSize(18)
        self.nameLineEdit_2Profile.setFont(font)
        self.nameLineEdit_2Profile.setText("")
        self.nameLineEdit_2Profile.setObjectName("nameLineEdit_2Profile")
        self.formLayout_3Profile.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nameLineEdit_2Profile)
        self.nameLabel_2Profile = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("CentSchbkCyrill BT")
        font.setPointSize(18)
        self.nameLabel_2Profile.setFont(font)
        self.nameLabel_2Profile.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.nameLabel_2Profile.setObjectName("nameLabel_2Profile")
        self.formLayout_3Profile.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.nameLabel_2Profile)
        self.ExitProfile = QtWidgets.QPushButton(profilewindow)
        self.ExitProfile.setGeometry(QtCore.QRect(630, 650, 121, 41))
        font = QtGui.QFont()
        font.setFamily("CentSchbkCyrill BT")
        font.setPointSize(16)
        self.ExitProfile.setFont(font)
        self.ExitProfile.setObjectName("ExitProfile")
        self.groupBox_2Profile = QtWidgets.QGroupBox(profilewindow)
        self.groupBox_2Profile.setGeometry(QtCore.QRect(840, 250, 341, 251))
        font = QtGui.QFont()
        font.setFamily("CentSchbkCyrill BT")
        font.setPointSize(18)
        self.groupBox_2Profile.setFont(font)
        self.groupBox_2Profile.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.groupBox_2Profile.setObjectName("groupBox_2Profile")
        self.formLayoutWidget_4 = QtWidgets.QWidget(self.groupBox_2Profile)
        self.formLayoutWidget_4.setGeometry(QtCore.QRect(20, 50, 301, 41))
        font = QtGui.QFont()
        font.setFamily("CentSchbkCyrill BT")
        self.formLayoutWidget_4.setFont(font)
        self.formLayoutWidget_4.setObjectName("formLayoutWidget_4")
        self.formLayout_4Profile = QtWidgets.QFormLayout(self.formLayoutWidget_4)
        self.formLayout_4Profile.setContentsMargins(0, 0, 0, 0)
        self.formLayout_4Profile.setObjectName("formLayout_4Profile")
        self.bloodGroupProfileComboBox_2 = QtWidgets.QComboBox(self.formLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("CentSchbkCyrill BT")
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.bloodGroupProfileComboBox_2.setFont(font)
        self.bloodGroupProfileComboBox_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bloodGroupProfileComboBox_2.setMouseTracking(True)
        self.bloodGroupProfileComboBox_2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.bloodGroupProfileComboBox_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.bloodGroupProfileComboBox_2.setMaxVisibleItems(5)
        self.bloodGroupProfileComboBox_2.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.bloodGroupProfileComboBox_2.setMinimumContentsLength(2)
        self.bloodGroupProfileComboBox_2.setIconSize(QtCore.QSize(0, 0))
        self.bloodGroupProfileComboBox_2.setFrame(True)
        self.bloodGroupProfileComboBox_2.setModelColumn(0)
        self.bloodGroupProfileComboBox_2.setObjectName("bloodGroupProfileComboBox_2")
        self.bloodGroupProfileComboBox_2.addItem("")
        self.bloodGroupProfileComboBox_2.addItem("")
        self.bloodGroupProfileComboBox_2.addItem("")
        self.bloodGroupProfileComboBox_2.addItem("")
        self.bloodGroupProfileComboBox_2.addItem("")
        self.bloodGroupProfileComboBox_2.addItem("")
        self.bloodGroupProfileComboBox_2.addItem("")
        self.bloodGroupProfileComboBox_2.addItem("")
        self.bloodGroupProfileComboBox_2.addItem("")
        self.formLayout_4Profile.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.bloodGroupProfileComboBox_2)
        self.bloodGroupProfileLabel_2 = QtWidgets.QLabel(self.formLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("CentSchbkCyrill BT")
        self.bloodGroupProfileLabel_2.setFont(font)
        self.bloodGroupProfileLabel_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bloodGroupProfileLabel_2.setObjectName("bloodGroupProfileLabel_2")
        self.formLayout_4Profile.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.bloodGroupProfileLabel_2)
        self.comboBoxProfile = QtWidgets.QComboBox(self.groupBox_2Profile)
        self.comboBoxProfile.setGeometry(QtCore.QRect(60, 180, 231, 31))
        font = QtGui.QFont()
        font.setFamily("CentSchbkCyrill BT")
        self.comboBoxProfile.setFont(font)
        self.comboBoxProfile.setObjectName("comboBoxProfile")
        self.comboBoxProfile.addItem("")
        self.comboBoxProfile.addItem("")
        self.comboBoxProfile.addItem("")
        self.comboBoxProfile.addItem("")
        self.labelProfile = QtWidgets.QLabel(self.groupBox_2Profile)
        self.labelProfile.setGeometry(QtCore.QRect(20, 120, 299, 39))
        font = QtGui.QFont()
        font.setFamily("CentSchbkCyrill BT")
        self.labelProfile.setFont(font)
        self.labelProfile.setObjectName("labelProfile")

        self.retranslateUi(profilewindow)
        self.ExitProfile.clicked.connect(profilewindow.hide)
        self.NextProfile.clicked.connect(profilewindow.hide)
        self.BackProfile.clicked.connect(profilewindow.hide)
        QtCore.QMetaObject.connectSlotsByName(profilewindow)

    def retranslateUi(self, profilewindow):
        _translate = QtCore.QCoreApplication.translate
        profilewindow.setWindowTitle(_translate("profilewindow", "Profile"))
        self.NextProfile.setText(_translate("profilewindow", "➜"))
        self.EnterdetailsProfile.setText(_translate("profilewindow", "Enter Your Details: "))
        self.BackProfile.setText(_translate("profilewindow", "Back"))
        self.groupBoxProfile.setTitle(_translate("profilewindow", "Personal Details"))
        self.nameLabelProfile.setText(_translate("profilewindow", "Name:"))
        self.ageGroupLabelProfile.setText(_translate("profilewindow", "Age Group:"))
        self.ageGroupComboBoxProfile.setItemText(0, _translate("profilewindow", "- select -"))
        self.ageGroupComboBoxProfile.setItemText(1, _translate("profilewindow", "03 - 10"))
        self.ageGroupComboBoxProfile.setItemText(2, _translate("profilewindow", "11- 18"))
        self.ageGroupComboBoxProfile.setItemText(3, _translate("profilewindow", "19 - 30"))
        self.ageGroupComboBoxProfile.setItemText(4, _translate("profilewindow", "31 - 45"))
        self.ageGroupComboBoxProfile.setItemText(5, _translate("profilewindow", "46 - 55"))
        self.ageGroupComboBoxProfile.setItemText(6, _translate("profilewindow", "55 - 75"))
        self.ageGroupComboBoxProfile.setItemText(7, _translate("profilewindow", "75 - 80"))
        self.ageGroupComboBoxProfile.setItemText(8, _translate("profilewindow", "80 or Above"))
        self.nameLabel_2Profile.setText(_translate("profilewindow", "Phone Number: "))
        self.ExitProfile.setText(_translate("profilewindow", "Exit"))
        self.groupBox_2Profile.setTitle(_translate("profilewindow", "Medical Details"))
        self.bloodGroupProfileComboBox_2.setItemText(0, _translate("profilewindow", "- select -"))
        self.bloodGroupProfileComboBox_2.setItemText(1, _translate("profilewindow", "A+"))
        self.bloodGroupProfileComboBox_2.setItemText(2, _translate("profilewindow", "A-"))
        self.bloodGroupProfileComboBox_2.setItemText(3, _translate("profilewindow", "B+"))
        self.bloodGroupProfileComboBox_2.setItemText(4, _translate("profilewindow", "B-"))
        self.bloodGroupProfileComboBox_2.setItemText(5, _translate("profilewindow", "O+"))
        self.bloodGroupProfileComboBox_2.setItemText(6, _translate("profilewindow", "O-"))
        self.bloodGroupProfileComboBox_2.setItemText(7, _translate("profilewindow", "AB+"))
        self.bloodGroupProfileComboBox_2.setItemText(8, _translate("profilewindow", "AB-"))
        self.bloodGroupProfileLabel_2.setText(_translate("profilewindow", "Blood Group:"))
        self.comboBoxProfile.setItemText(0, _translate("profilewindow", "NONE"))
        self.comboBoxProfile.setItemText(1, _translate("profilewindow", "Diabetes"))
        self.comboBoxProfile.setItemText(2, _translate("profilewindow", "Active Tuberculosis"))
        self.comboBoxProfile.setItemText(3, _translate("profilewindow", "HIV"))
        self.labelProfile.setText(_translate("profilewindow", "Major Diseases (if any): "))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    profilewindow = QtWidgets.QWidget()
    ui = Ui_profilewindow()
    ui.setupUi(profilewindow)
    profilewindow.show()
    sys.exit(app.exec_())
