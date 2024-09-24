# Experimental Virtual Interpreter for Lightweight Algorithmic Scripting and Integrated Operations (Evi-Lasio)

**Qualquer semelhança do nome da linguagem com pessoas reais ou não, é a mais pura e mera coincidência**

## Índice

- [Visão Geral](#visão-geral)
- [Instalação](#instalação)
- [Sintaxe](#sintaxe)
  - [Declarações de Variáveis](#1-declarações-de-variáveis)
  - [Instruções de Impressão](#2-instruções-de-impressão)
  - [Estruturas de Controle](#4-estruturas-de-controle)
    - [4.1 Instruções If](#41-instruções-if)
    - [4.2 Instruções Else](#42-instruções-else)
    - [4.3 Laços While](#43-laços-while)
  - [Chaves](#5-chaves)
  - [Operadores](#6-operadores)
- [Exemplo de Programa](#exemplo-de-programa)
- [Conclusão](#conclusão)

## Visão Geral

Evi-Lasio é uma linguagem imaginária criada para as listas 4 e 5 de paradigmas. Ela é uma linguagem criada para ser inconveniente e confusa de ser usada, os nomes de funções não fazem sentido e é uma linguagem incrivelmente limitada.

## Instalação

Para usar o Evi-Lasio, você precisa do Python e GCC instalados em seu computador.

Ao clonar este repositório você pode ser usado o arquivo `Evi-Lasio.bat` para listar os arquivos .evl presentes no diretório `Input` e então o script irá traduzir, colocar o respectivo `.c` dentro da pasta `Output` e executar o programa.

Alternativamente pode especificar um arquivo `.evl` na linha de comando, ou o script utilizará automaticamente o arquivo `main.evl` se nenhum for fornecido.

### Exemplo de uso:

1. Para usar um arquivo `.evl` específico:
    ```bash
    python EvlTranslator.py arquivo.evl
    ```

2. Para usar um arquivo dentro de uma pasta `Exemplo` especifica:
    ```bash
    pythom EvlTranslator.py ./Exemplo/arquivo.evl

4. Para usar o arquivo `main.evl` por padrão:
    ```bash
    python EvlTranslator.py
    ```

Isso gerará um arquivo `.c` correspondente no mesmo diretório, como `seu_arquivo.c` ou `main.c`.

## Sintaxe

### 1. Declarações de Variáveis

Para declarar uma variável, use a palavra-chave `evi`, seguida pelo nome da variável.
Para  declarar-la com um valor deve se usar seguido da declaração a palavra-chave `eh` seguida de um valor, terminando com dois pontos.

**Sintaxe:**
```
evi <nome_da_variavel>:
```

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

### 3. Input de Usuário

Para fazer com que uma variavel receba um valor do usuário, utlize da palavra chave `eh` seguida da função `vil?`.

**Sintaxe:**
```
<nome_variavel> eh vil?
```

**Exemplo:**
```
garrafas eh vil?
```

**Tradução para C:**
```c
scanf("%d", &garrafas);
```

### 4. Estruturas de Controle

#### 4.1 Instruções If

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

#### 4.2 Instruções Else

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

#### 4.3 Laços While

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

### 5. Chaves

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

### 6. Operadores

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