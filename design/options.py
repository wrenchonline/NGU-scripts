# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'options.ui',
# licensing of 'options.ui' applies.
#
# Created: Fri Nov  1 17:28:35 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_OptionsWindow(object):
    def setupUi(self, OptionsWindow):
        OptionsWindow.setObjectName("OptionsWindow")
        OptionsWindow.resize(330, 288)
        self.centralwidget = QtWidgets.QWidget(OptionsWindow)
        self.centralwidget.setGeometry(QtCore.QRect(0, 0, 318, 373))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.w_adv_duration = QtWidgets.QHBoxLayout()
        self.w_adv_duration.setObjectName("w_adv_duration")
        self.label_adv_duration = QtWidgets.QLabel(self.centralwidget)
        self.label_adv_duration.setObjectName("label_adv_duration")
        self.w_adv_duration.addWidget(self.label_adv_duration)
        self.line_adv_duration = QtWidgets.QLineEdit(self.centralwidget)
        self.line_adv_duration.setMaximumSize(QtCore.QSize(39, 16777215))
        self.line_adv_duration.setPlaceholderText("")
        self.line_adv_duration.setObjectName("line_adv_duration")
        self.w_adv_duration.addWidget(self.line_adv_duration)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.w_adv_duration.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.w_adv_duration)
        self.w_boost_equipment = QtWidgets.QHBoxLayout()
        self.w_boost_equipment.setObjectName("w_boost_equipment")
        self.check_gear = QtWidgets.QCheckBox(self.centralwidget)
        self.check_gear.setObjectName("check_gear")
        self.w_boost_equipment.addWidget(self.check_gear)
        self.radio_cube = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_cube.setEnabled(False)
        self.radio_cube.setObjectName("radio_cube")
        self.w_boost_equipment.addWidget(self.radio_cube)
        self.radio_equipment = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_equipment.setEnabled(False)
        self.radio_equipment.setObjectName("radio_equipment")
        self.w_boost_equipment.addWidget(self.radio_equipment)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.w_boost_equipment.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.w_boost_equipment)
        self.w_boost_inventory = QtWidgets.QHBoxLayout()
        self.w_boost_inventory.setObjectName("w_boost_inventory")
        self.check_boost_inventory = QtWidgets.QCheckBox(self.centralwidget)
        self.check_boost_inventory.setWhatsThis("")
        self.check_boost_inventory.setObjectName("check_boost_inventory")
        self.w_boost_inventory.addWidget(self.check_boost_inventory)
        self.button_boost_inventory = QtWidgets.QPushButton(self.centralwidget)
        self.button_boost_inventory.setEnabled(False)
        self.button_boost_inventory.setObjectName("button_boost_inventory")
        self.w_boost_inventory.addWidget(self.button_boost_inventory)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.w_boost_inventory.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.w_boost_inventory)
        self.w_merge_inventory = QtWidgets.QHBoxLayout()
        self.w_merge_inventory.setObjectName("w_merge_inventory")
        self.check_merge_inventory = QtWidgets.QCheckBox(self.centralwidget)
        self.check_merge_inventory.setObjectName("check_merge_inventory")
        self.w_merge_inventory.addWidget(self.check_merge_inventory)
        self.button_merge_inventory = QtWidgets.QPushButton(self.centralwidget)
        self.button_merge_inventory.setEnabled(False)
        self.button_merge_inventory.setObjectName("button_merge_inventory")
        self.w_merge_inventory.addWidget(self.button_merge_inventory)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.w_merge_inventory.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.w_merge_inventory)
        self.w_fruits = QtWidgets.QHBoxLayout()
        self.w_fruits.setObjectName("w_fruits")
        self.check_fruits = QtWidgets.QCheckBox(self.centralwidget)
        self.check_fruits.setWhatsThis("")
        self.check_fruits.setObjectName("check_fruits")
        self.w_fruits.addWidget(self.check_fruits)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.w_fruits.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.w_fruits)
        self.w_force = QtWidgets.QHBoxLayout()
        self.w_force.setObjectName("w_force")
        self.check_force = QtWidgets.QCheckBox(self.centralwidget)
        self.check_force.setObjectName("check_force")
        self.w_force.addWidget(self.check_force)
        self.combo_force = QtWidgets.QComboBox(self.centralwidget)
        self.combo_force.setEnabled(False)
        self.combo_force.setObjectName("combo_force")
        self.combo_force.addItem("")
        self.combo_force.addItem("")
        self.combo_force.addItem("")
        self.combo_force.addItem("")
        self.combo_force.addItem("")
        self.combo_force.addItem("")
        self.combo_force.addItem("")
        self.combo_force.addItem("")
        self.combo_force.addItem("")
        self.combo_force.addItem("")
        self.w_force.addWidget(self.combo_force)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.w_force.addItem(spacerItem5)
        self.verticalLayout_2.addLayout(self.w_force)
        self.w_major = QtWidgets.QHBoxLayout()
        self.w_major.setObjectName("w_major")
        self.check_major = QtWidgets.QCheckBox(self.centralwidget)
        self.check_major.setObjectName("check_major")
        self.w_major.addWidget(self.check_major)
        self.verticalLayout_2.addLayout(self.w_major)
        self.w_subcontract = QtWidgets.QHBoxLayout()
        self.w_subcontract.setObjectName("w_subcontract")
        self.check_subcontract = QtWidgets.QCheckBox(self.centralwidget)
        self.check_subcontract.setObjectName("check_subcontract")
        self.w_subcontract.addWidget(self.check_subcontract)
        self.verticalLayout_2.addLayout(self.w_subcontract)
        self.button_ok = QtWidgets.QPushButton(self.centralwidget)
        self.button_ok.setObjectName("button_ok")
        self.verticalLayout_2.addWidget(self.button_ok)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)

        self.retranslateUi(OptionsWindow)
        QtCore.QMetaObject.connectSlotsByName(OptionsWindow)

    def retranslateUi(self, OptionsWindow):
        OptionsWindow.setWindowTitle(QtWidgets.QApplication.translate("OptionsWindow", "NGU Script by Satyric - Options", None, -1))
        self.label_adv_duration.setText(QtWidgets.QApplication.translate("OptionsWindow", "Duration to spend in adventure:", None, -1))
        self.line_adv_duration.setToolTip(QtWidgets.QApplication.translate("OptionsWindow", "Duration in minutes that the questing method will run until returning to boost/merge/etc", None, -1))
        self.line_adv_duration.setText(QtWidgets.QApplication.translate("OptionsWindow", "2", None, -1))
        self.check_gear.setText(QtWidgets.QApplication.translate("OptionsWindow", "Boost gear", None, -1))
        self.radio_cube.setToolTip(QtWidgets.QApplication.translate("OptionsWindow", "This will only right click the cube", None, -1))
        self.radio_cube.setText(QtWidgets.QApplication.translate("OptionsWindow", "Boost cube", None, -1))
        self.radio_equipment.setToolTip(QtWidgets.QApplication.translate("OptionsWindow", "This will boost all equipment before clicking the cube", None, -1))
        self.radio_equipment.setText(QtWidgets.QApplication.translate("OptionsWindow", "Boost equipment", None, -1))
        self.check_boost_inventory.setToolTip(QtWidgets.QApplication.translate("OptionsWindow", "Put the gear you wish to boost starting in the first slot on inventory page 1. A value of 4 will boost the first 4 slots in the inventory. This overrides the Boost cube setting!", None, -1))
        self.check_boost_inventory.setText(QtWidgets.QApplication.translate("OptionsWindow", "Boost inventory", None, -1))
        self.button_boost_inventory.setText(QtWidgets.QApplication.translate("OptionsWindow", "Setup", None, -1))
        self.check_merge_inventory.setToolTip(QtWidgets.QApplication.translate("OptionsWindow", "Put the gear you wish to merge starting in the first slot on inventory page 1. A value of 4 will merge the first 4 slots in the inventory. ", None, -1))
        self.check_merge_inventory.setText(QtWidgets.QApplication.translate("OptionsWindow", "Merge inventory", None, -1))
        self.button_merge_inventory.setText(QtWidgets.QApplication.translate("OptionsWindow", "Setup", None, -1))
        self.check_fruits.setToolTip(QtWidgets.QApplication.translate("OptionsWindow", "This will click \"harvest all max tier fruits\"", None, -1))
        self.check_fruits.setText(QtWidgets.QApplication.translate("OptionsWindow", "Eat fruits", None, -1))
        self.check_force.setToolTip(QtWidgets.QApplication.translate("OptionsWindow", "Abandon quests until you get the selected zone. If you have major quests available, those will get done first.", None, -1))
        self.check_force.setText(QtWidgets.QApplication.translate("OptionsWindow", "Force Zone", None, -1))
        self.combo_force.setItemText(0, QtWidgets.QApplication.translate("OptionsWindow", "Sewers (e-pow)", None, -1))
        self.combo_force.setItemText(1, QtWidgets.QApplication.translate("OptionsWindow", "Forest (m-pow)", None, -1))
        self.combo_force.setItemText(2, QtWidgets.QApplication.translate("OptionsWindow", "High Security Base (e-NGU)", None, -1))
        self.combo_force.setItemText(3, QtWidgets.QApplication.translate("OptionsWindow", "The 2D Universe (e-bar)", None, -1))
        self.combo_force.setItemText(4, QtWidgets.QApplication.translate("OptionsWindow", "A Very Strange Place (e-beard)", None, -1))
        self.combo_force.setItemText(5, QtWidgets.QApplication.translate("OptionsWindow", "Mega Lands (m-beard)", None, -1))
        self.combo_force.setItemText(6, QtWidgets.QApplication.translate("OptionsWindow", "The Beardverse (drop chance)", None, -1))
        self.combo_force.setItemText(7, QtWidgets.QApplication.translate("OptionsWindow", "Chocolate World (stats)", None, -1))
        self.combo_force.setItemText(8, QtWidgets.QApplication.translate("OptionsWindow", "The Evilverse (e-wandoos)", None, -1))
        self.combo_force.setItemText(9, QtWidgets.QApplication.translate("OptionsWindow", "Pretty Pink Princess Land (m-wandoos)", None, -1))
        self.check_major.setToolTip(QtWidgets.QApplication.translate("OptionsWindow", "Does major quests as they become available, this will override the force zone option if you have any majors banked. If you don\'t have any majors available, it will go into itopod.", None, -1))
        self.check_major.setText(QtWidgets.QApplication.translate("OptionsWindow", "Only do major quests", None, -1))
        self.check_subcontract.setToolTip(QtWidgets.QApplication.translate("OptionsWindow", "This will subcontract all quests, make sure \"use major quest\" is unticked in game if you only wish to subcontract minor. Does ITOPOD in between.", None, -1))
        self.check_subcontract.setText(QtWidgets.QApplication.translate("OptionsWindow", "Subcontract", None, -1))
        self.button_ok.setText(QtWidgets.QApplication.translate("OptionsWindow", "Ok", None, -1))

