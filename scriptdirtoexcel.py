#Script de extracción de datos de un directorio NFS y volcado de información a un excel

from openpyxl import Workbook
from openpyxl.styles import Font, Fill
import os
wb = Workbook()

dirbook = []
route = r''

dirbook = os.listdir(r'')
dirbook.pop(4)
dirbook.pop(10)

print(dirbook)

for i in dirbook:
    # xl = wb.create_sheet(title=i)
    # xl['A1'] = 'Dato1'
    # xl['B1'] = 'Dato2'
    # xl['C1'] = 'Dato3'
    fts = os.listdir(route+'\\'+i)
    print(route+'\\'+i)
    for x in fts:
        dirr = x.split()
        print(dirr[2:3])












# wb.save('test.xlsx')
# wb.close()



