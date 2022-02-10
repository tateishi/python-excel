from openpyxl import Workbook

wb = Workbook()

print(wb.sheetnames)

ws = wb.active

print(ws.title)

ws.title = '名称未設定'
print(ws.title)

wb.save('downloads/sample.xlsx')