# Man in the Middle (MitM)
O ataque Man in the Middle (MitM) é uma técnica onde o atacante intercepta e possivelmente altera a comunicação entre duas partes sem que elas saibam. Esse tipo de ataque pode ser usado para roubar informações sensíveis, como credenciais de login, dados financeiros ou outras informações pessoais.

##  tipos de ataques MitM
1. **Ataque de Interceptação**: O atacante intercepta a comunicação entre duas partes, podendo ler ou modificar as mensagens trocadas.
2. **Ataque de Repetição**: O atacante captura uma mensagem legítima e a retransmite posteriormente para enganar uma das partes.
3. **Ataque de Eavesdropping**: O atacante escuta passivamente a comunicação sem alterar o conteúdo, apenas coletando informações.
4. **Ataque de Spoofing**: O atacante se faz passar por uma das partes na comunicação, enganando a outra parte para que revele informações sensíveis.
> **observação:** para realizar o teste iremos utilizar a ferramenta **sniffing** chamada **wireshark**, que é uma ferramenta popular para realizar ataques MitM. mas antes de iniciar o ataque, certifique-se de que você tem permissão para testar a rede alvo e que está em conformidade com as leis locais.

## capturando pacotes com wireshark
o wireshark é uma ferramenta poderosa para capturar e analisar pacotes de rede.
ele funciona colocando a interface de rede em modo promíscuo, permitindo que ele capture todos os pacotes que passam pela rede, não apenas aqueles destinados ao dispositivo onde o wireshark está sendo executado. além  ele é do tipo sniffer, ou seja, ele captura os pacotes de dados que trafegam em uma rede de computadores.
o wireshark pode ser usado para diversos fins, incluindo:
- **Análise de Rede**: identificar problemas de desempenho, gargalos e falhas na rede.
- **Segurança**: detectar atividades suspeitas, como tentativas de intrusão ou ataques de negação de serviço (DoS).
- **Desenvolvimento de Protocolos**: analisar o comportamento de novos protocolos de rede.
- **Educação**: aprender sobre protocolos de rede e como eles funcionam.

### passos para capturar pacotes com wireshark
1. **Instalação**: baixe e instale o wireshark a partir do site oficial (https://www.wireshark.org/).
2. **Seleção da Interface de Rede**: abra o wireshark e selecione a interface de rede que você deseja monitorar (por exemplo, Wi-Fi ou Ethernet).
3. **Iniciar Captura**: clique no botão "Iniciar Captura" (ícone de tubarão) para começar a capturar pacotes.
4. **Filtragem de Pacotes**: use filtros para focar em tipos específicos de tráfego (por exemplo, `http`, `tcp`, `ip.addr == 192.168.1.1`).

## ettercap
o ettercap é uma ferramenta de código aberto usada para realizar ataques de Man in the Middle (MitM) em redes locais. ele permite que os usuários interceptem, modifiquem e injetem pacotes de dados em comunicações de rede. o ettercap é amplamente utilizado por profissionais de segurança para testar a segurança de redes e identificar vulnerabilidades.

ele pode ser usado tanto para ip quanto para mac address, e pode ser utilizado em redes cabeadas ou sem fio.

ele pode ser operado por arp em que envenena a tabela arp dos dispositivos na rede, fazendo com que o tráfego destinado a um dispositivo seja redirecionado para o atacante. quando por PublicARP, ele envia respostas arp falsas para todos os dispositivos na rede, fazendo com que eles atualizem suas tabelas arp com o endereço mac do atacante como o gateway padrão.

### passos para realizar um ataque mitm com ettercap
1. **Instalação**: instale o ettercap a partir do repositório oficial da sua distribuição linux ou baixe o código-fonte do site oficial (https://www.ettercap-project.org/).
2. **Configuração da Rede**: certifique-se de que você está conectado à rede local onde deseja realizar o ataque mitm.
3. **Iniciar o Ettercap**: abra um terminal e execute o ettercap com privilégios de superusuário (`sudo ettercap -G` para a interface gráfica ou `sudo ettercap -T -q` para a interface de linha de comando).
4. **Selecionar a Interface de Rede**: escolha a interface de rede que você deseja usar para o ataque mitm.
5. **Escanear a Rede**: use o ettercap para escanear a rede e identificar os dispositivos conectados.
6. **Selecionar Alvos**: escolha os dispositivos que você deseja atacar (por exemplo, o gateway e a vítima).
7. **Iniciar o Ataque MitM**: inicie o ataque mitm usando o ettercap, que irá envenenar as tabelas arp dos dispositivos selecionados.
8. **Monitorar o Tráfego**: use o ettercap para monitorar e capturar o tráfego de rede entre os dispositivos atacados.
9. **Analisar os Dados**: analise os dados capturados para identificar informações sensíveis, como credenciais de login, dados financeiros ou outras informações pessoais.
10. **Encerrar o Ataque**: quando terminar, encerre o ataque mitm e restaure as tabelas arp dos dispositivos afetados para evitar interrupções na rede.