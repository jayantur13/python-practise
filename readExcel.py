import xlrd

wb = xlrd.open_workbook("excel.xls")
sheet = wb.sheet_by_index(0)  # We have 2 sheets index 0 and 1
print(sheet.cell_value(0, 0))  # Read 0,0
print(sheet.cell_value(2, 2))  # Read 2,2
print(sheet.ncols)  # No. of columns
print(sheet.nrows)  # No. of rows

# Get names of columns
for i in range(sheet.ncols):
    print(sheet.cell_value(0, i))

# Get names of rows
for i in range(sheet.nrows):
    print(sheet.cell_value(i, 0))

# Print specific row/col value
print(sheet.col_values(1))  # sheeet.row_values(1)
