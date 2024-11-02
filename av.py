import pandas as pd
def cadastrar_aluno(alunos):
    nome = input("Nome do aluno: ")
    turma = int(input("Turma: "))
    aluno = {"nome": nome.upper(), "turma": turma, "faltas": 0, "notas": []}
    alunos.append(aluno)
    print(f" {nome} cadastrado com sucesso!")

def mostrar_alunos(alunos):
    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        tabela = pd.DataFrame(alunos, index=pd.RangeIndex(start=1, stop=len(alunos) +1))
        print(tabela)

def remover_aluno(alunos):
    mostrar_alunos(alunos)
    if alunos:
        idx = int(input("Digite o índice do aluno a ser removido: ")) 
        if idx >=0 and idx < len(alunos):
            removido = alunos.pop(idx)
            print(f"Aluno {removido['nome']} removido com sucesso!")
        else:
            print("Índice inválido.")

def editar_nome(aluno):
    novo_nome = input("Digite o novo nome do aluno: ")
    aluno["nome"] = novo_nome.upper()
    print("Nome atualizado com sucesso!")

def editar_turma(aluno):
    nova_turma = int(input("Digite a nova turma do aluno: "))
    aluno["turma"] = nova_turma
    print("Turma atualizada com sucesso!")

def adicionar_nota(aluno):
    nota = float(input("Digite a nota do aluno: "))
    aluno["notas"].append(nota)
    print("Nota adicionada com sucesso!")

def adicionar_falta(aluno):
    faltas = int(input("Digite a quantidade de faltas a adicionar: "))
    aluno["faltas"] += faltas
    print("Faltas adicionadas com sucesso!")

def mostrar_media(aluno):
    if aluno["notas"]:
        media = sum(aluno["notas"]) / len(aluno["notas"])
        print(f"Média das notas: {media:.2f}")
    else:
        print("O aluno não possui notas.")

def mostrar_notas(aluno):
    if aluno["notas"]:
        for nota in aluno["notas"]:
            print(nota)
    else:
        print("O aluno não possui notas.")

def mostrar_faltas(aluno):
    print(f"Faltas: {aluno['faltas']}")

def pagina_do_aluno(alunos):
    mostrar_alunos(alunos)
    if alunos:
        idx = int(input("Digite o índice do aluno: ")) -1
        if  idx >= 0 and idx < len(alunos):
            aluno = alunos[idx]
            while True:
                print("\n--- Página do Aluno ---")
                print("1. Editar nome")
                print("2. Editar turma")
                print("3. Adicionar nota")
                print("4. Adicionar falta")
                print("5. Mostrar média")
                print("6. Mostrar notas")
                print("7. Mostrar faltas")
                print("8. Voltar")
                opcao = int(input("Escolha uma opção: "))
                if opcao == 1:
                    editar_nome(aluno)
                elif opcao == 2:
                    editar_turma(aluno)
                elif opcao == 3:
                    adicionar_nota(aluno)
                elif opcao == 4:
                    adicionar_falta(aluno)
                elif opcao == 5:
                    mostrar_media(aluno)
                elif opcao == 6:
                    mostrar_notas(aluno)
                elif opcao == 7:
                    mostrar_faltas(aluno)
                elif opcao == 8:
                    break
                else:
                    print("Opção inválida.")
    else:
        print("Não existem alunos")

def menu_principal():
    alunos = []
    while True:
        print("\n--- Menu Principal ---")
        print("1. Cadastrar Aluno")
        print("2. Mostrar Alunos")
        print("3. Remover Aluno")
        print("4. Página do Aluno")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            cadastrar_aluno(alunos)
        elif opcao == "2":
            mostrar_alunos(alunos)
        elif opcao == "3":
            remover_aluno(alunos)
        elif opcao == "4":
            pagina_do_aluno(alunos)
        elif opcao == "5":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida.")


menu_principal()
