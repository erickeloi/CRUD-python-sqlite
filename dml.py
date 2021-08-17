"""
DML - Data Manipulation Language
     'Linguagem Manipulação de Dados'

C - CREATE / Insert
R - READ / Select
U - UPDATE / Update
D - DELETE / Delete
"""
import sqlite3


def commit_close(operacao):
    def decorator(*args):
        banco = sqlite3.connect('empresas.db')
        cursor = banco.cursor()
        sql = operacao(*args)
        cursor.execute(sql)
        banco.commit()
        banco.close()

    return decorator


# sql_command = """CREATE TABLE Empresas (cnpj integer not null primary key, nome text,
# atividade_principal text not null, atividades_secundarias,
# uf text not null, telefone text, email text, abertura text not null)"""

@commit_close
def insert_db(cnpj: int or str, nome: str, atividade_principal: str, atividades_secundarias,
              uf: str, telefone: str, email: str, abertura: str):
    return f"""INSERT INTO Empresas(cnpj, nome, atividade_principal, atividades_secundarias, uf, telefone, email, abertura) 
    VALUES('{cnpj}', '{nome}', 
    '{atividade_principal}', '{atividades_secundarias}', '{uf}', '{telefone}', '{email}', '{abertura}')"""


@commit_close
def update_db(cnpj, atributo, novo_valor):
    return f"""
    UPDATE Empresas SET {atributo} = '{novo_valor}' WHERE cnpj = '{cnpj}'
    """


@commit_close
def delete_db(cnpj):
    return f"""DELETE FROM Empresas WHERE cnpj = '{cnpj}'"""


def read_all_info_db():
    banco = sqlite3.connect('empresas.db')
    cursor = banco.cursor()
    sql = "SELECT * FROM Empresas"
    cursor.execute(sql)
    dados = cursor.fetchall()
    banco.close()
    return dados


def show_all_db_info():
    dados = read_all_info_db()
    all_db_atributes_styled = ["CNPJ:", "Nome:", "Atividade Principal:\n", "Atividades Secundarias:\n", "UF:",
                               "Telefone:", "Email:", "Data de Abertura:"]
    for dado in dados:
        for index, info in enumerate(dado):
            if index == 2 or index == 3:
                print(f"{all_db_atributes_styled[index]} {info}\n")
            else:
                print(f"{all_db_atributes_styled[index]} {info}")
        print("--- fim da ficha ----\n")


def relevant_info_db():
    banco = sqlite3.connect('empresas.db')
    cursor = banco.cursor()
    sql = f"SELECT cnpj, nome, atividade_principal, atividades_secundarias FROM Empresas"
    cursor.execute(sql)
    dados = cursor.fetchall()
    banco.close()
    return dados


def show_relevant_info_db():
    print("Informações Relevantes:\n")
    print("Quais são as empresas cadastradas?")
    print("Quais serviços uma empresa disponibiliza?")
    print("Quais prestações de serviço foram feitas por uma dada empresa?\n")
    print("Mostrando Empresas e Serviços...\n")

    relevant_db_atributes_styled = ["CNPJ:", "Nome:", "Atividade Principal:\n", "Atividades Secundarias:\n"]
    dados = relevant_info_db()

    for dado in dados:
        for index, info in enumerate(dado):
            if index == 2 or index == 3:
                print(f"\n{relevant_db_atributes_styled[index]} {info}\n")
            else:
                print(f"{relevant_db_atributes_styled[index]} {info}")
        print("--- fim da ficha ---\n")


def find_one_specific_company(cnpj):
    banco = sqlite3.connect('empresas.db')
    cursor = banco.cursor()
    sql = f"SELECT * FROM Empresas WHERE cnpj = '{cnpj}'"
    cursor.execute(sql)
    dados = cursor.fetchall()
    banco.close()
    return dados


def show_one_specific_company(cnpj):
    dados = find_one_specific_company(cnpj)
    if dados:
        print("\nEmpresa Encontrada!\n")
        all_db_atributes_styled = ["CNPJ:", "Nome:", "Atividade Principal:\n", "Atividades Secundarias:\n", "UF:",
                                   "Telefone:", "Email:", "Data de Abertura:"]
        for dado in dados:
            for index, info in enumerate(dado):
                if index == 2 or index == 3:
                    print(f"{all_db_atributes_styled[index]} {info}\n")
                else:
                    print(f"{all_db_atributes_styled[index]} {info}")
            print("--- fim da ficha ----\n")

    else:
        print("Empresa não Cadastrada | Não Encontrada!")


def name_of_one_company_db(cnpj):
    banco = sqlite3.connect('empresas.db')
    cursor = banco.cursor()
    sql = f"SELECT nome FROM Empresas WHERE cnpj = '{cnpj}'"
    cursor.execute(sql)
    dados = cursor.fetchall()
    banco.close()
    return dados


def all_company_names_db():
    banco = sqlite3.connect('empresas.db')
    cursor = banco.cursor()
    sql = f"SELECT cnpj, nome FROM 'Empresas'"
    cursor.execute(sql)
    dados = cursor.fetchall()
    banco.close()
    return dados


def show_all_company_names():
    dados = all_company_names_db()
    if dados:
        print("Busca Realizada Com Sucesso!")
        print("Empresas Cadastradas:\n")

        for index, dado in dados:
            print(f"CNPJ: {index}")
            print(f"Nome: {dado}\n")
        print("Anote o CNPJ da Empresa que deseja Fazer uma Operação Específica!!!\n")
    else:
        print("Erro! Banco de Dados Vazio | Empresas Não encontradas")


