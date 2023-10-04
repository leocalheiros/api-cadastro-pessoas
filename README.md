# API Gerenciamento de Pessoas

## Descrição do Projeto

O Sistema de Gerenciamento de Pessoas é uma aplicação web construída com o framework Flask, que permite criar, encontrar, atualizar e excluir registros de pessoas em um banco de dados. Este projeto foi desenvolvido como uma demonstração de como criar uma aplicação web simples com Flask e implementar funcionalidades CRUD (Criar, Ler, Atualizar, Deletar) usando boas práticas de desenvolvimento.

## Funcionalidades Principais

- **Criar Pessoa:** Adicione novas pessoas ao banco de dados fornecendo seu nome, idade, bairro e profissão.

- **Encontrar Pessoa:** Pesquise pessoas existentes no banco de dados pelo nome.

- **Atualizar Pessoa:** Atualize as informações de uma pessoa existente no banco de dados, incluindo idade, bairro e profissão.

- **Deletar Pessoa:** Remova uma pessoa do banco de dados com base em seu nome.

## Configuração do Ambiente

Antes de executar o projeto, certifique-se de ter as seguintes dependências instaladas:

```bash
pip install -r requirements.txt
```

Para rodar o projeto execute:
```bash
python run.py
```

## Endpoints da API
### Criar pessoa

- **Endpoint**: `/create`
- **Método**: POST
- **Entrada**: JSON contendo nome, idade, bairro e profissão da pessoa.
- **Exemplo**: {
    "name": "João",
    "age": 30,
    "neighborhood": "Centro",
    "profession": "Engenheiro"
}

### Encontrar pessoa

- **Endpoint**: `/find`
- **Método**: GET
- **Entrada**: JSON contendo nome da pessoa a ser encontrada.
- **Exemplo**: {
    "name": "João",
}

### Atualizar pessoa

- **Endpoint**: `/update`
- **Método**: PUT
- **Entrada**:  JSON contendo nome, idade, bairro e profissão atualizados da pessoa.
- **Exemplo**: {
    "name": "João",
    "age": 35,
    "neighborhood": "Novo Bairro",
    "profession": "Gerente"
}

### Deletar pessoa

- **Endpoint**: `/delete`
- **Método**: DELETE
- **Entrada**:  JSON contendo nome da pessoa a ser deletada
- **Exemplo**: {
    "name": "João",
}
