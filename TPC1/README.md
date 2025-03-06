# Somador ON/OFF

### 2025/02/13

**[A104001]**: Frederico Cunha Afonso  

![Fred](../Photo.png)  

## Info
Este trabalho consistiu em criar "`um programa que soma-se todas as sequências de dígitos que encontre num texto`", tendo comportamentos diferentes, dependendo dos elementos "especiais" presentes no input dado (uma descrição mais aprofundada encontra-se no documento referenciado nos "Anexos").

Foram feitas duas resoluções para este enunciado:

* `someSum` que vai somando cada dígito individualmente
  * `"on12"` irá devolver `3`
  * `"1234on900"` irá devolver `10`

* `SUM` que interpreta os números lidos por inteiro
  * `"on12"` irá devolver `12`
  * `"1234off900"` irá devolver `1234`


### someSum
É de salientar que o programa é `case-insensitive` e que defini ambos programas com a intenção de **começar a soma desde o início do programa, sem precisar que seja interpretado um `ON` do input inicialmente**, estando a `flag`, posteriormente mencionada, inicialmente com o estado `True`

Após definir um booleano `flag: bool` um acumulador `x: int` e `ns: str`, o programa irá iterar pela string presente no input, passando cada char da string original para o acumulador `ns`. 
Caso seja detetado um `on` ou `off` no acumulador `ns`, a `flag` mudará de estado (`"on" -> True` | `"off" -> False`). 

Caso a `flag` se encontre num estado:

* `True`, o programa irá somar o dígito lido do input no acumulador `x`.
* `False`, irá guardar os próximos chars do input no acumulador `ns` para, nas próximas iterações, verificar se foram detetados algum dos seguintes elementos especiais: `on`, `off`, `=`, mais tarde apagando o acumulador caso a `flag` altere de estado.

Finalmente, caso seja detetado a ocorrência de um char `=` no input, será colocado o valor atual do acumulador `x: int` na saída (usando um simples `print`).

### SUM

Este programa irá funcionar exatamente da mesma maneira que o anterior, usando um acumulador extra (`acc: str`), onde, quando a `flag` estiver "ativa", irá guardar o valor do número a ser lido pelo programa do input. Após o número ser lido por completo do input (quando for encontrado um alfanumérico que não seja um dígito que siga o número lido recentemente) o programa somará o valor guardado no `acc` ao acumulador `x`

### Testes
Após desenvolver ambas resoluções, foram passados todos os testes feitos e confirmei que cada função estava a funcionar corretamente perante o contexto dado a cada uma

## Anexos 
- [`TP`](TPC1.ipynb) - [Resoluções e Testes] 
- [`Enunciado`](Enunciado.pdf) - [Enunciado] 
---