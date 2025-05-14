humor = str(input())
senta = int(input())
pata = int(input())
fica = int(input())
pega = int(input())
comando = str(input())
if comando == 'Senta':
    senta += 1
elif comando == 'Dá a patinha':
    pata += 1
elif comando == 'Fica':
    fica += 1
elif comando == 'Pega':
    pega += 1
if comando == 'Senta' and humor != 'Brincalhão' and senta >= 3:
    print("Byte é o melhor")
elif comando == 'Senta' and humor == 'Brincalhão':
    print("Ele parece estar muito animado para isso!")
elif comando == 'Dá a patinha' and pata >= 3:
    print("Ele é um bom garoto!")
elif comando == 'Fica' and humor != 'Brincalhão' and fica >= 3:
    print("Ele está aprendendo")
elif comando == 'Fica' and humor == 'Brincalhão':
    print("Ele não consegue ficar parado")
elif comando == 'Pega' and humor != 'Preguiçoso' and pega >= 3:
    print("Ele é muito ágil!")
elif comando == 'Pega' and humor == 'Preguiçoso':
    print("Quem não tem seu momento de preguiça?")
else:
    print("Parece que ele não aprendeu esse truque ainda")
if senta >= 3 or pata >=3 or fica >=3 or pega >= 3:
    print(f"O nosso novo mascote estava {humor} e aprendeu o(s) seguinte(s) truque(s):")
    if senta >= 3:
        print("Senta")
    if pata >= 3:
        print("Dá a patinha")
    if fica >= 3:
        print("Fica")
    if pega >= 3:
        print("Pega")
