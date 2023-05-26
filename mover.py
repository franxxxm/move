import os 


diretorio_das_pastas = "C:/Users/Administrador/Desktop/imagem"
pasta_com_todos_arquivos = 'C:\\Users\\Administrador\\Desktop\\imagem\\img'
extensao = ['png','jpg','jpeg','gif']

conteudo_do_bat = '@echo off \n'
for pasta_raiz, a, arquivos in os.walk(diretorio_das_pastas):
    for arquivo in arquivos:
        for tipos in extensao:
            final = arquivo.split(".")[1]
            if(tipos == final):
                caminho_completo = os.path.join(pasta_raiz, arquivo)
                caminho_completo = caminho_completo.replace("/", "\\")
                conteudo_do_bat += 'move "{}" "{}" \n'.format(caminho_completo, pasta_com_todos_arquivos)
                with open("movedor.bat", 'w', newline='\r\n') as pontoBAT:
                    pontoBAT.write(conteudo_do_bat)
