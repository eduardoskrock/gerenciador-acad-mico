#Nome: Eduardo Felipe Skrock | Curso: Análise e Desenvolvimento de Sistemas, turma 3

#Utilização do Json para armazenar os dados em um arquivo
import json

#Declaração das listas que armazenarão os elementos
lista_alunos = []
lista_professores = []
lista_turmas = []
lista_matriculas = []
lista_disciplinas = []

#Declaração da função que será o menu principal
def menuPrincipal():

    print('\33[34m\n\n====== GERENCIADOR PUC PR =====\n====== MENU PRINCIPAL =========\33[m\n')
    print('Escolha a opção desejada!')
    print('[1] Gerenciar Professores')
    print('[2] Gerenciar Alunos')
    print('[3] Gerenciar Turmas')
    print('[4] Gerenciar Matriculas')
    print('[5] Gerenciar Disciplinas')
    print('[0] Finalizar')
    return int(input('Digite a opção desejada: '))

#Declaração da função que será o menu secundário de todas as opções
def menuEspecifico():

    print('\nOlá! Escolha uma das opções abaixo:')
    print('[A] Incluir')
    print('[B] Listar ')
    print('[C] Atualizar/Editar')
    print('[D] Excluir')
    print('[E] Voltar ao Menu Principal')
    print('[F] Encerrar')
    return str(input('Digite a opção desejada: ')).upper()

#função que carrega os dados dos alunos do arquivo armazenado no Json
def carregarAlunos():
    try:
        with open ("alunos.json", "r") as file:
            lista_alunos = json.load (file)

    except FileNotFoundError:
        lista_alunos = []

    return lista_alunos

#função que salva os dados dos alunos no arquivo Json
def salvarAlunos(lista_alunos):
    with open ("alunos.json", "w") as f:
        json.dump (lista_alunos, f)

#função que faz a inclusão do codigo, nome e cpf do aluno
def incluirAluno():
    codigo_aluno = int(input ('Digite o código do aluno: '))
    nome_alunos = str(input ('Digite o nome do(a) aluno(a) a ser incluído: '))
    cpf_aluno = str(input ('Digite o CPF do aluno'))

    dados = {
        'codigo_aluno': codigo_aluno,
        'nome_aluno': nome_alunos,
        'cpf_aluno': cpf_aluno
    }

    lista_alunos.append(dados) #lista_alunos acrescentará os dados do dicionário ''dados''
    salvarAlunos(lista_alunos) #função salvarAlunos recebe os dados armazenados na lista_alunos

    print(f'O(a) aluno(a) {nome_alunos} foi salvo com sucesso.')
    input('Aperte qualquer tecla para continuar')

#Função que lista os alunos já cadastrados e, caso não tenha nenhum, o programa apontará
def listarAlunos():
    lista_aluno = carregarAlunos() #lista_alunos recebe a função carregarAlunos para acessar os dados salvos
    for dic in lista_aluno: #para o dicionário salvo na lista_alunos
        print ("* Código: {} - Nome: {} - CPF: {}".format (dic['codigo_aluno'], dic['nome_aluno'], dic['cpf_aluno'])) #mostra os dados salvos no dicionário lista_alunos
    if len (lista_aluno) == 0:  #Mostra quando não há nenhum aluno cadastrado
        print ('\033[91m' + '\nNão há alunos cadastrados!\n' + '\033[0m')

#Função que será responsável por fazer a edição dos dados e atualizar a lista
def editarAlunos():
    lista_alunos = carregarAlunos() #precisamos carregar os dados já salvos

    codigoAluno = int(input ('Digite o código do aluno a ser editado: ')) #pesquisa o código do aluno
    cadastro = False
    for item in lista_alunos: #para o item na lista_alunos
        if item['codigo_aluno'] == codigoAluno: #se o item código aluno na lista de alunos for igual ao solicitado
            print('O aluno foi encontrado. Informe os novos dados:') #continua o programa e pede os novos dados
            codigo_aluno = int(input ('Novo código: '))
            nome_aluno = str(input ('Novo nome: '))
            cpf_aluno = str(input ('Novo CPF: '))

            item['codigo_aluno'] = codigo_aluno #o item codigo_aluno será alterado e substituido na lista
            item['nome_aluno'] = nome_aluno
            item['cpf_aluno'] = cpf_aluno
            salvarAlunos(lista_alunos) #responsável por atualizar os dados na lista_alunos
            print('Os dados foram atualizados! Obrigado')

            cadastro = True
            break #interrompe o programa e finaliza a atualização
    if not cadastro: #caso nao localize nenhum codigo na lista_alunos, mostra a mensagem abaixo
        print ('Infelizmente o cadastro não foi encontrado.')

