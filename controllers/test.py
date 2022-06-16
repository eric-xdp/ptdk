from datetime import datetime, timedelta


def get_week_and_month(date):
    # date : 2022-05-16 str
    # 根据今日日期，得出周、月
    today = datetime.strptime(date,'%Y-%m-%d')
    monday = datetime.strftime(today - timedelta(today.weekday()), "%m.%d")
    sunday = datetime.strftime(today + timedelta(7 - today.weekday() - 1), "%m.%d")
    new_monday = str(int(monday.split('.')[0]))+'.'+ monday.split('.')[1]
    new_sunday = str(int(sunday.split('.')[0])) + '.' + sunday.split('.')[1]
    print(new_monday.split('.')[0], new_monday+'-'+new_sunday)

# get_week_and_month('2022-06-02')

# today = datetime.today().strftime('%Y-%m-%d')
#
# myweek = '5.16-5.22'
# wek = "2022-05-17"
# year = wek.split('-')[0]
# # 5.16
# start_date = year+'-'+myweek.split('-')[0].replace('.','-')
# end_date = year+'-'+myweek.split('-')[1].replace('.','-')
# print(start_date,end_date)


import pandas as pd
import openpyxl
class MakePandas():
    """
        封装Pandas对Excel表的处理。
        自用功能
    """
    def __init__(self, file_path):
        self.path = file_path
        self.book = openpyxl.load_workbook(self.path)
        self.excel_writer = pd.ExcelWriter(self.path, engine='openpyxl')
        self.excel_writer.book = self.book
        # self.excel_writer.sheets = dict((ws.title, ws) for ws in self.book.worksheets)

    # 获取指定的sheet表数据
    def get_data(self, sheet): return pd.read_excel(self.path, sheet_name=sheet).values

    # 添加一个空的sheet
    def add_sheet(self, sheet_name, columns):
        data = pd.DataFrame(columns=columns)
        data.to_excel(self.excel_writer, sheet_name=sheet_name, index=False)
        self.excel_writer.save()

    # 在指定的sheet内追加一行数据。
    def append_data_to_sheet(self, sheet_name, row_list):
        sheet = pd.read_excel(self.excel_writer, sheet_name=sheet_name)
        sheet_data = pd.DataFrame(sheet)
        print(sheet_data)
        sheet_data.loc[sheet_data.shape[0]] = row_list  # 与原数据同格式
        sheet_data.to_excel(self.excel_writer, sheet_name=sheet_name, index=False, header=True)
        self.excel_writer.save()



def copy_xlsx():

    path = ''