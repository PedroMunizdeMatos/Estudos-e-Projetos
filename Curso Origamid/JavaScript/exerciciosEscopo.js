// Por qual motivo o código abaixo retorna com erros?
// o Código abaixo não respeita as regras de escopo. o var vaza do escopo mas o const e o let não, gerando erro pois o js não reconhece do lado de fora, as variáveis que foram declaradas dentro do escopo.
//substituir o "var" dentro do console.log por "cor" e colocar o console.log dentro do escopo.
{
  var cor = 'preto'
  const marca = 'Fiat'
  let portas = 4
  console.log(cor, marca, portas)
}

// Como corrigir o erro abaixo?
//R: a variavél dois deve ser declarada fora do escopo da função somarDois para que também seja herdada na função dividirDoi. Também é necessário substituir o '+' por '/' na função dividirDois.
const dois = 2
function somarDois(x) {
  return x + dois
}
function dividirDois(x) {
  return x / dois
}
somarDois(4)
dividirDois(6)

// O que fazer para total retornar 500?
//R: uma opção que até otimizaria o código seria retiar o loop for, por usar linhas de código que não são necessárias e na verdade estão causando o erro. caso fosse estritamente necessário manter o loop, seria interessante mudar a forma de declarar. declarar como const fora e let dentro do escopo do for. Dessa forma o for iria continuar exercendo sua função atual mas sem atrabalhar as próximas linhas de código.

const numero = 50

for (let numero = 0; numero < 10; numero++) {
  console.log(numero)
}

const total = 10 * numero
console.log(total)
