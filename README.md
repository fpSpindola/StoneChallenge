# StoneChallenge

### Como executar:

Este projeto roda em um ambiente Python 3.7

### Configuração do ambiente

Após instalar um virtualenv, todas as dependencias contidas em requirements.txt (raiz do projeto) devem ser instaladas.
Uma vez que todas estiverem instaladas será necessário conferir o arquivo ".env" que está na raiz do projeto.  
Neste arquivo estão contidas as configurações de banco de dados e ElasticSearch (caso houvesse, para gravação de logs em batch)

### O Banco de Dados

O banco está hospedado no serviço AWS RDS. Decidi optar por esta infraestrutura para facilitar a execução do projeto em um ambiente local, ou seja, nenhuma configuração será necessária para conectar-se ao banco de dados da aplicação, este já está online e disponível na AWS

## Documentação das APIs

@funcionarios.route("/search", methods=["GET"])  
/v1/funcionarios/search

Retorna todos os funcionários do banco de dados


@funcionarios.route("/search/<int:func_id>", methods=["GET"])  
/v1/funcionarios/search/(func_id) 
 
Retorna um funcionário específico passado por parametro [func_id]

@funcionarios.route("/add", methods=["POST"])
/v1/funcionarios/search/(func_id)

Parametros do body da requisição:

**@param nome**    
**@param idade**  
**@param cargo**

Adiciona um novo funcionário ao banco de dados


@funcionarios.route("/<int:func_id>", methods=["PUT"])
/v1/funcionarios/(func_id)

Parametros do body da requisição:

**@param nome**  
**@param idade**  
**@param cargo**

Utilizando o método PUT, atualiza os dados de um funcionário já existente no banco de dados


@funcionarios.route("/<int:func_id>", methods=["DELETE"])
/v1/funcionarios/(func_id)

Utilizando o método DELETE, remove um funcionário do banco de dados baseado no seu id