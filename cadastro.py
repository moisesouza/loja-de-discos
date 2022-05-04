import datetime
import conexao_db

def cadastro():
    while True:
        print("Cadastre suas informações")
        clientes = []
        dados = {}  # cria uma lista para adicionar o id, nome e idade da pessoa
        dados['cpf'] = str(input('CPF:'))
        dados['nomeComp'] = input('Nome: ')
        dados['idade'] = input('Idade: ')
        dados['nascimento'] = input('Data de Nascimento: ')
        dados['email'] = input('Email: ')
        dados['telefone'] = input('Telefone: ')
        return print('Cadastro realizado com sucesso! ')


cadastro()
