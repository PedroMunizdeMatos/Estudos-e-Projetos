<?php 
$a = $_POST["v1"];
$b = $_POST["v2"];
$divisao = $a / $b;
echo "<p><h1>Consumo do Automóvel</h1></p>";
echo "<p>Consumo em KM/L: " . $divisao . "</p>";
echo "<p><a href='consumo.html'>Voltar</a></p>";
?>