import oracledb
try:
    conexao = oracledb. connect (
    user="system",
    password="capo1950",
    dsn="localhost/XEPDB1")
except Exception as erro:
print ( 'Erro em conexão', erro)
else:
print ('Conectado', conexao. version)
cursor=conexao.cursor()

num = 1

while (num != 0):

    print ("1. Inserir Produto")
    print ("2. Alterar Produto")
    print ("3. Apagar Produto")
    print ("4. Listar Produtos")
    print ("0. Sair do Sistema")

    num = int(input("Digite para Selecionar:"))

    if (num == 1):
        CodP = int(input("Digite o Código do Produto:"))
        Nome = str(input("Digite o Nome do Produto:"))
        Desc = str(input("Digite a Descrição do Produto:")) #!!!
        CP = float(input("Digite o Custo do Produto:"))
        porcen_CF = float(input("Digite o Custo Fixo do Produto:"))
        porcen_CV = float(input("Digite a Comissão de Vendas:"))
        porcen_IMP = float(input("Digite os Impostos Sobre o Produto:"))
        porcen_ML = float(input("Digite a Margem de Lucro do Produto:"))
        
        PV = (CP/(1-((porcen_CF+porcen_CV+porcen_IMP+porcen_ML)/100)))
        
        RB = PV - CP
        
        sql = "INSERT INTO [Tabela] (id_prod, nome_prod, desc_prod, custo_prod, custo_fixo, comissao_vendas, impostos, margem_lucro) VALUES (CodP, Nome, Desc, CP, porcen_CF, porcen_CV, porcen_IMP, porcen_ML)"
        
        cursor.execute (sql)
        
        print("Produto Inserido Com Sucesso.")