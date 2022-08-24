// Crie uma função para verificar se um valor é Truthy
function isTruthy(dado) {
  return !!dado
}
// Crie uma função matemática que retorne o perímetro de um quadrado
function perimetroQuad(lado) {
  return lado * 4
}
// lembrando: perímetro é a soma dos quatro lados do quadrado
// Crie uma função que retorne o seu nome completo
function nomeCompleto(nome, sobrenome) {
  if (!!nome & !!sobrenome) {
    return `${nome} ${sobrenome}`
  } else {
    return 'Digite o nome e o Sobrenome.'
  }
}
// ela deve possuir os parâmetros: nome e sobrenome
// Crie uma função que verifica se um número é par
function numPar(numero) {
  if (numero % 2 == 0) {
    return 'Número Par'
  } else {
    return 'Número Ímpar'
  }
}
// Crie uma função que retorne o tipo de
function tipoDado(tipo) {
  return typeof tipo
}
// dado do argumento passado nela (typeof)

// addEventListener é uma função nativa do JavaScript
// o primeiro parâmetro é o evento que ocorre e o segundo o Callback
// utilize essa função para mostrar no console o seu nome completo
// quando o evento 'click' ocorrer.
addEventListener('click', function () {
  console.log('Pedro Matos')
})

// Corrija o erro abaixo
var totalPaises = 193
function precisoVisitar(paisesVisitados) {
  return `Ainda faltam ${totalPaises - paisesVisitados} países para visitar`
}
function jaVisitei(paisesVisitados) {
  return `Já visitei ${paisesVisitados} do total de ${totalPaises} países`
}
precisoVisitar(20)
