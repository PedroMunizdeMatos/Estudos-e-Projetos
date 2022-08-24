// Crie uma array com os anos que o Brasil ganhou a copa
// 1959, 1962, 1970, 1994, 2002

var brasilCopa = ['1959', '1962', '1970', '1994', '2002']

brasilCopa.forEach(function (item) {
  console.log(item)
})

// Interaja com a array utilizando um loop, para mostrar
// no console a seguinte mensagem, `O brasil ganhou a copa de ${ano}`

brasilCopa.forEach(function (i) {
  console.log(`O Brasil ganhou a copa no ano de: ${i}`)
})

// Interaja com um loop nas frutas abaixo e pare ao chegar em Pera
// Coloque a última fruta da array acima em uma variável,
// sem remover a mesma da array.
var frutas = ['Banana', 'Maçã', 'Pera', 'Uva', 'Melância']

var ultimaFruta = frutas[frutas.length - 1]

frutas.forEach(function (pera) {
  console.log(pera)
  if (pera === 'Pera') {
    frutas.pop()
    frutas.pop()
  }
})
