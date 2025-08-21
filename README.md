

# Sistema de Cadastro de Peças

Este projeto é um sistema simples de gerenciamento de peças, desenvolvido em Python, que roda diretamente no terminal. Ele permite ao usuário adicionar, listar e buscar peças, utilizando os conceitos de Programação Orientada a Objetos (POO).

## Funcionalidades

  * **Adicionar Peça**: Permite cadastrar uma nova peça informando seu nome, fabricante e preço. Um ID único é gerado automaticamente para cada peça.
  * **Listar Todas as Peças**: Exibe uma lista completa de todas as peças que foram cadastradas no sistema.
  * **Buscar Peça por Nome**: Permite ao usuário buscar por uma peça específica digitando seu nome. A busca não diferencia maiúsculas de minúsculas.
  * **Menu Interativo**: A interação com o sistema é feita através de um menu de console simples e intuitivo.

## Estrutura do Código

O código está dividido em duas partes principais:

### 1\. Classe `Peca`

A classe `Peca` serve como um modelo para criar objetos que representam cada peça.

  * **Atributos**:

      * `Id`: (int) Identificador único da peça.
      * `nome`: (str) Nome da peça.
      * `fabric`: (str) Nome do fabricante.
      * `preco`: (int) Preço da peça.

  * **Métodos**:

      * `__init__(...)`: Método construtor, responsável por inicializar os atributos do objeto no momento da sua criação.
      * `MostraRegistro()`: Imprime no console todos os dados da peça de forma organizada.
      * `GetRegistro()`: Retorna um dicionário contendo todos os dados da peça, facilitando o acesso aos seus atributos (usado na função de busca).

### 2\. Bloco Principal (Main)

Esta é a seção onde o programa é executado. Ele contém um loop `while True` que exibe o menu de opções e gerencia a interação com o usuário, controlando a lista de peças cadastradas.

## Como Executar

### Pré-requisitos

  - É necessário ter o **Python 3** instalado em sua máquina.

### Passos

1.  Salve o código em um arquivo com a extensão `.py` (por exemplo, `cadastro_pecas.py`).
2.  Abra um terminal ou prompt de comando.
3.  Navegue até a pasta onde você salvou o arquivo.
4.  Execute o seguinte comando:
    ```bash
    python cadastro_pecas.py
    ```
5.  O menu interativo aparecerá no terminal e você poderá começar a usar o programa.