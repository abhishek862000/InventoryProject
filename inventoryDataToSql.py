import pandas as pd

class ExcelReader:
    def __init__(self,file_path):
        self.file_path=file_path
        self.df=pd.read_excel(file_path)
        
        
class DataPrinter:
    def __init__(self,df:pd):
        self.df=df
    def print(self):
        print(self.df.head(10).to_string())
        
class NanTONonPrinter :
    def __init__(self,df:pd.DataFrame):
        self.df=df
        #Replace all NaN values with "none"
    def fillNans(self,value="none"): 
        self.df = self.df.replace(r'^\s*$', pd.NA, regex=True)    
        self.df=self.df.fillna(value)
        return self.df
class DataExporter:
    def __init__(self, df: pd):
        self.df = df
    def to_excel(self, file_path):
        self.df.to_excel(file_path, index=False)

reader=ExcelReader("E:/Inventory Managment Project/Stock Details.xlsx")

NaNConverter=NanTONonPrinter(reader.df)
reader.df=NaNConverter.fillNans()
printer=DataPrinter(reader.df)
printer.print()