import oracledb
try:
 conexao = oracledb.connect(
 user="system",
 password="capo1950",
 dsn="localhost/XEPDB1")
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


#Calculo da Preço Venda

PV=[]

CP1=custo_prod[0]
CF1=custo_fixo[0]
CV1=comissao_vendas[0]
IMP1=impostos[0]
ML1=margem_lucro[0]

PV.append(CP1/(1-((CF1+CV1+IMP1+ML1)/(100))))

CP2=custo_prod[1]
CF2=custo_fixo[1]
CV2=comissao_vendas[1]
IMP2=impostos[1]
ML2=margem_lucro[1]

PV.append(CP2/(1-((CF2+CV2+IMP2+ML2)/(100))))

CP3=custo_prod[2]
CF3=custo_fixo[2]
CV3=comissao_vendas[2]
IMP3=impostos[2]
ML3=margem_lucro[2]

PV.append(CP3/(1-((CF3+CV3+IMP3+ML3)/(100))))

CP4=custo_prod[3]
CF4=custo_fixo[3]
CV4=comissao_vendas[3]
IMP4=impostos[3]
ML4=margem_lucro[3]

PV.append(CP4/(1-((CF4+CV4+IMP4+ML4)/(100))))

CP5=custo_prod[4]
CF5=custo_fixo[4]
CV5=comissao_vendas[4]
IMP5=impostos[4]
ML5=margem_lucro[4]

PV.append(CP5/(1-((CF5+CV5+IMP5+ML5)/(100))))

#Calculo da Renda Bruta

RB1=(PV[0]-CP1)
RB2=(PV[1]-CP2)
RB3=(PV[2]-CP3)
RB4=(PV[3]-CP4)
RB5=(PV[4]-CP5)

#Calculo Outros Custos

OC1=(PV[0]*(CF1/100)+PV[0]*(CV1/100))+(PV[0]*(IMP1/100))
OC2=(PV[1]*(CF2/100))+(PV[1]*(CV2/100))+(PV[1]*(IMP2/100))
OC3=(PV[2]*(CF3/100))+(PV[2]*(CV3/100))+(PV[2]*(IMP3/100))
OC4=(PV[3]*(CF4/100))+(PV[3]*(CV4/100))+(PV[3]*(IMP4/100))
OC5=(PV[4]*(CF5/100))+(PV[4]*(CV5/100))+(PV[4]*(IMP5/100))

#Formula % da Renda Bruta(porcenRB) e Custo de Pordutos

porcenRB1=((RB1*100)/PV[0])
porcenRB2=((RB2*100)/PV[1])
porcenRB3=((RB3*100)/PV[2])
porcenRB4=((RB4*100)/PV[3])
porcenRB5=((RB5*100)/PV[4])

porcenCP1 = (100 * CP1/PV[0])
porcenCP2 = (100 * CP2/PV[1])
porcenCP3 = (100 * CP3/PV[2])
porcenCP4 = (100 * CP4/PV[3])
porcenCP5 = (100 * CP5/PV[4])

#Valores Brutos de CF, CV, IMP e ML

bCF1 = ((CF1 * PV[0])/100)
bCF2 = ((CF2 * PV[1])/100)
bCF3 = ((CF3 * PV[2])/100)
bCF4 = ((CF4 * PV[3])/100)
bCF5 = ((CF5 * PV[4])/100)

bCV1 = ((CV1 * PV[0])/100)
bCV2 = ((CV2 * PV[1])/100)
bCV3 = ((CV3 * PV[2])/100)
bCV4 = ((CV4 * PV[3])/100)
bCV5 = ((CV5 * PV[4])/100)

bIMP1 = ((IMP1 * PV[0])/100)
bIMP2 = ((IMP2 * PV[1])/100)
bIMP3 = ((IMP3 * PV[2])/100)
bIMP4 = ((IMP4 * PV[3])/100)
bIMP5 = ((IMP5 * PV[4])/100)

bML1 = ((ML1 * PV[0])/100)
bML2 = ((ML2 * PV[1])/100)
bML3 = ((ML3 * PV[2])/100)
bML4 = ((ML4 * PV[3])/100)
bML5 = ((ML5 * PV[4])/100)


