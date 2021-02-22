<?php 
$a = $_POST["v1"];
$b = $_POST["v2"];
$c = $_POST["e1"];

$comissao = ($b * 15)/100;
$salario = $a + $comissao;

echo "<p><h1>Salário</h1></p>";

echo "<p>Empregado: $c </p>";

echo "<p>Salário Fixo: $a </p>";

echo "<p>Total de Vendas: $b </p>";

echo "<p>Comissão(15%): $comissao </p>";

echo "<p>Salário Final: $salario </p>";


