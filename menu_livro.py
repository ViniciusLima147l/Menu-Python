# Mensagem de boas-vindas
print("Bem vindo à Livraria do Vinícius Azevedo Lima")  

# Lista de livros e id global
lista_livro = []  # Lista que armazenará os dicionários com os livros
id_global = 0  # Controle do ID dos livros


# Função para cadastrar livro
def cadastrar_livro(id):
    print("----------------------------------------")
    print("------------ MENU CADASTRAR LIVRO ------------")
    print(f"Id do livro: {id}")
    nome = input("Por favor entre com o nome do livro: ")
    autor = input("Por favor entre com o autor do livro: ")
    editora = input("Por favor entre com a editora do livro: ")

    livro = {
        "id": id,
        "nome": nome,
        "autor": autor,
        "editora": editora
    }

    lista_livro.append(livro)  # Adiciona o dicionário à lista


# Função para consultar livros
def consultar_livro():
    while True:
        print("----------------------------------------")
        print("------------ MENU CONSULTAR LIVRO ------------")
        print("Escolha a opção desejada:")
        print("1 - Consultar Todos os Livros")
        print("2 - Consultar Livro por id")
        print("3 - Consultar Livro(s) por autor")
        print("4 - Retornar")
        opcao = input(">> ")

        if opcao == "1":
            for livro in lista_livro:
                print("----------------")
                print(f"id: {livro['id']}")
                print(f"nome: {livro['nome']}")
                print(f"autor: {livro['autor']}")
                print(f"editora: {livro['editora']}")
            print("----------------")
        elif opcao == "2":
            try:
                id_consulta = int(input("Digite o id do livro: "))
                encontrado = False
                for livro in lista_livro:
                    if livro['id'] == id_consulta:
                        print("----------------")
                        print(f"id: {livro['id']}")
                        print(f"nome: {livro['nome']}")
                        print(f"autor: {livro['autor']}")
                        print(f"editora: {livro['editora']}")
                        encontrado = True
                        break
                if not encontrado:
                    print("Id não encontrado.")
            except ValueError:
                print("Digite um valor numérico válido.")
        elif opcao == "3":
            autor_consulta = input("Digite o autor do(s) livro(s): ")
            encontrados = [livro for livro in lista_livro if livro['autor'].lower() == autor_consulta.lower()]
            if encontrados:
                for livro in encontrados:
                    print("----------------")
                    print(f"id: {livro['id']}")
                    print(f"nome: {livro['nome']}")
                    print(f"autor: {livro['autor']}")
                    print(f"editora: {livro['editora']}")
            else:
                print("Nenhum livro encontrado para este autor.")
        elif opcao == "4":
            break
        else:
            print("Opção inválida")


# Função para remover livro
def remover_livro():
    while True:
        print("----------------------------------------")
        print("------------ MENU REMOVER LIVRO ------------")
        try:
            id_remover = int(input("Digite o id do livro a ser removido: "))
            for livro in lista_livro:
                if livro['id'] == id_remover:
                    lista_livro.remove(livro)
                    print("Livro removido com sucesso!")
                    return
            print("Id inválido")
        except ValueError:
            print("Digite um valor numérico válido.")


# MENU PRINCIPAL
while True:
    print("----------------------------------------")
    print("------------ MENU PRINCIPAL ----------------")
    print("Escolha a opção desejada:")
    print("1 - Cadastrar Livro")
    print("2 - Consultar Livro(s)")
    print("3 - Remover Livro")
    print("4 - Sair")
    opcao = input(">> ")

    if opcao == "1":
        id_global += 1
        cadastrar_livro(id_global)
    elif opcao == "2":
        consultar_livro()
    elif opcao == "3":
        remover_livro()
    elif opcao == "4":
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida")
