import oracledb
try:
 conexao = oracledb.connect(
 user="BD150224114",
 password="Mwabf7",
 dsn="172.16.12.14/xe ")
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
    

    num = int(input("Digite para Selecionar: "))
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
    
    if (num == 2):

        menu = 1
        CodP = int(input("Digite o Código do Produto que Deseja Alterar os Dados: "))

        while (menu != 0):
            print('-'*50)
            menu= int(input("1. Alterar Nome\n2. Alterar a Descrição\n3. Alterar Custo do Produto\n4. Alterar Custo Fixo\n5. Alterar Comissão de Vendas\n6. Alterar Imposto\n7. Alterar Margem de Lucro\n0. Sair\n\nDigite para Selecionar: "))

            if (menu == 1):
                print('-'*50)
                novo_nome = input("Digite o Novo Nome do Produto: ")
                cursor.execute (f"""UPDATE estoque
                SET nome_prod = '{novo_nome}'
                WHERE id_prod = {CodP}""")
                

            if (menu == 2):
                print('-'*50)
                nova_descricao = input("Digite a Nova Descrição do Produto: ")
                cursor.execute (f"""UPDATE estoque
                SET desc_prod = '{nova_descricao}'
                WHERE id_prod = {CodP}""")  


            if (menu == 3):
                print('-'*50)
                novo_CP = input("Digite o Novo Custo do Produto: ")
                cursor.execute (f"""UPDATE estoque
                SET custo_prod = {novo_CP}
                WHERE id_prod = {CodP}""")    


            if (menu == 4):
                print('-'*50)
                novo_CF = input("Digite o Novo Custo Fixo do Produto: ")
                cursor.execute (f"""UPDATE estoque
                SET custo_fixo = {novo_CF}
                WHERE id_prod = {CodP}""") 


            if (menu == 5):
                print('-'*50)
                nova_CV = input("Digite a Nova Comissão de Vendas do Produto: ")
                cursor.execute (f"""UPDATE estoque
                SET comissao_vendas = {nova_CV}
                WHERE id_prod = {CodP}""")      


            if (menu == 6):
                print('-'*50)
                novo_IMP = input("Digite o Novo Imposto do Produto: ")
                cursor.execute (f"""UPDATE estoque
                SET impostos = {novo_IMP}
                WHERE id_prod = {CodP}""") 

            if (menu == 7):
                print('-'*50)
                nova_ML = input("Digite a Nova Margem de Lucro do Produto: ")
                cursor.execute (f"""UPDATE estoque
                SET margem_lucro = {nova_ML}
                WHERE id_prod = {CodP}""")
                
            conexao.commit()
cursor.close
conexao.close