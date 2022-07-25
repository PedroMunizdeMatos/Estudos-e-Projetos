import openpyxl

book = openpyxl.workbook()
book.create_sheet('Consulta')
consulta_page = book['Consulta']

consulta_page.append(['ID Chamado', 'Problema', 'Departamento', 'Pessoa', 'Data'])
consulta_page.append([linha[0], linha[1], linha[2], linha[3], linha[6]])
