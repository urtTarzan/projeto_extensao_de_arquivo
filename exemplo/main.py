import os 
from shutil import move
from datetime import datetime




def pasta_extensoes(pasta, relatorio = True):
    movimento=0

    #verficando e criando a pasta arquivos
    if not os.path.exists(pasta):
        os.mkdir(pasta)
        print("a pasta arquivos foi criada com sucesso!")

   #se TRUE criando pasta "relarios"
    if relatorio == True:
        cont=1
        if not os.path.exists("relatorios"):
            os.mkdir("relatorios")
            
        
        if not os.path.exists(f"relatorios/relatorio1.csv"):
                with open('relatorios/relatorio1.csv',"w") as relatorio_arquivo:
                     relatorio_arquivo.write("ARQUIVO,SITUACAO\n")  
        else:
            cont=1
            while True:
                if not os.path.exists(f"relatorios/relatorio{cont}.csv"):
                    with open(f'relatorios/relatorio{cont}.csv',"w") as relatorio_arquivo:
                        relatorio_arquivo.write("ARQUIVO,SITUACAO\n")
                        break
                else:
                    cont+=1
        print()
        print("criando relatorio...")
                   
    #varrendo,separando e tratando dados colocando-os e pastas com base em sua extensão
    for raiz, pastas, arquivos in os.walk(pasta):
        
            for arquivo in arquivos:
                        

                extensao = arquivo.split('.')[-1]
                caminho= os.path.join(pasta,arquivo)
                pasta_destino = os.path.join(pasta,extensao)   
                arquivo_final = os.path.join(pasta_destino,arquivo) 
        
                if not os.path.exists(pasta_destino):
                    os.mkdir(pasta_destino)
            
                if not os.path.exists(arquivo_final):


                    #tratando erros para relatorios
                    if "."not in arquivo:
                        erro_incoerente = True
                    else:
                        erro_incoerente = False
                

                    try:
                        move(caminho,arquivo_final)
                    except Exception as erro:
                        if relatorio == True:
                            if erro_incoerente == True:
                                with open(f'relatorios/relatorio{cont}.csv',"a") as relatorio_arquivo:
                                    relatorio_arquivo.write(f"{arquivo},esse arquivo nao tem uma extensao \n")
                            else:
                                with open(f'relatorios/relatorio{cont}.csv',"a") as relatorio_arquivo:
                                    relatorio_arquivo.write(f"{arquivo},erro em ser movido pois esta em outra pasta =( \n")
                            
                    else:
                        if relatorio == True:
                            with open(f'relatorios/relatorio{cont}.csv',"a") as relatorio_arquivo:
                                relatorio_arquivo.write(f"{arquivo},exito em {arquivo_final}\n")
                            movimento+=1
               
    # informações do relatorio
    if relatorio == True:
        if movimento == 0 :
            with open(f'relatorios/relatorio{cont}.csv',"a") as relatorio_arquivo:
                relatorio_arquivo.write(f"nenhum arquivo foi movido\n")
        else:
            with open(f'relatorios/relatorio{cont}.csv',"a") as relatorio_arquivo:
                relatorio_arquivo.write(f"foram movidos {movimento} arquivos\n")
        with open(f'relatorios/relatorio{cont}.csv',"a") as relatorio_arquivo:
                relatorio_arquivo.write(f"relatorio de {datetime.now().strftime('%H:%M:%S')}\n")
        


                        
                        
    if movimento !=0:
        print()
        print("arquivos movidos com sucesso!")
    else:
        print()
        print("nenhum arquivo foi movido")
    print()
                        
                         
# rode o script                      
pasta_extensoes("arquivos")

# depois cheque o relatorio que foi gerado

# pode desligar o relatorio com pasta_extensoes("arquivos", False)



