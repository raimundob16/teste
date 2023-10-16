import csv

# Função para cadastrar um novo usuário
def cadastra_usuario(usuarios, nome, telefone, email):
    usuario = {
        'Nome': nome,
        'Telefone': telefone,
        'Email': email,
    }
    usuarios.append(usuario)

# Função para salvar os usuários em um arquivo CSV
def salvar_usuarios(usuarios):
    with open('usuarios.csv', 'w', newline='') as arquivo_csv:
        campos = ['Nome', 'Telefone', 'Email']
        escritor_csv = csv.DictWriter(arquivo_csv, fieldnames=campos)
        escritor_csv.writeheader()
        for usuario in usuarios:
            escritor_csv.writerow(usuario)

# Função principal
def main():
    usuarios = []
    
    while True:
        print("\nEscolha uma opção:")
        print("1. Cadastrar usuário")
        print("2. Imprimir usuários")
        print("3. Sair")

        escolha = input("Opção: ")

        if escolha == '1':
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("E-mail: ")
            cadastra_usuario(usuarios, nome, telefone, email)
            print("Usuário cadastrado com sucesso.")
        elif escolha == '2':
            for usuario in usuarios:
                print(f"Nome: {usuario['Nome']} | Telefone: {usuario['Telefone']} | E-mail: {usuario['Email']}")
        elif escolha == '3':
            salvar_usuarios(usuarios)
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
