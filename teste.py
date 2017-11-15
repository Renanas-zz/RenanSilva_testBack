import sqlite3
#Criando um arquivo do tipo .db e fazendo uma referencia de cursor na variavel "c"
connection = sqlite3.connect('teste.db')
c = connection.cursor()

'''Criando variaveis para poder efetuar os cálculos necessários para exibir a média de vl_total 
   dos customers'''
soma=0.0
cont=0

#SQL
#Criando a tabela conforme documentação usando o banco SQLite
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS tb_customer_account(id_customer INTEGER PRIMARY KEY, \
              cpf_cnpj VARCHAR(11) NOT NULL, nm_customer VARCHAR(40) NOT NULL,\
              is_active BOOLEAN NOT NULL, vl_total REAL NULL)')

create_table()

#Fazendo dez inserts para alimentar a tabela para manipular os dados com uma rica base de dados
def dataentry():
    c.execute('INSERT INTO tb_customer_account VALUES (2000,"11122233344","Renan Silva",1,1800.53)')

    c.execute('INSERT INTO tb_customer_account VALUES (400,"22211177799","João Souza",1,1730.42)')

    c.execute('INSERT INTO tb_customer_account VALUES (1789,"56378190457","Maria Machado",1,560.00)')

    c.execute('INSERT INTO tb_customer_account VALUES (2120,"88877766655","Paulo Oliveira",1,280.76)')

    c.execute('INSERT INTO tb_customer_account VALUES (1903,"67583192875","Pedro Bandeira",0,788.12)')

    c.execute('INSERT INTO tb_customer_account VALUES (1500,"14167398724","Juliana Tonti",0,3079.64)')

    c.execute('INSERT INTO tb_customer_account VALUES (890,"67987183711","Larissa Aguiar",1,59.87)')

    c.execute('INSERT INTO tb_customer_account VALUES (2891,"98367387193","Henrique Ventura",0,362.90)')

    c.execute('INSERT INTO tb_customer_account VALUES (1682,"76910397588","Leandro Mitter",1,783.13)')

    c.execute('INSERT INTO tb_customer_account VALUES (2700,"17391877344","Victor Gonçalves",1,1134.46)')

    connection.commit()

dataentry()

#SQL
sql = 'SELECT vl_total FROM tb_customer_account WHERE nm_customer = ?'

def read_tb_customer_account(wordUsed):
    for row in c.execute(sql, (wordUsed,)):
        print(row)

#SQL
c.execute("""SELECT vl_total FROM tb_customer_account WHERE
          id_customer >= 1500 and id_customer <= 2700 and vl_total >= 560.00;""")
'''Coletando os valores que devem ser usados para o cálculo da média e colocando na variavel "soma"
   e somando o "cont"(contador) para a divisão da média.'''
for linha in c.fetchall():
    desempacotador=linha[0]
    soma= soma+desempacotador
    cont= cont+1

media = soma/cont

print('A média de vl_total dos customers que tenham um saldo maior que R$560.00 e '
      'id entre 1500 e 2700 é igual a R${:.2f}'.format(media))

c.execute("""SELECT * FROM tb_customer_account WHERE
          id_customer >= 1500 and id_customer <= 2700 and vl_total >= 560.00 ORDER BY vl_total DESC;""")
'''Exibindo os clientes que participaram do cáculo da média'''
print('Os costumers que participaram da média são...')
for linha in c.fetchall():
    print(linha)