#Saída

#p1
print (f"Produto: {nome_prod[0]}   Especifcacão: {desc_prod[0]}")
print ("---------------------------------------------------------")
print (f"Descriçao:                            Valor       %")
print (f"A. Preço de Venda                  =  R${PV[0]:.2f}     100.0%")
print (f"B. Custo de Aquisição (Fornecedor) =  R${CP1:.2f}     {porcenCP1:.2f}%") 
print (f"C. Receita Bruta                   =  R${RB1:.2f}     {porcenRB1:.2f}%")
print (f"D. Custo Fixo/Administrativo       =  R${bCF1:.2f}     {CF1:.2f}%")
print (f"E. Comissão de Vendas              =  R${bCV1:.2f}      {CV1:.2f}%")
print (f"F. Impostos                        =  R${bIMP1:.2f}      {IMP1:.2f}%")
print (f"G. Outros Custos (D+E+F)           =  R${OC1:.2f}     {IMP1+CV1+CF1:.2f}%")
print (f"H. Rentabilidade (C-G)             =  R${bML1:.2f}     {ML1:.2f}%")
if ML1 > 20:
    print("O Lucro Deste Produto é Alto.")
elif ML1 > 10 and ML1 <= 20:
    print("O Lucro Deste Produto é Médio.")
elif ML1 > 0 and ML1 <= 10:
    print("O Lucro Deste Produto é Baixo.")
elif ML1 == 0:
    print("Este Produto Não Gera Lucro ou Pejuízo (Equilíbrio).")
elif ML1 < 0:
    print("Este Produto Gera Prejuízo.")

print (" ")
print (" ")

#p2
print (f"Produto: {nome_prod[1]}   Especifcacão: {desc_prod[1]}")
print ("---------------------------------------------------------")
print (f"Descriçao:                            Valor       %")
print (f"A. Preço de Venda                  =  R${PV[1]:.2f}     100.0%")
print (f"B. Custo de Aquisição (Fornecedor) =  R${CP2:.2f}     {porcenCP2:.2f}%") 
print (f"C. Receita Bruta                   =  R${RB2:.2f}      {porcenRB2:.2f}%")
print (f"D. Custo Fixo/Administrativo       =  R${bCF2:.2f}      {CF2:.2f}%")
print (f"E. Comissão de Vendas              =  R${bCV2:.2f}      {CV2:.2f}%")
print (f"F. Impostos                        =  R${bIMP2:.2f}      {IMP2:.2f}%")
print (f"G. Outros Custos (D+E+F)           =  R${OC2:.2f}      {IMP2+CV2+CF2:.2f}%")
print (f"H. Rentabilidade (C-G)             =  R${bML2:.2f}      {ML2:.2f}%")

if ML2 > 20:
    print("O Lucro Deste Produto é Alto.")
elif ML2 > 10 and ML2 <= 20:
    print("O Lucro Deste Produto é Médio.")
elif ML2 > 0 and ML2 <= 10:
    print("O Lucro Deste Produto é Baixo.")
elif ML2 == 0:
    print("Este Produto Não Gera Lucro ou Pejuízo (Equilíbrio).")
elif ML2 < 0:
    print("Este Produto Gera Prejuízo.")

print (" ")
print (" ")

#p3
print (f"Produto: {nome_prod[2]}   Especifcacão: {desc_prod[2]}")
print ("---------------------------------------------------------")
print (f"Descriçao:                            Valor        %")
print (f"A. Preço de Venda                  =  R${PV[2]:.2f}     100.0%")
print (f"B. Custo de Aquisição (Fornecedor) =  R${CP3:.2f}      {porcenCP3:.2f}%") 
print (f"C. Receita Bruta                   =  R${RB3:.2f}     {porcenRB3:.2f}%")
print (f"D. Custo Fixo/Administrativo       =  R${bCF3:.2f}      {CF3:.2f}%")
print (f"E. Comissão de Vendas              =  R${bCV3:.2f}      {CV3:.2f}%")
print (f"F. Impostos                        =  R${bIMP3:.2f}      {IMP3:.2f}%")
print (f"G. Outros Custos (D+E+F)           =  R${OC3:.2f}     {IMP3+CV3+CF3:.2f}%")
print (f"H. Rentabilidade (C-G)             =  R${bML3:.2f}     {ML3:.2f}%")

