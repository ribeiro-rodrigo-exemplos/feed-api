# feed-api

O projeto foi desenvolvido utilizando o Python 3.
A API possui os seguintes recursos 

<b>GET /v1/feeds</b> - obtém o feed conforme solicitado no desafio <br/>
<b>POST /v1/users</b> - cria um novo usuario, o json deve ter o seguinte formato {"username":"nome","password":"senha"}<br/>
<b>POST /auth/token</b> - cria um token jwt que deve ser utilizado no header Authorization nas requisições realizadas ao /v1/feeds. O nome
de usuário e a senha devem ser informados no corpo da requisição no seguinte formato {"username":"nome","password":"senha"}.
