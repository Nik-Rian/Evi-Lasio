# Experimental Virtual Interpreter for Lightweight Algorithmic Scripting and Integrated Operations (Evi-Lasio)

**Qualquer semelhança do nome da linguagem com pessoas reais ou não, é a mais pura e mera coincidência**

Evi-Lasio é uma linguagem imaginária criada para as listas 4 e 5 de paradigmas. Ela é uma linguagem criada para ser inconveniente e confusa de ser usada, os nomes de funções não fazem sentido e é uma linguagem incrivelmente limitada.

## Índice

- [Visão Geral](#visão-geral)
- [Instalação](#instalação)
- [Sintaxe](#sintaxe)
  - [Declarações de Variáveis](#1-declarações-de-variáveis)
  - [Instruções de Impressão](#2-instruções-de-impressão)
  - [Estruturas de Controle](#3-estruturas-de-controle)
    - [3.1 Instruções If](#31-instruções-if)
    - [3.2 Instruções Else](#32-instruções-else)
    - [3.3 Laços While](#33-laços-while)
  - [Chaves](#4-chaves)
  - [Operadores](#5-operadores)
- [Exemplo de Programa](#exemplo-de-programa)
- [Conclusão](#conclusão)

## Visão Geral

Evi-Lasio é uma linguagem divertida e educativa que permite aos usuários explorar a programação de uma maneira leve e acessível. A tradução do código para C ajuda a compreender a lógica por trás da programação.

## Instalação

Para usar o Evi-Lasio, você precisa do Python instalado em seu computador. Clone este repositório e execute o arquivo `tradutor.py` para traduzir seus arquivos `.evl` para C.

```bash
git clone https://github.com/seu-usuario/Evi-Lasio.git
cd "Evi-Lasio"
python tradutor.py
```

## Sintaxe

### 1. Declarações de Variáveis

Para declarar uma variável, use a palavra-chave `evi`, seguida pelo nome da variável, pela palavra-chave `eh` e pelo valor inicial, terminando com dois pontos.

**Sintaxe:**
```
evi <nome_da_variável> eh <valor>:
```

**Exemplo:**
```
evi garrafas eh 99:
```

**Tradução para C:**
```c
int garrafas = 99;
```

### 2. Instruções de Impressão

Para imprimir saídas, use a função `evilas`. Strings podem conter variáveis entre asteriscos (`*`). Se não houver variáveis, basta imprimir a string.

**Sintaxe:**
```
evilas("<string_com_variáveis>"):
```

**Exemplo:**
```
evilas("*garrafas* garrafas de cerveja na prateleira, *garrafas* de cerveja."):
```

**Tradução para C:**
```c
printf("%d garrafas de cerveja na prateleira, %d de cerveja.", garrafas, garrafas);
```

### 3. Estruturas de Controle

#### 3.1 Instruções If

Use a palavra-chave `lasi` para criar uma instrução if. A condição usa o operador `eh?` para verificações de igualdade.

**Sintaxe:**
```
lasi(<condição>):
```

**Exemplo:**
```
lasi(garrafas Neh? 0):
```

**Tradução para C:**
```c
if(garrafas != 0) {
```

#### 3.2 Instruções Else

Use a palavra-chave `evio` para criar uma instrução else.

**Sintaxe:**
```
evio:
```

**Exemplo:**
```
evio:
```

**Tradução para C:**
```c
else {
```

#### 3.3 Laços While

Use a palavra-chave `lasio` para criar um laço while. A condição pode incluir vários operadores de comparação.

**Sintaxe:**
```
lasio(<condição>):
```

**Exemplo:**
```
lasio(garrafas Neh? 0):
```

**Tradução para C:**
```c
while(garrafas != 0) {
```

### 4. Chaves

Use os símbolos `>` e `<` para indicar o início e o fim de um bloco de código.

**Exemplo:**
```
>
    // código aqui
<
```

**Tradução para C:**
```c
{
    // código aqui
}
```

### 5. Operadores

Evi-Lasio suporta os seguintes operadores:

- **Igualdade**: `eh?` (tradução para `==`)
- **Desigualdade**: `Neh?` (tradução para `!=`)
- **Menor que**: `meh?` (tradução para `<`)
- **Maior que**: `Meh?` (tradução para `>`)

## Exemplo de Programa

Aqui está um exemplo completo que demonstra vários recursos do Evi-Lasio:

```plaintext
evi garrafas eh 99:
evilas("*garrafas* garrafas de cerveja na prateleira, *garrafas* de cerveja."):
lasio(garrafas Neh? 0):
>
    evilas("Pegue uma, passe para o próximo.\n"):
    garrafas eh garrafas - 1:
<
```

**Tradução para C:**
```c
#include <stdio.h>

int main() {
    int garrafas = 99;
    printf("%d garrafas de cerveja na prateleira, %d de cerveja.", garrafas, garrafas);
    while(garrafas != 0) {
        printf("Pegue uma, passe para o próximo.\n");
        garrafas = garrafas - 1;
    }
    return 0;
}
```

## Conclusão

Evi-Lasio é uma linguagem feita nas coxas, que provavelmente nunca será utilizada sériamente por ninguem, pelo menos não deveria. Serviu apenas como aprendizado para entender como algumas linguagens exotericas são criadas.