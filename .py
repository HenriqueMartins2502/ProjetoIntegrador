'''registro de produtos primeiro modelo.'''
NP=str(input("Qual o nome do produto:"))
ID_P=int(input("Digite o código do produto:"))
Descri=str(input("Descrição do produto:"))
CP=float(input("Digite o preço inicial do produto:"))
CF=float(input("Digite o custo fixo/Administrativo:"))
CV=float(input("Digite a comissão por venda:"))
IV=float(input("Digite os impostos:"))
ML=float(input("Digite a margem de lucro a ser obtida:"))
PV=CP/1-((CF+CV+IV+ML)/100)
RB=(PV-CP)
OC=((PV*(CF/100))+(PV*(CV/100))+(PV*(IV/100)))
porcenCP=((CP*100)/PV)
print(f"A. Preço de Venda: R${PV:.2f}/ 100%")
print(f"B. Custo de Aquisição (fornecedor): R${CP:.2f}/ {porcenCP:.2f}%")
print(f"C. Receita Bruta: R${RB:.2f}/ {(100-porcenCP)}%")
print(f"D. Custo Fixo/Administrativo: R${(PV*(CF/100)):.2f}/ {CF:.2f}%")
print(f"E. Comissão de Vendas: R${(PV*(CV/100)):.2f}/ {CV:.2f}%")
print(f"F. Impostos: R${(PV*(IV/100)):.2f}/ {IV:.2f}%")
print(f"G. Outros Custos: R${OC:.2f}/ {(CF+CV+IV)}%")
print(f"H. Rentabilidade: R${(RB-OC):.2f}/ {ML}%")