/* Build an aplication to calculate family expenses.

  Create an object who has 2 array tipe proprerties
    * expenses []
    * incomes []

  then, build a function to calculate total between expenses and incomes and show a message if that family has positive or negative balance followed by account balance.

*/

// solution

let family = {
  incomes: [250, 200, 450.56, 3200.27],
  expenses: [350.6, 127.9, 2400, 150, 120]
}

function sum(array) {
  let total = 0
  for (let value of array) total += value
  return total
}

function calculateBalance() {
  const calculateIncomes = sum(family.incomes)
  const calculateExpenses = sum(family.expenses)
  const total = calculateIncomes - calculateExpenses
  const itsOk = total >= 0
  let balanceText = 'negative balance'
  if (itsOk) {
    balanceText = 'positive balance'
  }
  console.log(`${balanceText}: $${total.toFixed(2)} USD Dollars`)
}

calculateBalance()
