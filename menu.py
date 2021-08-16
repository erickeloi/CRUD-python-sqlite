from leitor_de_dados import *
from dml import *

def options_list():
    print("-" * 45)
    print(
        f"\033[1;33m 1 -\033[1;35m Buscar informações dos CNPJ's padrões (17895646000187, 18033552000161, 1365284000104) direto na API\033[m")
    print(f"\033[1;33m 2 -\033[1;35m Buscar informações de um novo CNPJ na API do Receitaws \033[m")
    print(
        f"\033[1;33m 3 - \033[1;92mCadastrar\033[1;35m Nova Empresa no nosso Banco de Dados \033[1;92m( Create )\033[m")
    print(
        f"\033[1;33m 4 -\033[1;34m Mostrar\033[1;35m \033[1;94mTodas\033[1;35m informações das Empresas Cadastradas no Banco de dados\033[1;34m ( Read )\033[m")
    print(
        f"\033[1;33m 5 - \033[1;32mAtualizar\033[1;35m Informações de Alguma Empresa no Banco de Dados \033[1;32m( Update )\033[m")
    print(
        f"\033[1;33m 6 - \033[1;31mDeletar\033[m \033[1;35mEmpresa do Banco de Dados \033[1;31m( Delete )\033[m")
    print(f"\033[1;33m 7 - \033[1;35m\033[1;34mBuscar\033[1;35m Empresa pelo CNPJ no Banco de Dados\033[m")
    print(
        f"\033[1;33m 10 -\033[1;34m Buscar\033[1;35m \033[1;93minformações Relevantes\033[1;35m das Empresas Cadastradas\033[m")
    print(f"\033[1;33m 0 -\033[1;35m Sair do Sistema \033[m")

    print("-" * 45)


def options_value():
    while True:
        try:
            option = int(input("\033[1;33mDigite sua opção:\033[m "))
            if option in range(0, 8) or option == 10:
                break
            else:
                print("Opção inexistente")
        except:
            print("Valor de opção inválido!")
            options_list()

    if option == 0:
        print("-" * 45)
        print("Volte Sempre, Obrigado!")
        print("-" * 45)

    return option


def buscar_empresa_pelo_cnpj_menu():
    print("Buscar Empresa no Banco de dados!")
    cnpj = leiaCNPJ()
    show_one_specific_company(cnpj)


def cadastro_de_empresa_menu():
    print('CADASTRO DE NOVA EMPRESA NO BANCO DE DADOS')
    print('Informações necessárias:')
    print("""\033[1;92mCNPJ (Número), \033[1;33mNome da Empresa, \033[1;92mAtividade Principal da Empresa, \033[1;33mAtividades Secundarias,
\033[1;92UUF, \033[1;33mTelefone, \033[1;92mEmail, \033[1;33mData de Abertura\033[m""")
    cnpj = leiaCNPJ()
    if name_of_one_company_db(cnpj) == []:
        nome_da_empresa = leiaNOME()
        atividade_principal = leiaAtividadePrincipal()
        atividades_secundarias = leiaAtividadesSecundarias()
        uf = leiaUF()
        telefone = leiaTELEFONE()
        email = leiaEMAIL()
        abertura = leiaABERTURA()
        print("Cadastro de nova Empresa!")
        print("Informações Da Empresa::\n")
        print(f"CNPJ: {cnpj}\nNome: {nome_da_empresa}\n"
              f"Atividade Principal:\n{atividade_principal}\n"
              f"Atividades Secundarias:\n{atividades_secundarias}\n"
              f"UF:{uf}\nTelefone da Empresa:{telefone}\nEmail:{email}\nData De Abertura: {abertura}\n")

        continuar_operacao = str(
            input(f"Deseja Cadastrar a Empresa Acima no Banco de dados? [ S / N ]: ")).strip().upper()
        while continuar_operacao not in 'SN':
            continuar_operacao = str(
                input(f"Deseja Cadastrar a Empresa Acima no Banco de dados? [ S / N ]: ")).strip().upper()
        if continuar_operacao == 'N':
            return print("Operação Cancelada!")
        elif continuar_operacao == 'S':
            print("Cadastrando Empresa no Banco de dados...")
            insert_db(cnpj, nome_da_empresa, atividade_principal, atividades_secundarias, uf, telefone, email, abertura)
            print("Cadastro Concluido com Sucesso!")

    else:
        print(f"CNPJ ja existente! Empresa: '{name_of_one_company_db(cnpj)[0][0]}' Já cadastrada!\n"
              f" Não podemos cadastrar o mesmo CNPJ duas vezes,"
              f" Atualize os dados da empresa ou Exclua ela do banco de dados!")
        print("Tente novamente!")
        option = str(input("Deseja Continuar a operação? [ S / N ]: ")).strip().upper()
        while option not in 'SN':
            option = str(input("Deseja Continuar a operação? [ S / N ]: ")).strip().upper()
        if option == "N":
            return print("Operação Cancelada!")


