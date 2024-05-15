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

num = 1

while (num != 0):
    print('-'*50)
    print(" Bem vindo ao software de controle de estoque")
    print('-'*50)
    print ("1. Inserir Produto")
    print ("2. Alterar Produto")
    print ("3. Apagar Produto")
    print ("4. Listar Produtos")
    print ("0. Sair do Sistema")
    

    num = int(input("Digite para Selecionar:"))
    print('-'*50)
    if (num == 1):
        print(" ///CADASTRO DE PRODUTOS///")
        print('-'*50)
        CodP = int(input("Digite o Código do Produto:"))
        Nome = (input("Digite o Nome do Produto:"))
        Desc = (input("Digite a Descrição do Produto:")) #!!!
        CP = float(input("Digite o Custo do Produto:"))
        porcen_CF = float(input("Digite o Custo Fixo do Produto:"))
        porcen_CV = float(input("Digite a Comissão de Vendas:"))
        porcen_IMP = float(input("Digite os Impostos Sobre o Produto:"))
        porcen_ML = float(input("Digite a Margem de Lucro do Produto:"))
        
        cursor.execute (f"""INSERT INTO estoque (id_prod, nome_prod, desc_prod, custo_prod, custo_fixo, comissao_vendas, impostos, margem_lucro) 
        VALUES ({CodP}, '{Nome}', '{Desc}', {CP}, {porcen_CF}, {porcen_CV}, {porcen_IMP}, {porcen_ML})""")

        conexao.commit()
        print('-'*50)
        print("PRODUTO INSERIDO COM SUCESSO")
cursor.close()
conexao.close()
     
