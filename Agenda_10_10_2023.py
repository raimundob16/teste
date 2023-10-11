#cadastro de produto
def cadastra_usuario(usuarios,nome,telefone,email):
    usuario={
                'Nome' : nome,
                'Telefone' : telefone,
                'Email' : email,
            }
    usuarios.append(usuario)
    print("Usuario cadastrado com sucesso!")
    print("*************************************")

#imprimir_usuario
def imprimir_usuario(usuario):
    for indice, usuario in enumerate(usuario):
        print(f"ID usuario {indice + 1}")
        print(f"Nome {usuario['Nome']}")
        print(f"Telefone {usuario['Telefone']}")
        print(f"Email {usuario['Email']}")
        print("*************************************")
        print("\n")



#deletar
def deletar_usuario(usuarios,indice):
    if indice >= 0 and indice < len(usuarios):
        del usuarios[indice]
        print("Usuario deletado com sucesso!")
        print("*************************************")

        

#atualizar_usuario
def atualizar_usuario(usuarios, indice, nome, email, telefone):
     if indice >= 0 and indice < len(usuarios):
        usuarios[indice]['Nome'] = nome
        usuarios[indice]['Email'] = email
        usuarios[indice]['Telefone'] = telefone
        print("Usuario atualizado com sucesso!")
        print("**********************************")

usuarios = []

while True:
    print("\n Menu")
    print("1 - Cadastrar Usuario")
    print("2 - Imprimir Usuario")
    print("3 - Atualizar Usuario")
    print("4 - Deletar Usuario")
    print("5 - Sair")

    opcao = input("Escolha a opcao desejada: ")

    if opcao == '1':
        nome = input("Digite o nome do usuario: ")
        telefone = int(input("Digite o telefone do usuario: "))
        email = input("Digite o email do usuario: ")
        cadastra_usuario(usuarios,nome,telefone,email)
    elif opcao == '2':
        print(usuarios)
    elif opcao == '3':
        indice = int(input("Digite o ID do usuario: "))
        if 0 <= indice - 1 < len(usuarios):
            nome = input("Digite o nome do usuario: ")
            telefone = int(input("Digite o telefone do usuario: "))
            mail = input("Digite o email do usuario: ")
            atualizar_usuario(usuarios, indice, nome, email, telefone)
    elif opcao == '4':
        indice = int(input("Digite o ID do usuario para deletar: "))
        if 0 <= indice - 1 < len(usuarios):
            deletar_usuario(usuarios, indice - 1)

    elif opcao == '5':
        break
    else:
        print("Opcao Invalida!")