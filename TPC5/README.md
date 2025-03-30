# Máquina de Vending

### 2025/03/13

**[A104001]**: Frederico Cunha Afonso  

![Fred](../Photo.png)

## Info

Implementação de uma **máquina de vending** interativa, permitindo listar produtos, inserir moedas, selecionar itens e receber troco. O estoque é armazenado em um **arquivo JSON** e atualizado automaticamente.


- **Listar produtos disponíveis** com código, nome, quantidade e preço.  
- **Inserir moedas** e acompanhar o saldo acumulado.  
- **Selecionar produtos** pelo código, verificando saldo e disponibilidade.  
- **Receber troco** corretamente ao sair do sistema.  
- **Atualização automática do estoque** ao iniciar e encerrar o programa.  
- **Adicionar produtos ao estoque** (novos ou já existentes).  

| **Comando**                 | **Resposta da Máquina** |
|-----------------------------|------------------------|
| `LISTAR`                    | Lista de produtos e preços. |
| `MOEDA 1e, 20c, 5c, 5c .`   | `Saldo = 1e30c` |
| `SELECIONAR A23`            | `Pode retirar "água 0.5L"` |
| `SELECIONAR A23` (saldo insuf.) | `Saldo insuficiente` <br> `Saldo = 60c; Pedido = 70c` |
| `SAIR`                      | Manipulação de Dados efetuada salva |


### Testes
- [`Tests`](Stock.json) - [Testes] 


## Anexos 
- [`Enunciado`](Enunciado.pdf) - [Enunciado] 
- [`Resolução`](TPC5.py) - [Resolução] 
---