# -*- coding: UTF-8
import mysql.connector

connection = mysql.connector.connect(host='localhost', user='root', password='', database='mysql', charset='utf8')
cursor = connection.cursor(dictionary=True)  
cursor.execute("CREATE TABLE `calculadora` (`id` SMALLINT PRIMARY KEY AUTO_INCREMENT, `nome` VARCHAR(30) NOT NULL, `altura` FLOAT(20) NOT NULL, `peso` FLOAT(20) NOT NULL, `imc` FLOAT(20) NOT NULL);")
cursor.execute("INSERT INTO `calculadora` (`nome`, `altura`, `peso`, `imc`) VALUES ('Jucelino', '1.15', '45', '34.0313');")
cursor.execute("INSERT INTO `calculadora` (`nome`, `altura`, `peso`, `imc`) VALUES ('Cláudia', '1.45', '55', '26.1616');")
cursor.execute("INSERT INTO `calculadora` (`nome`, `altura`, `peso`, `imc`) VALUES ('Thiago', '1.55', '65', '27.0613');")
cursor.execute("INSERT INTO `calculadora` (`nome`, `altura`, `peso`, `imc`) VALUES ('Pedro', '1.65', '55', '20.0216');")
cursor.execute("INSERT INTO `calculadora` (`nome`, `altura`, `peso`, `imc`) VALUES ('Flávio', '1.85', '95', '20.0216');")
cursor.execute("UPDATE `calculadora` SET `altura` = '1.71' WHERE id = '4';")
cursor.execute("DELETE FROM `calculadora` WHERE `id` = 1")
connection.commit() 

print("Bem vindo ao calculador de IMC!")

nome = str(input("Digite seu nome:"))

altura = float(input("Digite sua altura em metros: "))

peso = float(input("Digite seu peso em Kg: "))
 
imc = peso / altura**2
 
print("Seu IMC é: %.4f" % imc)
 
if imc < 16:
    print("Você está em Magreza grave")
elif imc < 17:
    print("Você está em Magreza moderada")
elif imc < 18.5:
    print("Você está em Magreza leve")
elif imc < 25:
    print("Você está Saudável")
elif imc < 30:
    print("Você está em Sobrepeso")
elif imc < 35:
    print("Você está em Obesidade Grau I")
elif imc < 40:
    print("Você está em Obesidade Grau II (severa)")
else:
    print("Você está em Obesidade Grau III (mórbida)")
    
cursor.execute("INSERT INTO calculadora(nome, altura, peso, imc) VALUES('{}', {}, {}, {})".format(nome, altura, peso, imc))
connection.commit() 