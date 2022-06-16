import openpyxl
import os, shutil

def copy_xlsx(my_class,month):
    source_file = '班级学员月度达标率_模版.xlsx'
    my_xlsx = '{}学员月度达标率_{}.xlsx'.format(my_class,month)
    # print(os.path.exists())
    return shutil.copyfile(source_file, my_xlsx)

def write_xlsx():
    my_file = copy_xlsx('濠江班小组18B1','六月份')
    print(my_file)
    # mpd = MakePandas(my_file)
    row_list = [['1','2','3','4','5','6','7','8','9','10','11','12'],
                ['2','2','3','4','5','6','7','8','9','10','11','12'],
                ['3','2','3','4','5','6','7','8','9','10','11','12']]
    # 读表格
    myxlsx = openpyxl.load_workbook(my_file)
    my_sheet = myxlsx.get_sheet_by_name('源数据')
    for r in row_list:
        my_sheet.append(r)
    myxlsx.save(my_file)

write_xlsx()