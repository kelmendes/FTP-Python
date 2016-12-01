import funcao #Importando modulos


funcao.conexao('ftp.keumendes.net16.net', 'a7856848', 'klebson')
# Listando os diretorios
print ('++----------------------------------------------------------------------------------++')
print ('++                           Diretorios do Servidor                                 ++')
print ('++----------------------------------------------------------------------------------++')
funcao.listar('LIST')

 # Entrando no diretorio Public_HTML
print ('')
print ('')
print ('++----------------------------------------------------------------------------------++')
print ('++                        Diretorio/Arquivos - Public_html                          ++')
print ('++----------------------------------------------------------------------------------++')
funcao.diretorio('public_html')
funcao.listar('LIST')

funcao.encerrando_conexão()