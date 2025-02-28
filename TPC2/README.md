# Análise de um dataset de obras musicais

### 2025/02/20

**[A104001]**: Frederico Cunha Afonso  

![Fred](../Photo.png)  

## Info
O `.csv` no qual este trabalho se baseia, segue o seguinte formato:

`nome;desc;anoCriacao;periodo;compositor;duracao;_id`

Aqui, foi requesitado o desenvolvimento de um programa com o intuito de "`ler um dataset de obras, processá-lo e demonstrar diferentes métricas obtidas, relacionadas aos campos deste`", mais especificamente, este programa terá de ser capaz de:
* Gerar uma lista (ordenada alfabeticamente) dos compositores musicais presentes no dataset;
* Expor a distribuição das obras por período;
* Criar um dicionário em que a cada período está a associada uma lista alfabética dos títulos das obras desse período.


Para responder apropriadamente, atribuí 1 função por cada query desejada (`getCompositores`, `obrasPorPeriodo` e `DictObrasPorPeriodo`).

### getCompositores
Inicialmente, criei uma Expressão Regular genérica, capaz de identificadr informações dos campos presentes para todas as entradas do `.csv`:

* `\s[^;]*?(?:;\"\"\"|;\")[^;]+(?:\"\"\";|\";)[^;]*?;[^;]*?;[^;]*?;[^;]*?;.*`

Sendo a distribuição de `campos` por `áreas da Expressão Regular` a que se segue:

* `\s[^;]*? = nome`
* `[^;]+ = desc`
* `[^;]*? = anoCriacao`
* `[^;]*? = periodo`
* `[^;]*? = compositor`
* `[^;]*? = duracao`
* `.* = _id`

Assim sendo, para a `getCompositores` só foi necessário:
- Tornar a `área da Expressão Regular` relativa aos `compositores` no "grupo de captura";
- Concretizar uma lista do obtido;
- Introduzir os resultados num set (para evitar entradas repetidos);
- Ordenar o set usando a função `sorted(...)`.


```py
l = []
pattern = r'\s[^;]*?(?:;\"\"\"|;\")[^;]+(?:\"\"\";|\";)[^;]*?;[^;]*?;([^;]*?);[^;]*?;.*'

l = set(re.findall(pattern,file.read(),re.MULTILINE))
l = sorted(l)
```


### obrasPorPeriodo
Como aqui o desejado é, basicamente, obter o número de ocorrências de cada `periodo` presente no `.csv`, defini esse campo como "grupo de captura". 
Após obter a lista de resultados, guardei cada entrada desta num dicionário onde a chave é o nome do `periodo` e o valor associado é o número de ocorrências do tal `periodo`.

```py
l = []
d = {}

pattern = r'\s[^;]*?(?:;\"?(?:\"\"|[^\"])*?\"?;)\d{4};([^;]*?);[^;]*?;[^;]*?;\d*?'

l = re.findall(pattern,file.read(),re.MULTILINE)

for x in l:
    if x not in d:
        d[x] = l.count(x)
```

### DictObrasPorPeriodo
Finalmente temos a `DictObrasPorPeriodo`, que deve devolver "`um dicionário em que a cada período está a associada uma lista alfabética dos títulos das obras desse período`".

Sendo assim, podemos usar a mesma lógica da `obrasPorPeriodo` com algumas alterações:

- Definir o `nome` e o `periodo` como "grupo de captura" (obtendo assim uma lista de tuplos);
- Armazenar cada entrada da lista resultante num dicionário, onde a chave será o `periodo` encontrado, e o valor será uma lista do `nome` de todas as obras relativas a esse;
- Ordenar cada entrada do dicionário usando a função `sorted(...)`. 

```py
l = []
d = {}

pattern = r'\s([^;]*?)(?:;\"?(?:\"\"|[^\"])*?\"?;)\d{4};([^;]*?);[^;]*?;[^;]*?;\d*?'

l = re.findall(pattern,file.read(),re.MULTILINE)

for x in l:
    if x[1] in d: d[x[1]].append(x[0])
    else: d[x[1]] = [x[0]]

for y in d:
    d[y].sort()
```

### obrasStats
De maneira a encapsular todas as funções definidas, juntei-as todas na `obrasStats`, que, após ser dado o caminho para o ficheiro `.csv`, irá passá-lo para as outras funções, e estas irão devolver o resultado obtido num tuplo de 3 elementos.

```py
def obrasStats(path):
  return(getCompositores(path),obrasPorPeriodo(path),DictObrasPorPeriodo(path))
```

### Testes
Só foram feitos testes às primeiras 3 funções por conveniência e por ser redundante testar a última função `obrasStats` após testar as anteriores.
Os testes foram baseados num `.csv` providenciado pelos professores e devolveram resultados esperados para cada função definida.

## Anexos 
- [`TP`](TP2.ipynb) - [Enunciado, Resoluções e Testes] 
---
