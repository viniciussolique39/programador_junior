notas = []

contador = 1 


while contador <= 2:
  codigo_aluno = input("RM: ")
  nota = float(input("Nota: "))
  resultado = [codigo_aluno, nota]
  notas.append(resultado)

  contador = contador + 1

  print ("quantidade de notas", len(notas))

 