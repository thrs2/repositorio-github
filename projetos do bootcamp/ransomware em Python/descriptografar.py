import os
from cryptography.fernet import Fernet

def carregar_chave():
    """Carrega a chave de criptografia do arquivo 'chave.key'."""
    return open("chave.key", "rb") .read()

def descriptografar_arquivo(caminho_arquivo, chave):
    """Descriptografa o arquivo especificado usando a chave fornecida."""
    f = Fernet(chave)
    with open(caminho_arquivo, "rb") as arquivo:
        dados_criptografados = arquivo.read()
    dados_descriptografados = f.decrypt(dados_criptografados)
    with open(caminho_arquivo, "wb") as arquivo:
        arquivo.write(dados_descriptografados)

def encontrar_arquivos(diretorio):
    """Encontra todos os arquivos no diretório especificado, excluindo este script e o arquivo de chave."""
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            if nome != "descriptografar.py" and not nome.endswith("chave.key"):
                lista.append(caminho)
    return lista

def executar_descriptografia():
    """Executa o processo de descriptografia em todos os arquivos encontrados."""
    chave = carregar_chave()
    arquivos_para_descriptografar = encontrar_arquivos("prática")
    for arquivo in arquivos_para_descriptografar:
        descriptografar_arquivo(arquivo, chave)

if __name__ == "__main__":
    executar_descriptografia()