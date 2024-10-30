import pickle
import os
#Userin recent datasetlerinin saxladigi purelyzer.bin fayli
class BinaryFileManager():
    def __init__(self, file_path='purelyzer.bin'):
        self.file=file_path
    def remove_line(self,row=None):
        content = self.loader_bin()
        if row!=None:
            if 0 <= row < len(content):
                del content[row]
                with open(self.file, 'wb') as file:
                    pickle.dump(content, file)
                print(f"Line {row} has been removed from {self.file}.")
            else:
                raise IndexError('Error : Line value out of index!')
        else:
            content.clear()
            with open(self.file, 'wb') as file:
                pickle.dump(content, file)
                print('Binary file fully cleaned!')
                
    def loader_bin(self):
        if os.path.exists(self.file):
            with open(self.file, 'rb') as f:
                return pickle.load(f)
        return []
    
    def add_data(self, text=[]):
        binary_content = self.loader_bin()
        if text not in binary_content:
            for i in binary_content:
                if os.path.basename(text[0])==os.path.basename(i[0]):
                    binary_content.remove(i)
            
            binary_content.append(text)
            with open(self.file, 'wb') as f:
                pickle.dump(binary_content, f)
                print('Data has added successfully!')
                    
                    
    def fetch_data_list(self, row=None):
        if os.path.exists(self.file):
            with open(self.file, 'rb') as file:
                content = pickle.load(file)
            if row is not None: 
                return content[row] if content is not None else None
            else:
                return content if content is not None else None
        else:
            print(f"{self.file} does not exist.")
            return None

t = BinaryFileManager()
print(t.fetch_data_list())

#Example dataset elave etmek ucun
'''
t.add_data(['AirQualityUCI.csv',
        'CSV',
        ';',
        'False',
        '0-15',
        '',
        '',
        'Yes',
        'Utf-8'
        ,'3'])
        '''