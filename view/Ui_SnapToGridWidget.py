# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SnapToGridWidget.ui'
#
# Created: Tue Sep  1 12:58:50 2015
#      by: PyQt4 UI code generator 4.11.1
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

class Ui_SnapToGridWidget(object):
    def setupUi(self, SnapToGridWidget):
        SnapToGridWidget.setObjectName(_fromUtf8("SnapToGridWidget"))
        SnapToGridWidget.resize(293, 797)
        SnapToGridWidget.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.scrollArea = QtGui.QScrollArea(self.dockWidgetContents)
        self.scrollArea.setGeometry(QtCore.QRect(4, 4, 281, 761))
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 279, 759))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.line = QtGui.QFrame(self.scrollAreaWidgetContents)
        self.line.setGeometry(QtCore.QRect(10, 625, 251, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.add_layers_button = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.add_layers_button.setGeometry(QtCore.QRect(5, 5, 261, 32))
        self.add_layers_button.setObjectName(_fromUtf8("add_layers_button"))
        self.cancel_snap_button = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.cancel_snap_button.setGeometry(QtCore.QRect(140, 585, 115, 32))
        self.cancel_snap_button.setObjectName(_fromUtf8("cancel_snap_button"))
        self.create_backup_gbox = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.create_backup_gbox.setGeometry(QtCore.QRect(10, 485, 251, 96))
        self.create_backup_gbox.setCheckable(True)
        self.create_backup_gbox.setObjectName(_fromUtf8("create_backup_gbox"))
        self.label_9 = QtGui.QLabel(self.create_backup_gbox)
        self.label_9.setGeometry(QtCore.QRect(10, 30, 126, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.backup_folder_edit = QtGui.QLineEdit(self.create_backup_gbox)
        self.backup_folder_edit.setGeometry(QtCore.QRect(10, 50, 191, 21))
        self.backup_folder_edit.setReadOnly(True)
        self.backup_folder_edit.setObjectName(_fromUtf8("backup_folder_edit"))
        self.backup_folder_button = QtGui.QPushButton(self.create_backup_gbox)
        self.backup_folder_button.setGeometry(QtCore.QRect(210, 47, 28, 28))
        self.backup_folder_button.setText(_fromUtf8(""))
        self.backup_folder_button.setObjectName(_fromUtf8("backup_folder_button"))
        self.snap_layers_lwidget = QtGui.QListWidget(self.scrollAreaWidgetContents)
        self.snap_layers_lwidget.setGeometry(QtCore.QRect(10, 65, 251, 201))
        self.snap_layers_lwidget.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.snap_layers_lwidget.setObjectName(_fromUtf8("snap_layers_lwidget"))
        self.remove_layer_button = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.remove_layer_button.setGeometry(QtCore.QRect(5, 270, 131, 32))
        self.remove_layer_button.setObjectName(_fromUtf8("remove_layer_button"))
        self.remove_all_layers_button = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.remove_all_layers_button.setGeometry(QtCore.QRect(135, 270, 131, 32))
        self.remove_all_layers_button.setObjectName(_fromUtf8("remove_all_layers_button"))
        self.label_5 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setGeometry(QtCore.QRect(10, 45, 206, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.snap_settings_gbox = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.snap_settings_gbox.setGeometry(QtCore.QRect(10, 315, 251, 166))
        self.snap_settings_gbox.setObjectName(_fromUtf8("snap_settings_gbox"))
        self.layer_rbutton = QtGui.QRadioButton(self.snap_settings_gbox)
        self.layer_rbutton.setGeometry(QtCore.QRect(10, 50, 126, 20))
        self.layer_rbutton.setChecked(True)
        self.layer_rbutton.setObjectName(_fromUtf8("layer_rbutton"))
        self.map_extent_rbutton = QtGui.QRadioButton(self.snap_settings_gbox)
        self.map_extent_rbutton.setGeometry(QtCore.QRect(10, 75, 231, 20))
        self.map_extent_rbutton.setChecked(False)
        self.map_extent_rbutton.setObjectName(_fromUtf8("map_extent_rbutton"))
        self.label_6 = QtGui.QLabel(self.snap_settings_gbox)
        self.label_6.setGeometry(QtCore.QRect(15, 105, 191, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.grid_size_sbox = QtGui.QDoubleSpinBox(self.snap_settings_gbox)
        self.grid_size_sbox.setGeometry(QtCore.QRect(15, 125, 121, 24))
        self.grid_size_sbox.setDecimals(3)
        self.grid_size_sbox.setMinimum(0.001)
        self.grid_size_sbox.setMaximum(10.0)
        self.grid_size_sbox.setSingleStep(0.01)
        self.grid_size_sbox.setObjectName(_fromUtf8("grid_size_sbox"))
        self.label_7 = QtGui.QLabel(self.snap_settings_gbox)
        self.label_7.setGeometry(QtCore.QRect(10, 30, 126, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.restore_geom_gbox = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.restore_geom_gbox.setGeometry(QtCore.QRect(10, 645, 251, 91))
        self.restore_geom_gbox.setObjectName(_fromUtf8("restore_geom_gbox"))
        self.restore_button = QtGui.QPushButton(self.restore_geom_gbox)
        self.restore_button.setGeometry(QtCore.QRect(10, 30, 106, 32))
        self.restore_button.setObjectName(_fromUtf8("restore_button"))
        self.cancel_restore_button = QtGui.QPushButton(self.restore_geom_gbox)
        self.cancel_restore_button.setGeometry(QtCore.QRect(125, 30, 115, 32))
        self.cancel_restore_button.setObjectName(_fromUtf8("cancel_restore_button"))
        self.label = QtGui.QLabel(self.restore_geom_gbox)
        self.label.setGeometry(QtCore.QRect(20, 60, 166, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.snap_button = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.snap_button.setGeometry(QtCore.QRect(20, 585, 115, 32))
        self.snap_button.setObjectName(_fromUtf8("snap_button"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        SnapToGridWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(SnapToGridWidget)
        QtCore.QMetaObject.connectSlotsByName(SnapToGridWidget)
        SnapToGridWidget.setTabOrder(self.add_layers_button, self.snap_layers_lwidget)
        SnapToGridWidget.setTabOrder(self.snap_layers_lwidget, self.remove_layer_button)
        SnapToGridWidget.setTabOrder(self.remove_layer_button, self.remove_all_layers_button)
        SnapToGridWidget.setTabOrder(self.remove_all_layers_button, self.map_extent_rbutton)
        SnapToGridWidget.setTabOrder(self.map_extent_rbutton, self.layer_rbutton)
        SnapToGridWidget.setTabOrder(self.layer_rbutton, self.grid_size_sbox)
        SnapToGridWidget.setTabOrder(self.grid_size_sbox, self.create_backup_gbox)
        SnapToGridWidget.setTabOrder(self.create_backup_gbox, self.backup_folder_edit)
        SnapToGridWidget.setTabOrder(self.backup_folder_edit, self.backup_folder_button)
        SnapToGridWidget.setTabOrder(self.backup_folder_button, self.snap_button)
        SnapToGridWidget.setTabOrder(self.snap_button, self.cancel_snap_button)
        SnapToGridWidget.setTabOrder(self.cancel_snap_button, self.restore_button)
        SnapToGridWidget.setTabOrder(self.restore_button, self.cancel_restore_button)

    def retranslateUi(self, SnapToGridWidget):
        SnapToGridWidget.setWindowTitle(_translate("SnapToGridWidget", "Snap To Grid", None))
        self.add_layers_button.setText(_translate("SnapToGridWidget", "Add Selected TOC Layers", None))
        self.cancel_snap_button.setText(_translate("SnapToGridWidget", "Cancel", None))
        self.create_backup_gbox.setTitle(_translate("SnapToGridWidget", "Create Backup (Geometries only)", None))
        self.label_9.setText(_translate("SnapToGridWidget", "Backup Folder", None))
        self.remove_layer_button.setText(_translate("SnapToGridWidget", "Remove Selected", None))
        self.remove_all_layers_button.setText(_translate("SnapToGridWidget", "Remove All", None))
        self.label_5.setText(_translate("SnapToGridWidget", "Layers To Be Snapped", None))
        self.snap_settings_gbox.setTitle(_translate("SnapToGridWidget", "Snap Settings", None))
        self.layer_rbutton.setText(_translate("SnapToGridWidget", "Layer Extent", None))
        self.map_extent_rbutton.setText(_translate("SnapToGridWidget", "Current Map View (Intersecting)", None))
        self.label_6.setText(_translate("SnapToGridWidget", "Grid Size [0.001m - 10m]", None))
        self.label_7.setText(_translate("SnapToGridWidget", "Snap Extent:", None))
        self.restore_geom_gbox.setTitle(_translate("SnapToGridWidget", "Restore Geometries (from Backup)", None))
        self.restore_button.setText(_translate("SnapToGridWidget", "Restore", None))
        self.cancel_restore_button.setText(_translate("SnapToGridWidget", "Cancel", None))
        self.label.setText(_translate("SnapToGridWidget", "<html><head/><body><p><span style=\" color:#666666;\">For layers selected above.</span></p></body></html>", None))
        self.snap_button.setText(_translate("SnapToGridWidget", "Snap", None))

