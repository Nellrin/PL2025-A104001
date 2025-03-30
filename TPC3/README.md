# Conversor de MarkDown para HTML

### 2025/02/27

**[A104001]**: Frederico Cunha Afonso  

![Fred](../Photo.png)

## Info
Aqui vamos criar um conversor que parta de um ficheiro **MarkDown** e crie um ficheiro alternativo em **HTML**, tendo apenas em conta os seguintes elementos:

#### Cabeçalhos
A função `Header` transforma `# Título` em `<h1>Título</h1>`<br> 
Usa regex (`r'^(#+)\s(.+)'`) para capturar `#`, `##`, `###`, ..., **N**`#`'s e, após passar a uma função secundária, irá devolver uma tag `<hN>` com **N** igual ao número de `#` capturados.

#### Negrito
A função `Bold` troca `**texto**` por `<b>texto</b>`<br> 
Regex: `r'\*\*(.*?)\*\*'`.

#### Itálico
A função `Italic` troca `*texto*` por `<i>texto</i>`<br> 
Regex: `r'(?<!\*)\*(?!\*)(.*?)(?<!\*)\*(?!\*)'`

#### Listas Numeradas
A função `NumList` converte listas numeradas (e não numeradas) em listas em "bullet-point":

# Comparação de Listas Markdown → HTML<br> 
| Markdown (Input)        | HTML (Output)           |
|-------------------------|-------------------------|
| `1. Item 1` <br> `2. Item 2` <br> `3. Item 3` | `<ol>` <br> `<li>Item 1</li>` <br> `<li>Item 2</li>` <br> `<li>Item 3</li>` <br> `</ol>` |
| `* Item A` <br> `* Item B` <br> `* Item C` | `<ul>` <br> `<li>Item A</li>` <br> `<li>Item B</li>` <br> `<li>Item C</li>` <br> `</ul>` |
<br> Regex: `r'(^(\d\..+\n?)+)'`


#### Links<br> 
A função Link transforma `[texto](URL)` em `<a href="URL">texto</a>`<br> 
Regex: `r'[^!]\[(.*?)\]\((.*?)\)'`

#### Imagens<br> 
A função Image transforma `![alt](URL)` em `<img src="URL" alt="alt"/>`<br> 
Regex: `r'!\[(.*?)\]\((.*?)\)'`


#### Função Principal<br> 
`MD2HTML` aplica todas as transformações e cria um ficheiro resultante em `.html`

### Testes
Como teste, foi utilizado o ficheiro `README.md` deste trabalho como ficheiro de input. Podemos assim encontrar na diretoria  `Testes` o ficheiro resultante.

- [`Teste`](Testes/README.html) - [Testes] 


## Anexos 
- [`TP`](TPC3.ipynb) - [Resolução] 
- [`Enunciado`](Enunciado.pdf) - [Enunciado] 
---
