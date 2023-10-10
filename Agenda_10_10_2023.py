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
        print("Aluno deletado com sucesso!")
        print("*************************************")