#Função responsável por excluir o aluno
def excluirAluno():
    lista_alunos = carregarAlunos () #carrega os alunos da lista_alunos já salvos
    codigoAluno = int(input('Qual é o código do(a) aluno(a) a ser removido?')) #pede o código e faz a validação o código na lista_alunos
    cadastro = False

    for item in lista_alunos: #para o item na lista_alunos
        if item['codigo_aluno'] == codigoAluno: #se o item for igual
            print ('Aluno localizado. Excluindo da lista.')
            lista_alunos.remove(item) #remove o item da lista_alunos
            salvarAlunos (lista_alunos) #atualiza o arquivo e exclui o registro da lista
            break #pausa o processo
    else: #se não for localizado, mostra a mensagem abaixo:
        print('O aluno não foi localizado. Digite um código válido')

#Aqui começa o mesmo processo que fiz anteriormente nos 'alunos''
#Como não era obrigatorio, optei em não modularizar e não fazer todas as funcionalidades na reaproveitando a função pois senti dificuldade na versão 2 que fiz paralelo a esta.
def carregarProfessores():
    try:
        with open ("professores.json", "r") as file:
            lista_professores = json.load (file)

    except FileNotFoundError:
        lista_professores = []

    return lista_professores

def salvarProfessores(lista_professores):
        with open("professores.json", "w") as f:
            json.dump(lista_professores, f)

def incluirProfessores():
    codigo_professor = int(input ('Digite o código do(a) professor(a): '))
    nome_professor = str(input ('Digite o nome do(a) professor(a) a ser incluído: '))
    cpf_professor = str(input ('Digite o CPF do(a) professor(a)'))

    dados = {
        'codigo_professor': codigo_professor,
        'nome_professor': nome_professor,
        'cpf_professor': cpf_professor
    }

    lista_professores.append(dados)
    salvarProfessores(lista_professores)

    print (f'O(a) professor(a) {nome_professor} foi salvo com sucesso.')  # usando o format, conseguimos incluir o nome do aluno dentro da string, através dos {}, mostrando o nome recém cadastrado.
    input ('Aperte qualquer tecla para continuar')



def listarProfessores():
    lista_professores = carregarProfessores()
    for dic in lista_professores:
        print ("* Código: {} - Professor(a): {} - CPF: {}".format (dic['codigo_professor'], dic['nome_professor'], dic['cpf_professor']))
    if len (lista_professores) == 0:  # MOSTRA QUANDO NÃO HOUVER ALUNOS LISTADOS
        print ('\033[91m' + '\nNão há docentes cadastrados!\n' + '\033[0m')


def editarProfessores():
    lista_professores = carregarProfessores()

    codigoProfessor = int (input ('Digite o código do docente a ser editado: '))
    cadastro = False
    for item in lista_professores:
        if item['codigo_professor'] == codigoProfessor:
            print('O docente foi encontrado. Informe os novos dados:')
            codigo_professor = int (input ('Novo código: '))
            nome_professor = str (input ('Novo nome: '))
            cpf_professor = str (input ('Novo CPF: '))

            item['codigo_professor'] = codigo_professor
            item['nome_professor'] = nome_professor
            item['cpf_aluno'] = cpf_professor
            salvarProfessores(lista_professores)
            print('Os dados foram atualizados! Obrigado')

            cadastro = True
            break
    if not cadastro:
        print ('\033[91m' + '\nNão há docentes cadastrados!\n' + '\033[0m')

def excluirProfessores():
    lista_professores = carregarProfessores ()
    codigoProfessor = int(input('Qual é o código do(a) docente a ser removido?'))
    cadastro = False

    for item in lista_professores:
        if item['codigo_professor'] == codigoProfessor:
            print ('Docente localizado. Excluindo da lista.')
            lista_professores.remove(item)
            salvarProfessores (lista_professores)
            break
    else:
        print ('\033[91m' + '\nDocente não localizado. Tente novamente!\n' + '\033[0m')

def carregarTurmas():
    try:
        with open ("turmas.json", "r") as file:
            lista_turmas = json.load (file)

    except FileNotFoundError:
        lista_turmas = []

    return lista_turmas

def salvarTurmas(lista_turmas):
        with open("turmas.json", "w") as f:
            json.dump(lista_turmas, f)

