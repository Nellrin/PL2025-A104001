# Analisador Léxico

### 2025/03/06

**[A104001]**: Frederico Cunha Afonso  

![Fred](../Photo.png)

## Info
### Analisador Léxico para Query Language

Implementar um **analisador léxico** para uma linguagem de query. 

#### Como funciona

- Identifica **keywords** como `SELECT`, `WHERE`, `LIMIT`.
- Reconhece **variáveis** (`?var`), **strings** (`"texto"`), e **prefixos** (`foaf:name`).
- Processa **símbolos especiais** (`{`, `}`, `.`) e números (`1000`).
- Gera uma lista de tokens organizados por linha da query.

## 📜 Exemplo de Entrada e Saída

| **Query inicial** | **Tokens** |
|----------------------|--------------------|
| `SELECT ?nome ?desc WHERE {` | `('SELECT', 'SELECT')` <br> `('VAR', '?nome')` <br> `('VAR', '?desc')` <br> `('WHERE', 'where')` <br> `('L_PAR', '{')` |
| `?s a dbo:MusicalArtist.` | `('VAR', '?s')` <br> `('A', 'a')` <br> `('CPF', 'dbo')` <br> `('CPFVAR', 'MusicalArtist')` <br> `('EOL', '.')` |
| `?s foaf:name "Chuck Berry"@en .` | `('VAR', '?s')` <br> `('CPF', 'foaf')` <br> `('TP', ':')` <br> `('CPFVAR', 'name')` <br> `('STRING', '"Chuck Berry"')` <br> `('AT', '@')` <br> `('ENC', 'en')` <br> `('EOL', '.')` |
| `?w dbo:artist ?s.` | `('VAR', '?w')` <br> `('CPF', 'dbo')` <br> `('TP', ':')` <br> `('CPFVAR', 'artist')` <br> `('VAR', '?s')` <br> `('EOL', '.')` |
| `?w foaf:name ?nome.` | `('VAR', '?w')` <br> `('CPF', 'foaf')` <br> `('CPFVAR', 'name')` <br> `('VAR', '?nome')` <br> `('EOL', '.')` |
| `?w dbo:abstract ?desc` | `('VAR', '?w')` <br> `('CPF', 'dbo')` <br> `('TP', ':')` <br> `('CPFVAR', 'abstract')` <br> `('VAR', '?desc')` |
| `} LIMIT 1000` | `('R_PAR', '}')` <br> `('LIMIT', 'LIMIT')` <br> `('NUM', '1000')` |


### Testes
- [`Tests`](Tests/output.txt) - [Testes] 


## Anexos 
- [`Enunciado`](Enunciado.pdf) - [Enunciado] 
- [`Resolução`](TPC4.py) - [Resolução] 
---