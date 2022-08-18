// Crie um objeto com os seus dados pessoais
var pessoa = {
  nome: 'Pedro',
  sobrenome: 'Matos',
  idade: 24,
  peso: 90,
  altura: 1.71,
  profissao: 'Desenvolvedor',
  nomeCompleto() {
    return `${this.nome} ${this.sobrenome}`
  }
}
// Deve possui pelo menos duas propriedades nome e sobrenome

// Crie um método no objeto anterior, que mostre o seu nome completo
// Criando um Método no objeto separadamente (exatamente a mesma coisa que declarar o método dentro do objeto)
pessoa.nomeCompletoPos = function () {
  return `${this.nome} ${this.sobrenome}`
}
// Modifique o valor da propriedade preco para 3000
var carro = {
  preco: 1000,
  portas: 4,
  marca: 'Audi'
}

carro.preco = 3000
// Crie um objeto de um cachorro que represente um labrador,
// preto com 10 anos, que late ao ver um homem

var cachorro = {
  raca: 'Labrador',
  cor: 'Preto',
  idade: 10,
  latir(pessoa) {
    if (pessoa === 'homem') {
      return 'Latir'
    } else {
      return 'Nada'
    }
  }
}