def incluirTurmas():
    print ('\n\n=== INCLUIR TURMA ===\n\n')

    lista_professores = carregarProfessores()
    lista_disciplinas = carregarDisciplinas()
    lista_turmas = carregarTurmas()

    codigo_professor = int (input ('Digite o código do professor: '))
    #Verifica se o código do professor está na lista de professores
    if not any (codigo_professor == dic['codigo_professor'] for dic in lista_professores):
        print ('Professor não encontrado. Cadastre o professor ou tente novamente.')
        return

    codigo_disciplina = int (input ('Código da disciplina: '))
    #Verifica se o código da disciplina está na lista de disciplinas
    if not any (codigo_disciplina == dic['codigo_disciplina'] for dic in lista_disciplinas):
        print ('Código da disciplina  não encontrado. Operação cancelada.')
        return

    codigo_turma = int(input ('Digite o código da turma: '))
    #Salva a turma com os dados informados e verificados anteriormente
    turma = {
        'codigo_professor': codigo_professor,
        'codigo_disciplina': codigo_disciplina,
        'codigo_turma': codigo_turma
    }

    lista_turmas.append(turma)
    salvarTurmas(lista_turmas)
    print ('Matrícula incluída com sucesso.')
    input ('Aperte qualquer tecla para continuar.')

def listarTurmas():
    lista_turmas = carregarTurmas()
    for dic in lista_turmas:
        print ("*Turma: {} - Professor: {} - Disciplina: {}".format (dic['codigo_turma'], dic['codigo_professor'], dic['codigo_disciplina'] ))
    if len (lista_turmas) == 0:  #Mostra quando não tiver turmas cadastradas
        print ('\033[91m' + '\nNão há Turmas cadastradas! Tente novamente\n' + '\033[0m')

def editarTurmas():
    print ('\033[91m' + 'Utilize o menu principal para alterar dados\nde PROFESSORES e DISCIPLINAS' + '\033[0m')
    lista_turmas = carregarTurmas()

    codigoTurma = int(input('Digite o código da turma: '))
    cadastro = False
    for item in lista_turmas:
        if item['codigo_turma'] == codigoTurma:
            print('A turma foi encontrada. Informe os novos dados:')
            codigo_turma = int(input ('Novo código turma: '))
            item['codigo_turma'] = codigo_turma

            salvarTurmas(lista_turmas)
            print('Os dados foram atualizados! Obrigado')

            cadastro = True
            break
    if not cadastro:
        print ('\033[91m' + '\nA turma não foi localizada. Tente novamente!\n' + '\033[0m')

def excluirTurmas():
    lista_turmas = carregarTurmas()
    codigoTurma = int(input('Qual é o código da turma a ser removida?'))
    cadastro = False

    for item in lista_turmas:
        if item['codigo_turma'] == codigoTurma:
            print ('Turma localizado. Excluindo...')
            lista_turmas.remove(item)
            salvarTurmas(lista_turmas)
            break
    else:
        print ('\033[91m' + '\nA turma não foi localizada. Tente novamente!\n' + '\033[0m')

def carregarMatriculas():
    try:
        with open ("matriculas.json", "r") as file:
            lista_matriculas = json.load (file)

    except FileNotFoundError:
        lista_matriculas = []

    return lista_matriculas

def salvarMatriculas(lista_matriculas):
    with open ("matriculas.json", "w") as f:
        json.dump (lista_matriculas, f)

def incluirMatricula():
    print ('\n\n=== INCLUIR MATRÍCULA ===\n\n')
    lista_matriculas = carregarMatriculas()
    lista_turmas = carregarTurmas()
    lista_alunos = carregarAlunos()

    codigo_turma = int(input('Digite o código da turma: '))
    #Verifica se o código da turma existe na lista de turmas
    if not any (codigo_turma == dic['codigo_turma'] for dic in lista_turmas):
        print ('Turma não encontrado. Cadastre uma turma e tente novamente.')
        return

    codigo_aluno = int(input('Código do aluno: '))
    #Verifica se o código do aluno existe na lista de alunos
    if not any (codigo_aluno == dic['codigo_aluno'] for dic in lista_alunos):
        print ('Código do estudante não encontrado. Operação cancelada.')
        return

    matricula = {
        'codigo_turma': codigo_turma,
        'codigo_aluno': codigo_aluno
    }

    lista_matriculas.append (matricula)
    salvarMatriculas(lista_matriculas)
    print ('Matrícula incluída com sucesso.')
    input('Aperte qualquer tecla para continuar.')

