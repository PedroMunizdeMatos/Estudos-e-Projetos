<?php 

$a = $_POST["v1"];
$b = $_POST["v2"];
$s = $a + ($a*45/100);
$s2 = $s + ($s*28/100);

echo "<p><h1>Valor do Carro</p></h1>";

echo "<p>veículo: $b</p>";

echo "<p>Valor de Fábrica: $a</p>";

echo "<p>Valor com Impostos: $s</p>";

echo "<p>Valor Final: $s2</p>";
?>