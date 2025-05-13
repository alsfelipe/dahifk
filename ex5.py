#Cão A
nome_caoa = input()
pontuacao_prova_1a = int(input())
pontuacao_prova_2a = int(input())
pontuacao_prova_3a = int(input())
notaA = pontuacao_prova_1a + pontuacao_prova_2a + pontuacao_prova_3a
if nome_caoa == "Byte":
    print("Byte está na disputa! Não há dúvidas, o novo mascote do CIn é ele mesmo!")
    exit()
elif notaA == 30:
    print(f"Com uma pontuação perfeita, {nome_caoa} conquista o título de mascote do CIn!")
    exit()
#Cão B
nome_caob = input()
pontuacao_prova_1b = int(input())
pontuacao_prova_2b = int(input())
pontuacao_prova_3b = int(input())
notaB = pontuacao_prova_1b + pontuacao_prova_2b + pontuacao_prova_3b
if nome_caob == "Byte":
    print("Byte está na disputa! Não há dúvidas, o novo mascote do CIn é ele mesmo!")
    exit()
elif notaB == 30:
    print(f"Com uma pontuação perfeita, {nome_caob} conquista o título de mascote do CIn!")
    exit()
#Cão C
nome_caoc = input()
pontuacao_prova_1c = int(input())
pontuacao_prova_2c = int(input())
pontuacao_prova_3c = int(input())
notaC = pontuacao_prova_1c + pontuacao_prova_2c + pontuacao_prova_3c
if nome_caoc == "Byte":
    print("Byte está na disputa! Não há dúvidas, o novo mascote do CIn é ele mesmo!")
    exit()
elif notaC == 30:
    print(f"Com uma pontuação perfeita, {nome_caoc} conquista o título de mascote do CIn!")
    exit()
#Eliminação
if notaA < 15:
    print(f"Infelizmente {nome_caoa} está fora da disputa")
if notaB < 15:
    print(f"Infelizmente {nome_caob} está fora da disputa")
if notaC < 15:
    print(f"Infelizmente {nome_caoc} está fora da disputa")
#Vencedor
elif notaA > notaB and notaA > notaC:
    print(f"Após uma disputa acirrada, o novo mascote do CIn é {nome_caoa}")
elif notaB > notaA and notaB > notaC:
    print(f"Após uma disputa acirrada, o novo mascote do CIn é {nome_caob}")
elif notaC > notaA and notaC > notaB:
    print(f"Após uma disputa acirrada, o novo mascote do CIn é {nome_caoc}")

 

