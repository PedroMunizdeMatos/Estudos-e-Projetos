<?php 
$a = $_POST["v1"]; //nome
$b = $_POST["v2"]; //p1
$c = $_POST["v3"]; //p2
$d = $_POST["v4"]; //p3
$e = $_POST["v5"]; //p4

$media = ($b + $c + $d + $e)/4;

if($media <5){
    echo "<p>Aluno Reprovado</p>";
    echo "Nome:$a </br>";
    echo "Notas:$b, $c, $d, $e </br>";
    echo "Média: $media";
} elseif($media >=7){ 
    echo "<p>Aluno Aprovado</p>";
    echo "Nome:$a </br>";
    echo "Notas: $b, $c, $d e $e </br>";
    echo "Média: $media";
} else{
    echo "<p>Aluno em Recuperação</p>";
    echo "Nome:$a </br>";
    echo "Notas: $b, $c, $d e $e </br>";
    echo "Média: $media";
}

?>