
import datetime

def adicionar_tarefas(tarefas, titulo, descricao, data_vencimento):
    tarefa = {
        'Titulo': titulo,
        'Descricao': descricao,
        'Data_vencimento': data_vencimento,
    }
    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!")
    print("*************************************")

def listar_tarefas(tarefas):
    for indice, tarefa in enumerate(tarefas):
        print(f"ID Tarefa {indice + 1}")
        print(f"Titulo: {tarefa['Titulo']}")
        print(f"Descricao: {tarefa['Descricao']}")
        print(f"Data de Vencimento: {tarefa['Data_vencimento']}")
        print("*************************************")
        print("\n")

def excluir_tarefa(tarefas, indice):
    if indice >= 0 and indice < len(tarefas):
        del tarefas[indice]
        print("Tarefa deletada com sucesso!")
        print("*************************************")
    else:
        print("Índice inválido.")

def editar_tarefas(tarefas, indice, titulo, descricao, data_vencimento):
    if indice >= 0 and indice < len(tarefas):
        tarefas[indice]['Titulo'] = titulo
        tarefas[indice]['Descricao'] = descricao
        tarefas[indice]['Data_vencimento'] = data_vencimento
        print("Tarefa editada com sucesso!")
        print("**********************************")
    else:
        print("Índice inválido.")

def converter_data(data_str):
    dia, mes, ano = map(int, data_str.split('/'))
    return datetime(ano, mes, dia)

def tarefas_vencidas(tarefas, data_atual_str):
    data_atual = converter_data(data_atual_str)
    print("Tarefas vencidas:")
    for tarefa in tarefas:
        data_vencimento = converter_data(tarefa['Data_vencimento'])
        if data_vencimento < data_atual:
            print(f'Título: {tarefa["Titulo"]}')
            print(f'Descrição: {tarefa["Descricao"]}')
            print(f'Data de Vencimento: {tarefa["Data_vencimento"]}')
            print('************************************')

tarefas = []

while True:
    print("\nMenu:")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Editar Tarefa")
    print("4. Excluir Tarefa")
    print("5. Imprimir Tarefas Vencidas")
    print("6. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        titulo = input("Título da Tarefa: ")
        descricao = input("Descrição: ")
        data_vencimento = input("Data de Vencimento (DD/MM/AAAA): ")
        adicionar_tarefas(tarefas, titulo, descricao, data_vencimento)

    elif opcao == '2':
        listar_tarefas(tarefas)

    elif opcao == '3':
        indice = int(input("ID da Tarefa a ser editada: ")) - 1
        titulo = input("Novo Título: ")
        descricao = input("Nova Descrição: ")
        data_vencimento = input("Nova Data de Vencimento (DD/MM/AAAA): ")
        editar_tarefas(tarefas, indice, titulo, descricao, data_vencimento)

    elif opcao == '4':
        indice = int(input("ID da Tarefa a ser excluída: ")) - 1
        excluir_tarefa(tarefas, indice)

    elif opcao == '5':
        data_atual = input("Data atual (DD/MM/AAAA): ")
        tarefas_vencidas(tarefas, data_atual)

    elif opcao == '6':
        break

    else:
        print("Opção inválida! Escolha novamente.")
