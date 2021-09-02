## Установка / Installation

    git clone https://github.com/SaraFarron/commentsapi.git
    cd commentsapi
    docker-compose build

## Запуск / Run

    docker-compose up

## Описание / Description

API имеет 2 адреса: http://localhost:8000/comments/ и http://localhost:8000/posts/ для работы со статьями
и комментариями соответственно.


The API has 2 addresses: http://localhost:8000/comments/ and http://localhost:8000/posts/ for working with articles
and comments, respectively.

* /posts
    
    * get запрос выдает все статьи в БД, каждая "статья" имеет только id и title
    * post запросом можно создать статью, для этого в body form-data необходимо указать title
    
    * get request returns all articles in the database, each "article" has only id and title
    * post request, you can create an article, for this you need to specify title in the body form-data

* /comments

    * get запрос выдает все комментарии под указанной статьей или ответы к комментарию, необходимо указать id статьи (post) или комментария (comment) в теле запроса
    * post запрос позволяет создать новый комментарий, существует 2 сценария использования:
        * в теле запроса указан post (id статьи) - создается комментарий к статье
        * в теле запроса указан comment (id комментария) - создается ответ на указанный комментарий, на 1 комментарий можно создать несколько ответов
    
      В обоих случаях в post необходимо указывать text в теле с текстом комментария
    
    * get request returns all comments under the specified article or responses to a comment, you must specify the id of the article (post) or comment (comment) in the request body
    * post request allows you to create a new comment, there are 2 use cases:
        * post (article id) is specified in the request body - a comment to the article is created
        * comment (comment id) is specified in the request body - a response to the specified comment is created, multiple responses can be created for 1 comment
    
      In both cases, the post must contain text in the body with the text of the comment.

Пример запроса для создания статьи: / An example of a request to create an article: 

curl

    curl --location --request POST 'http://localhost:8000/posts' \
    --form 'title="Test post 2"'

python requests

    import requests
    
    url = "http://localhost:8000/posts"
    payload={'title': 'Test post 2'}
    response = requests.request("POST", url, data=payload)
    print(response.text)

Пример запроса для получения ответов на комментарий / Example of a request to get responses to a comment 

    curl --location --request GET 'http://localhost:8000/comments' \
    --form 'text="Comment 8"' \
    --form 'comment="22"'

## Задание / Task

##### Реализация была отклонена / Implementation was rejected

Основной проблемой было наличие большого числа try... except / Main issue was having too much try... except

Реализовать REST API для системы комментариев блога / Implement REST API for blog's comment system

Функциональные требования:
У системы должны быть методы API, которые обеспечивают
- Добавление статьи (Можно чисто номинально, как сущность, к которой крепятся комментарии).
- Добавление комментария к статье.
- Добавление комментария в ответ на другой комментарий (возможна любая вложенность).
- Получение всех комментариев к статье вплоть до 3 уровня вложенности.
- Получение всех вложенных комментариев для комментария 3 уровня.
- По ответу API комментариев можно воссоздать древовидную структуру.

Functional requirements:
The system must have API methods that provide
- Adding an article (It can be purely nominally, as an entity to which comments are attached).
- Adding a comment to the article.
- Adding a comment in response to another comment (any nesting is possible).
- Getting all comments to an article up to 3 nesting levels.
- Retrieving all nested comments for a level 3 comment.
- Based on the response from the Comments API, you can recreate the tree structure. 

Нефункциональные требования:
- Использование Django ORM.
- Следование принципам REST.
- Число запросов к базе данных не должно напрямую зависеть от количества комментариев, уровня вложенности.
- Решение в виде репозитория на Github, Gitlab или Bitbucket.
- readme, в котором указано, как собирать и запускать проект. Зависимости указать в requirements.txt либо использовать poetry/pipenv.
- Использование свежих версий python и Django.

Non-functional requirements:
- Using Django ORM.
- Following the principles of REST.
- The number of queries to the database should not directly depend on the number of comments, the level of nesting.
- Solution in the form of a repository on Github, Gitlab or Bitbucket.
- readme, which describes how to build and run the project. Specify dependencies in requirements.txt or use poetry / pipenv.
- Using fresh versions of python and Django. 

Будет плюсом:
- Использование PostgreSQL.
- docker-compose для запуска api и базы данных.
- Swagger либо иная документация к апи.

Will be a plus:
- Using PostgreSQL.
- docker-compose to run api and database.
- Swagger or other api documentation. 
