import ftplib #Importando a biblioteca

ftp = None
def conexao(site, usuario, senha):# Funcao para realizar login
    global ftp
    ftp = ftplib.FTP(site)
    ftp.login(user= usuario, passwd= senha)
    print("Voce esta trabalho no diretorio: ", ftp.pwd())


def listar(argumento): #Listar arquivos e diretorios do servidor
    ftp.retrlines(argumento)

def encerrando_conexão():
	ftp.quit()

def diretorio(caminho):
	ftp.cwd(caminho)

'''
    # Daki para baixo estou testando enviar UM arquivo para o servidor
    filename = "index.html"
    ftp.cwd('keumendes.net16.net')
    myfile = open('/index.html','rb')
    ftp.storlines('STOR '+filename, myfile)
 '''
