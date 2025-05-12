nome = (input())
acertos1 = int(input())
acertos2 = int(input())
acertos3 = int(input())
acertos4 = int(input())
acertos5 = int(input())
acertos6 = int(input())
nota1 = acertos1 
nota2 = acertos2 
nota3 = acertos3 
nota4 = acertos4 * (10/6)
nota5 = acertos5 * (10/6)
nota6 = acertos6 * (10/6)
media = (nota1 + nota2 + nota3 + nota4 + nota5 + nota6) / 6
acertos = [acertos1,acertos2,acertos3,acertos4,acertos5,acertos6]
nao_respondidas = sum(1 for acerto in acertos if acerto == 0)
print(f"A média de {nome} é {media:.1f}")
if nota1 <= nota2 <= nota3 <= nota4 <= nota5 <= nota6:
    print("Progresso constante! Parabéns pelo esforço!")
else:
    print("Alerta! Queda no rendimento.")
if nao_respondidas >= 2:
    print("Alerta! Múltiplas listas não respondidas.")
if media >= 8:
    print('Parabéns pelo excelente desempenho! Continue "au" sim.')
elif 7<= media < 8:
    print("Parabéns pelo bom desempenho!")
elif media < 7 :
    print("Alerta! Desempenho abaixo do esperado.")
   


