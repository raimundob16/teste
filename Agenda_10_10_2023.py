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