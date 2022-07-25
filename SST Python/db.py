import time
import mysql.connector
from mysql.connector import Error
import openpyxl

book = openpyxl.Workbook()
book.create_sheet('Consulta')
consulta_page = book['Consulta']

try:
    con = mysql.connector.connect(host='localhost',database='sst',user='root',password='')

    consulta_sql = "SELECT * FROM chamado"
    cursor = con.cursor()
    cursor.execute(consulta_sql)
    linhas = cursor.fetchall()
    print("Total de Registros retornados do Bando de Dados: ", cursor.rowcount)

    print("\nConsultando os chamados cadastrados...")
    time.sleep(1)
    consulta_page.append(['ID Chamado', 'Problema', 'Departamento', 'Pessoa'])
    for linha in linhas:
        consulta_page.append([linha[0], linha[1], linha[2], linha[3]])
except Error as e:
    print("Erro ao acessar tabela MySQL", e)
finally:
    print("\nsalvando...")
    time.sleep(1)
    book.save('Consulta_Python')
    if (con.is_connected()):
        con.close()
        cursor.close()
        print("Conexão encerrada.")
