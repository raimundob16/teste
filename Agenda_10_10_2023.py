#cadastro de produto
def cadastra_produto(usuarios,nome,telefone,email):
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