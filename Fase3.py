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

        if (len(Desc)%2 != 0):
            Desc += (Desc[-1:])
            
            import numpy as np

            Desc = Desc.replace(" ", "")

            Desc = Desc.lower()

            alfabeto = "abcdefghijklmnopqrstuvwxyz"

            chave = "mike"

            letra_to_num = dict(zip(alfabeto, range(len(alfabeto))))
            num_to_letra = dict(zip(range(len(alfabeto)), alfabeto))

            chave_num = [letra_to_num[i] for i in chave]

            chave_matriz = np.array(chave_num).reshape(2, 2)

            Desc_num = [letra_to_num[i] for i in Desc]

            Desc_array = np.array(Desc_num)

            Desc_pares = np.split(Desc_array, len(Desc)//2)

            Cod_pares = [np.matmul(Desc_pares[i], chave_matriz) % 26 for i in range(len(Desc)//2)]

            Cod_array = np.concatenate(Cod_pares)

            Desc_Co = [num_to_letra[Cod_array[i]] for i in range(len(Cod_array))]

            Desc_Co = ''.join(Desc_Co)

            Desc_Cod = Desc_Co[:-1]

        else:
            import numpy as np

            Desc = Desc.replace(" ", "")

            Desc = Desc.lower()

            alfabeto = "abcdefghijklmnopqrstuvwxyz"

            chave = "mike"

            letra_to_num = dict(zip(alfabeto, range(len(alfabeto))))
            num_to_letra = dict(zip(range(len(alfabeto)), alfabeto))

            chave_num = [letra_to_num[i] for i in chave]

            chave_matriz = np.array(chave_num).reshape(2, 2)

            Desc_num = [letra_to_num[i] for i in Desc]

            Desc_array = np.array(Desc_num)

            Desc_pares = np.split(Desc_array, len(Desc)//2)

            Cod_pares = [np.matmul(Desc_pares[i], chave_matriz) % 26 for i in range(len(Desc)//2)]

            Cod_array = np.concatenate(Cod_pares)

            Desc_Cod = [num_to_letra[Cod_array[i]] for i in range(len(Cod_array))]

            Desc_Cod = ''.join(Desc_Cod)
        
        cursor.execute (f"""INSERT INTO estoque (id_prod, nome_prod, desc_prod, custo_prod, custo_fixo, comissao_vendas, impostos, margem_lucro) 
        VALUES ({CodP}, '{Nome}', '{Desc_Cod}', {CP}, {porcen_CF}, {porcen_CV}, {porcen_IMP}, {porcen_ML})""")

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
                print("NOME ALTERADO COM SUCESSO")

            if (menu == 2):
                print('-'*50)
                nova_descricao = input("Digite a Nova Descrição do Produto: ")
                if (len(nova_descricao)%2 != 0):
                    nova_descricao += (nova_descricao[-1:])
            
                    import numpy as np

                    nova_descricao = nova_descricao.replace(" ", "")

                    nova_descricao = nova_descricao.lower()

                    alfabeto = "abcdefghijklmnopqrstuvwxyz"

                    chave = "mike"

                    letra_to_num = dict(zip(alfabeto, range(len(alfabeto))))
                    num_to_letra = dict(zip(range(len(alfabeto)), alfabeto))

                    chave_num = [letra_to_num[i] for i in chave]

                    chave_matriz = np.array(chave_num).reshape(2, 2)

                    Desc_num = [letra_to_num[i] for i in nova_descricao]

                    Desc_array = np.array(Desc_num)

                    Desc_pares = np.split(Desc_array, len(nova_descricao)//2)

                    Cod_pares = [np.matmul(Desc_pares[i], chave_matriz) % 26 for i in range(len(nova_descricao)//2)]

                    Cod_array = np.concatenate(Cod_pares)

                    Desc_Co = [num_to_letra[Cod_array[i]] for i in range(len(Cod_array))]

                    Desc_Co = ''.join(Desc_Co)

                    Desc_Cod = Desc_Co[:-1]

                else:
                    import numpy as np

                    nova_descricao = nova_descricao.replace(" ", "")

                    nova_descricao = nova_descricao.lower()

                    alfabeto = "abcdefghijklmnopqrstuvwxyz"

                    chave = "mike"

                    letra_to_num = dict(zip(alfabeto, range(len(alfabeto))))
                    num_to_letra = dict(zip(range(len(alfabeto)), alfabeto))

                    chave_num = [letra_to_num[i] for i in chave]

                    chave_matriz = np.array(chave_num).reshape(2, 2)

                    Desc_num = [letra_to_num[i] for i in nova_descricao]

                    Desc_array = np.array(Desc_num)

                    Desc_pares = np.split(Desc_array, len(nova_descricao)//2)

                    Cod_pares = [np.matmul(Desc_pares[i], chave_matriz) % 26 for i in range(len(nova_descricao)//2)]

                    Cod_array = np.concatenate(Cod_pares)

                    Desc_Cod = [num_to_letra[Cod_array[i]] for i in range(len(Cod_array))]

                    Desc_Cod = ''.join(Desc_Cod)
        
                cursor.execute (f"""UPDATE estoque
                SET desc_prod = '{Desc_Cod}'
                WHERE id_prod = {CodP}""")  
                print("DESCRIÇÃO ALTERADA COM SUCESSO")

            if (menu == 3):
                print('-'*50)
                novo_CP = input("Digite o Novo Custo do Produto: ")
                cursor.execute (f"""UPDATE estoque
                SET custo_prod = {novo_CP}
                WHERE id_prod = {CodP}""") 
                print("CUSTO DO PRODUTO ALTERADO COM SUCESSO")  


            if (menu == 4):
                print('-'*50)
                novo_CF = input("Digite o Novo Custo Fixo do Produto: ")
                cursor.execute (f"""UPDATE estoque
                SET custo_fixo = {novo_CF}
                WHERE id_prod = {CodP}""") 
                print("CUSTO FIXO ALTERADO COM SUCESSO")


            if (menu == 5):
                print('-'*50)
                nova_CV = input("Digite a Nova Comissão de Vendas do Produto: ")
                cursor.execute (f"""UPDATE estoque
                SET comissao_vendas = {nova_CV}
                WHERE id_prod = {CodP}""")    
                print("COMISSÃO DE VENDAS ALTERADO COM SUCESSO")  


            if (menu == 6):
                print('-'*50)
                novo_IMP = input("Digite o Novo Imposto do Produto: ")
                cursor.execute (f"""UPDATE estoque
                SET impostos = {novo_IMP}
                WHERE id_prod = {CodP}""") 
                print("IMPOSTO ALTERADO COM SUCESSO")

            if (menu == 7):
                print('-'*50)
                nova_ML = input("Digite a Nova Margem de Lucro do Produto: ")
                cursor.execute (f"""UPDATE estoque
                SET margem_lucro = {nova_ML}
                WHERE id_prod = {CodP}""")
                print("MARGEM DE LUCRO ALTERADA COM SUCESSO")
            conexao.commit()

    if num == 3:
        print('-'*50)
        CodP = int(input("Digite o Código do Produto que Deseja Apagar os Dados: "))
        print('-'*50)
        cursor.execute (f"""DELETE estoque
        WHERE id_prod = {CodP}""")
        print("PRODUTO DELETADO COM SUCESSO")
        conexao.commit()
cursor.close
conexao.close
