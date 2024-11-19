from PyQt5.QtWidgets import QMessageBox,QApplication,QRadioButton,QComboBox
import sys,pandas as pd
from PyQt5.QtGui import QFont
from scipy import stats
import warnings
from dateutil.parser import parse

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
        columns_edited=False
        if file_format.lower() == "csv":
            df = pd.read_csv(file_path)
            if len(df.columns) == 1:
                if ';' in df.columns[0]:
                    columns_edited = df.columns[0].split(';')
                elif ',' in df.columns[0]:
                    columns_edited = df.columns[0].split(',')
                elif '/' in df.columns[0]:
                    columns_edited = df.columns[0].split('/')
            df = pd.read_csv(file_path, delimiter=delimiter, header=header, 
                             usecols=usecols,na_values=na_values, nrows=nrows, 
                             parse_dates=parse_dates, encoding=encoding,skiprows=skip_row)
            if columns_edited:
                df.columns=columns_edited[0:usecols[-1]+1]
            
            
        elif file_format.lower() == "excel":
            df = pd.read_excel(file_path, header=header, usecols=usecols,
                               na_values=na_values, nrows=nrows, 
                               parse_dates=parse_dates,skiprows=skip_row)
            
            
        elif file_format.lower() == "json":
            df = pd.read_json(file_path, encoding=encoding)
            
        else:
            raise ValueError('Unsupported file format!')
        for i in df.columns:
            if i.lower()=='id':
                continue
            j=str(df[i].dropna().iloc[0])
            if ',' in j:
                if len(j.split(','))==2: #eger kesrdirse
                    df[i] = df[i].str.replace(',', '.', regex=False)
                    df[i] = pd.to_numeric(df[i],errors='coerce')
                    df[i]=df[i].astype(float)
                    
            elif ('.' not in j) and (',' not in j) and j.lstrip('-').isdigit():
                try:
                    df[i] = df[i].str.replace(',', '.', regex=False)
                except:
                    pass
                df[i] = pd.to_numeric(df[i],errors='coerce')
                df[i]=df[i].astype(float)
                    
            
        return df
    except Exception as e:
        print('OpenDataSet Error : ',e)


 
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
    
    options = [str(option) for option in options]
    options.insert(0, 'All')
    combo_box.addItems(options)
    combo_box.setFont(fontsize)
    
    layout = msg_box.layout()
    layout.addWidget(combo_box)
    
    msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    resp = msg_box.exec()
    
    if resp == QMessageBox.Ok:
        return combo_box.currentText()
    return None
    

#Problem
def calculate_statistics(data, i):
    formats = [
        "%m/%d/%Y", "%m-%d-%Y", "%Y/%m/%d", "%Y-%m-%d", "%d/%m/%Y", "%d-%m-%Y", "%Y%m%d",
        "%m/%d/%Y %I:%M:%S %p", "%m/%d/%Y %I:%M %p", "%m/%d/%Y %H:%M:%S", "%m/%d/%Y %H:%M",
        "%Y-%m-%d %H:%M:%S", "%Y-%m-%d %H:%M", "%d/%m/%Y %H:%M:%S", "%d/%m/%Y %H:%M",
        "%H:%M:%S", "%H:%M", "%I:%M:%S %p", "%I:%M %p", "%m.%d.%Y", "%d.%m.%Y",
        "%m.%d.%Y %H:%M:%S", "%m.%d.%Y %I:%M %p"
    ]

    for fmt in formats:
        try:
            data[i] = pd.to_datetime(data[i], format=fmt, errors='coerce')
            break
        except ValueError:
            continue

    # Eğer tarih dönüşümü başarısızsa tüm değerler NaT olacak
    if data[i].isna().all():
        print(f"No valid dates found for column: {i}")
        return None

    # Numeric timestamps (epoch) için işleme
    numeric_dates = data[i].dropna().astype(int) // 10**9

    if not numeric_dates.empty:
        mean = numeric_dates.mean()
        median = numeric_dates.median()
        mode = stats.mode(numeric_dates, keepdims=True)[0][0]  # Tek değer al
        try:
            result = {
                'mean': pd.to_datetime(mean, unit='s').date(),
                'median': pd.to_datetime(median, unit='s').date(),
                'mode': pd.to_datetime(mode, unit='s').date()
            }
            return result
        except pd.errors.OutOfBoundsDatetime:
            print(f"OutOfBoundsDatetime error in column: {i}")

    return None

