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
        soma4 = valor1 +int(valor3)
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
   
    def exercicio4(self):
        v1 = 2 
        v2 = 3
        v3 = 5
        v4 = 6
        soma = v1 + v2 + v3 + v4
        media = soma / 4
        print("A soma dos valores é:", soma)
        print("A media dos valores é:", media)

    def exercicio5(self, nota):
        if (nota <= 60):
            print("Reprovado")
        else:
            print("Aprovado")
    
    def exercicio6(self,nota):
        if (nota > 60):
            print("Aluno reprovado")
        else:
            print("Aluno aprovado")
        if (nota > 80):
            print("Aluno aprovado com certificado") 

    def exercicio7(self):
        lista = [0, 1, 2, 3, 4, 5] 
        print(lista[0])         
        print(lista[1])         
        print(lista[2])         
        print(lista[3])         
        print(lista[4])         
        print(lista[5])         

    def exercicio8(self):
        notas = [0]
        notas[0] = 80
        notas.append(60)
        notas.append(30)
        notas.append(40)
        notas.append(80)
        notas.append(90)
        print("Notas:", notas)
        notas.pop()
        notas.pop()
        print("Notas após remover os dois ultimos elemento:", notas)

    def exercicio9(self, notas): 
        if (notas >= 60):
            print("A nota é maior que 60") 
        else:
            print("A nota é menor que 60 ")

    def exercicio10(self):
        lista1 = [1, 3, 5, 7] 
        lista2 = [2, 4, 6, 8, 10, 12] 
        lista3 = [10, 20, 30]
        lista4 = [11, 22, 33, 44, 55, 66, 77]
        lista5 = [70, 60, 50, 40, 30 ,20, 10, 5, 0]
        for elemento in lista1:
         print(elemento)
         print("lista 1")
        for elemento in lista2:
         print(elemento)
         print("lista 2")
        for elemento in lista3:
         print(elemento)
         print("lista 3")
        for elemento in lista4:
         print(elemento)
         print("lista 4")
         print(elemento)
        for elemento in lista5:
         print(elemento)
         print("lista 5")

    def exercicio11(self):
        notas_escolares = [85, 42, 78, 90, 55, 60, 49, 73, 88, 35]
        for item in notas_escolares:
         if (item > 60):
           print("Aprovado")
        else:
            print("Reprovado")   
           
    def exercicio12(self):
        notas_escolares = [85, 42, 78, 90, 55, 60, 49, 73, 88, 35]
        for item in notas_escolares:            
         if (item < 60):   
            print("Aluno reprovado")
         else:
           print("Aluno aprovado")
         if (item > 80):
           print("Aluno foi aprovado com certificado")

    def exercicio13(self, cor):
       print(cor)

    def exercicio14(self, faixacor1, faixacor2): 
        print("A cor da quarta faixa é:", faixacor1)
        print("A cor da quinta faixa é:", faixacor2)

    def exercicio15(self, nomeAluno, idade, nota1, nota2):
       print("O nome do aluno é:", nomeAluno)
       print("A idade do aluno é:", idade)
       print(nota1, "é a primeira nota do aluno")
       print(nota2, "é a segunda nota do aluno")

    def exercicio16(self, nomeAluno, idade, nota1, nota2, nota3):
       soma = nota1 + nota2 + nota3
       print("A soma das notas é:", soma)
       if (soma > 180):
          print("Aluno aprovado")
       else:
          print("Aluno aprovado")     

exercicio = exercicio()
exercicio.exercicio1()
exercicio.exercicio2()
exercicio.exercicio3()
exercicio.exercicio4()
exercicio.exercicio5(64)
exercicio.exercicio5(45)
exercicio.exercicio5(60)
exercicio.exercicio6(58)
exercicio.exercicio6(65)
exercicio.exercicio6(82)
exercicio.exercicio7()
exercicio.exercicio8()
notas = [60, 55, 80, 90, 59, 30]
exercicio.exercicio9(notas[0])
exercicio.exercicio9(notas[1])
exercicio.exercicio9(notas[2])
exercicio.exercicio9(notas[3])
exercicio.exercicio9(notas[4])
exercicio.exercicio9(notas[5])
exercicio.exercicio10()
exercicio.exercicio11()
exercicio.exercicio12()
exercicio.exercicio13("Vermelho")
exercicio.exercicio14("Amarelo", "Vermelho")
exercicio.exercicio15("Matheus",15, 82, 100)
exercicio.exercicio16("Matheus", 15, 82, 95, 100)