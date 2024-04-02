largura = float(input("Largura do aposento: "))
comprimento = float(input("Comprimento do aposento: "))
qnt_litro = float(input("Quantidade de litros da Lata: "))
pe_direito = 2.8
porta = 0.8 * 2.1
capacidade_lata = qnt_litro * 3
paredes = (2 * ((largura * pe_direito) + (comprimento * pe_direito))) - porta

qnt_tintas = paredes / capacidade_lata

print(f"A quantidade de tintas necessária para pintar o aposento foi de : {qnt_tintas:.2f}")
