# Documentação

URL Base: `localhost:5000/api/v1`

## Cadastro de CPF/CNPJ
As rotas de cadastro de CPF/CNPJ possuem verificações antes de realizar a adição, podendo retornar com sucesso ou não.


### CPF

Route: `/cpf`

Método: `POST`

Descrição: Cadastra um CPF

Formato de requisição:

```json
{
  "cpf": "11144723019"
}
```

Formato de resposta com sucesso:

Código de status: `200`

```json
{
  "blocked_at": null,
  "cpf": "11144723019",
  "created_at": "Fri, 29 Apr 2022 20:09:36 GMT",
  "id": 3
}
```

Formato de resposta com erro:

Código de status: `400`
```json
{
  "error": "invalid cpf"
}
```

### CNPJ

Route: `/cnpj`

Método: `POST`

Descrição: Cadastra um CNPJ

Formato de requisição:


```json
{
  "cnpj": "49298927000149"
}
```

Formato de resposta com sucesso:

Código de status: `200`

```json
{
  "blocked_at": null,
  "cnpj": "49298927000149",
  "created_at": "Fri, 29 Apr 2022 20:09:36 GMT",
  "id": 3
}
```

Formato de resposta com erro:

Código de status: `400`
```json
{
  "error": "invalid cnpj"
}
```

## Busca de CPF/CNPJ

### CPF

Route: `/cpfs`

Método: `GET`

Descrição: Busca todos os CPFs cadastrados

Formato de requisição:

`http://localhost:5000/api/v1/cpfs`

Formato de resposta com sucesso:

Código de status: `200`

```json
{
  "count": 3,
  "results": [
      {
        "blocked_at": null,
        "cpf": "11421433923",
        "created_at": "Fri, 29 Apr 2022 15:56:19 GMT",
        "id": 1
      },
      {
        "blocked_at": null,
        "cpf": "11421433923",
        "created_at": "Fri, 29 Apr 2022 16:04:36 GMT",
        "id": 2
      },
      {
        "blocked_at": null,
        "cpf": "11421433923",
        "created_at": "Fri, 29 Apr 2022 20:09:36 GMT",
        "id": 3
      }
  ],
  "success": true
}
```

Formato de resposta com vazia:

Código de status: `200`
```json
{
  "count": 0,
  "results": [],
  "success": true
}
```


Route: `/cpf/<id>`

Método: `GET`

Descrição: Busca o CPF com o ID `id`

Formato de requisição:

`http://localhost:5000/api/v1/cpf/3`

Formato de resposta com sucesso:

Código de status: `200`

```json
{
  "blocked_at": null,
  "cpf": "11421433923",
  "created_at": "Fri, 29 Apr 2022 20:09:36 GMT",
  "id": 3
}
```

Formato de resposta com vazia:

Código de status: `200`
```json
[]
```

### CNPJ

Route: `/cnpjs`

Método: `GET`

Descrição: Busca todos os CNPJs cadastrados

Formato de requisição:

`http://localhost:5000/api/v1/cnpjs`

Formato de resposta com sucesso:

Código de status: `200`

```json
{
  "count": 1,
  "results": [
    {
      "blocked_at": null,
      "cnpj": "49298927000149",
      "created_at": "Fri, 29 Apr 2022 20:09:36 GMT",
      "id": 1
    }
  ],
  "success": true
}
```

Formato de resposta com vazia:

Código de status: `200`
```json
{
  "count": 0,
  "results": [],
  "success": true
}
```

Route: `/cnpj/<id>`

Método: `GET`

Descrição: Busca o CNPJ com o ID `id`

Formato de requisição:


`http://localhost:5000/api/v1/cnpj/1`

Formato de resposta com sucesso:

Código de status: `200`

```json
{
  "blocked_at": null,
  "cnpj": "49298927000149",
  "created_at": "Fri, 29 Apr 2022 20:09:36 GMT",
  "id": 1
}
```

Formato de resposta com vazia:

Código de status: `200`
```json
[]
```

## Deletar CPF/CNPJ
Em casos de enviar um id que não existe, a resposta será vazia

### CPF

Route: `/cpf/<id>`

Método: `DELETE`

Descrição: Deleta o CPF com o ID `id`

Formato de requisição:

`http://localhost:5000/api/v1/cpf/3`

Formato de resposta com sucesso:

Código de status: `200`

```json
{
  "blocked_at": null,
  "cpf": "11421433923",
  "created_at": "Fri, 29 Apr 2022 20:09:36 GMT",
  "id": 3
}
```

Formato de resposta com vazia:

Código de status: `400`
```json
[]
```

### CNPJ

Route: `/cnpj/<id>`

Método: `DELETE`

Descrição: Deleta o CNPJ com o ID `id`

Formato de requisição:

`http://localhost:5000/api/v1/cnpj/1`

Formato de resposta com sucesso:

Código de status: `200`

```json
{
  "blocked_at": null,
  "cnpj": "49298927000149",
  "created_at": "Fri, 29 Apr 2022 20:09:36 GMT",
  "id": 1
}
```

Formato de resposta com vazia:

Código de status: `400`
```json
[]
```

## Bloquear/Desbloquear CPF/CNPJ
Bloquear um CPF/CNPJ implica em não permitir que CPFs/CNPJs iguais a esse sejam validados.

`operation`: `[block, unblock]`

A URL se repete para ambas operações.
### CPF

Route: `/cpf/<id>/<operation>`

Método: `PUT`

Descrição: Bloqueia/Desbloqueia o CPF com o ID `id`

Formato de requisição:

`http://localhost:5000/api/v1/cpf/3/block`

Formato de resposta com sucesso:

Código de status: `200`

```json
{
    "blocked_at": "Fri, 29 Apr 2022 20:52:06 GMT",
    "cpf": "11421433923",
    "created_at": "Fri, 29 Apr 2022 15:56:19 GMT",
    "id": 1
}
```

Formato de resposta com vazia:

Código de status: `400`
```json
[]
```

### CNPJ

Route: `/cnpj/<id>/<operation>`

Método: `PUT`

Descrição: Bloqueia/Desbloqueia o CNPJ com o ID `id`

Formato de requisição:

`http://localhost:5000/api/v1/cnpj/2/block`

Formato de resposta com sucesso:

Código de status: `200`

```json
{
    "blocked_at": "Fri, 29 Apr 2022 21:00:34 GMT",
    "cnpj": "49298927000149",
    "created_at": "Fri, 29 Apr 2022 20:59:46 GMT",
    "id": 2
}
```

Formato de resposta com vazia:

Código de status: `400`
```json
[]
```

## Validar CPF/CNPJ
Caso o CPF/CNPJ esteja bloqueado, a validação retornará como falsa

### CPF

Route: `/cpf/validate?cpf=<cpf_text>`

Método: `GET`

Descrição: Valida o CPF `cpf_text`

Formato de requisição:

`http://localhost:5000/api/v1/cpf/validate?cpf=11421433923`

Formato de resposta com sucesso e válido:

Código de status: `200`

```json
{
    "valid": true
}
```

Formato de resposta com sucesso e inválido:

Código de status: `200`
```json
{
    "valid": false
}
```

### CNPJ

Route: `/cnpj/validate?cnpj=<cnpj_text>`

Método: `GET`

Descrição: Valida o CNPJ `cnpj_text`

Formato de requisição:

`http://localhost:5000/api/v1/cnpj/validate?cnpj=80230462000134`

Formato de resposta com sucesso e válido:

Código de status: `200`

```json
{
    "valid": true
}
```

Formato de resposta com sucesso e inválido:

Código de status: `200`
```json
{
    "valid": false
}
```