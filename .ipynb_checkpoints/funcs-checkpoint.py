from PyQt5.QtWidgets import QMessageBox,QApplication,QRadioButton,QComboBox
import sys,pandas as pd
from PyQt5.QtGui import QFont
def fmessagebox(message, title="Information", icon=QMessageBox.Information, buttons=QMessageBox.Ok):
    if not QApplication.instance():
        app = QApplication(sys.argv)
    msg_box = QMessageBox()
    msg_box.setIcon(icon)
    msg_box.setWindowTitle(title)
    msg_box.setText(message)
    msg_box.setStandardButtons(buttons)
    return msg_box.exec_()

def remove_null_data(dataset,choice):
    match choice:
        case 'row':
            dataset.dropna(axis=0, how='any', subset=None, inplace=True) 
        case 'column':
            dataset.dropna(axis=1, how='any', subset=None, inplace=True)
        case 'both':
            dataset.dropna(axis=0, how='all', subset=None, inplace=True)
            dataset.dropna(axis=1, how='all', subset=None, inplace=True)
            
def open_dataset_with_options(options_list):

    file_path = options_list[0]
    
    file_format = options_list[1]
    
    delimiter = options_list[2] if options_list[2] != '' else ','  
    
    header = 0 if options_list[3] == 'True' else None  
    skip_row= int(options_list[9]) if options_list[9]!='' else None
   
    usecols = options_list[4] if options_list[4] != '' else None  
    if usecols:
        try:
            if '-' in usecols:
                col_range = usecols.split('-')
                usecols = list(range(int(col_range[0]), int(col_range[1])))
            elif ',' in usecols:
                usecols = [int(col) for col in usecols.split(',')]
            else:  
                usecols = [int(usecols)]
        except ValueError:
            raise ValueError("Invalid column range or list format")
    

    na_values = options_list[5] if options_list[5] != '' else None  
    
    nrows = int(options_list[6]) if options_list[6] != '' else None  
    
    parse_dates = options_list[7] == 'True'  
    
    encoding = options_list[8] if options_list[8] != '' else None  
    
    
    try:
        if file_format.lower() == "csv":
            df = pd.read_csv(file_path, delimiter=delimiter, header=header, 
                             usecols=usecols,na_values=na_values, nrows=nrows, 
                             parse_dates=parse_dates, encoding=encoding,skiprows=skip_row)
            
            
        elif file_format.lower() == "excel":
            df = pd.read_excel(file_path, header=header, usecols=usecols,
                               na_values=na_values, nrows=nrows, 
                               parse_dates=parse_dates,skiprows=skip_row)
            
            
        elif file_format.lower() == "json":
            df = pd.read_json(file_path, encoding=encoding)
            
        else:
            raise ValueError('Unsupported file format!')
        return df
    except Exception as e:
        print('Error : ',e)
 
def radio_btn_unchecker(btn=QRadioButton):
    btn.setAutoExclusive(False)
    btn.setChecked(False)
    btn.setAutoExclusive(True)
    
def ask_question_with_comboBox(options=list):
    if not QApplication.instance():
        app = QApplication(sys.argv)
    msg_box = QMessageBox()
    msg_box.setWindowTitle('System Confirmation')
    msg_box.setText('Choose column you want to fill')
    fontsize = QFont()
    fontsize.setPointSize(15)
    msg_box.setFont(fontsize)
    combo_box = QComboBox()
    
    # Kullanıcıya göstermek için sütun isimlerini kullanıyoruz.
    options = [str(option) for option in options]
    options.insert(0, 'All')
    combo_box.addItems(options)
    combo_box.setFont(fontsize)
    
    # Adjust layout
    layout = msg_box.layout()
    layout.addWidget(combo_box)
    
    msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    resp = msg_box.exec()
    
    if resp == QMessageBox.Ok:
        return combo_box.currentText()
    return None
    
    
        
        







def fill_mv_func(dataset=pd.DataFrame(), fill_method=int):
    # Fill method indexs:
    # 1 - Median
    # 2 - Average
    # 3 - Mode
    # 4 - Sequential Forward Filling
    match fill_method:
        case 1:
            user_C_choice = ask_question_with_comboBox(list(dataset.columns))
            if user_C_choice == 'All':
                dataset.fillna(dataset.median(), inplace=True)
            elif user_C_choice:
                # Kullanıcı seçimini sütun ismine göre işle
                dataset[user_C_choice].fillna(dataset[user_C_choice].median(), inplace=True)
                
        case 2:
            user_C_choice = ask_question_with_comboBox(list(dataset.columns))
            if user_C_choice == 'All':
                dataset.fillna(dataset.mean(), inplace=True)
            elif user_C_choice:
                dataset[user_C_choice].fillna(dataset[user_C_choice].mean(), inplace=True)
                
        case 3:
            user_C_choice = ask_question_with_comboBox(list(dataset.columns))
            if user_C_choice == 'All':
                dataset.fillna(dataset.mode().iloc[0], inplace=True)
            elif user_C_choice:
                dataset[user_C_choice].fillna(dataset[user_C_choice].mode().iloc[0], inplace=True)
                
        case 4:
            user_C_choice = ask_question_with_comboBox(list(dataset.columns))
            if user_C_choice == 'All':
                dataset.fillna(method='ffill', inplace=True)
            elif user_C_choice:
                dataset[user_C_choice].fillna(method='ffill', inplace=True)
                
        case _:
            raise ValueError("Index value out of range!")