from datetime import datetime

def validate_date(date):
    date = str(date)
    formats = [
        "%m/%d/%Y", 
        "%m-%d-%Y", 
        "%Y/%m/%d", 
        "%Y-%m-%d", 
        "%d/%m/%Y", 
        "%d-%m-%Y",
        "%Y%m%d",
    
        "%m/%d/%Y %I:%M:%S %p",  
        "%m/%d/%Y %I:%M %p",     
        "%m/%d/%Y %H:%M:%S",     
        "%m/%d/%Y %H:%M",        
        "%Y-%m-%d %H:%M:%S",     
        "%Y-%m-%d %H:%M",        
        "%d/%m/%Y %H:%M:%S",     
        
        "%H:%M:%S",           
        "%H:%M",                
        "%I:%M:%S %p",          
        "%I:%M %p",             
    
        "%m.%d.%Y",           
        "%d.%m.%Y",              
        "%m.%d.%Y %H:%M:%S",    
        "%m.%d.%Y %I:%M %p",
        ]
    
    
    
    
    for fmt in formats:
        try:
            date_value = datetime.strptime(date, fmt)
            return True
        except ValueError:
            continue
    return False


def convert_to_pandas_type(input_text):
    try:
        # Tarih veya saat olup olmadığını kontrol et
        parsed = parse(input_text, fuzzy=False)
        
        # Sadece zaman varsa, timedelta formatında döndür
        if parsed.date() == pd.Timestamp("today").date():
            return pd.to_timedelta(f"{parsed.hour}:{parsed.minute}:{parsed.second}")
        
        # Hem tarih hem zaman varsa veya sadece tarih varsa, datetime formatında döndür
        return pd.to_datetime(input_text)
    
    except ValueError:
        return None

def clean_time_strings(series):
    try:
        return series.str.replace('.', ':', regex=False)
    except:
        pass

  
