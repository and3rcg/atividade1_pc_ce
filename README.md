# Atividade prática de Python/Django/DRF - Polícia Civil do Ceará

Repositório da atividade prática referente ao processo seletivo de Pessoa Desenvolvedora Python júnior.

## Instruções de inicialização

-   Clonar esse repositório para a máquina local (`git clone`);
-   Na pasta local do repositório, criar um ambiente virtual (`python -m venv venv`) e ativá-lo (`source venv/bin/activate` em Linux);
-   Instalar as dependências do arquivo requirements.txt (`pip install -r requirements.txt`);
-   Executar as migrações do banco de dados (`python manage.py migrate`);
-   Executar o comando especial para o preenchimento inicial dos dados (`python manage.py preencherdb`);
-   Iniciar o servidor (`python manage.py runserver`).

## Endpoints da API

Todos os modelos do projeto foram desenvolvidos como Viewsets, logo, eles possuem suporte a ações básicas de CRUD, conforme [a documentação oficial](https://www.django-rest-framework.org/api-guide/viewsets/#viewset-actions). Com os Viewsets, é possível executar as seguintes ações:

-   `GET`: Retorna um JSON com todos os objetos registrados no banco dados, ou um objeto específico, se sua chave primária for passada na URL;
-   `POST`: Cria um novo objeto com os dados passados no request;
-   `PATCH`: Atualiza um ou vários campos de um objeto específico, passados no request;
-   `DELETE`: Apaga uma instância de um objeto específico.

Dessa forma, essa API conta com os seguintes endpoints, nos quais é possível executar cada ação listada acima:

-   `/api/armas/`
-   `/api/calibres/`
-   `/api/municoes/`
-   `/api/objetos/`
-   `/api/tipos_objetos/`
