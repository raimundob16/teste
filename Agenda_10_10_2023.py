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
        
#atualizar_usuario
def atualizar_usuario(usuarios, indice, nome, email, telefone):
     if indice >= 0 and indice < len(usuarios):
        usuarios[indice]['Nome'] = nome
        usuarios[indice]['Email'] = email
        usuarios[indice]['Telefone'] = telefone
        print("Usuario atualizado com sucesso!")
        print("**********************************")
