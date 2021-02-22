<?php 
$a = $_POST["v1"];
$b = $_POST["v2"];

$divisao = $a / $b;
$soma = $a + $b;   
$subtracao = $a - $b; 
$multiplicacao = $a * $b;

echo "<p><h1>Calculadora Resultado</p></h1>";
echo "<p>Valor 1:$a</p>";
echo "<p>Valor 2:$b</p>";
echo "<p>Soma: " . $soma . "</p>";
echo "<p>Subtração: " . $subtracao . "</p>";
echo "<p>Muliplicação: " . $multiplicacao . "</p>";
echo "<p>Divisão: " . $divisao . "</p>";
echo "<p><a href='index.html'>Voltar</a></p>";
?>