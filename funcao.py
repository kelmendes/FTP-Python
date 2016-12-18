import ftplib, os, glob#Importando a biblioteca

ftp = None
def conexao(site, usuario, senha):# Funcao para realizar login
    global ftp
    ftp = ftplib.FTP(site)
    print("Welcome:", ftp.getwelcome())
    ftp.login(user= usuario, passwd= senha)
    print("Voce esta trabalho no diretorio: ", ftp.pwd())

def menu_principal():
	print ()
	print ('++----------------------------------------------------------------------------------++')
	print ('++                              Menu Principal                                      ++')
	print ('++----------------------------------------------------------------------------------++')
	print ('++  COD.        FUNCAO.                                                             ++')
	print ('++  01          Listar Arquivo e DIretorios                                         ++')
	print ('++  02          Acessar Um Diretorio do Servidor                                    ++')
	print ('++  03          Enviar Arquivos                                                     ++')
	print ('++  05          Criar Diretorio                                                     ++')
	print ('++  06          Remover Diretorio                                                   ++')
	print ('++  04          Sair                                                                ++')
	print ('++----------------------------------------------------------------------------------++')	


def listar(argumento): #Listar arquivos e diretorios do servidor
	print ()
	print ('++----------------------------------------------------------------------------------++')
	print ('++                           Listar Diretorios                                      ++')
	print ('++----------------------------------------------------------------------------------++')
	ftp.retrlines(argumento)

def encerrando_conexão():
	ftp.quit()

def diretorio_cwd(caminho):
	ftp.cwd(caminho)

def diretorio_mkd(caminho):
	ftp.mkd(caminho)

def diretorio_rmd(caminho):
	ftp.rmd(caminho)

def uploader(caminho):
    caminho += '*'
    for dire in glob.glob(caminho):
    	myfile = open(dire,'rb')
    	filename = os.path.basename(dire)
    	ftp.storlines('STOR ' + filename, myfile)
    	myfile.close()
