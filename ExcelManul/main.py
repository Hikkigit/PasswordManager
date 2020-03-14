import sys
import xlrd
import xlwt
import pandas
from datetime import date,datetime
import time


path="D:\工作\Password.xlsx"
#打开workbook
workbook=xlrd.open_workbook(path)
#以sheet顺序获取工作表
worktable=workbook.sheets()[0]
'''
返回所有sheet名
sheetnames=workbook.sheet_names()
#通过名字获取工作表
worktable=workbook.sheet_by_name(sheetname[0])
'''

nrows=worktable.nrows #有效行数
collecRow=worktable.row(10)#返回那一行的数据列表
collecRowType=worktable.row_types(10,start_colx=0,end_colx=None)#返回单元格格式的列表
collecCol=worktable.col(6)#返回那一列数据列表
print(collecCol)
collectype=worktable.col_types(6,start_rowx=0,end_rowx=None)
print(collectype)



for i in range(worktable.nrows):

    for j in range(worktable.ncols):
        coltype=worktable.cell_type(i,j)
        if coltype==3: #data类型为3
            print("Xldate=",worktable.cell(i,j))
            Time=xlrd.xldate.xldate_as_tuple(worktable.cell_value(i,j),workbook.datemode)
            print("Time=", Time)  #Time= (2019, 8, 30, 0, 0, 0)
            strTime=date(*Time[:3]).strftime("%Y/%m/%d") #formatTime: 2019/08/30,strftime():日期格式转化为字符串格式的函数
            print("formatTime:",strTime)
            print("CurrentTime:",time.localtime())
            '''time.struct_time(tm_year=2020, tm_mon=3, tm_mday=14, tm_hour=21, tm_min=50, tm_sec=14, tm_wday=5, tm_yday=74, tm_isdst=0)
               struct_time,时间元组
               time.sleep(3)
            '''
            timenow=time.strftime("%Y/%m/%d",time.localtime())
            print("现在时间：",timenow) #2020/03/14
            print(time.asctime(time.localtime())) #Sat Mar 14 22:09:58 2020
            print(datetime.now())#2020-03-14 22:12:42.547164
            formatday=datetime.strptime(strTime,"%Y/%m/%d")#2019-11-28 00:00:00，strptime():字符串格式转化为日期格式
            print(formatday)
            dis=(datetime.now()-formatday).days#date格式相减
            print(dis)
            if dis>=80:
                print("请修改密码！")








