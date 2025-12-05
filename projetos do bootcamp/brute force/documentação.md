# documentação brute force
esse documento tem como objetivo descrever as atividades práticas realizadas no laboratório de brute force durante o bootcamp de segurança cibernética promovido pelo Santander em parceria com a DIO.

## autenticação

autenticação atua como o processo de verificação da identidade de um usuário ou sistema antes de conceder acesso a recursos protegidos exemplo:

### protocolo de autenticação HTTP basic
- o cliente envia uma solicitação HTTP com um cabeçalho "Authorization" que contém as credenciais codificadas em base64. 
- o servidor decodifica as credenciais e verifica se são válidas.
- se as credenciais forem válidas, o servidor concede acesso ao recurso solicitado; caso contrário, retorna um erro de autenticação (401 Unauthorized).

### autenticação com estado de sessão
- o cliente envia uma solicitação de login com suas credenciais.
- o servidor verifica as credenciais e, se forem válidas, cria uma sessão para o usuário.
- o servidor envia um cookie de sessão ao cliente, que o armazena.
- em solicitações subsequentes, o cliente envia o cookie de sessão para o servidor.
- o servidor verifica o cookie de sessão para autenticar o usuário e conceder acesso aos recursos protegidos.

### autenticação federada
- o usuário tenta acessar um recurso protegido em um serviço (provedor de serviço).
- o serviço redireciona o usuário para um provedor de identidade confiável.
- o usuário autentica-se no provedor de identidade. ex: **google**, **facebook**, **edge**,**etc**.
- o provedor de identidade emite um token de autenticação.
- o usuário retorna ao serviço com o token.
- o serviço valida o token com o provedor de identidade.
- se o token for válido, o serviço concede acesso ao recurso protegido. 

## tipos de ataques de brute force
o ataque de brute force é uma técnica utilizada por invasores para obter acesso não autorizado a sistemas, contas ou dados, buscando as senhas por diversas combinações de tentativa e erro.

### ataque de dicionário
- o atacante utiliza uma lista pré-definida de palavras comuns, frases ou combinações de caracteres (dicionário) para tentar adivinhar a senha.
- eles podem ser feitas manualmente ou com o auxílio de vazamentos de senhas anteriores.

> exemplo: se a senha for "senha123", o atacante pode tentar combinações como "senha", "123", "senha123", etc.

- o ataque de dicionário é mais eficiente do que o brute force tradicional, pois se concentra em senhas que são mais prováveis de serem usadas pelos usuários.
 
 > motivo esse que as senhas sempre devem ser fortes e complexas, evitando palavras comuns ou combinações previsíveis.

 ### ataque por permutação

 - o atacante tenta todas as combinações possíveis de caracteres para adivinhar a senha.
 - esse tipo de ataque é mais demorado e exige mais recursos computacionais, especialmente para senhas longas e complexas.

 ### ataque híbrido
- o atacante combina técnicas de ataque de dicionário e permutação.
- eles começam com uma lista de palavras comuns e, em seguida, aplicam variações, como adicionar números ou caracteres especiais, para aumentar as chances de sucesso.

#### regras de modificação
- adicionar números no início ou no final da palavra (ex: "senha" -> "senha123")
- substituir letras por números ou caracteres especiais (ex: "a" -> "@", "e" -> "3")
- alterar a capitalização das letras (ex: "senha" -> "Senha" ou "SENHA")

#### junção de listas
- combinar duas ou mais listas de palavras para criar novas combinações (ex: lista1 = ["senha", "admin"], lista2 = ["123", "2024"] -> combinações: "senha123", "admin2024", etc.)

## passoword spraying e credencial stuffing
- password spraying: o atacante tenta um conjunto limitado de senhas comuns em um grande número de contas de usuário, evitando bloqueios de conta devido a múltiplas tentativas falhas.
- credencial stuffing: o atacante utiliza credenciais vazadas (combinações de nomes de usuário e senhas) de outras violações de dados para tentar acessar contas em diferentes serviços, explorando a tendência dos usuários de reutilizar senhas.

### kali linux
- o kali linux é uma distribuição linux baseada em debian, projetada para testes de penetração e auditorias de segurança.
- ele vem pré-instalado com uma ampla variedade de ferramentas de segurança, incluindo aquelas para ataques de brute force, como hydra, john the ripper e medusa.

### ferramentas de brute force no kali linux

#### medusa
- o medusa é uma ferramenta de força bruta paralela rápida e modular, usada para realizar ataques de brute force em vários protocolos, como FTP, SSH, HTTP, entre outros.
- ele suporta ataques de dicionário e pode ser configurado para usar diferentes listas de senhas e nomes de usuário.
- ele pode ser utilizado para muitos usuários e senhas simultaneamente, tornando-o eficiente para ataques em larga escala.
- ele é muito utilizado para auditorias de segurança em redes e sistemas.

#### hydra
- o hydra é uma ferramenta de força bruta rápida e flexível, capaz de realizar ataques em diversos protocolos, como FTP, SSH, Telnet, HTTP, entre outros.
- ele suporta ataques de dicionário e pode ser configurado para usar diferentes listas de senhas e nomes de usuário.
- no entanto não é tão eficiente para ataques offline, como arquivos de senha hash.

#### ncrack
- o ncrack é uma ferramenta de força bruta que foi criado pelo mesmo desenvolvedor do nmap. então ele é capaz de ser integrado com o nmap para realizar ataques de brute force em serviços descobertos durante a varredura de rede.
- ele é otimizado para latencia e desempenho, permitindo ataques em redes grandes e complexas.
- também possui o modo stealth, que ajuda a evitar a detecção por sistemas de segurança.
- ele não é recomendado para ataques web, como html forms ou autenticação baseada em cookies.

#### john the ripper
- o john the ripper é uma ferramenta é uma das mais populares para a quebra de senhas offline.
- quanto tiver o hash da senha, o john the ripper pode ser usado para tentar descobrir a senha original por meio de ataques de dicionário, permutação ou ataques híbridos.
- ele suporta uma ampla variedade de formatos de hash, incluindo MD5, SHA-1, SHA-256, entre outros.
- ele também possui recursos avançados, como regras de modificação e ataques baseados em máscara, que permitem personalizar as tentativas de quebra de senha.
- ele não é adequado para ataques online, como autenticação em serviços de rede.

#### wpscan
- o wpscan é uma ferramenta específica para a análise de segurança de sites baseados em wordpress.
- ele pode ser usado para identificar vulnerabilidades, temas e plugins desatualizados, e realizar ataques de brute force em contas de administrador do wordpress.
- ele suporta ataques de dicionário e pode ser configurado para usar diferentes listas de senhas e nomes de usuário.
- ele também tem integrado com o banco de dados de vulnerabilidades online do wordpress, permitindo identificar rapidamente problemas conhecidos.
- ele não é adequado para ataques em outros tipos de sites ou serviços que não sejam wordpress.

#### patator
- ele é voltado para usuários avançados que desejam uma ferramenta altamente personalizável para realizar ataques de brute force em diversos protocolos e serviços.
- o patator suporta ataques de dicionário e pode ser configurado para usar diferentes listas de senhas e nomes de usuário.
- ele permite a criação de scripts personalizados para automatizar ataques e adaptar-se a diferentes cenários.
- ele não é tão amigável para iniciantes, exigindo um conhecimento mais profundo sobre a ferramenta e os protocolos alvo.