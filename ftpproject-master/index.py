import funcao #Importando modulos

site = input('Informe o Site/Dominio: ')
user = input('Informe o Usuario: ')
senha = input('Informe a senha: ')
funcao.conexao(site, user, senha)

# Listando os diretorios
print ('++----------------------------------------------------------------------------------++')
print ('++                           Diretorios do Servidor                                 ++')
print ('++----------------------------------------------------------------------------------++')
funcao.listar('LIST')

#Criando Variavel OPCAO do menu principal
opc = 0
while (opc != 10):
	funcao.menu_principal()
	opc = int(input('Informe o codigo: '))
	if opc == 1:
		funcao.listar('LIST')
	elif opc == 2:
		funcao.listar('LIST')
		print ()
		print ()
		diretorio = input('Informe o Diretorio: ')
		funcao.diretorio_cwd(diretorio)
	elif opc == 3:
		diretorio = input('Informe o Diretorio onde esta o arquivo: ')
		funcao.uploader(diretorio)

	elif opc == 4:
		arquiv = input('Informe o arquivo: ')
		funcao.arquivo_delete(arquiv)
		print('Arquivo Deletado!')

	elif opc == 5:
		diretorio = input('Informe o Diretorio: ')
		funcao.diretorio_mkd(diretorio)
	elif opc == 6:
		diretorio = input('Informe o Diretorio: ')
		funcao.diretorio_rmd(diretorio)




print ()
print ()
print ('++----------------------------------------------------------------------------------++')
print ('++                                    GRUPO                                         ++')
print ('++----------------------------------------------------------------------------------++')
print ('++ Fabio Ferreira ')
print ('++ Fernando ')
print ('++ Klebson Mendes')
print ('++ Melquesedeque ')
print ('++----------------------------------------------------------------------------------++')
#Fechando conexao 
funcao.encerrando_conexão()
