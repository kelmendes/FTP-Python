from ftplib import FTP #Importando a biblioteca 

def main(): # Funcao para realizar login
    ftp = FTP('keumendes.net16.net') #Informando o Dominio(Site)
    ftp.login(user='a7856848', passwd='klebson') #Realizando Login
    print("Voce esta trabalho no diretorio: ", ftp.pwd())
    ftp.quit()
main()
