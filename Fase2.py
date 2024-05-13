import oracledb
try:
 conexao = oracledb.connect(
 user="BD150224114",
 password="Mwabf7",
 dsn="BD-ACD/xe ")
except Exception as erro:
 print ('Erro em conexão', erro)
else:
 print ("Conectado", conexao.version)
cursor=conexao.cursor()

#definição das listas
estoque=[]
id_prod=[]
nome_prod=[]
desc_prod=[]
custo_prod=[]
custo_fixo=[]
comissao_vendas=[]
impostos=[]
margem_lucro=[]

cont=0
    
cursor.execute("select id_prod from estoque")
id_prod = [row[0] for row in cursor.fetchall()]

cursor.execute("select nome_prod from estoque")
nome_prod = [row[0] for row in cursor.fetchall()]

cursor.execute("select desc_prod from estoque")
desc_prod = [row[0] for row in cursor.fetchall()]

cursor.execute("select custo_prod from estoque")
custo_prod = [row[0] for row in cursor.fetchall()]

cursor.execute("select custo_fixo from estoque")
custo_fixo = [row[0] for row in cursor.fetchall()]

cursor.execute("select comissao_vendas from estoque")
comissao_vendas = [row[0] for row in cursor.fetchall()]

cursor.execute("select impostos from estoque")
impostos = [row[0] for row in cursor.fetchall()]

cursor.execute("select margem_lucro from estoque")
margem_lucro = [row[0] for row in cursor.fetchall()]

estoque.append(id_prod)
estoque.append(nome_prod)
estoque.append(desc_prod)
estoque.append(custo_prod)
estoque.append(custo_fixo)
estoque.append(comissao_vendas)
estoque.append(impostos)
estoque.append(margem_lucro)

cursor.close
conexao.close

for i in range (len(estoque)):
    PV=custo_prod[i] / (1 - ((custo_fixo[i] + comissao_vendas[i] + impostos[i] + margem_lucro[i])/100))

    print (f"Produto: {nome_prod[i]}   Especifcacão: {desc_prod[i]}")
    print ("---------------------------------------------------------")
    print (f"Descriçao:                            Valor       %")
    print (f"A. Preço de Venda                  =  R${PV:.2f}     100.0%")
    print (f"B. Custo de Aquisição (Fornecedor) =  R${custo_prod[i]:.2f}     {(100*custo_prod[i]/PV):.2f}%") 
    print (f"C. Receita Bruta                   =  R${(PV-custo_prod[i]):.2f}     {(((PV-custo_prod[i])*100)/PV):.2f}%")
    print (f"D. Custo Fixo/Administrativo       =  R${((custo_fixo[i]*PV)/100):.2f}     {custo_fixo[i]:.2f}%")
    print (f"E. Comissão de Vendas              =  R${((comissao_vendas[i]*PV)/100):.2f}      {comissao_vendas[i]:.2f}%")
    print (f"F. Impostos                        =  R${((impostos[i]*PV)/100):.2f}      {impostos[i]:.2f}%")
    print (f"G. Outros Custos (D+E+F)           =  R${(PV*(custo_fixo[i]/100)+PV*(comissao_vendas[i]/100)+PV*(impostos[i]/100)):.2f}     {impostos[i]+comissao_vendas[i]+custo_fixo[i]:.2f}%")
    print (f"H. Rentabilidade (C-G)             =  R${((margem_lucro[i]*PV)/100):.2f}     {margem_lucro[i]:.2f}%")

    if margem_lucro[i] > 20:
        print("\nO Lucro Deste Produto é Alto.\n")
    elif margem_lucro[i] > 10 and margem_lucro[i] <= 20:
        print("\nO Lucro Deste Produto é Médio.\n")
    elif margem_lucro[i] > 0 and margem_lucro[i] <= 10:
        print("\nO Lucro Deste Produto é Baixo.\n")
    elif margem_lucro[i] == 0:
        print("\nEste Produto Não Gera Lucro ou Pejuízo (Equilíbrio).\n")
    elif margem_lucro[i] < 0:
        print("\nEste Produto Gera Prejuízo.\n")
