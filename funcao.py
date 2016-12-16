import ftplib, os#Importando a biblioteca

ftp = None
def conexao(site, usuario, senha):# Funcao para realizar login
    global ftp #Tranformando a variavel ftp lobal
    ftp = ftplib.FTP(site) #tentando acessar o site
    print("Welcome:", ftp.getwelcome())
    ftp.login(user= usuario, passwd= senha) #realizando loin no site
    print("Voce esta trabalho no diretorio: ", ftp.pwd())

def menu_principal(): #menu principal
	print ()
	print ('++----------------------------------------------------------------------------------++')
	print ('++                              Menu Principal                                      ++')
	print ('++----------------------------------------------------------------------------------++')
	print ('++  COD.        FUNCAO.                                                             ++')
	print ('++  01          Listar Arquivo e DIretorios                                         ++')
	print ('++  02          Acessar Um Diretorio do Servidor                                    ++')
	print ('++  03          Enviar Arquivo                                                      ++')
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

def encerrando_conexão(): #encerra conexao
	ftp.quit()

def diretorio_cwd(caminho): #acessar diretorio === comando cwd no linux
	ftp.cwd(caminho)

def diretorio_mkd(caminho): #criando diretoriso == mkdir no linux
	ftp.mkd(caminho)

def diretorio_rmd(caminho): #apango dietorio == rmdir no linux
	ftp.rmd(caminho)

def uploader(caminho): #@Uploader de um arquivo
    myfile = open(caminho,'rb')
    filename = os.path.basename(caminho)
    ftp.storlines('STOR ' + filename, myfile)
    myfile.close()