def listarMatriculas():
    lista_matriculas = carregarMatriculas()
    for dic in lista_matriculas:
        print("*\n Código turma: {} - Código aluno: {}".format (dic['codigo_turma'], dic['codigo_aluno']))
    if len (lista_matriculas) == 0:
        print('\033[91m' + '\nNão há matrículas cadastradas! Tente novamente\n' + '\033[0m')

def editarMatricula():
    print ('\033[91m' + '\nERRO! A MATRICULA É A RELAÇÃO DO ALUNO E SUA TURMA.' + '\033[0m')
    print('1 - Mude os dados através do menu "alunos".')
    print ('\033[91m' + '2 - Exclua a matrícula com o código do aluno ou adicione uma nova.' + '\033[0m')


def excluirMatriculas():
    lista_matriculas = carregarMatriculas()
    codigoAluno = int(input('Qual o código do aluno que você quer remover?'))
    cadastro = False

    for item in lista_matriculas:
        if item['codigo_aluno'] == codigoAluno:
            print ('Matricula localizada. Excluindo...')
            lista_matriculas.remove(item)
            salvarMatriculas(lista_matriculas)
            break
    else:
        print ('\033[91m' + '\nA matricula não foi localizada. Tente novamente!\n' + '\033[0m')

def carregarDisciplinas():
    try:
        with open ("disciplinas.json", "r") as file:
            lista_disciplinas = json.load (file)

    except FileNotFoundError:
        lista_disciplinas = []

    return lista_disciplinas

def salvarDisciplinas(lista_disciplinas):
    with open ("disciplinas.json", "w") as f:
        json.dump (lista_disciplinas, f)

def incluirDisciplinas():
    codigo_disciplina = int(input ('Digite o código da disciplina: '))
    nome_disciplina = str(input ('Digite o nome da disciplina:'))

    dados = {
        'codigo_disciplina': codigo_disciplina,
        'nome_disciplina': nome_disciplina,
    }

    lista_disciplinas.append(dados)
    salvarDisciplinas(lista_disciplinas)
    input ('Dados salvos! Aperte qualquer tecla para continuar')

def listarDisciplinas():
    lista_disciplinas = carregarDisciplinas()
    for dic in lista_disciplinas:
        print ("* Código Disciplina: {} - Nome Disciplina: {} ".format (dic['codigo_disciplina'], dic['nome_disciplina']))
    if len (lista_disciplinas) == 0:  # MOSTRA QUANDO NÃO HOUVER ALUNOS LISTADOS
        print ('\033[91m' + '\nNão há turmas cadastradas! Tente novamente\n' + '\033[0m')


def editarDisciplinas():
    lista_disciplinas = carregarDisciplinas()

    codigoDisciplina = int(input('Digite o código da disciplina a ser editada: '))
    cadastro = False
    for item in lista_disciplinas:

        if item['codigo_disciplina'] == codigoDisciplina:
            print('A disciplina foi encontrada. Informe os novos dados:')
            codigo_disciplina = int(input ('Novo código disciplina: '))
            nome_disciplina = str(input ('Novo nome disciplina: '))

            item['codigo_disciplina'] = codigo_disciplina
            item['nome_disciplina'] = nome_disciplina
            salvarDisciplinas(lista_disciplinas)
            print('Os dados foram atualizados! Obrigado')

            cadastro = True
            break
    if not cadastro:
        print ('\033[91m' + '\nA disciplina não foi localizada. Tente novamente!\n' + '\033[0m')

def excluirDisciplinas():
    lista_disciplinas = carregarDisciplinas()
    codigoDisciplina = int(input('Qual é o código da disciplina a ser removida?'))
    cadastro = False

    for item in lista_disciplinas:
        if item['codigo_disciplina'] == codigoDisciplina:
            print ('Disciplina localizada. Excluindo...')
            lista_disciplinas.remove(item)
            salvarDisciplinas(lista_disciplinas)
            break
    else:
        print ('\033[91m' + '\nA disciplina não foi localizada. Tente novamente!\n' + '\033[0m')


