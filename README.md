<div align="center">
<img src="https://i.imgur.com/ir3vFwk.png" width=100px>
<br>
<h1>TabNews.py</h1>

![Python](https://img.shields.io/badge/python-v3.7+-blue.svg) ![OS](https://img.shields.io/badge/OS-linux%20%7C%20windows-blue??style=flat&logo=Linux&logoColor=b0c0c0&labelColor=363D44)
<br>
<i>Uma biblioteca massinha para um lugar massinha :)</i>
<br>
<p>
<a href="#about">Sobre</a> •
<a href="#install">Instalação</a> •
<a href="#examples">Exemplos</a> •
<a href="#contribute">Contribuir</a> •
<a href="#license">Licença</a>
</p>
</div>

<div id="about"><h2>💻 Sobre o projeto</h2></div>

Essa é uma biblioteca Python para consumir a API do [Tabnews](https://www.tabnews.com.br). Ela tem o proposito de facilitar e optimizar a integração de aplicações Python com o site do TabNews;

<div id="install"><h2>📩 Como baixar a biblioteca?</h2></div>

Para instalar localmente a biblioteca em seu computador, você pode usar o [Pypi](https://pypi.org/), com o comando:

```bash
pip install tabnews
```
Ou instalar via git:

```bash
pip install git+https://github.com/Gustavosta/TabNews.py
```

<div id="examples"><h2>🔨 Exemplos de uso</h2></div>

Aqui vamos ver alguns exemplos de uso de como você pode usar a biblioteca para facilitar a comunicação com a API do Tabnews:

### ➡️ Exemplo 1:

Esse é um caso de uso bem simples, para mostrar como a autenticação funciona:

<div align="flex">
<pre>
<br><p align="center"><a href="#"><img src="https://i.imgur.com/F7a7Drk.png" width=40px align="left"></a>Welcome<a href="#"><img src="https://i.imgur.com/RPheDpA.png" width=40px align="right"></a></p>

```python
from tabnews import Client

EMAIL = 'user@example.com'
PASSWORD = 'SenhaExtremamenteSegura'

client = Client(EMAIL, PASSWORD)
user = client.get_user()
print(f'Logged in as {user.username}')
```
</pre>
</div>

### ➡️ Exemplo 2:

Esse é um exemplo de como fazer uma publicação via código.

<div align="flex">
<pre>
<br><p align="center"><a href="#"><img src="https://i.imgur.com/F7a7Drk.png" width=40px align="left"></a>Welcome<a href="#"><img src="https://i.imgur.com/RPheDpA.png" width=40px align="right"></a></p>

```python
from tabnews import Client

EMAIL = 'user@example.com'
PASSWORD = 'SenhaExtremamenteSegura'
client = Client(EMAIL, PASSWORD, use_preview_tabnews_host=True)

post = client.publish_post(
    title='isso é um teste',
    content='isso foi publicado com a biblioteca do Tabnews para Python :)',
    reference='https://github.com/Gustavosta/TabNews.py'
)

print(post)
```
</pre>
</div>

Repare que usei `use_preview_tabnews_host=True`. Esse parâmetro serve para postar coisas diretamente no ambiente de homologação usando a URL do ambiente extraída via API no [repositório oficial do Tabnews](https://github.com/filipedeschamps/tabnews.com.bR).


### ➡️ Exemplo 3:

Esse exemplo mostra como dar upvote em um post, passando como parâmetro o `username` do usuário e o `slug` ou `parent_id` de um conteúdo:

<div align="flex">
<pre>
<br><p align="center"><a href="#"><img src="https://i.imgur.com/F7a7Drk.png" width=40px align="left"></a>Welcome<a href="#"><img src="https://i.imgur.com/RPheDpA.png" width=40px align="right"></a></p>

```python
from tabnews import Client

TOKEN = 'TokenOuCookieExtraidoAPartirDaAutenticacao'
client = Client(token=TOKEN, save_session=True)
upvote = client.upvote(
    'filipedeschamps', 
    'tentando-construir-um-pedaco-de-internet-mais-massa'
)

print(upvote)
```
</pre>
</div>

Note que dessa vez, eu usei o parâmetro `token` no `client` para autenticação, o que também é possível, mas não tão recomendado, já que tokens podem expirar e não durarem muito.

### ➡️ Exemplo 4:

Esse exemplo mostra como obter os dados de uma postagem e como comentar em uma postagem:

<div align="flex">
<pre>
<br><p align="center"><a href="#"><img src="https://i.imgur.com/F7a7Drk.png" width=40px align="left"></a>Welcome<a href="#"><img src="https://i.imgur.com/RPheDpA.png" width=40px align="right"></a></p>

```python
from tabnews import Client

EMAIL = 'user@example.com'
PASSWORD = 'SenhaExtremamenteSegura'
client = Client(EMAIL, PASSWORD, save_session=True, use_preview_tabnews_host=True)

post = client.get_post(
    'sowlfie', 
    'isso-e-um-teste'
)
comment = client.publish_comment(
    parent_id=post.id,
    content='Teste de comentário'
)

print(comment)
```
</pre>
</div>

Repare que usei o parâmetro `save_session`, que a biblioteca usa para salvar as configurações de autenticação para a sessão e diminuir o tempo de autenticação (que por padrão é `True`). Você também pode usar: `config_path` para escolher o caminho de salvamento ou carregamento das configurações em formato `json`.

### ➡️ Exemplo 5:

Esse exemplo mostra como editar uma postagem ou comentário:

<div align="flex">
<pre>
<br><p align="center"><a href="#"><img src="https://i.imgur.com/F7a7Drk.png" width=40px align="left"></a>Welcome<a href="#"><img src="https://i.imgur.com/RPheDpA.png" width=40px align="right"></a></p>


```python
from tabnews import Client

EMAIL = 'user@example.com'
PASSWORD = 'SenhaExtremamenteSegura'
client = Client(EMAIL, PASSWORD, use_preview_tabnews_host=True)

post = client.edit_post(
    username='sowlfie', 
    slug='isso-e-um-teste',
    title='Isso é um teste (título editado)',
    content='isso foi publicado e editado com a biblioteca do Tabnews para Python :)', 
    reference='https://github.com/Gustavosta/TabNews.py'
)
comment = client.edit_comment(
    comment_slug='f0777d39-055a-4e44-b3cf-dabf0e2176bb',
    parent_id=post.id,
    content='Esse é um comentário publicado e editado com a mesma lib'
)
```
</pre>
</div>

### ➡️ Exemplo 6:

Esse exemplo mostra como deletar uma postagem ou comentário:

<div align="flex">
<pre>
<br><p align="center"><a href="#"><img src="https://i.imgur.com/F7a7Drk.png" width=40px align="left"></a>Welcome<a href="#"><img src="https://i.imgur.com/RPheDpA.png" width=40px align="right"></a></p>


```python
from tabnews import Client

EMAIL = 'user@example.com'
PASSWORD = 'SenhaExtremamenteSegura'
client = Client(EMAIL, PASSWORD, use_preview_tabnews_host=True)

post = client.delete_post(
    slug='isso-e-um-teste'
)
comment = client.delete_comment(
    comment_slug='f0777d39-055a-4e44-b3cf-dabf0e2176bb'
)
```
</pre>
</div>

<div id="contribute"><h2>💛 Quer contribuir</h2></div>

Caso queira contribuir, você pode criar uma issue documentando as alterações sugeridas antes de criar um pull request, linkar o PR à issue, preferencialmente utilizar nomes de branch com o seguinte padrao:

<numero da issue>/<tipo de alteração>-<descrição da issue>

EX: `001/Hotfix-correcao-tabela-principal`

Utilizar os tipos [Feature|Hotfix|Update]

Qualquer duvida ou sugestão, sinta-se a vontade para abrir uma nova issue, assim temos espaço para discutir as alterações/duvidas.

<div id="license"><h2>📜 Licença</h2></div>

[MIT License](/LICENSE)

