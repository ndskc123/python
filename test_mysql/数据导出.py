import MySQLdb
import openpyxl
book=openpyxl.load_workbook("./a.xlsx")
sheet=book['Sheet1']

list1=[]
list2=[]

db=MySQLdb.connect(host='localhost',user='root',passwd='123456',port=3306,charset='utf8')
cursor=db.cursor()
cursor.execute("show databases;")
cursor.execute("use test;")
cursor.execute("select * from xsb;")
for dates in cursor:
    for date in dates:
        list1.append(date)

for i in range(0,len(list1),8):
    b=list1[i:i+8]
    list2.append(b)
print(list2)
for row in range(1,len(list2)+1):
    for column in range(1,9):
        sheet.cell(row,column).value=list2[row-1][column-1]

book.save('./a.xlsx')
db.close()
