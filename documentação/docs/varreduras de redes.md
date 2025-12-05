## VARREDURAS DE REDES

a varredura de redes na área de cibersegurança é uma atividade com o objetivo de encontrar a computadores ativos com portas e serviços em aberto.

### tipos de varreduras
- **portas**: 443,80,21,22
- **redes**:  listar endereços de ip dentro de redes
- **vulnerabilidades**: buscar vulnerabilidades conhecidas

### varreduras e enumeração
| Termo        | Descrição                                                                                             |
|--------------|---------------------------------------------------------------------------------------------------------|
| Varredura    | Verifica quais redes/serviços estão abertos, ativos e/ou potencialmente vulneráveis no computador.     |
| Enumeração   | Analisa em detalhe os serviços descobertos: versão, usuários online, configurações expostas, etc.      |

### nmap
o nmap é uma ferramenta de código aberto usado para mapeamento de vulnerabilidades, serviços e portas abertas na rede.

***informações obtidas***:
-
- **NÚMERO DA PORTA**
- **PROTOCOLO**
- **NOME DO SERVIÇO**
---
- **ABERTO**
- **FILTRADO**
- **NÃO FILTRADO**
- **BLOQUEADO**

### atividade prática
usando o metasploitable e kali linux n0 virt-manager
> **observação:** o metasploitable está a ser usado na versão **ubuntu 8.04 lts**

após o comando ``nmap -v 192.168.100.0/24`` foi mostrado todas essas portas abertas no metasploitable 

![](<../.img/Captura de tela de 2025-11-24 19-54-58.png>)

já o comando ``nmap -v -sn 192.168.100.0/24`` mostrou que apenas os seguintes hosts estão ativos:
-
``Nmap scan report for 192.168.100.180
Host is up (0.00060s latency).
MAC Address: 52:54:00:60:4F:C5 (QEMU virtual NIC)``

