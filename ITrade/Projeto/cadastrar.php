<?php	

	  
session_start();
ob_start();
$btnCadUsuario = filter_input(INPUT_POST, 'btnCadUsuario', FILTER_SANITIZE_STRING);
if($btnCadUsuario){
	include_once 'conexao.php';
	$dados_rc = filter_input_array(INPUT_POST, FILTER_DEFAULT);
	
	$erro = false;
	
	$dados_st = array_map('strip_tags', $dados_rc);
	$dados = array_map('trim', $dados_st);
	
	if(in_array('',$dados)){
		$erro = true;
		$_SESSION['msg'] = "Necessário preencher todos os campos";
	}elseif((strlen($dados['senha'])) < 6){
		$erro = true;
		$_SESSION['msg'] = "A senha deve ter no minímo 6 caracteres";
	}elseif(stristr($dados['senha'], "'")) {
		$erro = true;
		$_SESSION['msg'] = "Caracter ( ' ) utilizado na senha é inválido";
	}else{
		$result_usuario = "SELECT id FROM usuarios WHERE usuario='". $dados['usuario'] ."'";
		$resultado_usuario = mysqli_query($conn, $result_usuario);
		if(($resultado_usuario) AND ($resultado_usuario->num_rows != 0)){
			$erro = true;
			$_SESSION['msg'] = "Este usuário já está sendo utilizado";
		}
		
		$result_usuario = "SELECT id FROM usuarios WHERE email='". $dados['email'] ."'";
		$resultado_usuario = mysqli_query($conn, $result_usuario);
		if(($resultado_usuario) AND ($resultado_usuario->num_rows != 0)){
			$erro = true;
			$_SESSION['msg'] = "Este e-mail já está cadastrado";
		}
	}
	
	
	//var_dump($dados);
	if(!$erro){
		//var_dump($dados);
		$dados['senha'] = password_hash($dados['senha'], PASSWORD_DEFAULT);
		
		$result_usuario = "INSERT INTO usuarios (nome, email, usuario, senha) VALUES (
						'" .$dados['nome']. "',
						'" .$dados['email']. "',
						'" .$dados['usuario']. "',
						'" .$dados['senha']. "'
						)";
		$resultado_usario = mysqli_query($conn, $result_usuario);
		if(mysqli_insert_id($conn)){
			$_SESSION['msgcad'] = "Usuário cadastrado com sucesso";
			header("Location: login.php");
		}else{
			$_SESSION['msg'] = "Erro ao cadastrar o usuário";
		}
	}
	
}
?>
<!DOCTYPE html>
<html lang="pt-br">
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
    <br>
    <br/>
    <br/>
		<div class="container">
			<div class="form-signin" style="background: #42dea4;">
				<h2>Cadastrar Usuário</h2>
				<?php
					if(isset($_SESSION['msg'])){
						echo $_SESSION['msg'];
						unset($_SESSION['msg']);
					}
				?>
				<form method="POST" action="">
					<!--<label>Nome</label>-->
					<input type="text" name="nome" placeholder="Digite o nome e o sobrenome" class="form-control"><br>
					
					<!--<label>E-mail</label>-->
					<input type="text" name="email" placeholder="Digite o seu e-mail" class="form-control"><br>
					
					<!--<label>Usuário</label>-->
					<input type="text" name="usuario" placeholder="Digite o usuário" class="form-control"><br>
					
					<!--<label>Senha</label>-->
					<input type="password" name="senha" placeholder="Digite a senha" class="form-control"><br>
					
					<input type="submit" name="btnCadUsuario" value="Cadastrar" class="btn btn-success"><br><br>
					
					<div class="row text-center" style="margin-top: 20px;"> 
						Lembrou? <a href="login.php">Clique aqui</a> para logar
					</div>
				</form>
			</div>
    </div>
          <br><br><br>
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