<?php
session_start();
?>
<!DOCTYPE html>
<html lang="pt-br">
	<head>
	<head>
    <!-- Meta tags Obrigatórias -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!--CSS-->
    <Link rel="stylesheet" href="css/estilo.css">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css"
      integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">

    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.3.1/css/all.css"
      integrity="sha384-mzrmE5qonljUremFsqc01SB46JvROS7bZs3IO2EmfFsd15uHvIt+Y8vEf7N7fWAU" crossorigin="anonymous">

    <title>iTrade - Compra, venda e troca de articos online</title>
    <link rel="icon" href="imagens/icone.png">
		<meta charset="utf-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<link href="css/bootstrap.css" rel="stylesheet">
		<link href="css/signin.css" rel="stylesheet">
	</head>
	<body>
	<header>
      <!--Inicio cabeçalho-->
      <nav class="navbar navbar-expand-md navbar-light  bg-light">
        <div class="container">
          <a href="index.html" class="navbar-brand">
            <!--LOGO-->
            <img src="imagens/trade2.png" width="150" style="margin-top: -30px;">
          </a>

          <button class="navbar-toggler" data-toggle="collapse" data-target="#nav-principal">
            <i class="fas fa-bars text-black"></i>
          </button>

          <div class="collapse navbar-collapse" id="nav-principal">
            <!--Menu-->
            <ul class="navbar-nav ml-auto">
              <li class="nav-item">
                <a href="index.html" class="nav-link">Início</a>
              </li>

              <div class="dropdown-divider"> |</div>


              <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="minhaconta.html" id="navbarDropdown" role="button"
                  data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                  Minha conta
                </a>
                <div class="dropdown-menu" aria-labelledby="navbarDropdown">
                  <a class="dropdown-item" href="historicoativ.html">Histórico de Atividades</a>
                  <a class="dropdown-item" href="meusanuncios.html">Meus Anúncios</a>
                  <div class="dropdown-divider"></div>
                  <a class="dropdown-item" href="criaranuncio.html">Cria novo Anúncio</a>

				</div>
              </li>
              <li class="nav-item">
                <a href="login.php" class="nav-link">Entre</a>
              </li>

              <li class="nav-item">
                <a href="cadastrar.php" class="nav-link">Cadastre-se</a>
              </li>
              </li>
              <a href="contato.html" class="nav-link" style="margin-top:10px;">Fale Conosco</a>
			  </li>
			  </li>
              <a href="quem.html" class="nav-link" style="margin-top:10px;">Quem somos</a>
              </li>
            </ul>
			
          </div>
		  <!--Fim Menu-->
		</div>

      </nav>

    </header>
	<br/>
	<br/>
	<br/>
		<div class="container">
			<div class="form-signin" style="background: #42dea4;">
				<h2 class="text-center">Login</h2>
				<form method="POST" action="valida.php">
					<!--<label>Usuário</label>-->
					<input type="text" name="usuario" placeholder="Digite o seu usuário" class="form-control"><br>
					
					<!--<label>Senha</label>-->
					<input type="password" name="senha" placeholder="Digite a sua senha" class="form-control"><br>
					
					<input type="submit" name="btnLogin" value="Acessar" class="btn btn-success btn-block">
					
					<div class="row text-center" style="margin-top: 20px;"> 
						<h4>Você ainda não possui uma conta?</h4>
						<a href="cadastrar.php">Crie grátis</a>
					</div>
					
					
				</form>
			</div>
		</div>	
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
		<script src="js/bootstrap.min.js"></script>
		<footer>
      <div class="container">
        <div class="row">
          <div class="col-md-4">
            <a href="index.html">
              <img src="imagens/trade2.png" width="120" style="margin-left: 50px;">
            </a>

          </div>
          <div class="col-md-4">
            <div class="footer-copyright text-center py-3">© 2020 Copyright: ITrade LTDA
            </div>
          </div>

          <div class="col-md-4">
            <form class="form-inline my-2 my-lg-0">
              <input class="form-control mr-sm-2" type="search" placeholder="O que está procurando?" aria-label="Search">
              <button class="btn btn-primary my-2 my-sm-0" type="submit">Pesquisar</button>
            </form>
          </div>
        </div>
      </div>
    </footer>

<!-- JavaScript (Opcional) -->
<!-- jQuery primeiro, depois Popper.js, depois Bootstrap JS -->
<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
  integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo"
  crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js"
  integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49"
  crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js"
  integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy"
  crossorigin="anonymous"></script>
	</body>

</html>