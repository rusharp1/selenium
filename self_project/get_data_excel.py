import openpyxl

def get_excel_data(file_path):
    workbook = openpyxl.load_workbook(file_path)
    ws = workbook.active
    # 
    excel_value = []
    for row in ws.iter_rows(min_row = 2, max_col=6, values_only=True):
        row_list = list(row)
        if row[-1]:
            tmp = [item.strip() for item in row[-1].split(',')]
        else:
            tmp = []
        row_list[-1] = tmp
        excel_value.append(row_list)
    # 
    return excel_value