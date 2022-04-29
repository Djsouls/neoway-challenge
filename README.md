# Desafio Fullstack Neoway

## Descrição do problema e solução
O problema proposto é um sistema simples de gerenciamento de CPF/CNPJ (CRUD), implementando uma interface REST mínima no back-end.

Levando em conta a arquitetura de API REST para o back-end o projeto foi desenvolvimento de maneira a desacoplar o máximo possível as soluções front-end e back-end, de modo que a API desenvolvida seja de uso geral e o front-end possa substituir a API sem grandes complicações.

Idealmente, esses projetos deveriam estar em repositórios separados, mas foram mantidos no mesmo repositório por simplicidade de execução e avaliação.

## Stack escolhida
Para o front-end, o framework escolhido foi `Vue2`, devido a familiaridade com a ferramenta e o suporte estável para a biblioteca de componentes `Vuetify` (a versão de `Vuetify` para `Vue3` ainda está em beta), utilizando do plugin `Vue-Router` para dar suporte a SPA.

No back-end a o (micro-)framework escolhido foi [Flask](https://flask.palletsprojects.com/en/2.1.x/), devido ao escopo reduzido do problema e a simplicidade de uso do framwork. Flask é um framework leve que funciona a partir de plugins, perfeito para soluções simples (como a proposta no problema) que não necessitam de todo o overhead de um framework mais robusto, como Django REST Framework por exemplo.

Como banco de dados foi escolhido o PostgreSQL, devido a conhecimento e uso prévio deste banco de dados.

## Ressalvas sobre a solução
O desenvolvimento aqui foi feito em cima do o ambiente de desenvolvimento do framework Flask, devido principalmente ao fato de que este é um exercício de conhecimento. Para o caso de executar a aplicação em um ambiente de produção algumas alterações deveriam ser feitas, como por exemplo configurar corretamente o [WSGI](https://pt.wikipedia.org/wiki/Web_Server_Gateway_Interface) entre outros detalhes.

## Melhorias futuras

### Sobre as validações
Houve dúvida sobre se a validação deveria ser realizada na parte do frontend, ou backend, não ficou muito claro no enunciado. Assim, implementei em ambas as partes.

A partir da página : `http://localhost:8080/validate` no seu browser, será mostrada uma `View` de validação feita pelo backend, essa página faz uma requisição de validação ao backend e age de acordo com o resultado.

Já na página `http://localhost:8080/`, existe uma validação feita no frontend ao tentar inserir um CPF/CNPJ novo, não permitindo a ação caso o CPF/CNPJ seja inválido

### Sobre testes do frontend
Não foram implementados testes no frontend pela falta de experiência com eles, entretanto é um forte ponto de melhoria futura.

### Sobre a rota `/status`
Para se possuir métricas de maneira robusta, o ideal seria utilizar uma ferramenta de monitoramento, como DataDog ou similiares, entretanto, não foi possível realizar a integração deste tipo de ferramenta a tempo, devido principalmente a falta de experiência prévia.

A implementação da informação `uptime` é feita através de uma requisição feita ao `uptime` do banco de dados, já que ambas instâncias (API e Banco de Dados) são inicializadas em conjunto através do `docker-compose`, o `uptime` do servidor de banco de dados é relativamente fiel ao `uptime` da API.

Em relação ao número de requisições; sem utilizar ferramentas externas não consegui pensar em uma maneira simples de fazer, foi cogitado implementar um sistema próprio de ""monitoramento de rotas"" (utilizando contadores globais), mas pareceu muito fora do escopo.

Resumindo, a rota `/status` retorna apenas o `uptime` do servidor de banco de dados. Uma boa melhoria nesse ponto seria ou a integração de alguma ferramenta de monitoramento, ou implementação dessas métricas de maneira fiel.

### Documentação
A documentação atual foi feita manualmente, utilizando linguagem de Markdown. Uma boa melhoria seria uso de um padrão conhecido, como por exemplo [OpenAPI](https://www.openapis.org/), que fornece outras vantagens além de apenas a documentação em si, como geração de código automático e validação de dados.

## Documentação
A documentação API se encontra dentro do diretório `/api` em formato de markdown, e existem alguns fluxos mostrados de uso da interface web dentro do diretório `/web`

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

## Testes
Os testes são rodados toda vez que a instância irá subir, entretanto, para executar os testes apenas, a partir do diretório raiz, execute: `docker build -t tests --target tests .`
