<?php 
$a = $_POST["v1"];
$b = $_POST["v2"];
$c = $_POST["v3"];
$d = $_POST["v4"];
$f = $_POST["e1"];

$media = ($a + $b + $c + $d)/4;

echo "<p><h1>Notas</p></h1>";

echo "<p>Aluno: $f</p>";

echo "<p>Média Final: $media</p>";


