import openpyxl

path= r"E:\selenium\registration_data.xlsx"

workbook = openpyxl.load_workbook(path)

write_sheet = workbook.active

for r in range(1,6):
    for c in range(1,4):
        write_sheet.cell(row=r, column=c).value = "Welcome"

workbook.save(path)