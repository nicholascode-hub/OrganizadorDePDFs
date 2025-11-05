import os
import shutil

def organizar_pdfs(diretorio_origem, diretorio_destino):
    # Cria a pasta destino se não existir
    os.makedirs(diretorio_destino, exist_ok=True)

    # Lista todos os arquivos na pasta origem
    for arquivo in os.listdir(diretorio_origem):
        caminho_arquivo = os.path.join(diretorio_origem, arquivo)

        # Verifica se é um arquivo e termina com .pdf (case insensitive)
        if os.path.isfile(caminho_arquivo) and arquivo.lower().endswith('.pdf'):
            destino = os.path.join(diretorio_destino, arquivo)

            # Move o arquivo para o diretório destino
            shutil.move(caminho_arquivo, destino)
            print(f"Movido: {arquivo} -> {diretorio_destino}")

if __name__ == "__main__":
    origem = r"" #caminho de origem
    destino = r"" #destino 
    organizar_pdfs(origem, destino)