def atualizar_info_menu():
    lista_de_atributos_bonita = ["Nome", "Atividade Principal", "Atividades Secundarias:", "UF", "Telefone", "Email", "Data de Abertura"]
    lista_de_atributos_funcional = ["nome", "atividade_principal", "atividades_secundarias", "uf", "telefone", "email", "abertura"]

    def atualizar_atributo_no_db(cnpj, atributo_escolhido, novo_valor):
        update_db(cnpj, atributo_escolhido, novo_valor)
    while True:
        print("Atualizar alguma informação de uma empresa cadastrada no banco de dados!")
        cnpj = leiaCNPJ()

        nome_da_empresa = name_of_one_company_db(cnpj)
        if nome_da_empresa:
            print(f"\nNome da Empresa Escolhida: {nome_da_empresa[0][0]}\n")
            print("Essa é a Empresa Correta?")
            option = str(input(
                "Digite 'S' Para Continuar a Atualização de dados dessa Empresa\nOu Digite 'N' Para Cancelar a Operação\nOpção: ")).strip().upper()
            while option not in 'SN':
                option = str(input(
                    "Digite 'S' Para Continuar a Atualização de dados dessa Empresa\nOu Digite 'N' Para Cancelar a Operação\nOpção: ")).strip().upper()
            if option == 'N':
                print("Operação Cancelada! Nada foi feito!")
                break
            # Empresa certa, continuando a atualização de dados
            elif option == 'S':
                print(f"Que atributo deseja alterar dessa empresa? (O CNPJ não pode ser alterado!)")
                for index, atributo in enumerate(lista_de_atributos_bonita):
                    print(f"[{index}] - {atributo}")

                indice = int(input("Digite o índice do atributo desejado: "))
                while indice not in range(0, len(lista_de_atributos_bonita)):
                    indice = int(input("Digite o índice do atributo desejado: "))

                print(f"Atributo '{lista_de_atributos_bonita[indice]}' Selecionado")
                atributo_escolhido = lista_de_atributos_funcional[indice]

                if indice == 0:
                    print(f"Insira o Novo {lista_de_atributos_bonita[indice]} da empresa: ")

                    novo_valor = leiaNOME()

                    atualizar_atributo_no_db(cnpj, atributo_escolhido, novo_valor)
                elif indice == 1:
                    print(f"Insira o Novo {lista_de_atributos_bonita[indice]} da empresa: ")

                    novo_valor = leiaAtividadePrincipal()

                    atualizar_atributo_no_db(cnpj, atributo_escolhido, novo_valor)
                elif indice == 2:
                    print(f"Insira o Novo {lista_de_atributos_bonita[indice]} da empresa: ")

                    novo_valor = leiaAtividadesSecundarias()

                    atualizar_atributo_no_db(cnpj, atributo_escolhido, novo_valor)
                elif indice == 3:
                    print(f"Insira o Novo {lista_de_atributos_bonita[indice]} da empresa: ")

                    novo_valor = leiaUF()

                    atualizar_atributo_no_db(cnpj, atributo_escolhido, novo_valor)
                elif indice == 4:
                    print(f"Insira o Novo {lista_de_atributos_bonita[indice]} da empresa: ")

                    novo_valor = leiaTELEFONE()

                    atualizar_atributo_no_db(cnpj, atributo_escolhido, novo_valor)
                elif indice == 5:
                    print(f"Insira o Novo {lista_de_atributos_bonita[indice]} da empresa: ")

                    novo_valor = leiaEMAIL()

                    atualizar_atributo_no_db(cnpj, atributo_escolhido, novo_valor)
                elif indice == 6:
                    print(f"Insira o Novo {lista_de_atributos_bonita[indice]} da empresa: ")

                    novo_valor = leiaABERTURA()

                    atualizar_atributo_no_db(cnpj, atributo_escolhido, novo_valor)

                return print("Operação realizada com Sucesso! Informação Atualizada!")


        else:
            print(f"Erro! CNPJ: '{cnpj}'. Não encontrado")
            continuar_operacao = str(input(f"Deseja Tentar Novamente? [ S / N ]: ")).strip().upper()
            while continuar_operacao not in 'SN':
                continuar_operacao = str(input(f"Deseja Tentar Novamente? [ S / N ]: ")).strip().upper()
            if continuar_operacao == 'N':
                break
            elif continuar_operacao == 'S':
                print()


def exclusao_de_empresa_menu():
    while True:
        print("Menu De Exclusão de Empresa")
        print("Digite o CNPJ da Empresa que se deseja excluir (apenas números) ")
        cnpj = leiaCNPJ()

        nome_da_empresa = name_of_one_company_db(cnpj)
        if nome_da_empresa:
            print(f"\nNome da Empresa Escolhida: {nome_da_empresa[0][0]}\n")
            option = str(input("Digite 'S' Para Confirmar a Exclusão da Empresa\nOu Digite 'N' Para Cancelar a Operação\nOpção: ")).strip().upper()[0]
            while option not in 'SN':
                option = str(input("Digite 'S' Para Confirmar a Exclusão da Empresa\nOu Digite 'N' Para Cancelar a Operação\nOpção: ")).strip().upper()[0]
            if option == 'N':
                print("Operação Cancelada! Nada foi feito!")
                break
            elif option == 'S':
                print(f"Excluindo A Empresa {nome_da_empresa[0][0]} do Banco de Dados...")
                delete_db(cnpj)
                print("Exclusão Realizada com Sucesso!")
                break

        else:
            print(f"Erro! CNPJ: '{cnpj}'. Não encontrado")
            continuar_operacao = str(input(f"Deseja Tentar Novamente? [ S / N ]: ")).strip().upper()
            while continuar_operacao not in 'SN':
                continuar_operacao = str(input(f"Deseja Tentar Novamente? [ S / N ]: ")).strip().upper()
            if continuar_operacao == 'N':
                break
            elif continuar_operacao == 'S':
                print()


def menu():
    print("-" * 45)
    print("Console EasyGestor/ErickEloi Empresas".center(45))

    options_list()
    option = options_value()

    return option
