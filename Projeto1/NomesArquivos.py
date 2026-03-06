from pathlib import Path

'''objetivo: Criar um programa que peça o caminho de uma pasta e depois crie um arquivo dentro dessa pasta contendo os nomes de todos os arquivos da pasta. 
Criterios:
1 - O script não pode atualizar o arquivo sem avisar;
2 - O script só deve executar se não for importado;
3 - O script deve dizer onde o arquivo foi criado;
4 - O arquivos precisa sempre testar se a pasta existe, caso não deverá parar o programa e alertar o usuário.
'''

def nomes_arquivos(caminho):
    #Se o caminho for válido, a função executará.
    if not Path(caminho).exists() or not Path(caminho).is_dir():
        print("Caminho não encontrado!!!")

    else:
        destino = Path(caminho)

        #Se já existir um arquivo com esse nome, o script vai alertar sobre a atualização.
        if Path(destino/'Nomes_arquivos.txt').exists():
            print('Arquivo de nomes já existe e será atualizado!')

        #vai criar o arquivo e capturar os nomes    
        Path(destino/'Nomes_arquivos.txt').touch
        arquivo = Path(destino/'Nomes_arquivos.txt')
        nomes = "\n".join(nome_arquivo.name for nome_arquivo in destino.iterdir())

        arquivo.write_text(nomes)

        print(f'Arquivo criado com sucesso {arquivo.name}')
    
            

if __name__ == "__main__":
    caminho = input("Digite o nome o caminho da pasta: ")
    nomes_arquivos(caminho)




