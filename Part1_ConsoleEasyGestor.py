import requests
import backoff
from dml import *
from menu import *


CNPJS = [17895646000187, 18033552000161, 1365284000104]
contador: int = 0


@backoff.on_exception(backoff.expo, requests.exceptions.RequestException, max_tries=10, max_time=150)
def get_info(cnpj_id):
    global contador

    api_request = requests.get(f"https://www.receitaws.com.br/v1/cnpj/{cnpj_id}")

    if api_request.status_code == 429:
        contador = contador + 1

        if contador == 10:
            print("Servidor indisponível, por favor tentar novamente mais tarde.")
            return 'Servidor Indisponivel'

        print(f"Servidor Ocupado! Realizando pedido pela {contador+1}° vez... (Máximo de 10 tentativas)\n")
        raise requests.exceptions.RequestException

    json_infos = api_request.json()
    contador = 0

    if json_infos['status'] == 'ERROR' and json_infos['message'] == 'CNPJ inválido':
        print(f"Erro!\nCnpj informado: {cnpj_id},\nCnpj Inválido.\n")
        return 'CNPJ Inválido'

    return json_infos


def console_log_infos(json_infos):
    if json_infos == 'CNPJ Inválido':
        return None
    elif json_infos == 'Servidor Indisponivel':
        print("Tente novamente mais tarde! Servidor indisponível")
    else:
        print(f'CNPJ: {json_infos["cnpj"]}')
        print(f'Nome: {json_infos["nome"]}')

        print(f'Atividade Principal:\n{json_infos["atividade_principal"][0]["text"]}\n')

        print(f'Atividades Secundarias:')
        for key, infos in enumerate(json_infos["atividades_secundarias"]):
            print(f'{key+1}. {json_infos["atividades_secundarias"][key]["text"]}')
        print()

        print(f'UF: {json_infos["uf"]}')
        print(f'Telefone: {json_infos["telefone"]}')
        print(f'Email: {json_infos["email"]}')
        print(f'Data de abertura: {json_infos["abertura"]}')
        print(f'--- fim da ficha --- \n')


# Busca as Empresas pela API da Receitaws
def show_default_info():
    for CNPJ in CNPJS:
        console_log_infos(get_info(CNPJ))


def continuar():
    continuar = str(input("Operação finalizada, aperte 'Enter' até voltar ao menu principal: "))


while True:
    response = menu()
    if response == 1:
        show_default_info()
        continuar()
    elif response == 2:
        while True:
            numero = leiaCNPJ()
            console_log_infos(get_info(numero))
            continuar()
            break
    elif response == 3:
        cadastro_de_empresa_menu()
        continuar()
    elif response == 4:
        show_all_db_info()
        continuar()
    elif response == 10:
        show_relevant_info_db()
        continuar()
    elif response == 0:
        break
