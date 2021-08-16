def leiaCNPJ():
    while True:
        numero = str(input("Digite aqui o CNPJ da empresa: "))
        if numero.isnumeric():
            print(f"Você digitou o CNPJ: {numero}")
            return numero
        else:
            print("ERRO! Digite um CNPJ apenas numerico")


def leiaNOME():
    while True:
        nome = str(input("Digite aqui o Nome da empresa: "))
        if nome:
            print(f"Você digitou o Nome da Empresa: {nome}")
            return nome
        else:
            print("ERRO! Digite um nome válido para a empresa")


def leiaAtividadePrincipal():
    while True:
        AtividadePrincipal = str(input("Digite aqui a Atividade Principal da empresa: "))
        if AtividadePrincipal:
            print(f"Você digitou a Atividade Principal: {AtividadePrincipal}")
            return AtividadePrincipal
        else:
            print("ERRO! Digite uma Atividade Principal Válida para a empresa")


def leiaAtividadesSecundarias():
    contador = 1
    lista_de_atividades = []
    while True:
        AtividadeSecundaria = ""
        prosseguir = ""

        AtividadeSecundaria = str(input(f"Digite aqui a Atividade Secundaria n°{contador} da empresa: "))
        if AtividadeSecundaria:
            print(f"Você digitou a Atividade Secundaria: {AtividadeSecundaria}")
            lista_de_atividades.append(f'{contador}. {AtividadeSecundaria}')
            contador += 1
            print(f"Atividade Adicionada com sucesso!")

            prosseguir = str(input("Deseja Adicionar mais uma Atividade Secundaria? [ S / N ]: ")).strip().upper()
            while prosseguir not in "SN" or prosseguir == "":
                prosseguir = str(input("Deseja Adicionar mais uma Atividade Secundaria? [ S / N ]: ")).strip().upper()

            if prosseguir == "N":
                if len(lista_de_atividades) == 1:
                    print("Atividade Secundaria Adicionada:")
                    print(lista_de_atividades[0])
                    return lista_de_atividades[0]
                elif len(lista_de_atividades) > 1:
                    print("Atividades Secundarias Adicionadas:")
                    for atividade in lista_de_atividades:
                        print(f"{atividade}")
                    return listToString(lista_de_atividades)

        else:
            print("ERRO! Digite uma Atividade Principal Válida para a empresa")


def leiaUF():
    uf_validas = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE",
                  "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"]
    while True:
        uf = str(input("Digite aqui a Unidade Federativa (UF) da empresa: ")).strip().upper()
        if uf in uf_validas:
            print(f"Você digitou a UF: {uf}")
            return uf
        else:
            print("ERRO! Digite uma Unidade Federativa válida para a empresa")


def leiaTELEFONE():
    ddd = str(input("Digite aqui o número de DDD do número de telefone vínculado a empresa (Somente números): "))
    while not ddd.isnumeric() or len(ddd) != 2 or ddd == '10':
        print("DDD Inválido!")
        ddd = str(input("Digite aqui o número de DDD do número de telefone vínculado a empresa (Somente números): "))
    if ddd.isnumeric() and len(ddd) == 2 and ddd != '10':
        print(f"Você digitou o DDD: {ddd}")
        while True:
            telefone = str(input("Digite aqui o telefone da empresa ( Deve conter 8 digitos ): "))
            if telefone.isnumeric() and len(telefone) == 8:
                print(f"Você digitou o número telefone: {telefone[:4]}-{telefone[4:]}")
                print(f"(DDD) + TELEFONE: ({ddd}) {telefone[:4]}-{telefone[4:]}")
                telefone_completo = f"({ddd}) {telefone[:4]}-{telefone[4:]}"
                return telefone_completo
            else:
                print("ERRO! Digite um número telefone válido (8 Digitos apenas numericos)")


def leiaEMAIL():
    while True:
        email = str(input("Digite o email da empresa: "))
        email = email.replace(" ", "")
        if '@' in email:
            continuar = str(input(f"O email '{email}' está correto? [ S / N ]: ")).strip().upper()
            while continuar not in 'SN':
                continuar = str(input(f"O email '{email}' está correto? [ S / N ]: ")).strip().upper()

            if continuar == 'S':
                return email
        else:
            print("Email inválido, tente novamente")


def leiaABERTURA():
    while True:
        dia = str(input("Digite o Dia de abertura da empresa ( 2 digitos ): "))
        if dia.isnumeric() and len(dia) == 2 and (0 < int(dia) < 32):
            print(f"Dia '{dia}' Computado com Sucesso")
            while True:
                mes = str(input("Digite o Mês de abertura da empresa ( 2 digitos ): "))
                if mes.isnumeric() and len(mes) == 2 and (0 < int(mes) < 13):
                    print(f"Mês '{mes}' Computado com Sucesso")
                    while True:
                        ano = str(input("Digite o Ano de abertura da empresa ( 4 digitos ): "))
                        if ano.isnumeric() and len(ano) == 4 and (1000 < int(ano) <= 2021):
                            print(f"ano '{ano}' Computado com Sucesso")
                            print(f"Ano de Abertura da Empresa: '{dia}/{mes}/{ano}' Computado com Sucesso")
                            return f"{dia}/{mes}/{ano}"

                        print("Ano inválido!, digite somente números")
                print("Se o valor for menor que 10, coloque o ' 0 ' na frente ( Exemplo: '01' ) ")

        print("Se o valor for menor que 10, coloque o ' 0 ' na frente ( Exemplo: '01' ) ")


def listToString(list):
    string = "\n"

    # return long string
    return str(string.join(list))
