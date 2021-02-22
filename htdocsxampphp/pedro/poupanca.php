<?php 
$a = $_POST["v1"];
$b = $_POST["v2"];

$s = $a*($b*0.7/100);

echo "<p><h1>Rendimentos</p></h1>";

echo "<p>Seus rendimentos durante $b meses Totalizaram $s </p>";

?>