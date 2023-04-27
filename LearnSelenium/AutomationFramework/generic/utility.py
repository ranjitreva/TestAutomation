import openpyxl


class Excel:

    def get_cell_value(file_path, sheet_name, row, col):
        # Open the excel/workbook file
        workbook = openpyxl.open(file_path)
        # Go to sheet --> Cell --> Get the value
        value1 = workbook[sheet_name].cell(row, col).value
        # Print the value and return it
        print("XL Cell value is :", value1)
        return value1
