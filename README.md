# prototipo_backend
## Pacientes
### Listar pacientes
URL:/pacientes
Método: GET
Descrição:Retorna a lista de todos os pacientes cadastrados.  

### Criar paciente
URL: /pacientes
Método: POST
Descrição: Cria um novo paciente.
Parâmetros (body JSON):
{
  "id": 1,
  "nome": "João Silva",
  "cpf": "123.456.789-00"
}

## Profissionais
### Listar profissionais:
/profissionais - GET
### Criar profissionais:
/profissionais - POST

## Consultas
### Listar consultas
/Consultas - GET
### Criar consultas
/Consultas - POST

## Exames
### Listar - GET
### Criar - POST

## Prescrições
### Listar - GET
### Criar - POST

## Autenticação
URL: /login → POST
Descrição: Verifica login e senha do usuário.
Body JSON:
{
  "login": "admin",
  "senha": "1234"
}
Exemplo de resposta:
{
  "message": "Login realizado com sucesso!",
  "id": 1
}
Códigos de status: 200 → login correto, 401 → login ou senha incorretos
