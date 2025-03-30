# Conversor de MarkDown para HTML

### 2025/02/27

**[A104001]**: Frederico Cunha Afonso  

![Fred](../Photo.png)

## Info
Aqui vamos criar um conversor que parta de um ficheiro **MarkDown** e crie um ficheiro alternativo em **HTML**`, tendo apenas em conta os seguintes elementos:

### Cabeçalhos
A função `Header` transforma `# Título` em `<h1>Título</h1>`

Usa regex (`r'^(#+)\s(.+)'`) para capturar `#`, `##`, `###`, ..., **N**`#`'s e, após passar a uma função secundária, irá devolver uma tag `<hN>` com **N** igual ao número de `#` capturados.

### Negrito
A função `Bold` troca `**texto**` por `<b>texto</b>`

Regex: `r'\*\*(.*?)\*\*'`.

### Itálico
A função `Italic` troca `*texto*` por `<i>texto</i>`

Regex: `r'(?<!\*)\*(?!\*)(.*?)(?<!\*)\*(?!\*)'`

### Listas Numeradas
A função `NumList` converte listas numeradas (e não numeradas) em listas em "bullet-point":

# Comparação de Listas Markdown → HTML

| Markdown (Input)       | HTML (Output)          |
|------------------------|------------------------|
| 1. Item 1             | `<ol>`                  |
| 2. Item 2             | `  <li>Item 1</li>`     |
| 3. Item 3             | `  <li>Item 2</li>`     |
|                        | `  <li>Item 3</li>`     |
|                        | `</ol>`                 |
|                        |                        |
| * Item A              | `<ul>`                  |
| * Item B              | `  <li>Item A</li>`     |
| * Item C              | `  <li>Item B</li>`     |
|                        | `  <li>Item C</li>`     |
|                        | `</ul>`                 |


Regex: `r'(^(\d\..+\n?)+)'`

### Links
A função Link transforma `[texto](URL)` em `<a href="URL">texto</a>`

Regex: `r'[^!]\[(.*?)\]\((.*?)\)'`

### Imagens
A função Image transforma `![alt](URL)` em `<img src="URL" alt="alt"/>`

Regex: `r'!\[(.*?)\]\((.*?)\)'`


### Função Principal
`MD2HTML` aplica todas as transformações e cria um ficheiro resultante em `.html`


### Testes
Como teste, foi utilizado o ficheiro `README.md` deste trabalho como ficheiro de input. Podemos assim encontrar na diretoria  `Testes` o ficheiro resultante.

- [`Teste`](Testes/README.html) - [Testes] 


## Anexos 
- [`TP`](TPC3.ipynb) - [Resolução] 
- [`Enunciado`](Enunciado.pdf) - [Enunciado] 
---
