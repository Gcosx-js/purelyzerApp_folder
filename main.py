#Elmir Guliyev | github.com/gcosx-js
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QThread,pyqtSignal
from purelyzer_ui import Ui_Form
import pandas as pd
import funcs as f
import binary as bin
import logging,os,sys,pickle
import datetime,traceback
import threading,subprocess

class PurelyzerApp(QWidget):
    def __init__(self) -> None:
            super().__init__()
            self.app = Ui_Form()
            self.app.setupUi(self)
            self.auto_save_bool = True
            self.bin_manager = bin.BinaryFileManager()
            
            self.load_dataset_thread()
            self.load_to_table(dataset_lo=self.dataset)
            '''
            self.dataset_path = 'AirQualityUCI.csv'
            self.log_path =f'{os.path.basename(self.dataset_path).split('.')[0]}_save.log'
            self.dataset = pd.read_csv(self.dataset_path,sep=';',usecols=range(15))
            '''
            #Log tutma alani
            logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s %(message)s',
                        filename=self.log_path,
                        filemode='w')
            
            #Doldurma ve silme butonlarinin baglantilari
            self.app.done_remove_mv_btn.clicked.connect(self.remove_mv_donebtn)
            self.refresh_overview_datas()
            
            self.app.fill_mv_done_btn.clicked.connect(self.fill_mv_doneBTN_clicked)
            self.app.custom_v_lineedit.textChanged.connect(self.referenced_unchecker_for_f_mv)
    

    def referenced_unchecker_for_f_mv(self):
        f.radio_btn_unchecker(self.app.median_radiobtn)
        f.radio_btn_unchecker(self.app.average_radiobtn)
        f.radio_btn_unchecker(self.app.mod_radiobtn)
        f.radio_btn_unchecker(self.app.sequential_radiobtn)
        
    def refresh_overview_datas(self):
        
            try:
                if self.dataset is None:
                    raise ValueError("Dataset is not loaded properly.")
                
                overview_list_items = [
                    f'Row count : {self.dataset.shape[0]}',
                    f'Column count : {self.dataset.shape[1]}',
                    f'Missing values count : {self.dataset.isnull().sum().sum()}',
                    f'Duplicate values count : {self.dataset.duplicated().sum()}'
                ]
                
                self.app.general_overview_listwidget.clear()
                for i in range(len(overview_list_items)):
                    
                    self.app.general_overview_listwidget.insertItem(i, QListWidgetItem(overview_list_items[i]))
                self.load_to_table(dataset_lo=self.dataset)
            
            except Exception as e:
                error_trace = traceback.format_exc()
                logging.error(f"Full Traceback: {error_trace}")
                subprocess.run([sys.executable, "force_quit.py", str(e)])
                self.close()
            
            
    def load_dataset_thread(self):
            self.load_thread = QThread()
            def load_dataset_thread2():
                    with open("data.pkl", "rb") as file:
                        self.dataset_options_main =pickle.load(file)

                    self.dataset_path=self.dataset_options_main[0]
                    self.log_path =f'log_files/{os.path.basename(self.dataset_path).split('.')[0]}_save.log'
                    self.dataset = f.open_dataset_with_options(self.dataset_options_main)
                    self.load_thread.quit()
                
                
            self.load_thread.run = load_dataset_thread2
            self.load_thread.start()
            self.load_thread.wait()
            return
                
    def remove_mv_donebtn(self):
        logging.info('"Remove missing values" button clicked!')
        if self.app.full_null_radiobtn.isChecked():
            full_null_row_count = self.dataset.isna().all(axis=1).sum()
            full_null_column_count=self.dataset.isna().all(axis=0).sum()
            
            resp=f.fmessagebox(f'Do you want to remove {full_null_row_count} rows and {full_null_column_count} columns ?',
                               'Confirmation',
                               QMessageBox.Question,
                               QMessageBox.Yes|QMessageBox.No)
            if resp==QMessageBox.Yes:
                f.remove_null_data(self.dataset,choice='both')
                f.fmessagebox(f'{full_null_row_count} rows and {full_null_column_count} columns has been deleted!')
                logging.info(f'{full_null_row_count} rows and {full_null_column_count} columns has been deleted!')
                f.radio_btn_unchecker(self.app.full_null_radiobtn)
                
                self.refresh_overview_datas()
                
            else:
                f.fmessagebox('Operation cancelled!')
                logging.warn('"Remove entirely full row/column" operation cancelled!')

        elif self.app.row_remove_mv_btn.isChecked():
            nan_rows_count = self.dataset.isna().any(axis=1).sum()
            resp=f.fmessagebox(f'Do you want to remove {nan_rows_count} rows?',
                               'Confirmation',
                               QMessageBox.Question,
                               QMessageBox.Yes|QMessageBox.No)
            if resp==QMessageBox.Yes:
                f.remove_null_data(self.dataset,choice='row')
                f.fmessagebox(f'{nan_rows_count} rows has been deleted!')
                logging.info(f'{nan_rows_count} rows has been deleted!')
                f.radio_btn_unchecker(self.app.row_remove_mv_btn)
                self.refresh_overview_datas()
            else:
                f.fmessagebox('Operation cancelled!')
                logging.warn('"Remove rows" operation cancelled!')
                
         
        elif self.app.column_remove_mv_btn.isChecked():
            nan_columns_count = self.dataset.isna().any(axis=0).sum()
            resp=f.fmessagebox(f'Do you want to remove {nan_columns_count} columns?',
                               'Confirmation',
                               QMessageBox.Question,
                               QMessageBox.Yes|QMessageBox.No)
            if resp==QMessageBox.Yes:
                f.remove_null_data(self.dataset,choice='column')
                f.fmessagebox(f'{nan_columns_count} columns has been deleted!')
                logging.info(f'{nan_columns_count} columns has been deleted!')
                self.refresh_overview_datas()
                
            else:
                f.fmessagebox('Operation cancelled!')
                logging.warn('"Remove columns" operation cancelled!')
                
    
    def closeEvent(self,event):
        logging.info('Close Event Triggered!')
        if not self.auto_save_bool:
            resp=f.fmessagebox(f'You have unsaved dataset : "{os.path.basename(self.dataset_path)}". Are you sure you want to exit without export?',
                               'Confirmation',
                               QMessageBox.Question,
                               QMessageBox.Yes|QMessageBox.No)
            if resp==QMessageBox.Yes:
                event.accept()
                logging.info(f'"Pureleyzer" Closed!')
                
            elif resp==QMessageBox.No:
                event.ignore()
                self.app.main_stacked_widget.setCurrentIndex(4)
                logging.info('Close Event Ingored!')
            else:
                event.ignore()
        else:
            event.accept()
            logging.info(f'"Pureleyzer" Closed!')
    
        #Thread istifade ederek eyni zamanda loading prosesi
    def load_to_table(self,dataset_lo=pd.DataFrame):
        threading.Thread(target=self._load_data, args=(dataset_lo,)).start()  
    def _load_data(self, dataset_lo):
        self.app.overview_table_widget.clearContents() 
        self.app.overview_table_widget.setColumnCount(len(dataset_lo.columns) + 1)
        self.app.overview_table_widget.setRowCount(len(dataset_lo.index))
        self.app.overview_table_widget.setHorizontalHeaderLabels(['ID'] + list(dataset_lo.columns))
        self.app.overview_table_widget.resizeRowsToContents()
        header = self.app.overview_table_widget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        
        
        
        
        for i in range(len(dataset_lo.index)):
            
            id_item = QTableWidgetItem(str(dataset_lo.index[i]))
            id_item.setFont(font)
            self.app.overview_table_widget.setItem(i, 0, id_item)
            
            for j in range(len(dataset_lo.columns)):
                item = QTableWidgetItem(str(dataset_lo.iat[i, j]))
                item.setFont(font)
                self.app.overview_table_widget.setItem(i, j + 1, item)
                
        self.app.overview_table_widget.resizeColumnsToContents()
        
            
                   
    
    def fill_mv_doneBTN_clicked(self,index):
        logging.info('Fill Missing Value Button Clicked!')
        resp=f.fmessagebox(f'Are you sure to fill NA values?',
                               'Confirmation',
                               QMessageBox.Question,
                               QMessageBox.Yes|QMessageBox.No)
        if resp==QMessageBox.Yes:
            if self.app.median_radiobtn.isChecked():
                try:
                    f.fill_mv_func(self.dataset,1)
                    self.refresh_overview_datas()
                    logging.info('Fill with MEDIAN has used successfully!')
                except UserWarning:
                    f.fmessagebox('No missing value found!')

            elif self.app.average_radiobtn.isChecked():
                try:
                    f.fill_mv_func(self.dataset,2)
                    self.refresh_overview_datas()
                    logging.info('Fill with AVERAGE has used successfully!')
                except UserWarning:
                    f.fmessagebox('No missing value found!')
            elif self.app.mod_radiobtn.isChecked():
                
                try:
                    f.fill_mv_func(self.dataset,3)
                    self.refresh_overview_datas()
                    logging.info('Fill with MOD has used successfully!')
                except UserWarning:
                    f.fmessagebox('No missing value found!')
                    
            elif self.app.sequential_radiobtn.isChecked():
                try:
                    f.fill_mv_func(self.dataset,4)
                    self.refresh_overview_datas()
                    logging.info('Fill with SEQUENTIAL has used successfully!')
                except UserWarning:
                    f.fmessagebox('No missing value found!')
            
            elif self.app.custom_v_lineedit!='':
                try:
                    f.fill_mv_func(dataset=self.dataset,fill_method=5,custom_value=self.app.custom_v_lineedit.text())
                    self.refresh_overview_datas()
                    logging.info('Fill with MOD has used successfully!')
                except UserWarning:
                    f.fmessagebox('No missing value found!')
        else:
            f.radio_btn_unchecker(self.app.median_radiobtn)
            f.radio_btn_unchecker(self.app.average_radiobtn)
            f.radio_btn_unchecker(self.app.mod_radiobtn)
            f.radio_btn_unchecker(self.app.sequential_radiobtn)
            logging.warn('Filling process cancelled!')
        
                
'''   
def main():
    app = QApplication([])
    purelyzer_page = PurelyzerApp()
    purelyzer_page.show()
    app.exec_()

if __name__ == "__main__":
    main()
'''