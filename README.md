# Desafio Fullstack Neoway

## Descrição do problema e solução
O problema proposto é um sistema simples de gerenciamento de CPF/CNPJ (CRUD), implementando uma interface REST mínima no back-end.

Levando em conta a arquitetura de API REST para o back-end o projeto foi desenvolvimento de maneira a desacoplar o máximo possível as soluções front-end e back-end, de modo que a API desenvolvida seja de uso geral e o front-end possa substituir a API sem grandes complicações.

## Stack escolhida
Para o front-end, o framework escolhido foi `Vue3`, devido a familiaridade com a ferramenta e oportunidade de aprender sobre uma versão mais nova (atualmente trabalho com a versão 2), utilizando do plugin `Vue-Router` para dar suporte a SPA.

No back-end a o (micro-)framework escolhido foi [Flask](https://flask.palletsprojects.com/en/2.1.x/), devido ao escopo reduzido do problema e a simplicidade de uso do framwork.

Como banco de dados foi escolhido o PostgreSQL, devido a conhecimento e uso prévio deste banco de dados.

## Execução
A execução dos projetos front-end e back-end acontece de maneira desacoplada, ou seja, ambos projetos não possuem relação direta um com o outro.

Para executar o front-end, no seu terminal favorito entre no diretório `web`
```
cd web/
```
e suba o container com
```
docker-compose up
```

Para executar o back-end, entre no diretório `api`
```
cd api/
```
e também suba o container
```
docker-compose up
```

Se tudo der certo, a aplicação deve estar disponível através da url `http://localhost:8080/`.