if ML3 > 20:
    print("O Lucro Deste Produto é Alto.")
elif ML3 > 10 and ML3 <= 20:
    print("O Lucro Deste Produto é Médio.")
elif ML3 > 0 and ML3 <= 10:
    print("O Lucro Deste Produto é Baixo.")
elif ML3 == 0:
    print("Este Produto Não Gera Lucro ou Pejuízo (Equilíbrio).")
elif ML3 < 0:
    print("Este Produto Gera Prejuízo.")

print (" ")
print (" ")

#p4
print (f"Produto: {nome_prod[3]}   Especifcacão: {desc_prod[3]}")
print ("--------------------------------------------------------")
print (f"Descriçao:                            Valor       %")
print (f"A. Preço de Venda                  =  R${PV[3]:.2f}     100.0%")
print (f"B. Custo de Aquisição (Fornecedor) =  R${CP4:.2f}     {porcenCP4:.2f}%") 
print (f"C. Receita Bruta                   =  R${RB4:.2f}      {porcenRB4:.2f}%")
print (f"D. Custo Fixo/Administrativo       =  R${bCF4:.2f}      {CF4:.2f}%")
print (f"E. Comissão de Vendas              =  R${bCV4:.2f}      {CV4:.2f}%")
print (f"F. Impostos                        =  R${bIMP4:.2f}      {IMP4:.2f}%")
print (f"G. Outros Custos (D+E+F)           =  R${OC4:.2f}      {IMP4+CV4+CF4:.2f}%")
print (f"H. Rentabilidade (C-G)             =  R${bML4:.2f}      {ML4:.2f}%")

if ML4 > 20:
    print("O Lucro Deste Produto é Alto.")
elif ML4 > 10 and ML4 <= 20:
    print("O Lucro Deste Produto é Médio.")
elif ML4 > 0 and ML4 <= 10:
    print("O Lucro Deste Produto é Baixo.")
elif ML4 == 0:
    print("Este Produto Não Gera Lucro ou Pejuízo (Equilíbrio).")
elif ML4 < 0:
    print("Este Produto Gera Prejuízo.")

print (" ")
print (" ")

#p5
print (f"Produto: {nome_prod[4]}   Especifcacão: {desc_prod[4]}")
print ("------------------------------------------------------------------------")
print (f"Descriçao:                            Valor              %")
print (f"A. Preço de Venda                  =  R${PV[4]:.2f}     100.0%")
print (f"B. Custo de Aquisição (Fornecedor) =  R${CP5:.2f}     {porcenCP5:.2f}%") 
print (f"C. Receita Bruta                   =  R${RB5:.2f}      {porcenRB5:.2f}%")
print (f"D. Custo Fixo/Administrativo       =  R${bCF5:.2f}      {CF5:.2f}%")
print (f"E. Comissão de Vendas              =  R${bCV5:.2f}      {CV5:.2f}%")
print (f"F. Impostos                        =  R${bIMP5:.2f}      {IMP5:.2f}%")
print (f"G. Outros Custos (D+E+F)           =  R${OC5:.2f}      {IMP5+CV5+CF5:.2f}%")
print (f"H. Rentabilidade (C-G)             =  R${bML5:.2f}    {ML5:.2f}%\n\n")

if ML5 > 20:
    print("O Lucro Deste Produto é Alto.")
elif ML5 > 10 and ML5 <= 20:
    print("O Lucro Deste Produto é Médio.")
elif ML5 > 0 and ML5 <= 10:
    print("O Lucro Deste Produto é Baixo.")
elif ML5 == 0:
    print("Este Produto Não Gera Lucro ou Pejuízo (Equilíbrio).")
elif ML5 < 0:
    print("Este Produto Gera Prejuízo.")
