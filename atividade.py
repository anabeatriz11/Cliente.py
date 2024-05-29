class exercicio:
    def __init__(self):
       print('')
    
    def exercicio1(self):
        nomeFuncio = "Ana"
        idade = 17
        salario = 3800
        cargo = "diretora geral"
        turno = "matutino"
        setor = "RH"
        print("Funcionaria:", nomeFuncio)
        print("idade:", idade)
        print("salario:", salario)
        print("cargo:",  cargo)
        print("turno:", turno)
        print("setor:", setor)

    def exercicio2(self):
        nomeEscola = "Estadual"
        estado = "Parana"
        numProfes = 30
        cidade = "Cruzeiro do Oeste"
        numMili = 4
        logradouro = "Rua Tal"
        numero = 43
        numAlunos = 500
        colegioMilitar = "True"
        disciplinas = "port", "ing", "mat", "art", "geo"
        print("Escola:", nomeEscola)
        print("Estado:", estado)
        print("Professores:", numProfes)
        print("Cidade:", cidade)
        print("Militares:", numMili)
        print("Local:", logradouro)
        print("Numero endereco:", numero)
        print("Numero de alunos:",numAlunos)
        print("Colegio Militar?:", colegioMilitar)
        print("As disciplinas sao:", disciplinas)

    def exercicio3(self):
        valor1 = 10
        valor2 = 5
        valor3 = "2"  
        valor4 = 8
        valor5 = -5
        soma1 = valor1 + valor2
        soma2 = valor1 + valor2 + valor4
        soma3 = valor1 + valor2 - valor5
        soma4 = valor1 + valor3
        soma5 = valor1 * valor2
        soma6 = (valor4 * valor2)/2
        soma7 = (valor1 + valor2 + valor4 + valor5)/4
        print("Resultado da equacao 1:", soma1)
        print("Resultado da equacao 2:", soma2)
        print("Resultado da equacao 3:", soma3)
        print("Resultado da equacao 4:", soma4)
        print("Resultado da equacao 5:", soma5)
        print("Resultado da equacao 6:", soma6)
        print("Resultado da equacao 7:", soma7)
   
ex = exercicio()
ex.exercicio1()
ex.exercicio2()
ex.exercicio3()