def fill_mv_func(dataset=pd.DataFrame(), fill_method=int):
    # Fill method indexs:
    # 1 - Median
    # 2 - Average(mean)
    # 3 - Mode
    # 4 - Sequential Forward Filling
    
    #############
    # STATIK KOD#
    #############
    
    try:
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always", UserWarning)  # UserWarning'leri tut

            match fill_method:
                case 1:
                    user_C_choice = ask_question_with_comboBox(list(dataset.columns))
                    if user_C_choice == 'All':
                        if dataset.isnull().values.any():
                            for i in dataset.columns:
                                if dataset[i].dropna().iloc[0] and validate_date(str(dataset[i].dropna().iloc[0])):
                                    try:
                                        dataset[i] = clean_time_strings(dataset[i])
                                        dataset[i] = pd.to_datetime(dataset[i], errors='coerce')
                                        l_stats = calculate_statistics(dataset, i)
                                        if l_stats is not None:
                                            dataset[i].fillna(l_stats['median'], inplace=True)
                                            
                                    except Exception as e:
                                        print(f"Case 1 Fill Error in column {i}: {e}")
                                        
                                else:
                                    try:
                                        dataset[i].fillna(dataset[i].median(), inplace=True)
                                    except Exception as e:
                                        print('Case 1 Fill Error', e)
                                        continue
                        else:
                            warnings.warn("No missing values found", UserWarning)

                    elif user_C_choice:
                        if dataset[user_C_choice].isnull().any():
                            if validate_date(str(dataset[user_C_choice].dropna().iloc[0])):
                                dataset[i] = clean_time_strings(dataset[i])
                                dataset[i] = pd.to_datetime(dataset[i], errors='coerce')
                                l_stats = calculate_statistics(dataset, i)    
                                if l_stats is not None:
                                    dataset[i].fillna(l_stats['median'], inplace=True)
                            else:
                                dataset[user_C_choice].fillna(dataset[user_C_choice].median(), inplace=True)
                        else:
                            warnings.warn("No missing values found", UserWarning)
                case 2:
                    user_C_choice = ask_question_with_comboBox(list(dataset.columns))
                    if user_C_choice == 'All':
                        if dataset.isnull().values.any():
                            for i in dataset.columns:
                                if dataset[i].dropna().iloc[0] and validate_date(str(dataset[i].dropna().iloc[0])):
                                    try:
                                        dataset[i] = clean_time_strings(dataset[i])
                                        dataset[i] = pd.to_datetime(dataset[i], errors='coerce')
                                        l_stats = calculate_statistics(dataset, i)
                                        if l_stats is not None:
                                            dataset[i].fillna(l_stats['mean'], inplace=True)
                                            
                                    except Exception as e:
                                        print(f"Case 2 Fill Error in column {i}: {e}")
                                else:
                                    try:
                                        dataset[i].fillna(dataset[i].mean(), inplace=True)
                                    except Exception as e:
                                        print('Case 2 Fill Error', e)
                                        continue
                        else:
                            warnings.warn("No missing values found", UserWarning)
                            
                    elif user_C_choice:
                        if dataset[user_C_choice].isnull().any():
                            if validate_date(str(dataset[user_C_choice].dropna().iloc[0])):
                                dataset[i] = clean_time_strings(dataset[i])
                                dataset[i] = pd.to_datetime(dataset[i], errors='coerce')
                                l_stats = calculate_statistics(dataset, i)    
                                if l_stats is not None:
                                    dataset[i].fillna(l_stats['mean'], inplace=True)
                            else:
                                dataset[user_C_choice].fillna(dataset[user_C_choice].mean(), inplace=True)
                        else:
                            warnings.warn("No missing values found", UserWarning)
                case 3:
                    user_C_choice = ask_question_with_comboBox(list(dataset.columns))
                    if user_C_choice == 'All':
                        if dataset.isnull().values.any():
                            for i in dataset.columns:
                                if dataset[i].dropna().iloc[0] and validate_date(str(dataset[i].dropna().iloc[0])):
                                    try:
                                        dataset[i] = clean_time_strings(dataset[i])
                                        dataset[i] = pd.to_datetime(dataset[i], errors='coerce')
                                        l_stats = calculate_statistics(dataset, i)
                                        if l_stats is not None:
                                            dataset[i].fillna(l_stats['mode'], inplace=True)
                                            
                                    except Exception as e:
                                        print(f"Case 3 Fill Error in column {i}: {e}")
                                else:
                                    try:
                                        dataset[i].fillna(dataset[i].mode().iloc[0], inplace=True)
                                        print('m',dataset[i])
                                    except Exception as e:
                                        print('Case 3 Fill Error', e)
                                        continue
                        else:
                            warnings.warn("No missing values found", UserWarning)
                            
                    elif user_C_choice:
                        if dataset[user_C_choice].isnull().any():
                            if validate_date(str(dataset[user_C_choice].dropna().iloc[0])):
                                dataset[i] = clean_time_strings(dataset[i])
                                dataset[i] = pd.to_datetime(dataset[i], errors='coerce')
                                l_stats = calculate_statistics(dataset, i)    
                                if l_stats is not None:
                                    dataset[i].fillna(l_stats['mean'], inplace=True)
                            else:
                                dataset[user_C_choice].fillna(dataset[user_C_choice].mean(), inplace=True)
                        else:
                            warnings.warn("No missing values found", UserWarning)
                case 4:
                    user_C_choice = ask_question_with_comboBox(list(dataset.columns))
                    if user_C_choice == 'All':
                        if dataset.isnull().values.any():
                            dataset.fillna(method='ffill', inplace=True)
                        else:
                            warnings.warn("No missing values found", UserWarning)
                    elif user_C_choice:
                        if dataset[user_C_choice].isnull().any():
                            dataset[user_C_choice].fillna(method='ffill', inplace=True)
                        else:
                            warnings.warn("No missing values found", UserWarning)
                case _:
                    raise ValueError("Index value out of range!")
                
            if any(issubclass(warning.category, UserWarning) for warning in w):
                raise UserWarning("UserWarning: Missing values were expected but not found.")

    except UserWarning as uw:
        raise UserWarning

    except Exception as e:
        print("There is a filling problem:", e)
        
        