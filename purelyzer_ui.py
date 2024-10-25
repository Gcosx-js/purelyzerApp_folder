
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys
import os
sys.stderr = open(os.devnull, 'w')

class Ui_Form(QtWidgets.QWidget):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1390, 755)
        Form.setFixedSize(1390,755)
        
        Form.setStyleSheet("#Form{\n"
"    background-color:rgba(20,20,20,255);\n"
"}")    
        self.main_stacked_widget = QtWidgets.QStackedWidget(Form)
        self.main_stacked_widget.setGeometry(QtCore.QRect(310, 20, 1081, 801))
        self.main_stacked_widget.setStyleSheet("background-color:rgba(30,30,30,240);")
        self.main_stacked_widget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.main_stacked_widget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.main_stacked_widget.setLineWidth(0)
        self.main_stacked_widget.setObjectName("main_stacked_widget")
        self.overview_page = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setPointSize(13)
        self.overview_page.setFont(font)
        self.overview_page.setObjectName("overview_page")
        self.label = QtWidgets.QLabel(self.overview_page)
        self.label.setGeometry(QtCore.QRect(80, 60, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Lucida Grande")
        font.setPointSize(27)
        self.label.setFont(font)
        self.label.setToolTip("")
        self.label.setStyleSheet("color:white;\n"
"background-color:transparent;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.overview_page)
        self.label_2.setGeometry(QtCore.QRect(70, 110, 431, 211))
        font = QtGui.QFont()
        font.setFamily("Lucida Grande")
        font.setPointSize(29)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border:1px transparent;\n"
"border-radius:20px;\n"
"background-color:rgba(20,20,20,255);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.general_overview_listwidget = QtWidgets.QListWidget(self.overview_page)
        self.general_overview_listwidget.setGeometry(QtCore.QRect(90, 140, 401, 161))
        font = QtGui.QFont()
        font.setPointSize(23)
        self.general_overview_listwidget.setFont(font)
        self.general_overview_listwidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.general_overview_listwidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.general_overview_listwidget.setStyleSheet("QListWidget {\n"
"    color:white;\n"
"    background-color:transparent;\n"
"    outline:0;\n"
"    border:1px transparent;\n"
"}\n"
"QListWidget::item {\n"
"    color:white;\n"
"    background-color:transparent;\n"
"     margin: 3px;\n"
"    border:1px transparent;\n"
"}\n"
"QListWidget::item:selected{\n"
"    background-color:transparent;\n"
"    color:white;\n"
"    border:1px solid #808080;\n"
"}\n"
"\n"
"\n"
"")
        self.general_overview_listwidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.general_overview_listwidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.general_overview_listwidget.setLineWidth(0)
        self.general_overview_listwidget.setObjectName("general_overview_listwidget")
        item = QtWidgets.QListWidgetItem()
        self.general_overview_listwidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.general_overview_listwidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.general_overview_listwidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.general_overview_listwidget.addItem(item)
        self.label_4 = QtWidgets.QLabel(self.overview_page)
        self.label_4.setGeometry(QtCore.QRect(80, 350, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Lucida Grande")
        font.setPointSize(27)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:white;\n"
"background-color:transparent;")
        self.label_4.setObjectName("label_4")
        self.missing_v_stacked = QtWidgets.QStackedWidget(self.overview_page)
        self.missing_v_stacked.setGeometry(QtCore.QRect(70, 400, 421, 291))
        self.missing_v_stacked.setStyleSheet("border:1px transparent;\n"
"border-radius:20px;\n"
"background-color:rgba(20,20,20,255);\n"
"")
        self.missing_v_stacked.setObjectName("missing_v_stacked")
        self.mv_main_page = QtWidgets.QWidget()
        self.mv_main_page.setObjectName("mv_main_page")
        self.remove_mv_btn = QtWidgets.QPushButton(self.mv_main_page)
        self.remove_mv_btn.setGeometry(QtCore.QRect(40, 70, 321, 61))
        font = QtGui.QFont()
        font.setFamily(".Lucida Grande UI")
        font.setPointSize(23)
        self.remove_mv_btn.setFont(font)
        self.remove_mv_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.remove_mv_btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.remove_mv_btn.setStyleSheet("QPushButton{\n"
"    background-color:rgba(80,80,80,0.5);\n"
"    color:white;\n"
"    border-color:1px transparent ;\n"
"    border-radius:20px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:rgba(30,30,30,240);\n"
"    color:white;\n"
"}\n"
"QPushButton:checked{\n"
"    background-color:red;\n"
"    color:white;\n"
"}")
        self.remove_mv_btn.setIconSize(QtCore.QSize(35, 35))
        self.remove_mv_btn.setCheckable(False)
        self.remove_mv_btn.setChecked(False)
        self.remove_mv_btn.setObjectName("remove_mv_btn")
        self.fill_missing_v_btn = QtWidgets.QPushButton(self.mv_main_page)
        self.fill_missing_v_btn.setGeometry(QtCore.QRect(40, 160, 321, 61))
        font = QtGui.QFont()
        font.setFamily(".Lucida Grande UI")
        font.setPointSize(23)
        self.fill_missing_v_btn.setFont(font)
        self.fill_missing_v_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.fill_missing_v_btn.setToolTip("")
        self.fill_missing_v_btn.setToolTipDuration(3)
        self.fill_missing_v_btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.fill_missing_v_btn.setStyleSheet("QPushButton{\n"
"    background-color:rgba(80,80,80,0.5);\n"
"    color:white;\n"
"    border-color:1px transparent ;\n"
"    border-radius:20px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:rgba(30,30,30,240);\n"
"    color:white;\n"
"}")
        self.fill_missing_v_btn.setIconSize(QtCore.QSize(35, 35))
        self.fill_missing_v_btn.setCheckable(False)
        self.fill_missing_v_btn.setObjectName("fill_missing_v_btn")
        self.missing_v_stacked.addWidget(self.mv_main_page)
        self.mv_fill_page = QtWidgets.QWidget()
        self.mv_fill_page.setObjectName("mv_fill_page")
        self.label_3 = QtWidgets.QLabel(self.mv_fill_page)
        self.label_3.setGeometry(QtCore.QRect(20, 50, 361, 131))
        font = QtGui.QFont()
        font.setFamily("Lucida Grande")
        font.setPointSize(29)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border:1px solid rgba(80,80,80,0.5);\n"
"border-radius:20px;\n"
"background-color:rgba(20,20,20,255);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.median_radiobtn = QtWidgets.QRadioButton(self.mv_fill_page)
        self.median_radiobtn.setGeometry(QtCore.QRect(40, 70, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.median_radiobtn.setFont(font)
        self.median_radiobtn.setStyleSheet("color:white;")
        self.median_radiobtn.setCheckable(True)
        self.median_radiobtn.setChecked(False)
        self.median_radiobtn.setObjectName("median_radiobtn")
        self.label_5 = QtWidgets.QLabel(self.mv_fill_page)
        self.label_5.setGeometry(QtCore.QRect(30, 0, 451, 51))
        font = QtGui.QFont()
        font.setFamily("Lucida Grande")
        font.setPointSize(21)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:white;\n"
"background-color:transparent;")
        self.label_5.setObjectName("label_5")
        self.average_radiobtn = QtWidgets.QRadioButton(self.mv_fill_page)
        self.average_radiobtn.setGeometry(QtCore.QRect(150, 70, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.average_radiobtn.setFont(font)
        self.average_radiobtn.setStyleSheet("color:white;")
        self.average_radiobtn.setChecked(False)
        self.average_radiobtn.setObjectName("average_radiobtn")
        self.sequential_radiobtn = QtWidgets.QRadioButton(self.mv_fill_page)
        self.sequential_radiobtn.setGeometry(QtCore.QRect(40, 130, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.sequential_radiobtn.setFont(font)
        self.sequential_radiobtn.setStyleSheet("color:white;")
        self.sequential_radiobtn.setObjectName("sequential_radiobtn")
        self.mod_radiobtn = QtWidgets.QRadioButton(self.mv_fill_page)
        self.mod_radiobtn.setGeometry(QtCore.QRect(270, 70, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.mod_radiobtn.setFont(font)
        self.mod_radiobtn.setStyleSheet("color:white;")
        self.mod_radiobtn.setObjectName("mod_radiobtn")
        self.custom_v_lineedit = QtWidgets.QLineEdit(self.mv_fill_page)
        self.custom_v_lineedit.setGeometry(QtCore.QRect(20, 190, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.custom_v_lineedit.setFont(font)
        self.custom_v_lineedit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.custom_v_lineedit.setStyleSheet("border:1px solid rgba(80,80,80,0.5);\n"
"border-radius:20px;\n"
"background-color:rgba(20,20,20,255);\n"
"color:white;")
        self.custom_v_lineedit.setAlignment(QtCore.Qt.AlignCenter)
        self.custom_v_lineedit.setObjectName("custom_v_lineedit")
        self.fill_mv_done_btn = QtWidgets.QPushButton(self.mv_fill_page)
        self.fill_mv_done_btn.setGeometry(QtCore.QRect(270, 191, 113, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.fill_mv_done_btn.setFont(font)
        self.fill_mv_done_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.fill_mv_done_btn.setStyleSheet("QPushButton{\n"
"    border:1px solid rgba(80,80,80,0.5);\n"
"    border-radius:15px;\n"
"    background-color:rgba(20,20,20,255);\n"
"    color:white;\n"
"}\n"
"QPushButton:hover{\n"
"    border:1px solid rgba(0,230,0,0.5);\n"
"    border-radius:15px;\n"
"    background-color:rgba(20,20,20,255);\n"
"    color:rgba(0,230,0,0.5);\n"
"}\n"
"\n"
"")
        self.fill_mv_done_btn.setObjectName("fill_mv_done_btn")
        self.cancel_fill_mv_btn = QtWidgets.QPushButton(self.mv_fill_page)
        self.cancel_fill_mv_btn.setGeometry(QtCore.QRect(20, 240, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.cancel_fill_mv_btn.setFont(font)
        self.cancel_fill_mv_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cancel_fill_mv_btn.setStyleSheet("QPushButton{\n"
"    border:1px solid rgba(80,80,80,0.5);\n"
"    border-radius:15px;\n"
"    background-color:rgba(20,20,20,255);\n"
"    color:white;\n"
"}\n"
"QPushButton:hover{\n"
"    border:1px solid rgba(230,0,0,0.5);\n"
"    border-radius:15px;\n"
"    background-color:rgba(20,20,20,255);\n"
"    color:rgba(240,0,0,0.5);\n"
"}\n"
"\n"
"")
        self.cancel_fill_mv_btn.setObjectName("cancel_fill_mv_btn")
        self.missing_v_stacked.addWidget(self.mv_fill_page)
        self.mv_remove_page = QtWidgets.QWidget()
        self.mv_remove_page.setObjectName("mv_remove_page")
        self.label_6 = QtWidgets.QLabel(self.mv_remove_page)
        self.label_6.setGeometry(QtCore.QRect(20, 150, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Lucida Grande")
        font.setPointSize(29)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("border:1px solid rgba(80,80,80,0.5);\n"
"border-radius:20px;\n"
"background-color:rgba(20,20,20,255);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.done_remove_mv_btn = QtWidgets.QPushButton(self.mv_remove_page)
        self.done_remove_mv_btn.setGeometry(QtCore.QRect(280, 150, 113, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.done_remove_mv_btn.setFont(font)
        self.done_remove_mv_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.done_remove_mv_btn.setStyleSheet("QPushButton{\n"
"    border:1px solid rgba(80,80,80,0.5);\n"
"    border-radius:15px;\n"
"    background-color:rgba(20,20,20,255);\n"
"    color:white;\n"
"}\n"
"QPushButton:hover{\n"
"    border:1px solid rgba(0,230,0,0.5);\n"
"    border-radius:15px;\n"
"    background-color:rgba(20,20,20,255);\n"
"    color:rgba(0,230,0,0.5);\n"
"}\n"
"\n"
"")
        self.done_remove_mv_btn.setObjectName("done_remove_mv_btn")
        self.column_remove_mv_btn = QtWidgets.QRadioButton(self.mv_remove_page)
        self.column_remove_mv_btn.setGeometry(QtCore.QRect(40, 160, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.column_remove_mv_btn.setFont(font)
        self.column_remove_mv_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.column_remove_mv_btn.setStyleSheet("color:white;")
        self.column_remove_mv_btn.setCheckable(True)
        self.column_remove_mv_btn.setChecked(False)
        self.column_remove_mv_btn.setObjectName("column_remove_mv_btn")
        self.label_7 = QtWidgets.QLabel(self.mv_remove_page)
        self.label_7.setGeometry(QtCore.QRect(20, 20, 381, 51))
        font = QtGui.QFont()
        font.setFamily("Lucida Grande")
        font.setPointSize(21)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:white;\n"
"background-color:transparent;")
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")
        self.row_remove_mv_btn = QtWidgets.QRadioButton(self.mv_remove_page)
        self.row_remove_mv_btn.setGeometry(QtCore.QRect(160, 160, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.row_remove_mv_btn.setFont(font)
        self.row_remove_mv_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.row_remove_mv_btn.setStyleSheet("color:white;")
        self.row_remove_mv_btn.setCheckable(True)
        self.row_remove_mv_btn.setChecked(False)
        self.row_remove_mv_btn.setObjectName("row_remove_mv_btn")
        self.full_null_radiobtn = QtWidgets.QRadioButton(self.mv_remove_page)
        self.full_null_radiobtn.setGeometry(QtCore.QRect(40, 100, 361, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.full_null_radiobtn.setFont(font)
        self.full_null_radiobtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.full_null_radiobtn.setStyleSheet("color:white;")
        self.full_null_radiobtn.setCheckable(True)
        self.full_null_radiobtn.setChecked(False)
        self.full_null_radiobtn.setObjectName("full_null_radiobtn")
        self.label_8 = QtWidgets.QLabel(self.mv_remove_page)
        self.label_8.setGeometry(QtCore.QRect(20, 90, 371, 51))
        font = QtGui.QFont()
        font.setFamily("Lucida Grande")
        font.setPointSize(29)
        self.label_8.setFont(font)
        self.label_8.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_8.setStyleSheet("border:1px solid rgba(80,80,80,0.5);\n"
"border-radius:20px;\n"
"background-color:rgba(20,20,20,255);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.cancel_remove_mv_btn = QtWidgets.QPushButton(self.mv_remove_page)
        self.cancel_remove_mv_btn.setGeometry(QtCore.QRect(20, 220, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.cancel_remove_mv_btn.setFont(font)
        self.cancel_remove_mv_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cancel_remove_mv_btn.setStyleSheet("QPushButton{\n"
"    border:1px solid rgba(80,80,80,0.5);\n"
"    border-radius:15px;\n"
"    background-color:rgba(20,20,20,255);\n"
"    color:white;\n"
"}\n"
"QPushButton:hover{\n"
"    border:1px solid rgba(230,0,0,0.5);\n"
"    border-radius:15px;\n"
"    background-color:rgba(20,20,20,255);\n"
"    color:rgba(240,0,0,0.5);\n"
"}\n"
"\n"
"")
        self.cancel_remove_mv_btn.setObjectName("cancel_remove_mv_btn")
        self.label_8.raise_()
        self.label_6.raise_()
        self.done_remove_mv_btn.raise_()
        self.column_remove_mv_btn.raise_()
        self.label_7.raise_()
        self.row_remove_mv_btn.raise_()
        self.full_null_radiobtn.raise_()
        self.cancel_remove_mv_btn.raise_()
        self.missing_v_stacked.addWidget(self.mv_remove_page)
        self.label_14 = QtWidgets.QLabel(self.overview_page)
        self.label_14.setGeometry(QtCore.QRect(600, 60, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Lucida Grande")
        font.setPointSize(27)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color:white;\n"
"background-color:transparent;")
        self.label_14.setObjectName("label_14")
        self.remove_dup_btn = QtWidgets.QPushButton(self.overview_page)
        self.remove_dup_btn.setGeometry(QtCore.QRect(610, 140, 391, 61))
        font = QtGui.QFont()
        font.setFamily(".Lucida Grande UI")
        font.setPointSize(23)
        self.remove_dup_btn.setFont(font)
        self.remove_dup_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.remove_dup_btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.remove_dup_btn.setStyleSheet("QPushButton{\n"
"    background-color:rgba(80,80,80,0.5);\n"
"    color:white;\n"
"    border-color:1px transparent ;\n"
"    border-radius:20px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:rgba(30,30,30,240);\n"
"    color:white;\n"
"}\n"
"QPushButton:checked{\n"
"    background-color:red;\n"
"    color:white;\n"
"}")
        self.remove_dup_btn.setIconSize(QtCore.QSize(35, 35))
        self.remove_dup_btn.setCheckable(False)
        self.remove_dup_btn.setChecked(False)
        self.remove_dup_btn.setObjectName("remove_dup_btn")
        self.show_in_table_btn = QtWidgets.QPushButton(self.overview_page)
        self.show_in_table_btn.setGeometry(QtCore.QRect(620, 230, 371, 61))
        font = QtGui.QFont()
        font.setFamily(".Lucida Grande UI")
        font.setPointSize(23)
        self.show_in_table_btn.setFont(font)
        self.show_in_table_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.show_in_table_btn.setToolTip("")
        self.show_in_table_btn.setToolTipDuration(3)
        self.show_in_table_btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.show_in_table_btn.setStyleSheet("QPushButton{\n"
"    background-color:rgba(80,80,80,0.5);\n"
"    color:white;\n"
"    border-color:1px transparent ;\n"
"    border-radius:20px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:rgba(30,30,30,240);\n"
"    color:white;\n"
"}")
        self.show_in_table_btn.setIconSize(QtCore.QSize(35, 35))
        self.show_in_table_btn.setCheckable(False)
        self.show_in_table_btn.setObjectName("show_in_table_btn")
        self.label_9 = QtWidgets.QLabel(self.overview_page)
        self.label_9.setGeometry(QtCore.QRect(590, 110, 431, 211))
        font = QtGui.QFont()
        font.setFamily("Lucida Grande")
        font.setPointSize(29)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("border:1px transparent;\n"
"border-radius:20px;\n"
"background-color:rgba(20,20,20,255);")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.overview_table_widget = QtWidgets.QTableWidget(self.overview_page)
        self.overview_table_widget.setGeometry(QtCore.QRect(590, 340, 431, 341))
        self.overview_table_widget.setStyleSheet("""
    QTableWidget {
        background-color: rgba(20, 20, 20, 255);
        color: #f0f0f0;
        gridline-color: #3e3e3e;
        border: 1px solid #3e3e3e;
        padding-right: 0px;
        selection-background-color: #444444;
        selection-color: #ffffff;
}

QHeaderView::section {
    background-color: #3e3e3e; /* Başlık arka plan rengi: Orta gri */
    color: #f0f0f0; /* Başlık metin rengi: Beyaz */
    padding: 4px;
    border: 1px solid #2b2b2b; /* Başlık kenarlık rengi: Koyu gri */
}

QTableWidget::item {
    selection-background-color: #444444; /* Seçili öğe arka plan rengi */
    selection-color: #ffffff; /* Seçili öğe metin rengi */
    margin: 5px;
}

QTableWidget::item:selected {
    background-color: #444444; /* Seçili öğe arka plan rengi */
    color: #ffffff; /* Seçili öğe metin rengi */
    border: 1px solid yellow;
}

QScrollBar:vertical {
    background-color: #2b2b2b; /* Dikey kaydırma çubuğu arka plan rengi: Koyu gri */
    width: 15px;
    margin: 0px;
}

QScrollBar::handle:vertical {
    background-color: #5a5a5a; /* Dikey kaydırma çubuğu tutamağı: Gri */
    min-height: 20px;
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    background-color: #3e3e3e; /* Kaydırma çubuğu butonları: Orta gri */
    height: 15px;
}

QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
    background: none;
}
""")
        self.overview_table_widget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.overview_table_widget.setGridStyle(QtCore.Qt.SolidLine)
        self.overview_table_widget.setObjectName("overview_table_widget")
        self.overview_table_widget.setColumnCount(0)
        self.overview_table_widget.setRowCount(0)
        self.overview_table_widget.horizontalHeader().setCascadingSectionResizes(False)
        self.overview_table_widget.horizontalHeader().setSortIndicatorShown(False)
        self.overview_table_widget.horizontalHeader().setStretchLastSection(True)
        self.overview_table_widget.verticalHeader().setVisible(False)
        self.overview_table_widget.verticalHeader().setCascadingSectionResizes(False)
        self.overview_table_widget.verticalHeader().setSortIndicatorShown(False)
        self.overview_table_widget.verticalHeader().setStretchLastSection(False)
        self.label_9.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.general_overview_listwidget.raise_()
        self.label_4.raise_()
        self.missing_v_stacked.raise_()
        self.label_14.raise_()
        self.remove_dup_btn.raise_()
        self.show_in_table_btn.raise_()
        self.overview_table_widget.raise_()
        self.main_stacked_widget.addWidget(self.overview_page)
        self.preprosessing_page = QtWidgets.QWidget()
        self.preprosessing_page.setObjectName("preprosessing_page")
        self.label_10 = QtWidgets.QLabel(self.preprosessing_page)
        self.label_10.setGeometry(QtCore.QRect(80, 390, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Lucida Grande")
        font.setPointSize(27)
        self.label_10.setFont(font)
        self.label_10.setToolTip("")
        self.label_10.setStyleSheet("color:white;\n"
"background-color:transparent;")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.preprosessing_page)
        self.label_11.setGeometry(QtCore.QRect(80, 390, 491, 61))
        font = QtGui.QFont()
        font.setFamily("Lucida Grande")
        font.setPointSize(27)
        self.label_11.setFont(font)
        self.label_11.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_11.setToolTip("")
        self.label_11.setStyleSheet("color:white;\n"
"background-color:transparent;")
        self.label_11.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_11.setObjectName("label_11")
        self.prompt_done_btn = QtWidgets.QPushButton(self.preprosessing_page)
        self.prompt_done_btn.setGeometry(QtCore.QRect(580, 400, 130, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.prompt_done_btn.setFont(font)
        self.prompt_done_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.prompt_done_btn.setStyleSheet("QPushButton{\n"
"    border:1px solid rgba(80,80,80,0.5);\n"
"    border-radius:15px;\n"
"    background-color:rgba(20,20,20,255);\n"
"    color:white;\n"
"}\n"
"QPushButton:hover{\n"
"    border:1px solid rgba(0,230,0,0.5);\n"
"    border-radius:15px;\n"
"    background-color:rgba(20,20,20,255);\n"
"    color:rgba(0,230,0,0.5);\n"
"}\n"
"\n"
"")
        self.prompt_done_btn.setObjectName("prompt_done_btn")
        self.prompt_reset_btn = QtWidgets.QPushButton(self.preprosessing_page)
        self.prompt_reset_btn.setGeometry(QtCore.QRect(720, 400, 130, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.prompt_reset_btn.setFont(font)
        self.prompt_reset_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.prompt_reset_btn.setStyleSheet("QPushButton{\n"
"    border:1px solid rgba(80,80,80,0.5);\n"
"    border-radius:15px;\n"
"    background-color:rgba(20,20,20,255);\n"
"    color:white;\n"
"}\n"
"QPushButton:hover{\n"
"    border:1px solid rgba(230,0,0,0.5);\n"
"    border-radius:15px;\n"
"    background-color:rgba(20,20,20,255);\n"
"    color:rgba(240,0,0,0.5);\n"
"}\n"
"\n"
"")
        self.prompt_reset_btn.setObjectName("prompt_reset_btn")
        self.promp_back_btn = QtWidgets.QPushButton(self.preprosessing_page)
        self.promp_back_btn.setGeometry(QtCore.QRect(860, 400, 130, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.promp_back_btn.setFont(font)
        self.promp_back_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.promp_back_btn.setStyleSheet("QPushButton{\n"
"    border:1px solid rgba(80,80,80,0.5);\n"
"    border-radius:15px;\n"
"    background-color:rgba(20,20,20,255);\n"
"    color:white;\n"
"}\n"
"QPushButton:hover{\n"
"    border:1px solid yellow;\n"
"    border-radius:15px;\n"
"    background-color:rgba(20,20,20,255);\n"
"    color:yellow;\n"
"}\n"
"\n"
"")
        self.promp_back_btn.setObjectName("promp_back_btn")
        self.sql_query_area_stacked_widget = QtWidgets.QStackedWidget(self.preprosessing_page)
        self.sql_query_area_stacked_widget.setGeometry(QtCore.QRect(60, 440, 961, 271))
        self.sql_query_area_stacked_widget.setStyleSheet("color:white;\n"
"background-color:transparent;")
        self.sql_query_area_stacked_widget.setObjectName("sql_query_area_stacked_widget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.sql_text_area = QtWidgets.QPlainTextEdit(self.page)
        self.sql_text_area.setGeometry(QtCore.QRect(10, 10, 931, 261))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sql_text_area.sizePolicy().hasHeightForWidth())
        self.sql_text_area.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.sql_text_area.setFont(font)
        self.sql_text_area.setStyleSheet("\n"
"QPlainTextEdit {\n"
"    border:1px transparent;\n"
"    border-radius:20px;\n"
"    background-color:rgba(20,20,20,255);    \n"
"    color:white;\n"
"    padding-left:10; \n"
"    padding-top:10; \n"
"    padding-bottom:10; \n"
"    padding-right:10\n"
"}\n"
"")
        self.sql_text_area.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sql_text_area.setPlainText("")
        self.sql_text_area.setObjectName("sql_text_area")
        self.sql_query_area_stacked_widget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.prompt_table_widget = QtWidgets.QTableWidget(self.page_2)
        self.prompt_table_widget.setGeometry(QtCore.QRect(10, 10, 931, 261))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.prompt_table_widget.setFont(font)
        self.prompt_table_widget.setStyleSheet("/* QTableWidget için Dark Theme */\n"
"\n"
"QTableWidget {\n"
"    background-color:rgba(20,20,20,255);;   /* Arka plan rengi: Koyu gri */\n"
"    color: #f0f0f0;              /* Metin rengi: Beyaz */\n"
"    gridline-color: #3e3e3e;     /* Hücre ızgara çizgileri: Orta gri */\n"
"    border: 1px solid #3e3e3e;   /* Dış sınır: Orta gri */\n"
"    border-radius:15px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #3e3e3e;   /* Başlık arka plan rengi: Orta gri */\n"
"    color: #f0f0f0;              /* Başlık metin rengi: Beyaz */\n"
"    padding: 4px;\n"
"    border: 1px solid #2b2b2b;   /* Başlık kenarlık rengi: Koyu gri */\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    selection-background-color: #444444; /* Seçili öğe arka plan rengi: Koyu gri */\n"
"    selection-color: #ffffff;            /* Seçili öğe metin rengi: Beyaz */\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: #444444; /* Seçili öğe arka plan rengi: Koyu gri */\n"
"    color: #ffffff;            /* Seçili öğe metin rengi: Beyaz */\n"
"    border:1px solid yellow;\n"
"}\n"
"QTableCornerButton::section {\n"
"    background-color: #2b2b2b; /* Rengi koyu gri olarak değiştir */\n"
"    border: 1px solid #3e3e3e; /* Kenarlık rengi orta gri */\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    background-color: #2b2b2b; /* Dikey kaydırma çubuğu arka plan rengi: Koyu gri */\n"
"    width: 15px;\n"
"    margin: 0px 3px 0px 3px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background-color: #5a5a5a; /* Dikey kaydırma çubuğu tutamağı: Gri */\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    background-color: #3e3e3e; /* Kaydırma çubuğu butonları: Orta gri */\n"
"    height: 15px;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}")
        self.prompt_table_widget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.prompt_table_widget.setGridStyle(QtCore.Qt.SolidLine)
        self.prompt_table_widget.setObjectName("prompt_table_widget")
        self.prompt_table_widget.setColumnCount(0)
        self.prompt_table_widget.setRowCount(0)
        self.prompt_table_widget.horizontalHeader().setCascadingSectionResizes(False)
        self.prompt_table_widget.horizontalHeader().setSortIndicatorShown(False)
        self.prompt_table_widget.horizontalHeader().setStretchLastSection(True)
        self.prompt_table_widget.verticalHeader().setVisible(False)
        self.prompt_table_widget.verticalHeader().setCascadingSectionResizes(False)
        self.prompt_table_widget.verticalHeader().setSortIndicatorShown(False)
        self.prompt_table_widget.verticalHeader().setStretchLastSection(False)
        self.sql_query_area_stacked_widget.addWidget(self.page_2)
        self.pre_pros_chart_area = QtWidgets.QLabel(self.preprosessing_page)
        self.pre_pros_chart_area.setGeometry(QtCore.QRect(500, 20, 501, 361))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pre_pros_chart_area.setFont(font)
        self.pre_pros_chart_area.setStyleSheet("border:1px;\n"
"border-radius:20px;\n"
"background-color:rgba(20,20,20,255);    \n"
"color:rgba(255,255,255,0.5);")
        self.pre_pros_chart_area.setAlignment(QtCore.Qt.AlignCenter)
        self.pre_pros_chart_area.setObjectName("pre_pros_chart_area")
        self.label_13 = QtWidgets.QLabel(self.preprosessing_page)
        self.label_13.setGeometry(QtCore.QRect(70, 20, 421, 361))
        self.label_13.setStyleSheet("border:1px red;\n"
"border-radius:20px;\n"
"background-color:rgba(20,20,20,255);    ")
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.dataset_cb = QtWidgets.QComboBox(self.preprosessing_page)
        self.dataset_cb.setGeometry(QtCore.QRect(273, 50, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.dataset_cb.setFont(font)
        self.dataset_cb.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dataset_cb.setStyleSheet("QComboBox {\n"
"           background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0.8,\n"
"                            stop:0 rgb(71, 78, 83),\n"
"                            stop:1 rgb(49, 54, 58));\n"
"            border: 1px solid gray;\n"
"            border-radius: 7px;\n"
"            color: #f2f2f2;\n"
"            font-size: 14px;\n"
"            padding-left:16px;\n"
"        }\n"
"        \n"
"        QComboBox:hover {\n"
"           background-color: qlineargradient(x1:0, y1:0, x2:1,  y2:0.8,\n"
"                            stop:0 rgb(66, 73, 78),\n"
"                            stop:1 rgb(54, 49, 53));\n"
"\n"
"\n"
"        }\n"
"        \n"
"        QComboBox:focus {\n"
"           background-color: qlineargradient(x1:0, y1:0, x2:1,  y2:0.8,\n"
"                            stop:0 rgb(61, 68, 73),\n"
"                            stop:1 rgb(39, 44, 48));\n"
"\n"
"                            }\n"
"        QComboBox::down-arrow { width: 0px; image: url(:None); }\n"
"        QComboBox::drop-down { border: none; background:none;}\n"
"        \n"
"    QComboBox QAbstractItemView {\n"
"        border:0px;\n"
"        background-color: #31363A;\n"
"    }\n"
"        \n"
"        \n"
"    QComboBox::item {\n"
"        min-height: 35px;\n"
"        min-width: 50px;\n"
"        outline: none;\n"
"    }\n"
"    QComboBox::item:selected{\n"
"        color: black;\n"
"        background-color: lightgray;\n"
"    }       \n"
"     ")
        self.dataset_cb.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.dataset_cb.setObjectName("dataset_cb")
        self.dataset_cb.addItem("")
        self.label_15 = QtWidgets.QLabel(self.preprosessing_page)
        self.label_15.setGeometry(QtCore.QRect(90, 40, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Lucida Grande")
        font.setPointSize(22)
        self.label_15.setFont(font)
        self.label_15.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_15.setToolTip("")
        self.label_15.setStyleSheet("color:white;\n"
"background-color:transparent;")
        self.label_15.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.preprosessing_page)
        self.label_16.setGeometry(QtCore.QRect(90, 90, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Lucida Grande")
        font.setPointSize(22)
        self.label_16.setFont(font)
        self.label_16.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_16.setToolTip("")
        self.label_16.setStyleSheet("color:white;\n"
"background-color:transparent;")
        self.label_16.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_16.setObjectName("label_16")
        self.x_axis_cb = QtWidgets.QComboBox(self.preprosessing_page)
        self.x_axis_cb.setGeometry(QtCore.QRect(273, 100, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.x_axis_cb.setFont(font)
        self.x_axis_cb.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.x_axis_cb.setStyleSheet("QComboBox {\n"
"           background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0.8,\n"
"                            stop:0 rgb(71, 78, 83),\n"
"                            stop:1 rgb(49, 54, 58));\n"
"            border: 1px solid gray;\n"
"            border-radius: 7px;\n"
"            color: #f2f2f2;\n"
"            font-size: 14px;\n"
"            padding-left:16px;\n"
"        }\n"
"        \n"
"        QComboBox:hover {\n"
"           background-color: qlineargradient(x1:0, y1:0, x2:1,  y2:0.8,\n"
"                            stop:0 rgb(66, 73, 78),\n"
"                            stop:1 rgb(54, 49, 53));\n"
"\n"
"\n"
"        }\n"
"        \n"
"        QComboBox:focus {\n"
"           background-color: qlineargradient(x1:0, y1:0, x2:1,  y2:0.8,\n"
"                            stop:0 rgb(61, 68, 73),\n"
"                            stop:1 rgb(39, 44, 48));\n"
"\n"
"                            }\n"
"        QComboBox::down-arrow { width: 0px; image: url(:None); }\n"
"        QComboBox::drop-down { border: none; background:none;}\n"
"        \n"
"    QComboBox QAbstractItemView {\n"
"        border:0px;\n"
"        background-color: #31363A;\n"
"    }\n"
"        \n"
"        \n"
"    QComboBox::item {\n"
"        min-height: 35px;\n"
"        min-width: 50px;\n"
"        outline: none;\n"
"    }\n"
"    QComboBox::item:selected{\n"
"        color: black;\n"
"        background-color: lightgray;\n"
"    }       \n"
"     ")
        self.x_axis_cb.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.x_axis_cb.setObjectName("x_axis_cb")
        self.x_axis_cb.addItem("")
        self.label_17 = QtWidgets.QLabel(self.preprosessing_page)
        self.label_17.setGeometry(QtCore.QRect(90, 140, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Lucida Grande")
        font.setPointSize(22)
        self.label_17.setFont(font)
        self.label_17.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_17.setToolTip("")
        self.label_17.setStyleSheet("color:white;\n"
"background-color:transparent;")
        self.label_17.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_17.setObjectName("label_17")
        self.y_axis_cb = QtWidgets.QComboBox(self.preprosessing_page)
        self.y_axis_cb.setGeometry(QtCore.QRect(273, 150, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.y_axis_cb.setFont(font)
        self.y_axis_cb.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.y_axis_cb.setStyleSheet("QComboBox {\n"
"           background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0.8,\n"
"                            stop:0 rgb(71, 78, 83),\n"
"                            stop:1 rgb(49, 54, 58));\n"
"            border: 1px solid gray;\n"
"            border-radius: 7px;\n"
"            color: #f2f2f2;\n"
"            font-size: 14px;\n"
"            padding-left:16px;\n"
"        }\n"
"        \n"
"        QComboBox:hover {\n"
"           background-color: qlineargradient(x1:0, y1:0, x2:1,  y2:0.8,\n"
"                            stop:0 rgb(66, 73, 78),\n"
"                            stop:1 rgb(54, 49, 53));\n"
"\n"
"\n"
"        }\n"
"        \n"
"        QComboBox:focus {\n"
"           background-color: qlineargradient(x1:0, y1:0, x2:1,  y2:0.8,\n"
"                            stop:0 rgb(61, 68, 73),\n"
"                            stop:1 rgb(39, 44, 48));\n"
"\n"
"                            }\n"
"        QComboBox::down-arrow { width: 0px; image: url(:None); }\n"
"        QComboBox::drop-down { border: none; background:none;}\n"
"        \n"
"    QComboBox QAbstractItemView {\n"
"        border:0px;\n"
"        background-color: #31363A;\n"
"    }\n"
"        \n"
"        \n"
"    QComboBox::item {\n"
"        min-height: 35px;\n"
"        min-width: 50px;\n"
"        outline: none;\n"
"    }\n"
"    QComboBox::item:selected{\n"
"        color: black;\n"
"        background-color: lightgray;\n"
"    }       \n"
"     ")
        self.y_axis_cb.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.y_axis_cb.setObjectName("y_axis_cb")
        self.y_axis_cb.addItem("")
        self.label_18 = QtWidgets.QLabel(self.preprosessing_page)
        self.label_18.setGeometry(QtCore.QRect(90, 190, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Lucida Grande")
        font.setPointSize(22)
        self.label_18.setFont(font)
        self.label_18.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_18.setToolTip("")
        self.label_18.setStyleSheet("color:white;\n"
"background-color:transparent;")
        self.label_18.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_18.setObjectName("label_18")
        self.chart_type_cb = QtWidgets.QComboBox(self.preprosessing_page)
        self.chart_type_cb.setGeometry(QtCore.QRect(273, 200, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.chart_type_cb.setFont(font)
        self.chart_type_cb.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.chart_type_cb.setStyleSheet("QComboBox {\n"
"           background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0.8,\n"
"                            stop:0 rgb(71, 78, 83),\n"
"                            stop:1 rgb(49, 54, 58));\n"
"            border: 1px solid gray;\n"
"            border-radius: 7px;\n"
"            color: #f2f2f2;\n"
"            font-size: 14px;\n"
"            padding-left:16px;\n"
"        }\n"
"        \n"
"        QComboBox:hover {\n"
"           background-color: qlineargradient(x1:0, y1:0, x2:1,  y2:0.8,\n"
"                            stop:0 rgb(66, 73, 78),\n"
"                            stop:1 rgb(54, 49, 53));\n"
"\n"
"\n"
"        }\n"
"        \n"
"        QComboBox:focus {\n"
"           background-color: qlineargradient(x1:0, y1:0, x2:1,  y2:0.8,\n"
"                            stop:0 rgb(61, 68, 73),\n"
"                            stop:1 rgb(39, 44, 48));\n"
"\n"
"                            }\n"
"        QComboBox::down-arrow { width: 0px; image: url(:None); }\n"
"        QComboBox::drop-down { border: none; background:none;}\n"
"        \n"
"    QComboBox QAbstractItemView {\n"
"        border:0px;\n"
"        background-color: #31363A;\n"
"    }\n"
"        \n"
"        \n"
"    QComboBox::item {\n"
"        min-height: 35px;\n"
"        min-width: 50px;\n"
"        outline: none;\n"
"    }\n"
"    QComboBox::item:selected{\n"
"        color: black;\n"
"        background-color: lightgray;\n"
"    }       \n"
"     ")
        self.chart_type_cb.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.chart_type_cb.setObjectName("chart_type_cb")
        self.chart_type_cb.addItem("")
        self.chart_type_cb.addItem("")
        self.chart_type_cb.addItem("")
        self.chart_type_cb.addItem("")
        self.chart_type_cb.addItem("")
        self.chart_type_cb.addItem("")
        self.show_gridline_checkBox = QtWidgets.QCheckBox(self.preprosessing_page)
        self.show_gridline_checkBox.setGeometry(QtCore.QRect(90, 260, 161, 31))
        self.show_gridline_checkBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.show_gridline_checkBox.setStyleSheet("QCheckBox {\n"
"           background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0.8,\n"
"                            stop:0 rgb(71, 78, 83),\n"
"                            stop:1 rgb(49, 54, 58));\n"
"            border: 1px solid gray;\n"
"            border-radius: 7px;\n"
"            color: #f2f2f2;\n"
"            font-size: 14px;\n"
"            padding-left:16px;\n"
"        }\n"
"        \n"
"        QCheckBox:hover {\n"
"           background-color: qlineargradient(x1:0, y1:0, x2:1,  y2:0.8,\n"
"                            stop:0 rgb(66, 73, 78),\n"
"                            stop:1 rgb(54, 49, 53));\n"
"\n"
"\n"
"        }\n"
"        \n"
"        QCheckBox:focus {\n"
"           background-color: qlineargradient(x1:0, y1:0, x2:1,  y2:0.8,\n"
"                            stop:0 rgb(61, 68, 73),\n"
"                            stop:1 rgb(39, 44, 48));\n"
"\n"
" }\n"
"       \n"
"    QCheckBox QAbstractItemView {\n"
"        border:0px;\n"
"        background-color: #31363A;\n"
"    }\n"
"        \n"
" \n"
"     ")
        self.show_gridline_checkBox.setObjectName("show_gridline_checkBox")
        self.chart_color_btn = QtWidgets.QPushButton(self.preprosessing_page)
        self.chart_color_btn.setGeometry(QtCore.QRect(272, 260, 191, 32))
        self.chart_color_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.chart_color_btn.setStyleSheet("QPushButton {\n"
"           background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0.8,\n"
"                            stop:0 rgb(71, 78, 83),\n"
"                            stop:1 rgb(49, 54, 58));\n"
"            border: 1px solid gray;\n"
"            border-radius: 7px;\n"
"            color: #f2f2f2;\n"
"            font-size: 14px;\n"
"            padding-left:16px;\n"
"        }\n"
"        \n"
"        QPushButton:hover {\n"
"           background-color: qlineargradient(x1:0, y1:0, x2:1,  y2:0.8,\n"
"                            stop:0 rgb(66, 73, 78),\n"
"                            stop:1 rgb(54, 49, 53));\n"
"\n"
"\n"
"        }\n"
"        \n"
"        QPushButton:focus {\n"
"           background-color: qlineargradient(x1:0, y1:0, x2:1,  y2:0.8,\n"
"                            stop:0 rgb(61, 68, 73),\n"
"                            stop:1 rgb(39, 44, 48));\n"
"\n"
"                            }\n"
"\n"
"    QPushButton QAbstractItemView {\n"
"        border:0px;\n"
"        background-color: #31363A;\n"
"    }\n"
"")
        self.chart_color_btn.setObjectName("chart_color_btn")
        self.plot_chart_btn = QtWidgets.QPushButton(self.preprosessing_page)
        self.plot_chart_btn.setGeometry(QtCore.QRect(90, 320, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.plot_chart_btn.setFont(font)
        self.plot_chart_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.plot_chart_btn.setStyleSheet("QPushButton {\n"
"           background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0.8,\n"
"                            stop:0 rgb(71, 78, 83),\n"
"                            stop:1 rgb(49, 54, 58));\n"
"            border: 1px solid gray;\n"
"            border-radius: 7px;\n"
"            color: #f2f2f2;\n"
"            font-size: 14px;\n"
"            padding-left:16px;\n"
"        }\n"
"        \n"
"        QPushButton:hover {\n"
"           background-color: qlineargradient(x1:0, y1:0, x2:1,  y2:0.8,\n"
"                            stop:0 rgb(66, 73, 78),\n"
"                            stop:1 rgb(54, 49, 53));\n"
"\n"
"\n"
"        }\n"
"        \n"
"        QPushButton:focus {\n"
"           background-color: qlineargradient(x1:0, y1:0, x2:1,  y2:0.8,\n"
"                            stop:0 rgb(61, 68, 73),\n"
"                            stop:1 rgb(39, 44, 48));\n"
"\n"
"                            }\n"
"\n"
"    QPushButton QAbstractItemView {\n"
"        border:0px;\n"
"        background-color: #31363A;\n"
"    }\n"
"")
        self.plot_chart_btn.setObjectName("plot_chart_btn")
        self.main_stacked_widget.addWidget(self.preprosessing_page)
        self.transformation_page = QtWidgets.QWidget()
        self.transformation_page.setObjectName("transformation_page")
        self.label_20 = QtWidgets.QLabel(self.transformation_page)
        self.label_20.setGeometry(QtCore.QRect(40, 40, 411, 51))
        font = QtGui.QFont()
        font.setFamily("Lucida Grande")
        font.setPointSize(27)
        self.label_20.setFont(font)
        self.label_20.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_20.setToolTip("")
        self.label_20.setStyleSheet("color:white;\n"
"background-color:transparent;")
        self.label_20.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_20.setObjectName("label_20")
        self.label_24 = QtWidgets.QLabel(self.transformation_page)
        self.label_24.setGeometry(QtCore.QRect(30, 90, 421, 311))
        self.label_24.setStyleSheet("border:1px red;\n"
"border-radius:20px;\n"
"background-color:rgba(20,20,20,255);    ")
        self.label_24.setText("")
        self.label_24.setObjectName("label_24")
        self.z_score_radio_btn = QtWidgets.QRadioButton(self.transformation_page)
        self.z_score_radio_btn.setGeometry(QtCore.QRect(50, 170, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.z_score_radio_btn.setFont(font)
        self.z_score_radio_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.z_score_radio_btn.setStyleSheet("QRadioButton {\n"
"           background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0.8,\n"
"                            stop:0 rgb(71, 78, 83),\n"
"                            stop:1 rgb(49, 54, 58));\n"
"            border: 1px solid gray;\n"
"            border-radius: 7px;\n"
"            color: #f2f2f2;\n"
"            font-size: 20px;\n"
"            padding-left:20px;\n"
"        }\n"
"        \n"
"        QRadioButton:hover {\n"
"           background-color: qlineargradient(x1:0, y1:0, x2:1,  y2:0.8,\n"
"                            stop:0 rgb(66, 73, 78),\n"
"                            stop:1 rgb(54, 49, 53));\n"
"\n"
"\n"
"        }")
        self.z_score_radio_btn.setCheckable(True)
        self.z_score_radio_btn.setChecked(False)
        self.z_score_radio_btn.setObjectName("z_score_radio_btn")
        self.min_max_radio_btn = QtWidgets.QRadioButton(self.transformation_page)
        self.min_max_radio_btn.setGeometry(QtCore.QRect(50, 230, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.min_max_radio_btn.setFont(font)
        self.min_max_radio_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.min_max_radio_btn.setStyleSheet("QRadioButton {\n"
"           background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0.8,\n"
"                            stop:0 rgb(71, 78, 83),\n"
"                            stop:1 rgb(49, 54, 58));\n"
"            border: 1px solid gray;\n"
"            border-radius: 7px;\n"
"            color: #f2f2f2;\n"
"            font-size: 20px;\n"
"            padding-left:20px;\n"
"        }\n"
"        \n"
"        QRadioButton:hover {\n"
"           background-color: qlineargradient(x1:0, y1:0, x2:1,  y2:0.8,\n"
"                            stop:0 rgb(66, 73, 78),\n"
"                            stop:1 rgb(54, 49, 53));\n"
"\n"
"\n"
"        }")
        self.min_max_radio_btn.setCheckable(True)
        self.min_max_radio_btn.setChecked(False)
        self.min_max_radio_btn.setObjectName("min_max_radio_btn")
        self.minvalue_lineedit = QtWidgets.QLineEdit(self.transformation_page)
        self.minvalue_lineedit.setEnabled(False)
        self.minvalue_lineedit.setGeometry(QtCore.QRect(50, 290, 181, 31))
        self.minvalue_lineedit.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.minvalue_lineedit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.minvalue_lineedit.setStyleSheet("QLineEdit {\n"
"           background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0.8,\n"
"                            stop:0 rgb(71, 78, 83),\n"
"                            stop:1 rgb(49, 54, 58));\n"
"            border: 1px solid gray;\n"
"            border-radius: 7px;\n"
"            color: #f2f2f2;\n"
"            font-size: 20px;\n"
"        }\n"
"        \n"
"        QLineEdit:hover {\n"
"           background-color: qlineargradient(x1:0, y1:0, x2:1,  y2:0.8,\n"
"                            stop:0 rgb(66, 73, 78),\n"
"                            stop:1 rgb(54, 49, 53));\n"
"\n"
"\n"
"        }")
        self.minvalue_lineedit.setAlignment(QtCore.Qt.AlignCenter)
        self.minvalue_lineedit.setReadOnly(False)
        self.minvalue_lineedit.setObjectName("minvalue_lineedit")
        self.maxvalue_lineedit = QtWidgets.QLineEdit(self.transformation_page)
        self.maxvalue_lineedit.setEnabled(False)
        self.maxvalue_lineedit.setGeometry(QtCore.QRect(250, 290, 181, 31))
        self.maxvalue_lineedit.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.maxvalue_lineedit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.maxvalue_lineedit.setStyleSheet("QLineEdit {\n"
"           background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0.8,\n"
"                            stop:0 rgb(71, 78, 83),\n"
"                            stop:1 rgb(49, 54, 58));\n"
"            border: 1px solid gray;\n"
"            border-radius: 7px;\n"
"            color: #f2f2f2;\n"
"            font-size: 20px;\n"
"        }\n"
"        \n"
"        QLineEdit:hover {\n"
"           background-color: qlineargradient(x1:0, y1:0, x2:1,  y2:0.8,\n"
"                            stop:0 rgb(66, 73, 78),\n"
"                            stop:1 rgb(54, 49, 53));\n"
"\n"
"\n"
"        }")
        self.maxvalue_lineedit.setAlignment(QtCore.Qt.AlignCenter)
        self.maxvalue_lineedit.setReadOnly(False)
        self.maxvalue_lineedit.setClearButtonEnabled(False)
        self.maxvalue_lineedit.setObjectName("maxvalue_lineedit")
        self.scaling_column_box = QtWidgets.QComboBox(self.transformation_page)
        self.scaling_column_box.setGeometry(QtCore.QRect(50, 110, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.scaling_column_box.setFont(font)
        self.scaling_column_box.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.scaling_column_box.setStyleSheet("QComboBox {\n"
"           background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0.8,\n"
"                            stop:0 rgb(71, 78, 83),\n"
"                            stop:1 rgb(49, 54, 58));\n"
"            border: 1px solid gray;\n"
"            border-radius: 7px;\n"
"            color: #f2f2f2;\n"
"            font-size: 20px;\n"
"            padding-left:20px;\n"
"        }\n"
"        \n"
"        QComboBox:hover {\n"
"           background-color: qlineargradient(x1:0, y1:0, x2:1,  y2:0.8,\n"
"                            stop:0 rgb(66, 73, 78),\n"
"                            stop:1 rgb(54, 49, 53));\n"
"\n"
"\n"
"        }")
        self.scaling_column_box.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.scaling_column_box.setObjectName("scaling_column_box")
        self.scaling_column_box.addItem("")
        self.scaling_apply_btn = QtWidgets.QPushButton(self.transformation_page)
        self.scaling_apply_btn.setGeometry(QtCore.QRect(50, 340, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.scaling_apply_btn.setFont(font)
        self.scaling_apply_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.scaling_apply_btn.setStyleSheet("QPushButton{\n"
"    background-color:rgba(80,80,80,0.5);\n"
"    color:white;\n"
"    border-color:1px transparent ;\n"
"    border-radius:20px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:rgba(30,30,30,240);\n"
"    color:white;\n"
"}\n"
"QPushButton:checked{\n"
"    background-color:red;\n"
"    color:white;\n"
"}")
        self.scaling_apply_btn.setObjectName("scaling_apply_btn")
        self.label_25 = QtWidgets.QLabel(self.transformation_page)
        self.label_25.setGeometry(QtCore.QRect(30, 480, 421, 201))
        self.label_25.setStyleSheet("border:1px red;\n"
"border-radius:20px;\n"
"background-color:rgba(20,20,20,255);    ")
        self.label_25.setText("")
        self.label_25.setObjectName("label_25")
        self.add_rempve_column_btn = QtWidgets.QPushButton(self.transformation_page)
        self.add_rempve_column_btn.setGeometry(QtCore.QRect(50, 620, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.add_rempve_column_btn.setFont(font)
        self.add_rempve_column_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_rempve_column_btn.setStyleSheet("QPushButton{\n"
"    background-color:rgba(80,80,80,0.5);\n"
"    color:white;\n"
"    border-color:1px transparent ;\n"
"    border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:rgba(30,30,30,240);\n"
"    color:white;\n"
"}\n"
"QPushButton:checked{\n"
"    background-color:red;\n"
"    color:white;\n"
"}")
        self.add_rempve_column_btn.setObjectName("add_rempve_column_btn")
        self.add_and_remove_row_btn = QtWidgets.QPushButton(self.transformation_page)
        self.add_and_remove_row_btn.setGeometry(QtCore.QRect(50, 560, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.add_and_remove_row_btn.setFont(font)
        self.add_and_remove_row_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_and_remove_row_btn.setStyleSheet("QPushButton{\n"
"    background-color:rgba(80,80,80,0.5);\n"
"    color:white;\n"
"    border-color:1px transparent ;\n"
"    border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:rgba(30,30,30,240);\n"
"    color:white;\n"
"}\n"
"QPushButton:checked{\n"
"    background-color:red;\n"
"    color:white;\n"
"}")
        self.add_and_remove_row_btn.setObjectName("add_and_remove_row_btn")
        self.label_26 = QtWidgets.QLabel(self.transformation_page)
        self.label_26.setGeometry(QtCore.QRect(530, 90, 421, 331))
        self.label_26.setStyleSheet("border:1px red;\n"
"border-radius:20px;\n"
"background-color:rgba(20,20,20,255);    ")
        self.label_26.setText("")
        self.label_26.setObjectName("label_26")
        self.merge_columns_btn = QtWidgets.QPushButton(self.transformation_page)
        self.merge_columns_btn.setGeometry(QtCore.QRect(50, 500, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.merge_columns_btn.setFont(font)
        self.merge_columns_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.merge_columns_btn.setStyleSheet("QPushButton{\n"
"    background-color:rgba(80,80,80,0.5);\n"
"    color:white;\n"
"    border-color:1px transparent ;\n"
"    border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:rgba(30,30,30,240);\n"
"    color:white;\n"
"}\n"
"QPushButton:checked{\n"
"    background-color:red;\n"
"    color:white;\n"
"}")
        self.merge_columns_btn.setObjectName("merge_columns_btn")
        self.label_21 = QtWidgets.QLabel(self.transformation_page)
        self.label_21.setGeometry(QtCore.QRect(40, 430, 291, 51))
        font = QtGui.QFont()
        font.setFamily("Lucida Grande")
        font.setPointSize(27)
        self.label_21.setFont(font)
        self.label_21.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_21.setToolTip("")
        self.label_21.setStyleSheet("color:white;\n"
"background-color:transparent;")
        self.label_21.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.transformation_page)
        self.label_22.setGeometry(QtCore.QRect(540, 40, 401, 51))
        font = QtGui.QFont()
        font.setFamily("Lucida Grande")
        font.setPointSize(27)
        self.label_22.setFont(font)
        self.label_22.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_22.setToolTip("")
        self.label_22.setStyleSheet("color:white;\n"
"background-color:transparent;")
        self.label_22.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_22.setObjectName("label_22")
        self.label_27 = QtWidgets.QLabel(self.transformation_page)
        self.label_27.setGeometry(QtCore.QRect(540, 110, 401, 111))
        self.label_27.setStyleSheet("QLabel{\n"
"    border:1px solid gray;\n"
"    border-radius:20px;\n"
"    background-color:rgba(20,20,20,255);    \n"
"}\n"
"")
        self.label_27.setText("")
        self.label_27.setObjectName("label_27")
        self.label_23 = QtWidgets.QLabel(self.transformation_page)
        self.label_23.setGeometry(QtCore.QRect(560, 130, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Lucida Grande")
        font.setPointSize(20)
        self.label_23.setFont(font)
        self.label_23.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_23.setToolTip("")
        self.label_23.setStyleSheet("color: rgb(229, 229, 229);\n"
"background-color:transparent;")
        self.label_23.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_23.setObjectName("label_23")
        self.change_dt_select_column = QtWidgets.QComboBox(self.transformation_page)
        self.change_dt_select_column.setGeometry(QtCore.QRect(560, 170, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.change_dt_select_column.setFont(font)
        self.change_dt_select_column.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.change_dt_select_column.setStyleSheet("QComboBox {\n"
"           background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0.8,\n"
"                            stop:0 rgb(71, 78, 83),\n"
"                            stop:1 rgb(49, 54, 58));\n"
"            border: 1px solid gray;\n"
"            border-radius: 7px;\n"
"            color: #f2f2f2;\n"
"            font-size: 16px;\n"
"            padding-left:20px;\n"
"        }\n"
"        \n"
"        QComboBox:hover {\n"
"           background-color: qlineargradient(x1:0, y1:0, x2:1,  y2:0.8,\n"
"                            stop:0 rgb(66, 73, 78),\n"
"                            stop:1 rgb(54, 49, 53));\n"
"\n"
"\n"
"        }")
        self.change_dt_select_column.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.change_dt_select_column.setObjectName("change_dt_select_column")
        self.change_dt_select_column.addItem("")
        self.label_28 = QtWidgets.QLabel(self.transformation_page)
        self.label_28.setGeometry(QtCore.QRect(560, 250, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Lucida Grande")
        font.setPointSize(20)
        self.label_28.setFont(font)
        self.label_28.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_28.setToolTip("")
        self.label_28.setStyleSheet("color: rgb(229, 229, 229);\n"
"background-color:transparent;")
        self.label_28.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_28.setObjectName("label_28")
        self.select_new_data_type = QtWidgets.QComboBox(self.transformation_page)
        self.select_new_data_type.setGeometry(QtCore.QRect(560, 290, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.select_new_data_type.setFont(font)
        self.select_new_data_type.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.select_new_data_type.setStyleSheet("QComboBox {\n"
"           background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0.8,\n"
"                            stop:0 rgb(71, 78, 83),\n"
"                            stop:1 rgb(49, 54, 58));\n"
"            border: 1px solid gray;\n"
"            border-radius: 7px;\n"
"            color: #f2f2f2;\n"
"            font-size: 16px;\n"
"            padding-left:20px;\n"
"        }\n"
"        \n"
"        QComboBox:hover {\n"
"           background-color: qlineargradient(x1:0, y1:0, x2:1,  y2:0.8,\n"
"                            stop:0 rgb(66, 73, 78),\n"
"                            stop:1 rgb(54, 49, 53));\n"
"\n"
"\n"
"        }")
        self.select_new_data_type.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.select_new_data_type.setObjectName("select_new_data_type")
        self.select_new_data_type.addItem("")
        self.select_new_data_type.addItem("")
        self.select_new_data_type.addItem("")
        self.select_new_data_type.addItem("")
        self.select_new_data_type.addItem("")
        self.label_29 = QtWidgets.QLabel(self.transformation_page)
        self.label_29.setGeometry(QtCore.QRect(540, 230, 401, 111))
        self.label_29.setStyleSheet("QLabel{\n"
"    border:1px solid gray;\n"
"    border-radius:20px;\n"
"    background-color:rgba(20,20,20,255);    \n"
"}\n"
"")
        self.label_29.setText("")
        self.label_29.setObjectName("label_29")
        self.data_type_apply_changes = QtWidgets.QPushButton(self.transformation_page)
        self.data_type_apply_changes.setGeometry(QtCore.QRect(550, 360, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.data_type_apply_changes.setFont(font)
        self.data_type_apply_changes.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.data_type_apply_changes.setStyleSheet("QPushButton{\n"
"    background-color:rgba(80,80,80,0.5);\n"
"    color:white;\n"
"    border-color:1px transparent ;\n"
"    border-radius:20px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:rgba(30,30,30,240);\n"
"    color:white;\n"
"}\n"
"QPushButton:checked{\n"
"    background-color:red;\n"
"    color:white;\n"
"}")
        self.data_type_apply_changes.setObjectName("data_type_apply_changes")
        self.label_31 = QtWidgets.QLabel(self.transformation_page)
        self.label_31.setGeometry(QtCore.QRect(540, 430, 291, 51))
        font = QtGui.QFont()
        font.setFamily("Lucida Grande")
        font.setPointSize(27)
        self.label_31.setFont(font)
        self.label_31.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_31.setToolTip("")
        self.label_31.setStyleSheet("color:white;\n"
"background-color:transparent;")
        self.label_31.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_31.setObjectName("label_31")
        self.summary_of_changes_listwidget = QtWidgets.QListWidget(self.transformation_page)
        self.summary_of_changes_listwidget.setGeometry(QtCore.QRect(530, 481, 421, 201))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.summary_of_changes_listwidget.setFont(font)
        self.summary_of_changes_listwidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.summary_of_changes_listwidget.setStyleSheet("/* QTableWidget için Dark Theme */\n"
"\n"
"QListWidget {\n"
"    background-color:rgba(20,20,20,255);;   /* Arka plan rengi: Koyu gri */\n"
"                  /* Metin rengi: Beyaz */\n"
"    color: rgb(210, 210, 210);\n"
"    padding:20px;\n"
"    gridline-color: #3e3e3e;     /* Hücre ızgara çizgileri: Orta gri */\n"
"    border: 1px solid #3e3e3e;   /* Dış sınır: Orta gri */\n"
"    border-radius:15px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #3e3e3e;   \n"
"    color: #f0f0f0;         \n"
"    padding: 4px;\n"
"    border: 1px solid #2b2b2b;   /* Başlık kenarlık rengi: Koyu gri */\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    selection-background-color: #444444; /* Seçili öğe arka plan rengi: Koyu gri */\n"
"    selection-color: #ffffff;            /* Seçili öğe metin rengi: Beyaz */\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    background-color: transparent; \n"
"    color: #ffffff;\n"
"    border:1px solid rgba(162, 31, 188,0.5);\n"
"    border-radius:10px;\n"
"}\n"
"\n"
"\n"
"QScrollBar:vertical {\n"
"    background-color: #2b2b2b; \n"
"    width: 15px;\n"
"    margin: 0px 3px 0px 3px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background-color: #5a5a5a; \n"
"    min-height: 20px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    background-color: #3e3e3e; \n"
"    height: 15px;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}")
        self.summary_of_changes_listwidget.setObjectName("summary_of_changes_listwidget")
        item = QtWidgets.QListWidgetItem()
        self.summary_of_changes_listwidget.addItem(item)
        self.label_26.raise_()
        self.label_29.raise_()
        self.label_24.raise_()
        self.label_20.raise_()
        self.z_score_radio_btn.raise_()
        self.min_max_radio_btn.raise_()
        self.minvalue_lineedit.raise_()
        self.maxvalue_lineedit.raise_()
        self.scaling_column_box.raise_()
        self.scaling_apply_btn.raise_()
        self.label_25.raise_()
        self.add_rempve_column_btn.raise_()
        self.add_and_remove_row_btn.raise_()
        self.merge_columns_btn.raise_()
        self.label_21.raise_()
        self.label_22.raise_()
        self.label_27.raise_()
        self.label_23.raise_()
        self.change_dt_select_column.raise_()
        self.label_28.raise_()
        self.select_new_data_type.raise_()
        self.data_type_apply_changes.raise_()
        self.label_31.raise_()
        self.summary_of_changes_listwidget.raise_()
        self.main_stacked_widget.addWidget(self.transformation_page)
        self.statistics_page = QtWidgets.QWidget()
        self.statistics_page.setObjectName("statistics_page")
        self.pixmap_plot_area = QtWidgets.QLabel(self.statistics_page)
        self.pixmap_plot_area.setGeometry(QtCore.QRect(30, 290, 1011, 421))
        self.pixmap_plot_area.setStyleSheet("border:1px red;\n"
"border-radius:20px;\n"
"background-color:rgba(20,20,20,255);    ")
        self.pixmap_plot_area.setText("")
        self.pixmap_plot_area.setObjectName("pixmap_plot_area")
        self.label_32 = QtWidgets.QLabel(self.statistics_page)
        self.label_32.setGeometry(QtCore.QRect(30, 230, 401, 51))
        font = QtGui.QFont()
        font.setFamily("Lucida Grande")
        font.setPointSize(27)
        self.label_32.setFont(font)
        self.label_32.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_32.setToolTip("")
        self.label_32.setStyleSheet("color:white;\n"
"background-color:transparent;")
        self.label_32.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.statistics_page)
        self.label_33.setGeometry(QtCore.QRect(20, 70, 1021, 151))
        self.label_33.setStyleSheet("border:1px red;\n"
"border-radius:20px;\n"
"background-color:rgba(20,20,20,255);    ")
        self.label_33.setText("")
        self.label_33.setObjectName("label_33")
        self.frequency_btn = QtWidgets.QPushButton(self.statistics_page)
        self.frequency_btn.setGeometry(QtCore.QRect(40, 90, 320, 41))
        self.frequency_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.frequency_btn.setStyleSheet("QPushButton {\n"
"           background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0.8,\n"
"                            stop:0 rgb(71, 78, 83),\n"
"                            stop:1 rgb(49, 54, 58));\n"
"            border: 1px solid gray;\n"
"            border-radius: 7px;\n"
"            color: #f2f2f2;\n"
"            font-size: 20px;\n"
"            padding-left:20px;\n"
"        }\n"
"        \n"
"        QPushButton:hover {\n"
"           background-color: qlineargradient(x1:0, y1:0, x2:1,  y2:0.8,\n"
"                            stop:0 rgb(66, 73, 78),\n"
"                            stop:1 rgb(54, 49, 53));\n"
"\n"
"\n"
"        }")
        self.frequency_btn.setObjectName("frequency_btn")
        self.correlation_btn = QtWidgets.QPushButton(self.statistics_page)
        self.correlation_btn.setGeometry(QtCore.QRect(370, 90, 320, 41))
        self.correlation_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.correlation_btn.setStyleSheet("QPushButton {\n"
"           background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0.8,\n"
"                            stop:0 rgb(71, 78, 83),\n"
"                            stop:1 rgb(49, 54, 58));\n"
"            border: 1px solid gray;\n"
"            border-radius: 7px;\n"
"            color: #f2f2f2;\n"
"            font-size: 20px;\n"
"            padding-left:20px;\n"
"        }\n"
"        \n"
"        QPushButton:hover {\n"
"           background-color: qlineargradient(x1:0, y1:0, x2:1,  y2:0.8,\n"
"                            stop:0 rgb(66, 73, 78),\n"
"                            stop:1 rgb(54, 49, 53));\n"
"\n"
"\n"
"        }")
        self.correlation_btn.setObjectName("correlation_btn")
        self.outliers_btn = QtWidgets.QPushButton(self.statistics_page)
        self.outliers_btn.setGeometry(QtCore.QRect(700, 90, 320, 41))
        self.outliers_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.outliers_btn.setStyleSheet("QPushButton {\n"
"           background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0.8,\n"
"                            stop:0 rgb(71, 78, 83),\n"
"                            stop:1 rgb(49, 54, 58));\n"
"            border: 1px solid gray;\n"
"            border-radius: 7px;\n"
"            color: #f2f2f2;\n"
"            font-size: 20px;\n"
"            padding-left:20px;\n"
"        }\n"
"        \n"
"        QPushButton:hover {\n"
"           background-color: qlineargradient(x1:0, y1:0, x2:1,  y2:0.8,\n"
"                            stop:0 rgb(66, 73, 78),\n"
"                            stop:1 rgb(54, 49, 53));\n"
"\n"
"\n"
"        }")
        self.outliers_btn.setObjectName("outliers_btn")
        self.label_34 = QtWidgets.QLabel(self.statistics_page)
        self.label_34.setGeometry(QtCore.QRect(30, 20, 401, 51))
        font = QtGui.QFont()
        font.setFamily("Lucida Grande")
        font.setPointSize(27)
        self.label_34.setFont(font)
        self.label_34.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_34.setToolTip("")
        self.label_34.setStyleSheet("color:white;\n"
"background-color:transparent;")
        self.label_34.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_34.setObjectName("label_34")
        self.value_counts_btn = QtWidgets.QPushButton(self.statistics_page)
        self.value_counts_btn.setGeometry(QtCore.QRect(40, 150, 320, 41))
        self.value_counts_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.value_counts_btn.setStyleSheet("QPushButton {\n"
"           background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0.8,\n"
"                            stop:0 rgb(71, 78, 83),\n"
"                            stop:1 rgb(49, 54, 58));\n"
"            border: 1px solid gray;\n"
"            border-radius: 7px;\n"
"            color: #f2f2f2;\n"
"            font-size: 20px;\n"
"            padding-left:20px;\n"
"        }\n"
"        \n"
"        QPushButton:hover {\n"
"           background-color: qlineargradient(x1:0, y1:0, x2:1,  y2:0.8,\n"
"                            stop:0 rgb(66, 73, 78),\n"
"                            stop:1 rgb(54, 49, 53));\n"
"\n"
"\n"
"        }")
        self.value_counts_btn.setObjectName("value_counts_btn")
        self.histograms_btn = QtWidgets.QPushButton(self.statistics_page)
        self.histograms_btn.setGeometry(QtCore.QRect(370, 150, 320, 41))
        self.histograms_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.histograms_btn.setStyleSheet("QPushButton {\n"
"           background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0.8,\n"
"                            stop:0 rgb(71, 78, 83),\n"
"                            stop:1 rgb(49, 54, 58));\n"
"            border: 1px solid gray;\n"
"            border-radius: 7px;\n"
"            color: #f2f2f2;\n"
"            font-size: 20px;\n"
"            padding-left:20px;\n"
"        }\n"
"        \n"
"        QPushButton:hover {\n"
"           background-color: qlineargradient(x1:0, y1:0, x2:1,  y2:0.8,\n"
"                            stop:0 rgb(66, 73, 78),\n"
"                            stop:1 rgb(54, 49, 53));\n"
"\n"
"\n"
"        }")
        self.histograms_btn.setObjectName("histograms_btn")
        self.distribution_btn = QtWidgets.QPushButton(self.statistics_page)
        self.distribution_btn.setGeometry(QtCore.QRect(700, 150, 320, 41))
        self.distribution_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.distribution_btn.setStyleSheet("QPushButton {\n"
"           background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0.8,\n"
"                            stop:0 rgb(71, 78, 83),\n"
"                            stop:1 rgb(49, 54, 58));\n"
"            border: 1px solid gray;\n"
"            border-radius: 7px;\n"
"            color: #f2f2f2;\n"
"            font-size: 20px;\n"
"            padding-left:20px;\n"
"        }\n"
"        \n"
"        QPushButton:hover {\n"
"           background-color: qlineargradient(x1:0, y1:0, x2:1,  y2:0.8,\n"
"                            stop:0 rgb(66, 73, 78),\n"
"                            stop:1 rgb(54, 49, 53));\n"
"\n"
"\n"
"        }")
        self.distribution_btn.setObjectName("distribution_btn")
        self.main_stacked_widget.addWidget(self.statistics_page)
        self.finalization_page = QtWidgets.QWidget()
        self.finalization_page.setObjectName("finalization_page")
        self.label_35 = QtWidgets.QLabel(self.finalization_page)
        self.label_35.setGeometry(QtCore.QRect(40, 40, 1001, 641))
        self.label_35.setStyleSheet("border:1px red;\n"
"border-radius:20px;\n"
"background-color:rgba(20,20,20,255);    ")
        self.label_35.setText("")
        self.label_35.setObjectName("label_35")
        self.file_extension_combobox = QtWidgets.QComboBox(self.finalization_page)
        self.file_extension_combobox.setGeometry(QtCore.QRect(420, 160, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.file_extension_combobox.setFont(font)
        self.file_extension_combobox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.file_extension_combobox.setStyleSheet("QComboBox {\n"
"           background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0.8,\n"
"                            stop:0 rgb(71, 78, 83),\n"
"                            stop:1 rgb(49, 54, 58));\n"
"            border: 1px solid gray;\n"
"            border-radius: 7px;\n"
"            color: #f2f2f2;\n"
"            font-size: 20px;\n"
"            padding-left:20px;\n"
"        }\n"
"        \n"
"        QComboBox:hover {\n"
"           background-color: qlineargradient(x1:0, y1:0, x2:1,  y2:0.8,\n"
"                            stop:0 rgb(66, 73, 78),\n"
"                            stop:1 rgb(54, 49, 53));\n"
"\n"
"\n"
"        }")
        self.file_extension_combobox.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.file_extension_combobox.setObjectName("file_extension_combobox")
        self.file_extension_combobox.addItem("")
        self.file_extension_combobox.addItem("")
        self.file_extension_combobox.addItem("")
        self.file_extension_combobox.addItem("")
        self.file_extension_combobox.addItem("")
        self.file_extension_combobox.addItem("")
        self.browse_files_btn = QtWidgets.QPushButton(self.finalization_page)
        self.browse_files_btn.setGeometry(QtCore.QRect(420, 220, 131, 41))
        self.browse_files_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.browse_files_btn.setStyleSheet("QPushButton {\n"
"           background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0.8,\n"
"                            stop:0 rgb(71, 78, 83),\n"
"                            stop:1 rgb(49, 54, 58));\n"
"            border: 1px solid gray;\n"
"            border-radius: 7px;\n"
"            color: #f2f2f2;\n"
"            font-size: 20px;\n"
"        }\n"
"        \n"
"        QPushButton:hover {\n"
"           background-color: qlineargradient(x1:0, y1:0, x2:1,  y2:0.8,\n"
"                            stop:0 rgb(66, 73, 78),\n"
"                            stop:1 rgb(54, 49, 53));\n"
"\n"
"\n"
"        }")
        self.browse_files_btn.setObjectName("browse_files_btn")
        self.label_36 = QtWidgets.QLabel(self.finalization_page)
        self.label_36.setGeometry(QtCore.QRect(80, 130, 491, 521))
        self.label_36.setStyleSheet("QLabel{\n"
"    border:1px solid gray;\n"
"    border-radius:20px;\n"
"    background-color:rgba(20,20,20,255);    \n"
"}\n"
"")
        self.label_36.setText("")
        self.label_36.setObjectName("label_36")
        self.file_name_lineedit = QtWidgets.QLineEdit(self.finalization_page)
        self.file_name_lineedit.setEnabled(True)
        self.file_name_lineedit.setGeometry(QtCore.QRect(100, 160, 301, 41))
        self.file_name_lineedit.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.file_name_lineedit.setMouseTracking(True)
        self.file_name_lineedit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.file_name_lineedit.setStyleSheet("QLineEdit {\n"
"           background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0.8,\n"
"                            stop:0 rgb(71, 78, 83),\n"
"                            stop:1 rgb(49, 54, 58));\n"
"            border: 1px solid gray;\n"
"            border-radius: 7px;\n"
"            color: #f2f2f2;\n"
"            font-size: 20px;\n"
"        }\n"
"        \n"
"        QLineEdit:hover {\n"
"           background-color: qlineargradient(x1:0, y1:0, x2:1,  y2:0.8,\n"
"                            stop:0 rgb(66, 73, 78),\n"
"                            stop:1 rgb(54, 49, 53));\n"
"\n"
"\n"
"        }")
        self.file_name_lineedit.setMaxLength(200)
        self.file_name_lineedit.setAlignment(QtCore.Qt.AlignCenter)
        self.file_name_lineedit.setReadOnly(False)
        self.file_name_lineedit.setObjectName("file_name_lineedit")
        self.file_root_info_label = QtWidgets.QLabel(self.finalization_page)
        self.file_root_info_label.setGeometry(QtCore.QRect(100, 220, 301, 41))
        self.file_root_info_label.setStyleSheet("QLabel{\n"
"    color:rgba(80,80,80,0.9);\n"
"    border:1px solid rgba(80, 80, 80,0.5);\n"
"    border-radius:20px;\n"
"    font:20px;\n"
"    background-color:rgba(20,20,20,255);    \n"
"}\n"
"")
        self.file_root_info_label.setAlignment(QtCore.Qt.AlignCenter)
        self.file_root_info_label.setObjectName("file_root_info_label")
        self.csv_delimiter_combobox = QtWidgets.QComboBox(self.finalization_page)
        self.csv_delimiter_combobox.setGeometry(QtCore.QRect(100, 360, 451, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.csv_delimiter_combobox.setFont(font)
        self.csv_delimiter_combobox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.csv_delimiter_combobox.setStyleSheet("QComboBox {\n"
"           background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0.8,\n"
"                            stop:0 rgb(71, 78, 83),\n"
"                            stop:1 rgb(49, 54, 58));\n"
"            border: 1px solid gray;\n"
"            border-radius: 7px;\n"
"            color: #f2f2f2;\n"
"            font-size: 20px;\n"
"            padding-left:20px;\n"
"        }\n"
"        \n"
"        QComboBox:hover {\n"
"           background-color: qlineargradient(x1:0, y1:0, x2:1,  y2:0.8,\n"
"                            stop:0 rgb(66, 73, 78),\n"
"                            stop:1 rgb(54, 49, 53));\n"
"\n"
"\n"
"        }")
        self.csv_delimiter_combobox.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.csv_delimiter_combobox.setObjectName("csv_delimiter_combobox")
        self.csv_delimiter_combobox.addItem("")
        self.csv_delimiter_combobox.addItem("")
        self.csv_delimiter_combobox.addItem("")
        self.csv_delimiter_combobox.addItem("")
        self.label_38 = QtWidgets.QLabel(self.finalization_page)
        self.label_38.setGeometry(QtCore.QRect(100, 320, 441, 41))
        font = QtGui.QFont()
        font.setFamily("Lucida Grande")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_38.setFont(font)
        self.label_38.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_38.setToolTip("")
        self.label_38.setStyleSheet("color:gray;\n"
"background-color:transparent;")
        self.label_38.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_38.setObjectName("label_38")
        self.customize_excel_options_btn = QtWidgets.QPushButton(self.finalization_page)
        self.customize_excel_options_btn.setGeometry(QtCore.QRect(100, 420, 451, 41))
        self.customize_excel_options_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.customize_excel_options_btn.setStyleSheet("QPushButton {\n"
"           background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0.8,\n"
"                            stop:0 rgb(71, 78, 83),\n"
"                            stop:1 rgb(49, 54, 58));\n"
"            border: 1px solid gray;\n"
"            border-radius: 7px;\n"
"            color: #f2f2f2;\n"
"            font-size: 20px;\n"
"        }\n"
"        \n"
"        QPushButton:hover {\n"
"           background-color: qlineargradient(x1:0, y1:0, x2:1,  y2:0.8,\n"
"                            stop:0 rgb(66, 73, 78),\n"
"                            stop:1 rgb(54, 49, 53));\n"
"\n"
"\n"
"        }")
        self.customize_excel_options_btn.setObjectName("customize_excel_options_btn")
        self.label_39 = QtWidgets.QLabel(self.finalization_page)
        self.label_39.setGeometry(QtCore.QRect(80, 70, 491, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_39.setFont(font)
        self.label_39.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_39.setToolTip("")
        self.label_39.setStyleSheet("color:white;\n"
"font:30px;\n"
"background-color:transparent;")
        self.label_39.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_39.setAlignment(QtCore.Qt.AlignCenter)
        self.label_39.setObjectName("label_39")
        self.create_report_checkbox = QtWidgets.QCheckBox(self.finalization_page)
        self.create_report_checkbox.setGeometry(QtCore.QRect(100, 520, 451, 41))
        self.create_report_checkbox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.create_report_checkbox.setStyleSheet("QCheckBox {\n"
"           background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0.8,\n"
"                            stop:0 rgb(71, 78, 83),\n"
"                            stop:1 rgb(49, 54, 58));\n"
"            border: 1px solid gray;\n"
"            border-radius: 7px;\n"
"            color: #f2f2f2;\n"
"            font-size: 20px;\n"
"            padding-left:15px;\n"
"        }\n"
"        \n"
"        QCheckBox:hover {\n"
"           background-color: qlineargradient(x1:0, y1:0, x2:1,  y2:0.8,\n"
"                            stop:0 rgb(66, 73, 78),\n"
"                            stop:1 rgb(54, 49, 53));\n"
"\n"
"\n"
"        }\n"
"        \n"
"        QCheckBox:focus {\n"
"           background-color: qlineargradient(x1:0, y1:0, x2:1,  y2:0.8,\n"
"                            stop:0 rgb(61, 68, 73),\n"
"                            stop:1 rgb(39, 44, 48));\n"
"\n"
" }\n"
"       \n"
"    QCheckBox QAbstractItemView {\n"
"        border:0px;\n"
"        background-color: #31363A;\n"
"    }\n"
"        \n"
" \n"
"     ")
        self.create_report_checkbox.setObjectName("create_report_checkbox")
        self.export_final_btn = QtWidgets.QPushButton(self.finalization_page)
        self.export_final_btn.setGeometry(QtCore.QRect(339, 580, 211, 41))
        self.export_final_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.export_final_btn.setStyleSheet("QPushButton {\n"
"           \n"
"        background-color: rgba(33, 225, 36,0.5);\n"
"            border: 1px solid gray;\n"
"            border-radius: 7px;\n"
"            color: #f2f2f2;\n"
"            font-size: 20px;\n"
"        }\n"
"QPushButton:hover{\n"
"           \n"
"        background-color: rgba(33, 225, 36,0.2);\n"
"            border: 1px solid gray;\n"
"            border-radius: 7px;\n"
"            color: #f2f2f2;\n"
"            font-size: 20px;\n"
"        }\n"
"")
        self.export_final_btn.setObjectName("export_final_btn")
        self.export_reset_btn = QtWidgets.QPushButton(self.finalization_page)
        self.export_reset_btn.setGeometry(QtCore.QRect(100, 580, 211, 41))
        self.export_reset_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.export_reset_btn.setStyleSheet("QPushButton {\n"
"        \n"
"    background-color: rgba(231, 55, 34,0.2);\n"
"            border: 1px solid gray;\n"
"            border-radius: 7px;\n"
"            color: #f2f2f2;\n"
"            font-size: 20px;\n"
"        }\n"
"        \n"
"QPushButton:hover {\n"
"        \n"
"    background-color: rgba(221, 65, 34,0.5);\n"
"            border: 1px solid gray;\n"
"            border-radius: 7px;\n"
"            color: #f2f2f2;\n"
"            font-size: 20px;\n"
"        }\n"
"        ")
        self.export_reset_btn.setObjectName("export_reset_btn")
        self.line = QtWidgets.QFrame(self.finalization_page)
        self.line.setGeometry(QtCore.QRect(90, 480, 471, 20))
        self.line.setStyleSheet("")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_7 = QtWidgets.QFrame(self.finalization_page)
        self.line_7.setGeometry(QtCore.QRect(90, 290, 471, 20))
        self.line_7.setStyleSheet("")
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.label_40 = QtWidgets.QLabel(self.finalization_page)
        self.label_40.setGeometry(QtCore.QRect(600, 130, 401, 291))
        self.label_40.setStyleSheet("QLabel{\n"
"    border:1px solid gray;\n"
"    border-radius:20px;\n"
"    background-color:rgba(20,20,20,255);    \n"
"}\n"
"")
        self.label_40.setText("")
        self.label_40.setObjectName("label_40")
        self.open_recent_files_combobox = QtWidgets.QComboBox(self.finalization_page)
        self.open_recent_files_combobox.setGeometry(QtCore.QRect(620, 200, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.open_recent_files_combobox.setFont(font)
        self.open_recent_files_combobox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.open_recent_files_combobox.setStyleSheet("QComboBox {\n"
"           background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0.8,\n"
"                            stop:0 rgb(71, 78, 83),\n"
"                            stop:1 rgb(49, 54, 58));\n"
"            border: 1px solid gray;\n"
"            border-radius: 7px;\n"
"            color: #f2f2f2;\n"
"            font-size: 20px;\n"
"            padding-left:20px;\n"
"        }\n"
"        \n"
"        QComboBox:hover {\n"
"           background-color: qlineargradient(x1:0, y1:0, x2:1,  y2:0.8,\n"
"                            stop:0 rgb(66, 73, 78),\n"
"                            stop:1 rgb(54, 49, 53));\n"
"\n"
"\n"
"        }")
        self.open_recent_files_combobox.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.open_recent_files_combobox.setObjectName("open_recent_files_combobox")
        self.open_recent_files_combobox.addItem("")
        self.label_41 = QtWidgets.QLabel(self.finalization_page)
        self.label_41.setGeometry(QtCore.QRect(620, 150, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_41.setFont(font)
        self.label_41.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_41.setToolTip("")
        self.label_41.setStyleSheet("color:white;\n"
"font:20px;\n"
"background-color:transparent;")
        self.label_41.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_41.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_41.setObjectName("label_41")
        self.save_file_btn = QtWidgets.QPushButton(self.finalization_page)
        self.save_file_btn.setGeometry(QtCore.QRect(620, 300, 361, 41))
        self.save_file_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.save_file_btn.setStyleSheet("QPushButton {\n"
"           background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0.8,\n"
"                            stop:0 rgb(71, 78, 83),\n"
"                            stop:1 rgb(49, 54, 58));\n"
"            border: 1px solid gray;\n"
"            border-radius: 7px;\n"
"            color: #f2f2f2;\n"
"            font-size: 20px;\n"
"        }\n"
"        \n"
"        QPushButton:hover {\n"
"           background-color: qlineargradient(x1:0, y1:0, x2:1,  y2:0.8,\n"
"                            stop:0 rgb(66, 73, 78),\n"
"                            stop:1 rgb(54, 49, 53));\n"
"\n"
"\n"
"        }")
        self.save_file_btn.setObjectName("save_file_btn")
        self.undo_last_changes_btn = QtWidgets.QPushButton(self.finalization_page)
        self.undo_last_changes_btn.setGeometry(QtCore.QRect(620, 360, 361, 41))
        self.undo_last_changes_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.undo_last_changes_btn.setStyleSheet("QPushButton {\n"
"           background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0.8,\n"
"                            stop:0 rgb(71, 78, 83),\n"
"                            stop:1 rgb(49, 54, 58));\n"
"            border: 1px solid gray;\n"
"            border-radius: 7px;\n"
"            color: #f2f2f2;\n"
"            font-size: 20px;\n"
"        }\n"
"        \n"
"        QPushButton:hover {\n"
"           background-color: qlineargradient(x1:0, y1:0, x2:1,  y2:0.8,\n"
"                            stop:0 rgb(66, 73, 78),\n"
"                            stop:1 rgb(54, 49, 53));\n"
"\n"
"\n"
"        }")
        self.undo_last_changes_btn.setObjectName("undo_last_changes_btn")
        self.label_44 = QtWidgets.QLabel(self.finalization_page)
        self.label_44.setGeometry(QtCore.QRect(560, 70, 491, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_44.setFont(font)
        self.label_44.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_44.setToolTip("")
        self.label_44.setStyleSheet("color:white;\n"
"font:30px;\n"
"background-color:transparent;")
        self.label_44.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_44.setAlignment(QtCore.Qt.AlignCenter)
        self.label_44.setObjectName("label_44")
        self.line_8 = QtWidgets.QFrame(self.finalization_page)
        self.line_8.setGeometry(QtCore.QRect(610, 260, 381, 20))
        self.line_8.setStyleSheet("")
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.last_file_info_listwidget = QtWidgets.QListWidget(self.finalization_page)
        self.last_file_info_listwidget.setGeometry(QtCore.QRect(610, 520, 381, 131))
        font = QtGui.QFont()
        font.setPointSize(23)
        self.last_file_info_listwidget.setFont(font)
        self.last_file_info_listwidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.last_file_info_listwidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.last_file_info_listwidget.setStyleSheet("QListWidget {\n"
"    color:white;\n"
"    background-color:transparent;\n"
"    outline:0;\n"
"    border:1px gray;\n"
"}\n"
"QListWidget::item {\n"
"    color:gray;\n"
"    background-color:transparent;\n"
"     margin: 3px;\n"
"    border:1px transparent;\n"
"}\n"
"QListWidget::item:selected{\n"
"    background-color:transparent;\n"
"    color:white;\n"
"    border:1px solid #808080;\n"
"}\n"
"\n"
"\n"
"")
        self.last_file_info_listwidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.last_file_info_listwidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.last_file_info_listwidget.setLineWidth(0)
        self.last_file_info_listwidget.setObjectName("last_file_info_listwidget")
        item = QtWidgets.QListWidgetItem()
        self.last_file_info_listwidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.last_file_info_listwidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.last_file_info_listwidget.addItem(item)
        self.label_42 = QtWidgets.QLabel(self.finalization_page)
        self.label_42.setGeometry(QtCore.QRect(600, 500, 401, 151))
        self.label_42.setStyleSheet("QLabel{\n"
"    border:1px solid gray;\n"
"    border-radius:20px;\n"
"    background-color:rgba(20,20,20,255);    \n"
"}\n"
"")
        self.label_42.setText("")
        self.label_42.setObjectName("label_42")
        self.label_43 = QtWidgets.QLabel(self.finalization_page)
        self.label_43.setGeometry(QtCore.QRect(600, 450, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_43.setFont(font)
        self.label_43.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_43.setToolTip("")
        self.label_43.setStyleSheet("color:white;\n"
"font:30px;\n"
"background-color:transparent;")
        self.label_43.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_43.setAlignment(QtCore.Qt.AlignCenter)
        self.label_43.setObjectName("label_43")
        self.label_35.raise_()
        self.label_42.raise_()
        self.label_36.raise_()
        self.file_extension_combobox.raise_()
        self.browse_files_btn.raise_()
        self.file_name_lineedit.raise_()
        self.file_root_info_label.raise_()
        self.csv_delimiter_combobox.raise_()
        self.label_38.raise_()
        self.customize_excel_options_btn.raise_()
        self.label_39.raise_()
        self.create_report_checkbox.raise_()
        self.export_final_btn.raise_()
        self.export_reset_btn.raise_()
        self.line.raise_()
        self.line_7.raise_()
        self.label_40.raise_()
        self.open_recent_files_combobox.raise_()
        self.label_41.raise_()
        self.save_file_btn.raise_()
        self.undo_last_changes_btn.raise_()
        self.label_44.raise_()
        self.line_8.raise_()
        self.last_file_info_listwidget.raise_()
        self.label_43.raise_()
        self.main_stacked_widget.addWidget(self.finalization_page)
        self.settings_page = QtWidgets.QWidget()
        self.settings_page.setObjectName("settings_page")
        self.label_45 = QtWidgets.QLabel(self.settings_page)
        self.label_45.setGeometry(QtCore.QRect(40, 40, 1001, 641))
        self.label_45.setStyleSheet("QLabel{\n"
"    border:2px red;\n"
"    border-radius:20px;\n"
"    background-color:rgba(20,20,20,255);    \n"
"}")
        self.label_45.setText("")
        self.label_45.setObjectName("label_45")
        self.label_46 = QtWidgets.QLabel(self.settings_page)
        self.label_46.setGeometry(QtCore.QRect(90, 140, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_46.setFont(font)
        self.label_46.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_46.setToolTip("")
        self.label_46.setStyleSheet("color:rgba(255,255,255,0.9);\n"
"font:30px;\n"
"background-color:transparent;")
        self.label_46.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_46.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_46.setObjectName("label_46")
        self.app_version_info_label = QtWidgets.QLabel(self.settings_page)
        self.app_version_info_label.setGeometry(QtCore.QRect(90, 180, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.app_version_info_label.setFont(font)
        self.app_version_info_label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.app_version_info_label.setToolTip("")
        self.app_version_info_label.setStyleSheet("color:gray;\n"
"font:25px;\n"
"background-color:transparent;")
        self.app_version_info_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.app_version_info_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.app_version_info_label.setObjectName("app_version_info_label")
        self.label_48 = QtWidgets.QLabel(self.settings_page)
        self.label_48.setGeometry(QtCore.QRect(90, 260, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_48.setFont(font)
        self.label_48.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_48.setToolTip("")
        self.label_48.setStyleSheet("color:rgba(255,255,255,0.9);\n"
"font:30px;\n"
"background-color:transparent;")
        self.label_48.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_48.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_48.setObjectName("label_48")
        self.support_info_label = QtWidgets.QLabel(self.settings_page)
        self.support_info_label.setGeometry(QtCore.QRect(90, 300, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.support_info_label.setFont(font)
        self.support_info_label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.support_info_label.setToolTip("")
        self.support_info_label.setStyleSheet("color:gray;\n"
"font:25px;\n"
"background-color:transparent;")
        self.support_info_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.support_info_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.support_info_label.setObjectName("support_info_label")
        self.github_info_label = QtWidgets.QLabel(self.settings_page)
        self.github_info_label.setGeometry(QtCore.QRect(90, 420, 391, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.github_info_label.setFont(font)
        self.github_info_label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.github_info_label.setToolTip("")
        self.github_info_label.setStyleSheet("color:gray;\n"
"font:25px;\n"
"background-color:transparent;")
        self.github_info_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.github_info_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.github_info_label.setObjectName("github_info_label")
        self.label_51 = QtWidgets.QLabel(self.settings_page)
        self.label_51.setGeometry(QtCore.QRect(90, 380, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_51.setFont(font)
        self.label_51.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_51.setToolTip("")
        self.label_51.setStyleSheet("color:rgba(255,255,255,0.9);\n"
"font:30px;\n"
"background-color:transparent;")
        self.label_51.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_51.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_51.setObjectName("label_51")
        self.developer_info_label = QtWidgets.QLabel(self.settings_page)
        self.developer_info_label.setGeometry(QtCore.QRect(90, 540, 391, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.developer_info_label.setFont(font)
        self.developer_info_label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.developer_info_label.setToolTip("")
        self.developer_info_label.setStyleSheet("color:gray;\n"
"font:25px;\n"
"background-color:transparent;")
        self.developer_info_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.developer_info_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.developer_info_label.setObjectName("developer_info_label")
        self.label_53 = QtWidgets.QLabel(self.settings_page)
        self.label_53.setGeometry(QtCore.QRect(90, 500, 351, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_53.setFont(font)
        self.label_53.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_53.setToolTip("")
        self.label_53.setStyleSheet("color:rgba(255,255,255,0.9);\n"
"font:30px;\n"
"background-color:transparent;")
        self.label_53.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_53.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_53.setObjectName("label_53")
        self.privacy_policy_btn = QtWidgets.QPushButton(self.settings_page)
        self.privacy_policy_btn.setGeometry(QtCore.QRect(710, 210, 271, 41))
        self.privacy_policy_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.privacy_policy_btn.setStyleSheet("QPushButton{\n"
"    font:25px;\n"
"    color: rgb(167, 104, 224);\n"
"    background-color:transparent;\n"
"    border:1px solid rgb(216, 106, 195);\n"
"}\n"
"")
        self.privacy_policy_btn.setObjectName("privacy_policy_btn")
        self.auto_backup_btn = QtWidgets.QPushButton(self.settings_page)
        self.auto_backup_btn.setGeometry(QtCore.QRect(710, 150, 271, 41))
        self.auto_backup_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.auto_backup_btn.setStyleSheet("""QPushButton{
                font:25px;
                color:rgba(0,255,0,0.7);
                border:1px solid rgba(0,255,0,0.7);
                }""")
        self.auto_backup_btn.setObjectName("auto_backup_btn")
        self.main_stacked_widget.addWidget(self.settings_page)
        self.overview_btn = QtWidgets.QPushButton(Form)
        self.overview_btn.setGeometry(QtCore.QRect(-10, 110, 301, 81))
        font = QtGui.QFont()
        font.setFamily(".Lucida Grande UI")
        font.setPointSize(23)
        self.overview_btn.setFont(font)
        self.overview_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.overview_btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.overview_btn.setStyleSheet("QPushButton{\n"
"    background-color:transparent;\n"
"    color:white;\n"
"    border-color:1px transparent ;\n"
"    border-radius:20px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:rgba(30,30,30,240);\n"
"    color:white;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/menu/icons/overview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.overview_btn.setIcon(icon)
        self.overview_btn.setIconSize(QtCore.QSize(35, 35))
        self.overview_btn.setCheckable(False)
        self.overview_btn.setObjectName("overview_btn")
        self.preprosessing_btn = QtWidgets.QPushButton(Form)
        self.preprosessing_btn.setGeometry(QtCore.QRect(-10, 210, 301, 81))
        font = QtGui.QFont()
        font.setFamily(".Lucida Grande UI")
        font.setPointSize(23)
        self.preprosessing_btn.setFont(font)
        self.preprosessing_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.preprosessing_btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.preprosessing_btn.setStyleSheet("QPushButton{\n"
"    background-color:transparent;\n"
"    color:white;\n"
"    border-color:1px transparent ;\n"
"    border-radius:20px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:rgba(30,30,30,240);\n"
"    color:white;\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/menu/icons/filter.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.preprosessing_btn.setIcon(icon1)
        self.preprosessing_btn.setIconSize(QtCore.QSize(35, 35))
        self.preprosessing_btn.setCheckable(False)
        self.preprosessing_btn.setObjectName("preprosessing_btn")
        self.tranformation_btn = QtWidgets.QPushButton(Form)
        self.tranformation_btn.setGeometry(QtCore.QRect(-10, 310, 301, 81))
        font = QtGui.QFont()
        font.setFamily(".Lucida Grande UI")
        font.setPointSize(23)
        self.tranformation_btn.setFont(font)
        self.tranformation_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tranformation_btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tranformation_btn.setStyleSheet("QPushButton{\n"
"    background-color:transparent;\n"
"    color:white;\n"
"    border-color:1px transparent ;\n"
"    border-radius:20px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:rgba(30,30,30,240);\n"
"    color:white;\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/menu/icons/scale.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tranformation_btn.setIcon(icon2)
        self.tranformation_btn.setIconSize(QtCore.QSize(35, 35))
        self.tranformation_btn.setCheckable(False)
        self.tranformation_btn.setObjectName("tranformation_btn")
        self.statistics_btn = QtWidgets.QPushButton(Form)
        self.statistics_btn.setGeometry(QtCore.QRect(-10, 410, 301, 81))
        font = QtGui.QFont()
        font.setFamily(".Lucida Grande UI")
        font.setPointSize(23)
        self.statistics_btn.setFont(font)
        self.statistics_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.statistics_btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.statistics_btn.setStyleSheet("QPushButton{\n"
"    background-color:transparent;\n"
"    color:white;\n"
"    border-color:1px transparent ;\n"
"    border-radius:20px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:rgba(30,30,30,240);\n"
"    color:white;\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/menu/icons/statistics.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.statistics_btn.setIcon(icon3)
        self.statistics_btn.setIconSize(QtCore.QSize(35, 35))
        self.statistics_btn.setCheckable(False)
        self.statistics_btn.setObjectName("statistics_btn")
        self.settings_btn = QtWidgets.QPushButton(Form)
        self.settings_btn.setGeometry(QtCore.QRect(-30, 660, 301, 81))
        font = QtGui.QFont()
        font.setFamily(".Lucida Grande UI")
        font.setPointSize(23)
        self.settings_btn.setFont(font)
        self.settings_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.settings_btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.settings_btn.setStyleSheet("QPushButton{\n"
"    background-color:transparent;\n"
"    color:white;\n"
"    border-color:1px transparent ;\n"
"    border-radius:20px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:rgba(30,30,30,240);\n"
"    color:white;\n"
"}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/menu/icons/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settings_btn.setIcon(icon4)
        self.settings_btn.setIconSize(QtCore.QSize(35, 35))
        self.settings_btn.setCheckable(False)
        self.settings_btn.setObjectName("settings_btn")
        self.finalization_btn = QtWidgets.QPushButton(Form)
        self.finalization_btn.setGeometry(QtCore.QRect(-10, 510, 301, 81))
        font = QtGui.QFont()
        font.setFamily(".Lucida Grande UI")
        font.setPointSize(23)
        self.finalization_btn.setFont(font)
        self.finalization_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.finalization_btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.finalization_btn.setStyleSheet("QPushButton{\n"
"    background-color:transparent;\n"
"    color:white;\n"
"    border-color:1px transparent ;\n"
"    border-radius:20px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:rgba(30,30,30,240);\n"
"    color:white;\n"
"}")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/menu/icons/export.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.finalization_btn.setIcon(icon5)
        self.finalization_btn.setIconSize(QtCore.QSize(35, 35))
        self.finalization_btn.setCheckable(False)
        self.finalization_btn.setObjectName("finalization_btn")
        self.orta_xett = QtWidgets.QFrame(Form)
        self.orta_xett.setGeometry(QtCore.QRect(20, 625, 251, 1))
        self.orta_xett.setStyleSheet("background-color:rgba(255,255,255,0.5)")
        self.orta_xett.setLineWidth(0)
        self.orta_xett.setFrameShape(QtWidgets.QFrame.HLine)
        self.orta_xett.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.orta_xett.setObjectName("orta_xett")
        self.line_1 = QtWidgets.QFrame(Form)
        self.line_1.setEnabled(True)
        self.line_1.setGeometry(QtCore.QRect(-3, 110, 10, 81))
        self.line_1.setStyleSheet("background-color:transparent;\n"
"border-color:transparent;\n"
"border-radius:5px;")
        self.line_1.setLineWidth(0)
        self.line_1.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_1.setObjectName("line_1")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(-3, 210, 10, 81))
        self.line_2.setStyleSheet("background-color:transparent;\n"
"color:white;\n"
"border-color:transparent;\n"
"border-radius:5px;")
        self.line_2.setLineWidth(0)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setGeometry(QtCore.QRect(-3, 310, 10, 81))
        self.line_3.setStyleSheet("background-color:transparent;\n"
"color:white;\n"
"border-color:transparent;\n"
"border-radius:5px;")
        self.line_3.setLineWidth(0)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(Form)
        self.line_4.setGeometry(QtCore.QRect(-3, 410, 10, 81))
        self.line_4.setStyleSheet("background-color:transparent;\n"
"color:white;\n"
"border-color:transparent;\n"
"border-radius:5px;")
        self.line_4.setLineWidth(0)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(Form)
        self.line_5.setGeometry(QtCore.QRect(-3, 510, 10, 81))
        self.line_5.setStyleSheet("background-color:transparent;\n"
"color:white;\n"
"border-color:transparent;\n"
"border-radius:5px;")
        self.line_5.setLineWidth(0)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(Form)
        self.line_6.setGeometry(QtCore.QRect(-3, 660, 10, 81))
        self.line_6.setStyleSheet("background-color:transparent;\n"
"color:white;\n"
"border-color:transparent;\n"
"border-radius:5px;")
        self.line_6.setLineWidth(0)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.purelyzer_logo = QtWidgets.QLabel(Form)
        self.purelyzer_logo.setGeometry(QtCore.QRect(30, 40, 251, 61))
        self.purelyzer_logo.setText("")
        self.purelyzer_logo.setPixmap(QtGui.QPixmap(":/logo/logo-no-background.png"))
        self.purelyzer_logo.setScaledContents(True)
        self.purelyzer_logo.setObjectName("purelyzer_logo")

        self.retranslateUi(Form)
        self.missing_v_stacked.setCurrentIndex(0)
        self.sql_query_area_stacked_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Purelyzer Data Cleaning Tool"))
        self.label.setText(_translate("Form", "Data summary"))
        __sortingEnabled = self.general_overview_listwidget.isSortingEnabled()
        self.general_overview_listwidget.setSortingEnabled(False)
        self.general_overview_listwidget.setSortingEnabled(__sortingEnabled)
        self.label_4.setText(_translate("Form", "Missing values "))
        self.remove_mv_btn.setText(_translate("Form", "Remove missing values"))
        self.fill_missing_v_btn.setText(_translate("Form", "Fill missing values"))
        self.median_radiobtn.setText(_translate("Form", "Median"))
        self.label_5.setText(_translate("Form", "Select the option you want to fill"))
        self.average_radiobtn.setText(_translate("Form", "Average"))
        self.sequential_radiobtn.setText(_translate("Form", " Sequential Forward Loading"))
        self.mod_radiobtn.setText(_translate("Form", "Mod"))
        self.custom_v_lineedit.setPlaceholderText(_translate("Form", "Type custom value.."))
        self.fill_mv_done_btn.setText(_translate("Form", "Done"))
        self.cancel_fill_mv_btn.setText(_translate("Form", "Cancel"))
        self.done_remove_mv_btn.setText(_translate("Form", "Done"))
        self.column_remove_mv_btn.setText(_translate("Form", "Column"))
        self.label_7.setText(_translate("Form", "Select the item with missing data that you want to delete"))
        self.row_remove_mv_btn.setText(_translate("Form", "Row"))
        self.full_null_radiobtn.setText(_translate("Form", "Entirely NULL Row/Column"))
        self.cancel_remove_mv_btn.setText(_translate("Form", "Cancel"))
        self.label_14.setText(_translate("Form", "Duplicate values"))
        self.remove_dup_btn.setText(_translate("Form", "Remove duplicates"))
        self.show_in_table_btn.setText(_translate("Form", "View duplicates"))
        self.label_11.setText(_translate("Form", "Custom SQL query for filtering data"))
        self.prompt_done_btn.setText(_translate("Form", "Done"))
        self.prompt_reset_btn.setText(_translate("Form", "Reset"))
        self.promp_back_btn.setText(_translate("Form", "Back"))
        self.sql_text_area.setPlaceholderText(_translate("Form", "Write an SQL query for your data.."))
        self.pre_pros_chart_area.setText(_translate("Form", "There is no plotted chart!"))
        self.dataset_cb.setItemText(0, _translate("Form", "Filtered data"))
        self.label_15.setText(_translate("Form", "Dataset:"))
        self.label_16.setText(_translate("Form", "X-Axis:"))
        self.x_axis_cb.setItemText(0, _translate("Form", "x axis"))
        self.label_17.setText(_translate("Form", "Y-Axis"))
        self.y_axis_cb.setItemText(0, _translate("Form", "y axis"))
        self.label_18.setText(_translate("Form", "Chart type:"))
        self.chart_type_cb.setItemText(0, _translate("Form", "Line chart"))
        self.chart_type_cb.setItemText(1, _translate("Form", "Bar chart"))
        self.chart_type_cb.setItemText(2, _translate("Form", "Scatter plot"))
        self.chart_type_cb.setItemText(3, _translate("Form", "Histogram"))
        self.chart_type_cb.setItemText(4, _translate("Form", "Box plot"))
        self.chart_type_cb.setItemText(5, _translate("Form", "Pie chart"))
        self.show_gridline_checkBox.setText(_translate("Form", "Show gridlines"))
        self.chart_color_btn.setText(_translate("Form", "Choos chart color"))
        self.plot_chart_btn.setText(_translate("Form", "Plot chart"))
        self.label_20.setText(_translate("Form", "Data Scaling & Normalization"))
        self.z_score_radio_btn.setText(_translate("Form", "   Z-score normalization"))
        self.min_max_radio_btn.setText(_translate("Form", "   Min-max scaling"))
        self.minvalue_lineedit.setPlaceholderText(_translate("Form", "Min value"))
        self.maxvalue_lineedit.setPlaceholderText(_translate("Form", "Max value"))
        self.scaling_column_box.setItemText(0, _translate("Form", "Column 1"))
        self.scaling_apply_btn.setText(_translate("Form", "Apply scaling"))
        self.add_rempve_column_btn.setText(_translate("Form", "Add && Remove column"))
        self.add_and_remove_row_btn.setText(_translate("Form", "Add && Remove row"))
        self.merge_columns_btn.setText(_translate("Form", "Merge Columns"))
        self.label_21.setText(_translate("Form", "Data Enhancement"))
        self.label_22.setText(_translate("Form", "Change Columns Data Type"))
        self.label_23.setText(_translate("Form", "Select Column "))
        self.change_dt_select_column.setItemText(0, _translate("Form", "Column 1"))
        self.label_28.setText(_translate("Form", "Select New Data Type"))
        self.select_new_data_type.setItemText(0, _translate("Form", "Integer"))
        self.select_new_data_type.setItemText(1, _translate("Form", "Float"))
        self.select_new_data_type.setItemText(2, _translate("Form", "String"))
        self.select_new_data_type.setItemText(3, _translate("Form", "Boolean"))
        self.select_new_data_type.setItemText(4, _translate("Form", "Date"))
        self.data_type_apply_changes.setText(_translate("Form", "Apply changes "))
        self.label_31.setText(_translate("Form", "Summary of changes"))
        __sortingEnabled = self.summary_of_changes_listwidget.isSortingEnabled()
        self.summary_of_changes_listwidget.setSortingEnabled(False)
        item = self.summary_of_changes_listwidget.item(0)
        item.setText(_translate("Form", "No changes is there!"))
        self.summary_of_changes_listwidget.setSortingEnabled(__sortingEnabled)
        self.label_32.setText(_translate("Form", "Pixmap Plot Area "))
        self.frequency_btn.setText(_translate("Form", "Frequency Distribution"))
        self.correlation_btn.setText(_translate("Form", "Correlation Matrix"))
        self.outliers_btn.setText(_translate("Form", "Outliers Dedection"))
        self.label_34.setText(_translate("Form", "Statistical Analysis Tools"))
        self.value_counts_btn.setText(_translate("Form", "Value Counts"))
        self.histograms_btn.setText(_translate("Form", "Histograms"))
        self.distribution_btn.setText(_translate("Form", "Distribution Plot"))
        self.file_extension_combobox.setItemText(0, _translate("Form", ".csv"))
        self.file_extension_combobox.setItemText(1, _translate("Form", ".xlx"))
        self.file_extension_combobox.setItemText(2, _translate("Form", ".xlsx"))
        self.file_extension_combobox.setItemText(3, _translate("Form", ".json"))
        self.file_extension_combobox.setItemText(4, _translate("Form", ".xml"))
        self.file_extension_combobox.setItemText(5, _translate("Form", ".txt"))
        self.browse_files_btn.setText(_translate("Form", "Browse"))
        self.file_name_lineedit.setPlaceholderText(_translate("Form", "File name"))
        self.file_root_info_label.setText(_translate("Form", "/Desktop"))
        self.csv_delimiter_combobox.setItemText(0, _translate("Form", "Comma ( , )"))
        self.csv_delimiter_combobox.setItemText(1, _translate("Form", "Semicolon ( ; )"))
        self.csv_delimiter_combobox.setItemText(2, _translate("Form", "Tab ( / )"))
        self.csv_delimiter_combobox.setItemText(3, _translate("Form", "Pipe ( | )"))
        self.label_38.setText(_translate("Form", "*Choose CSV Delimiter"))
        self.customize_excel_options_btn.setText(_translate("Form", "Customize Excel Options (.xlx/.xlxs)"))
        self.label_39.setText(_translate("Form", "Export options"))
        self.create_report_checkbox.setText(_translate("Form", "  Create Report File"))
        self.export_final_btn.setText(_translate("Form", "EXPORT"))
        self.export_reset_btn.setText(_translate("Form", "RESET"))
        self.open_recent_files_combobox.setItemText(0, _translate("Form", "untitled.csv"))
        self.label_41.setText(_translate("Form", "Open Recent Files"))
        self.save_file_btn.setText(_translate("Form", "Save file"))
        self.undo_last_changes_btn.setText(_translate("Form", "Undo Last changes"))
        self.label_44.setText(_translate("Form", "Other options"))
        __sortingEnabled = self.last_file_info_listwidget.isSortingEnabled()
        self.last_file_info_listwidget.setSortingEnabled(False)
        item = self.last_file_info_listwidget.item(0)
        item.setText(_translate("Form", "Row count : 1234567"))
        item = self.last_file_info_listwidget.item(1)
        item.setText(_translate("Form", "Column count : 12345678"))
        item = self.last_file_info_listwidget.item(2)
        item.setText(_translate("Form", "File size : 100 gb"))
        self.last_file_info_listwidget.setSortingEnabled(__sortingEnabled)
        self.label_43.setText(_translate("Form", "Last File Summary"))
        self.label_46.setText(_translate("Form", "App Version"))
        self.app_version_info_label.setText(_translate("Form", "v1.0.0"))
        self.label_48.setText(_translate("Form", "Support or Contact"))
        self.support_info_label.setText(_translate("Form", "infopurelyzer@gmail.com"))
        self.github_info_label.setText(_translate("Form", "github.com/gcosx-js/purelyzer-app"))
        self.label_51.setText(_translate("Form", "Github"))
        self.developer_info_label.setText(_translate("Form", "Elmir Guliyev"))
        self.label_53.setText(_translate("Form", "Developing and Desing"))
        self.privacy_policy_btn.setText(_translate("Form", "Privacy && Policy"))
        self.auto_backup_btn.setText(_translate("Form", "Auto Save Log : ON"))
        self.overview_btn.setText(_translate("Form", "  Data Overview  "))
        self.preprosessing_btn.setText(_translate("Form", "  Preprosessing   "))
        self.tranformation_btn.setText(_translate("Form", "  Transformation "))
        self.statistics_btn.setText(_translate("Form", "  Statistics          "))
        self.settings_btn.setText(_translate("Form", "  Settings      "))
        self.finalization_btn.setText(_translate("Form", "  Finalization      "))
        self.main_stacked_widget.setCurrentIndex(0)
        
        self.overview_btn.setStyleSheet("""QPushButton{
	background-color:rgba(40,40,40,255);
	color:white;
	border-color:1px transparent ;
	border-radius:20px;
}
QPushButton:hover{
	background-color:rgba(40,40,40,255);
	color:white;
}""")
        self.line_1.setStyleSheet('''background-color:white;
color:white;
border-color:transparent;
border-radius:5px;''')
        self.privacy_policy_btn.clicked.connect(self.show_text)
        self.missing_v_stacked.setCurrentIndex(0)
        self.remove_mv_btn.clicked.connect(lambda:self.missing_v_stacked.setCurrentIndex(2))
        self.fill_missing_v_btn.clicked.connect(lambda:self.missing_v_stacked.setCurrentIndex(1))
        self.cancel_fill_mv_btn.clicked.connect(lambda:self.missing_v_stacked.setCurrentIndex(0))
        self.cancel_remove_mv_btn.clicked.connect(lambda:self.missing_v_stacked.setCurrentIndex(0))
        
        self.leftbuttons_dict = {self.overview_btn:0,
                                      self.preprosessing_btn:1,
                                      self.tranformation_btn:2,
                                      self.statistics_btn:3,
                                      self.finalization_btn:4,
                                      self.settings_btn:5}
            
        self.leftlines_dict = {self.line_1:1,
                                   self.line_2:2,
                                   self.line_3:3,
                                   self.line_4:4,
                                   self.line_5:5,
                                   self.line_6:6
                                   }

            
        for button in self.leftbuttons_dict.keys():
                button.clicked.connect(self.leftbuttons_clicked)
    def leftbuttons_clicked(self,call=False):
        clicked_button = self.sender()
        btn_index = self.leftbuttons_dict.get(clicked_button)
        self.main_stacked_widget.setCurrentIndex(btn_index)
        
        clicked_button.setStyleSheet("""QPushButton{
	background-color:rgba(40,40,40,255);
	color:white;
	border-color:1px transparent ;
	border-radius:20px;
}
QPushButton:hover{
	background-color:rgba(40,40,40,255);
	color:white;
}""")
        target_line= next((k for k, v in self.leftlines_dict.items() if v == btn_index+1), None)
        target_line.setStyleSheet('''background-color:white;
color:white;
border-color:transparent;
border-radius:5px;''')
        for i in self.leftbuttons_dict:
            if i!=clicked_button:
                i.setStyleSheet("""QPushButton{
	background-color:transparent;
	color:white;
	border-color:1px transparent ;
	border-radius:20px;
}
QPushButton:hover{
	background-color:rgba(30,30,30,240);
	color:white;
}""")
        for i in self.leftlines_dict:
            if i!=target_line:
                i.setStyleSheet("""background-color:transparent;
color:white;
border-color:transparent;
border-radius:5px;""")
                
                
            #point
            
            self.min_max_radio_btn.clicked.connect(self.min_max_rb_clckd)     
               
    def min_max_rb_clckd(self):
            self.minvalue_lineedit.setEnabled(True)
            self.maxvalue_lineedit.setEnabled(True)
            self.minvalue_lineedit.setStyleSheet("""QLineEdit {
           background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0.8,
                            stop:0 rgb(71, 78, 83),
                            stop:1 rgb(49, 54, 58));
            border: 1px solid white;
            border-radius: 7px;
            color: #f2f2f2;
            font-size: 20px;
        }
        
        QLineEdit:hover {
           background-color: qlineargradient(x1:0, y1:0, x2:1,  y2:0.8,
                            stop:0 rgb(66, 73, 78),
                            stop:1 rgb(54, 49, 53));


        }""")
            self.maxvalue_lineedit.setStyleSheet("""QLineEdit {
           background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0.8,
                            stop:0 rgb(71, 78, 83),
                            stop:1 rgb(49, 54, 58));
            border: 1px solid white;
            border-radius: 7px;
            color: #f2f2f2;
            font-size: 20px;
        }
        
        QLineEdit:hover {
           background-color: qlineargradient(x1:0, y1:0, x2:1,  y2:0.8,
                            stop:0 rgb(66, 73, 78),
                            stop:1 rgb(54, 49, 53));


        }""")
            
            
            
            self.z_score_radio_btn.clicked.connect(self.z_score_rb_clcked)
    def z_score_rb_clcked(self):
        self.minvalue_lineedit.setEnabled(False)
        self.minvalue_lineedit.setText('')
        self.maxvalue_lineedit.setText('')
        self.maxvalue_lineedit.setEnabled(False)
        self.minvalue_lineedit.setStyleSheet("""QLineEdit {
           background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0.8,
                            stop:0 rgb(71, 78, 83),
                            stop:1 rgb(49, 54, 58));
            border: 1px solid gray;
            border-radius: 7px;
            color: #f2f2f2;
            font-size: 20px;
        }
        
        QLineEdit:hover {
           background-color: qlineargradient(x1:0, y1:0, x2:1,  y2:0.8,
                            stop:0 rgb(66, 73, 78),
                            stop:1 rgb(54, 49, 53));


        }""")
        self.maxvalue_lineedit.setStyleSheet("""QLineEdit {
           background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0.8,
                            stop:0 rgb(71, 78, 83),
                            stop:1 rgb(49, 54, 58));
            border: 1px solid gray;
            border-radius: 7px;
            color: #f2f2f2;
            font-size: 20px;
        }
        
        QLineEdit:hover {
           background-color: qlineargradient(x1:0, y1:0, x2:1,  y2:0.8,
                            stop:0 rgb(66, 73, 78),
                            stop:1 rgb(54, 49, 53));


        }""")    
        
    def show_text(self):
                msg=QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle('Purelyzer | Privacy and Policy')
                msg.setText('''1. Data Collection

Our Tool operates locally on your device and does not collect or transmit any personal data to external servers. The data you import into the Tool is solely processed and stored on your local device. We do not access, collect, or retain any data unless explicitly shared with us for support or troubleshooting purposes.

2. Data Usage

All data imported into the Tool is used strictly for the purpose of data cleaning, transformation, and analysis. The Tool provides functionality such as handling missing data, removing duplicates, and performing statistical analysis, but no data is shared, collected, or sent externally unless initiated by you.

3. Data Security

Because your data remains on your local device, its security depends on the safeguards you have in place. We recommend following best practices for data protection, such as securing your device with strong passwords and using encryption if needed. We are not responsible for any data loss, theft, or unauthorized access that occurs outside of the Tool’s functionality.

4. Third-Party Services

The Tool does not integrate with third-party services or platforms that may access your data. All operations are handled within the Tool itself.''')
                
                msg.setStandardButtons(QMessageBox.Ok)
                resp = msg.exec_()
                
                
        
        
import icons_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