menu_principal = 1
while menu_principal != 0:
    menu_principal = menuPrincipal()

    if menu_principal == 1:
        print('===== GERENCIAR PROFESSORES =====')
        menu_professores = 'A'
        while menu_professores != 'Z':
            menu_professores = menuEspecifico().upper()

            if menu_professores == 'A':
                menu_professores = incluirProfessores()

            elif menu_professores == 'B':
                menu_professores = listarProfessores()
            elif menu_professores == 'C':
                menu_professores = editarProfessores()
            elif menu_professores == 'D':
                menu_professores = excluirProfessores()
            elif menu_professores == 'E':
                break #Caso o usuário deseje voltar ao menu principal, o comando break finaliza o laço de repetição destas condicionais e volta ao laço do meu principal
            elif menu_professores == 'F':
                menu_principal = 0
                print ('O programa foi finalizado.')
                break

            else:
                print('Digite a opção correspondente ao que você deseja.')
                input('Aperte qualquer tecla') #interrompe o laço até que o usuário degite quaquer tecla
                #usando o Upper lá na variável 'Menu_professores', independente da grafia que o usuario usou para insira a letra, ela será um caractere maiusculo.

    elif menu_principal == 2:
        print('\n===== GERENCIAR ALUNOS =====')
        menu_alunos = 'A'
        while menu_alunos != 'Z':
            menu_alunos = menuEspecifico()

            if menu_alunos == 'A':
                menu_alunos = incluirAluno()

            elif menu_alunos == 'B':
                menu_alunos = listarAlunos()

            elif menu_alunos == 'C':
                menu_alunos = editarAlunos()

            elif menu_alunos == 'D':
                menu_alunos = excluirAluno()

            elif menu_alunos == 'E':
                break
            elif menu_alunos == 'F':
                menu_principal = 0
                print('O programa foi finalizado.')
                break
            else:
                print('Digite a opção correspondente ao que você deseja.')


    elif menu_principal == 3:

        print('\n===== GERENCIAR TURMAS =====\n')
        print('\033[91m' + 'ATENÇÃO! Para cadastrar TURMA\né necessário cadastrar previamente PROFESSOR e DISCIPLINA' + '\033[0m')
        menu_turmas = 'A'

        while menu_turmas != 'Z':
            menu_turmas = menuEspecifico()

            if menu_turmas   == 'A':
                menu_turmas = incluirTurmas()

            elif menu_turmas == 'B':
                    menu_turmas = listarTurmas()

            elif menu_turmas == 'C':
                    menu_turmas = editarTurmas()


            elif menu_turmas == 'D':
                    menu_turmas = excluirTurmas()


            elif menu_turmas == 'E':
                break

            elif menu_turmas == 'F':
                menu_principal = 0
                print ('O programa foi finalizado.')
                break

            else:
                print('Digite a opção correspondente ao que você deseja.')


    elif menu_principal == 4:
        print('\n===== GERENCIAR MATRICULAS =====\n')
        print('\033[91m' + 'ATENÇÃO! Para cadastrar a matrícula\né necessário cadastrar previamente TURMA e ALUNO' + '\033[0m')
        menu_matriculas = 'A'
        while menu_matriculas != 'Z':
            menu_matriculas = menuEspecifico ()

            if menu_matriculas == 'A':
                menu_matriculas = incluirMatricula()

            elif menu_matriculas == 'B':
                menu_matriculas = listarMatriculas()

            elif menu_matriculas == 'C':
                menu_matriculas = editarMatricula()

            elif menu_matriculas == 'D':
                menu_matriculas = excluirMatriculas()

            elif menu_matriculas == 'E':
                break
            elif menu_matriculas == 'F':
                menu_principal = 0
                print('O programa foi finalizado.')
                break
            else:
                print('Digite a opção correspondente ao que você deseja.')
    elif menu_principal == 5:
        print('===== GERENCIAR DISCIPLINAS =====')
        menu_disciplinas = 'A'
        while menu_disciplinas != 'Z':
            menu_disciplinas = menuEspecifico()

            if menu_disciplinas == 'A':
                menu_disciplinas = incluirDisciplinas()

            elif menu_disciplinas == 'B':
                menu_disciplinas = listarDisciplinas()

            elif menu_disciplinas == 'C':
                menu_disciplinas = editarDisciplinas()

            elif menu_disciplinas == 'D':
                menu_disciplinas = excluirDisciplinas()

            elif menu_disciplinas == 'E':
                break
            elif menu_disciplinas == 'F':
                menu_principal = 0
                print('O programa foi finalizado.')
                break
            else:
                print('Digite a opção correspondente ao que você deseja.')
    elif menu_principal == 0:
        print('Encerrando...')
        break
    else:
        print('Opção inválida. Escolha o número da opção desejada.')