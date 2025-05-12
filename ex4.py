#input
renda_dolar = int(input())
cotacao_dolar = float(input())
racao_real = int(input())
aluguel_real = int(input())
onibus_real = int(input())
#cáuculos
renda_real = renda_dolar * cotacao_dolar
gastos = racao_real + aluguel_real + onibus_real
#impressão
if renda_real > gastos:
    print("Me chama pra sua casa um dia pra gente comer Pedigree! Com essa grana dá pra alugar uma ManCão!")
elif renda_real == gastos:
    print("Vai dar pra alugar sua casa, mas sugiro que você vá trabalhar se quiser gastar com outra coisa!")
elif renda_real < gastos:
    print("Eu acho melhor você ir morar comigo no Cin! O RU é só 4 reais e lá no DA tem saco de dormir!")
if racao_real > aluguel_real and racao_real > onibus_real:
    print("A inflaCão deu pros cachorros, viu! Sugiro que você vá no Coffee Break dos calouros e leve toda a comida!")
    maior_gasto = "Ração".capitalize()
elif aluguel_real > racao_real and aluguel_real > onibus_real:
    print("Não está fácil pra ninguém... Tenta dividir o aluguel com algum estudante aí!")
    maior_gasto = "Aluguel".capitalize()
elif onibus_real > racao_real and onibus_real > aluguel_real:
    print("Você consegue voar, por que quer orçamento de ônibus? Vai ser feliz!")
    maior_gasto = "Ônibus".capitalize()
print(f"MESADA (dólares): {renda_dolar:.2f} dólares")
print(f"MESADA (reais): {renda_real:.2f} reais")
print(f"MAIOR GASTO: {maior_gasto}")
