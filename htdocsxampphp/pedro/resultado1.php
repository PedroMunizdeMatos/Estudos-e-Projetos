<html>
 <head></head>
 <body>
 
<h1> Resultado</h1>
<br>
<?php


$a = $_GET["valor1"];
$b = $_GET["valor2"];
$soma = $a+$b;
$subtracao =$a-$b;
$multiplicacao = $a*$b;
$op= $_GET["op"];


if($op=="Soma"){
echo " o valor da soma:",$soma;}

if($op=="subtracao"){
echo "o valor da subtracao:",$subtracao;}

if($op=="multiplicaçao"){
echo "o valor da multiplicacao:",$multiplicacao;
}

?>
<br>

<A HREF="index1.html" >Voltar</a>



 <body>
 </html>