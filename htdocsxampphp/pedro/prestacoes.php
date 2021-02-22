<?php 
$a = $_POST["v1"]; //dia
$b = $_POST["v2"]; //mês
$c = $_POST["v3"]; //ano
$d = $_POST["v4"]; //valor
$e = $_POST["v5"]; //parcelamento

if ($b>6) {
    $soma1 = $b+1;
    $soma2 = $b+2;
    $soma3 = $b+3;
    $soma4 = $b+4;
    $soma5 = $b+5;
    $soma6 = $b-6;
} elseif ($b<=6) {
    $soma1 = $b+1;
    $soma2 = $b+2;
    $soma3 = $b+3;
    $soma4 = $b+4;
    $soma5 = $b+5;
    $soma6 = $b+6;
}

if ($soma6 = $b-6) {
    $j = $c + 1;
} else {
    $j = $c;
}

//divisão para número de parcelas
$divisão1 = $d/2; 
$divisão2 = $d/3;
$divisão3 = $d/4;
$divisão4 = $d/5;
$divisão5 = $d/6;

echo "<p><h1>Parcelamento</p></h1>";
echo "<p>Valor total da compra:R$$d</p>";
echo "<p>Data da Compra:$a/$b/$c</p>";
echo "<p>Número de Parcelas: $e</p><br/>";

if($e == 1){
    echo "<p>Pagamento à vista</p>";
    echo "Valor da parcela: $d";
} elseif($e == 2){ 
    echo "<p><h3>Primeira Parcela:</h3>R$$divisão1";
    echo "<p>Data:$a/$soma1/$c";
    echo "<p><h3>Segunda Parcela:</h3>R$$divisão1";
    echo "<p>Data:$a/$soma2/$c";
} elseif($e == 3){ 
    echo "<p><h3>Primeira Parcela:</h3>R$$divisão2";
    echo "<p>Data:$a/$soma1/$c";
    echo "<p><h3>Segunda Parcela:</h3>R$$divisão2";
    echo "<p>Data:$a/$soma2/$c";
    echo "<p><h3>Terceira Parcela:</h3>R$$divisão2";
    echo "<p>Data:$a/$soma3/$c";
} elseif ($e == 4){ 
    echo "<p><h3>Primeira Parcela:</h3>R$$divisão3";
    echo "<p>Data:$a/$soma1/$c";
    echo "<p><h3>Segunda Parcela:</h3>R$$divisão3";
    echo "<p>Data:$a/$soma2/$c";
    echo "<p><h3>Terceira Parcela:</h3>R$$divisão3";
    echo "<p>Data:$a/$soma3/$c";
    echo "<p><h3>Quarta Parcela:</h3>R$$divisão3";
    echo "<p>Data:$a/$soma4/$c";
} elseif ($e == 5){ 
    echo "<p><h3>Primeira Parcela:</h3>R$$divisão4";
    echo "<p>Data:$a/$soma1/$c";
    echo "<p><h3>Segunda Parcela:</h3>R$$divisão4";
    echo "<p>Data:$a/$soma2/$c";
    echo "<p><h3>Terceira Parcela:</h3>R$$divisão4";
    echo "<p>Data:$a/$soma3/$c";
    echo "<p><h3>Quarta Parcela:</h3>R$$divisão4";
    echo "<p>Data:$a/$soma4/$c";
    echo "<p><h3>Quinta Parcela:</h3>R$$divisão4";
    echo "<p>Data:$a/$soma5/$c";
} elseif ($e == 6){ 
    echo "<p><h3>Primeira Parcela:</h3>R$$divisão5";
    echo "<p>Data:$a/$soma1/$c";
    echo "<p><h3>Segunda Parcela:</h3>R$$divisão5";
    echo "<p>Data:$a/$soma2/$c";
    echo "<p><h3>Terceira Parcela:</h3>R$$divisão5";
    echo "<p>Data:$a/$soma3/$c";
    echo "<p><h3>Quarta Parcela:</h3>R$$divisão5";
    echo "<p>Data:$a/$soma4/$c";
    echo "<p><h3>Quinta Parcela:</h3>R$$divisão5";
    echo "<p>Data:$a/$soma5/$c";
    echo "<p><h3>Sexta Parcela:</h3>R$$divisão5";
    echo "<p>Data:$a/$soma6/$j";
}



?>