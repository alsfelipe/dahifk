#Voto 1
nome1 = input()
na = nome1.lower()
quem_indicou1 = input()
na2 = na.split()
na3 = "".join(na2)
pontuacao1 = len(na3)
if "cin" in na3:
    pontuacao1 += 10
#Voto 2
nome2 = input()
nb = nome2.lower()
nb2 = nb.split()
nb3 = "".join(nb2)
quem_indicou2 = input()
pontuacao2 = len(nb3)
if "cin" in nb3:
     pontuacao2 += 10
#Voto 3
nome3 = input()
nc = nome3.lower()
nc2 = nc.split()
nc3 = "".join(nc2)
quem_indicou3 = input()
pontuacao3 = len(nc3)
if "cin" in nc3:
     pontuacao3 += 10
#Exclusões
if "felino espião" == quem_indicou1 or 'gato' in na3:
    pontuacao1 = 0
if "felino espião" == quem_indicou2 or 'gato' in nb3:
    pontuacao2 = 0
if "felino espião" == quem_indicou3 or 'gato' in nc3:
    pontuacao3 = 0
#Impressão 1
if 'cin' in na3 or 'cin' in nb3 or 'cin' in nc3:
    print("Os melhores nomes são aqueles que fazem referência a minha casinha :)")
if 'felino espião' in quem_indicou1 or 'felino espião' in quem_indicou2 or 'felino espião' in quem_indicou3:
    print("Essa não! Os gatos querem arruinar o aniversário de Byte. Não deixe isso acontecer.")
print("RANKING DOS NOMES:")
if pontuacao1 > pontuacao2 and pontuacao1 > pontuacao3 and pontuacao2 > pontuacao3:
    nome_primeiro_lugar = na
    nome_segundo_lugar = nb
    nome_terceiro_lugar = nc
elif pontuacao1 > pontuacao2 and pontuacao1 > pontuacao3 and pontuacao3 > pontuacao2:
    nome_primeiro_lugar = na
    nome_segundo_lugar = nc
    nome_terceiro_lugar = nb
elif pontuacao2 > pontuacao1 and pontuacao2 > pontuacao3 and pontuacao1 > pontuacao3:
    nome_primeiro_lugar = nb
    nome_segundo_lugar = na
    nome_terceiro_lugar = nc
elif pontuacao2 > pontuacao1 and pontuacao2 > pontuacao3 and pontuacao3 > pontuacao1:
    nome_primeiro_lugar = nb
    nome_segundo_lugar = nc 
    nome_terceiro_lugar = na
elif pontuacao3 > pontuacao1 and pontuacao3 > pontuacao2 and pontuacao1 > pontuacao2:
    nome_primeiro_lugar = nc
    nome_segundo_lugar = na
    nome_terceiro_lugar = nb
elif pontuacao3 > pontuacao1 and pontuacao3 > pontuacao2 and pontuacao2 > pontuacao1:
    nome_primeiro_lugar = nc
    nome_segundo_lugar = nb
    nome_terceiro_lugar = na
print(f"Primeiro lugar: {nome_primeiro_lugar}")
print(f"Segundo lugar: {nome_segundo_lugar}")
print(f"Terceiro lugar: {nome_terceiro_lugar}")
