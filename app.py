'''
@ project: Le
@ file: app
@ user: 罗申申
@ email: luoshenshen@buaa.edu.cn
@ tool: PyCharm
@ time: 2021/5/25 17:46
'''
import xlrd
import translation
import ctypes, sys
from xlutils.copy import copy

STD_OUTPUT_HANDLE = -11
FOREGROUND_PINK = 0x0d
std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)


def set_cmd_text_color(color, handle=std_out_handle):
    b = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return b


set_cmd_text_color(FOREGROUND_PINK)
sys.stdout.write('''

Hiーーーーー
　☆ *　. 　☆
　　. ∧＿∧　∩　* ☆     ☆ 。 ☆ 。 ☆  乐姐好  ☆ 。 ☆ 。 ☆
* ☆ ( ・∀・)/ .
　. ⊂　　 ノ* ☆
☆ * (つ ノ .☆
　　 (ノ

''')

path = input("\n\n （づ￣3￣）づ╭❤～  巧乐学姐, 请输入需要翻译的Excel文件名:")
work_book = xlrd.open_workbook(path)
sheets_name = work_book.sheet_names()
change_book = copy(work_book)

print("\n\n  (๑•̀ㅂ•́)و✧  这个Excel一共有", work_book.nsheets, "张表单", '分别是', sheets_name)
sheet = int(input("\n\n  φ(゜▽゜*)♪  请输入需要翻译第几个表单, -------tips:从第1个表开始, 就输入1:"))

sheet_work = work_book.sheet_by_index(sheet-1)

sheet_change = change_book.get_sheet(sheet-1)

rows = sheet_work.nrows
columns = sheet_work.ncols
print("\n\n  (o゜▽゜)o☆[BINGO!]  这个表单共有:", rows, "行,", columns, "列")


def col_work(column,start):
    cols = sheet_work.col_values(column-1, start-1)
    for val,i in zip(cols,range(len(cols))):
        en = val
        ch = translation.translator(en)
        sheet_change.write(start+i-1, column-1, ch)
        print(ch)
    change_book.save('success.xls')


if __name__ == "__main__":
    col = int(input("\n\n  ʅ（´◔౪◔）ʃ  输入需要翻译第几列, tips:从第1列开始, 就输入1:"))
    start = int(input("\n\n  o(￣▽￣)ｄ  输入从第"+str(col)+'列的第几行开始翻译:'))
    col_work(col, start)
    print('\n\n  (ˉ▽￣～) 切~~  小事一桩，OK了')