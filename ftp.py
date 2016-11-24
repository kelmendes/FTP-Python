from ftplib import FTP

def main():
    ftp = FTP('ftp.ibiblio.org')
    print("Bem Vindo:", ftp.getwelcome())
    ftp.login()
    print("Voce esta trabalho no diretorio: ", ftp.pwd())
    ftp.quit()

if _name_=='_main_':
    main()
