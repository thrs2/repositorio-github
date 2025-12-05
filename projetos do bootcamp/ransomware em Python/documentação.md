# Ransomware em Python
oque é um malware ?
Malware é um software malicioso desenvolvido para causar danos a sistemas computacionais, roubar informações ou comprometer a segurança de dispositivos. Existem diversos tipos de malware, incluindo vírus, worms, trojans, spyware, adware e ransomware.

## exemplos de malware conhecidos
- virús: é o mais conhecido, ele se anexa a arquivos legítimos e se espalha quando esses arquivos são compartilhados.
- worm: é um tipo de malware que se replica automaticamente e se espalha por redes, explorando vulnerabilidades em sistemas.
- trojan: é um malware que se disfarça como um software legítimo, mas na verdade realiza ações maliciosas quando executado.
- spyware: é um software que coleta informações sobre o usuário sem o seu consentimento, muitas vezes para fins de espionagem.
- adware: é um software que exibe anúncios indesejados no dispositivo do usuário, muitas vezes coletando dados de navegação para direcionar os anúncios.
- ransomware: é um tipo de malware que criptografa os arquivos do usuário e exige um resgate para desbloqueá-los.

  ### como eles entram no sistema?
  - anexados a e-mails de phishing
  - downloads de software malicioso
  - vulnerabilidades em software desatualizado
  - sites comprometidos
  - dispositivos removíveis infectados

## Ransomware
Ransomware é um tipo de malware que criptografa os arquivos de um sistema infectado, tornando-os inacessíveis ao usuário. O atacante então exige um resgate, geralmente em criptomoedas, em troca da chave de descriptografia necessária para recuperar os arquivos.

o código no arquivo [ransomware teste](<ransomware em python/ransomware.py>) implementa um ransomware simples em Python usando a biblioteca `cryptography`. Ele gera uma chave de criptografia, encontra arquivos específicos em um diretório, criptografa esses arquivos e exibe uma mensagem de resgate.