import random
banco = [
    {"matricula": 1, "nome": "Leticia", "curso": "Java"},
    {"matricula": 2, "nome": "Humberto", "curso": "Python"}
]
mat_atual = 2
# CRUD
def adicionarAluno(nome: str, curso: str) -> None:
    global mat_atual
    mat_atual += 1
    aluno = {
        "matricula": mat_atual,
        "nome": nome,
        "curso": curso
    }
    banco.append(aluno)
    print("Aluno cadastrado com sucesso!")

def listarAlunos() -> None:
    for aluno in banco:
        print(f"Matricula: {aluno['matricula']}")
        print(f"Nome: {aluno['nome']}")
        print(f"Curso: {aluno['curso']}")
        print("---------------------------")

def buscarAlunos(matricula: int) -> None:
    existe = False
    for aluno in banco:
        if aluno['matricula'] == matricula:
            print(f"Matricula: {aluno['matricula']}")
            print(f"Nome: {aluno['nome']}")
            print(f"Curso: {aluno['curso']}")
            existe = True
    if not existe:
        print("Aluno não encontrado!")

def editarAluno(matricula: int, novo_nome: str, novo_curso: str) -> None:
    existe = False
    for aluno in banco:
        if aluno['matricula'] == matricula:
            aluno['nome'] = novo_nome
            aluno['curso'] = novo_curso
            existe = True
            print('Dados alterados com sucesso!')
    if not existe:
        print("Aluno não encontrado!")

def deletarAluno(matricula: int) -> None:
    existe = False
    for aluno in banco:
        if aluno['matricula'] == matricula:
            banco.remove(aluno)
            print('Aluno removido com sucesso!')
            existe = True
    if not existe:
        print("Aluno não encontrado!")


while True:

    opcoes = int(input("------MENU-------\n1 - Adicionar aluno\n2 - Buscar aluno\n3 - Editar aluno\n4 - Deletar aluno\n5 - Listar alunos\n6 - Sair\nSelecione uma opção "))

    if opcoes == 1:
        nome = input("Digite o nome do aluno")
        curso = input("Digite o curso do aluno")
        adicionarAluno(nome, curso)
    elif opcoes == 2:
        matricula = int(input("Digite a matricula do aluno"))
        buscarAlunos(matricula)
    elif opcoes == 3:
        matricula = int(input("Digite a matricula do aluno"))
        novo_nome = input("Digite o nome do aluno")
        novo_curso = input("Digite o curso do aluno")
        editarAluno(matricula, novo_nome, novo_curso)
    elif opcoes == 4:
        matricula = int(input("Digite a matricula do aluno"))
        deletarAluno(matricula)
    elif opcoes == 5:
        listarAlunos()
    elif opcoes == 6:
        break


