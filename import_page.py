import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
import binary  as bin
import funcs as f
import os,logging,pickle
from main import PurelyzerApp
print('OK')
class ImportPage_UI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("Dataset Import Page")
        self.manager = bin.BinaryFileManager()
        
        self.setStyleSheet("""
            QWidget {
                background-color: #2E2E2E;
                color: white;
                font-size: 14px;
            }
            QLineEdit, QComboBox, QPushButton, QSpinBox {
                background-color: #4E4E4E;
                color: white;
                border: 1px solid #FFFFFF;
                padding: 5px;
            }
            QPushButton:hover{
                background-color: #4E4E5E;
                border-color:black;
            }
            QLabel {
                color: #FFFFFF;
            }
            QRadioButton {
                color: white;
            }
            QCheckBox {
                color: white;
            }
        """)
        self.file_format_label = QLabel("What is the file format?")
        self.file_format_combo = QComboBox()
        self.file_format_combo.addItems(["CSV", "Excel", "JSON"])
        self.delimiter_label = QLabel("What is the delimiter?")
        self.delimiter_input = QLineEdit()
        self.delimiter_input.setPlaceholderText("E.g.: ',', ';', '|' (leave empyt for delimited data)")
        self.header_label = QLabel("Does the first row contain column headers?")
        self.header_yes = QRadioButton("Yes")
        self.header_no = QRadioButton("No")
        self.header_group = QButtonGroup()
        self.header_group.addButton(self.header_yes)
        self.header_group.addButton(self.header_no)
        self.columns_label = QLabel("Which columns range do you want to read?")
        self.columns_input = QLineEdit()
        self.columns_input.setPlaceholderText("E.g.: 3-10 or leave empty for all")

        self.missing_value_label = QLabel("Is there a placeholder for missing values?")
        self.missing_value_input = QLineEdit()
        self.missing_value_input.setPlaceholderText("E.g.: NA, ?, None or leave for empyt for all")
        self.skip_rows_input=QLineEdit()
        self.skip_rows_input.setPlaceholderText('E.g. : 3 (The first 3 rows will skip) ')
        self.skip_row_label=QLabel('How many rows do you want to skip? ')
        self.rows_label = QLabel("How many rows do you want to read (leave empty for all)?")
        self.rows_input = QLineEdit()
        self.rows_input.setPlaceholderText('E.g. : 250 ')
        self.date_convert_label = QLabel("Should date columns be automatically converted?")
        self.date_convert_checkbox = QCheckBox("Yes")
        self.manager = bin.BinaryFileManager()
        self.encoding_label = QLabel("What is the character encoding?")
        self.encoding_input = QLineEdit()
        self.encoding_input.setPlaceholderText("E.g.: utf-8, latin1 or leave empty for default")
        self.done_btn=QPushButton('Done import')
        self.recent_datasets_label = QLabel("Recent Datasets")
        self.recent_datasets_combo = QComboBox()
        self.recent_datasets_combo.addItem('None')
        self.list_recent_datasets = self.manager.fetch_data_list()
        for i in self.list_recent_datasets:
            j= os.path.basename(i[0])
            self.recent_datasets_combo.addItem(j)
        self.browse_file_btn=QPushButton('Browse for dataset file')
        self.browse_file_btn.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
        layout = QVBoxLayout()
        layout.addWidget(self.browse_file_btn)
        layout.addWidget(self.recent_datasets_label)
        layout.addWidget(self.recent_datasets_combo)
        layout.addWidget(self.file_format_label)
        layout.addWidget(self.file_format_combo)
        layout.addWidget(self.delimiter_label)
        layout.addWidget(self.delimiter_input)
        layout.addWidget(self.header_label)
        layout.addWidget(self.header_yes)
        layout.addWidget(self.header_no)
        layout.addWidget(self.columns_label)
        layout.addWidget(self.columns_input)
        layout.addWidget(self.missing_value_label)
        layout.addWidget(self.missing_value_input)
        layout.addWidget(self.rows_label)
        layout.addWidget(self.rows_input)
        layout.addWidget(self.skip_row_label)
        layout.addWidget(self.skip_rows_input)
        layout.addWidget(self.date_convert_label)
        layout.addWidget(self.date_convert_checkbox)
        layout.addWidget(self.encoding_label)
        layout.addWidget(self.encoding_input)
        
        layout.addWidget(self.done_btn)
        self.setLayout(layout)
        self.done_btn.clicked.connect(self.finish_with_options)
        self.recent_datasets_combo.currentIndexChanged.connect(self.finish_with_recent)
        self.browse_file_btn.clicked.connect(self.browse_file)
        
        
    def browse_file(self):
        options = "CSV files (*.csv);;JSON files (*.json);;Excel files (*.xls *.xlsx)"
        self.browsed_file_path, _ = QFileDialog.getOpenFileName(self, "Select a file", "", options)
        if self.browsed_file_path!='' and (self.browsed_file_path.endswith('.csv') or
                                           self.browsed_file_path.endswith('.json') or 
                                           self.browsed_file_path.endswith('.xlx') or 
                                           self.browsed_file_path.endswith('.xlsx')):
            base_path=os.path.basename(self.browsed_file_path)
            for i in self.manager.fetch_data_list():
                if i[0]==base_path:
                    self.finish_with_recent(opt=base_path)
                    break
            self.browse_file_btn.setText(base_path)
        else:
            QMessageBox.warning(self,'Error','Please choose a file for import!')
         
        
    def finish_with_recent(self,opt=False):
        if type(opt)==int:
            
            if self.recent_datasets_combo.currentText() !='None':
                resp=f.fmessagebox(f'Do you want to import {self.recent_datasets_combo.currentText()} and also import options?',
                                    'Confirmation',
                                    QMessageBox.Question,
                                    QMessageBox.Yes|QMessageBox.No)
                if resp==QMessageBox.Yes:
                    for i in self.manager.fetch_data_list():
                        if i[0]==self.recent_datasets_combo.currentText():
                            with open("data.pkl", "wb") as file:
                                pickle.dump(i, file)
                                print(i)
                            break
                    
                    self.new_ui=PurelyzerApp()   
                    self.new_ui.show()
                    self.close()
                    
                    
                else:
                    self.recent_datasets_combo.setCurrentIndex(0)
        elif opt and opt!=1:
            resp=f.fmessagebox(f'{opt} has import options in database, click "YES" for use. Else, click "NO" for replace with your new import options!',
                                    'Confirmation',
                                    QMessageBox.Question,
                                    QMessageBox.Yes|QMessageBox.No)
            if resp==QMessageBox.Yes:
                for i in self.manager.fetch_data_list():
                    if i[0]==opt:
                        with open("data.pkl", "wb") as file:
                                print('dump',i)
                                pickle.dump(i, file)
                                break
                self.new_ui=PurelyzerApp()   
                self.new_ui.show()
                self.close()
                
                
            
                
    
    def finish_with_options(self):
        try:
                self.browsed_file_path
        except Exception as e:
                QMessageBox.warning(self,'Error','Please choose a file for import!')
        else:
            resp=f.fmessagebox(f'Do you want to import {os.path.basename(self.browsed_file_path)} and also save options?',
                                    'Confirmation',
                                    QMessageBox.Question,
                                    QMessageBox.Yes|QMessageBox.No)
            if resp==QMessageBox.Yes:
                options_list=[
                            str(self.file_format_combo.currentText()),
                            str(self.delimiter_input.text()),
                            str(self.header_yes.isChecked()),
                            str(self.columns_input.text()),#5
                            str(self.missing_value_input.text()),
                            str(self.rows_input.text()),
                            str(self.date_convert_checkbox.isChecked()),
                            str(self.encoding_input.text()),
                            str(self.skip_rows_input.text())]
                if self.browsed_file_path!='' and (self.browsed_file_path.endswith('.csv') or
                                            self.browsed_file_path.endswith('.json') or 
                                            self.browsed_file_path.endswith('.xlx') or 
                                            self.browsed_file_path.endswith('.xlsx')):
                            options_list.insert(0,self.browsed_file_path)
                            with open("data.pkl", "wb") as file:
                                pickle.dump(options_list, file)
                            self.manager.add_data(options_list)
                            self.new_ui=PurelyzerApp()   
                            self.new_ui.show()
                            self.manager.add_data(options_list)
                            self.close()


                else:
                        QMessageBox.warning(self,'Error','Please choose a file for import!')
            
            

app = QApplication([])
main_screen = ImportPage_UI()
main_screen.show()
app.exec_()