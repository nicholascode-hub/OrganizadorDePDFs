# [Organizador de PDFs]

Este script Python automatiza a organização de arquivos PDF, movendo todos os arquivos com extensão .pdf de um diretório de origem para um diretório de destino especificado. Ideal para manter sua pasta de downloads ou outras pastas organizadas com PDFs em um local específico.

## [Funcionalidades]

- [Cria a pasta de destino automaticamente caso ela não exista.]
- [Move todos os arquivos PDF (extensão .pdf, sem distinção de maiúsculas ou minúsculas) do diretório origem para o diretório destino.]
- [Exibe no console cada arquivo movido.]

## [Requisitos]

- [Python 3.x instalado.]
- [Permissões de leitura e escrita nas pastas de origem e destino.]

## [Como usar]

- [Edite as variáveis origem e destino no bloco principal do script para os diretórios desejados.]

- Execute o script:

python main.py


[Todos os arquivos PDF da pasta de origem serão movidos para a pasta de destino.]

## [Exemplo]

origem = r"C:\Users\Downloads"
destino = r"C:\Users\Documentos\libraryPDF"
organizar_pdfs(origem, destino)

text

## [Observações]

- [O script não copia, mas move os arquivos, ou seja, eles serão removidos da pasta de origem.]
- [Somente arquivos com extensão .pdf são tratados.]

## [Licença]

[Este projeto está aberto para uso e modificação livre.]
