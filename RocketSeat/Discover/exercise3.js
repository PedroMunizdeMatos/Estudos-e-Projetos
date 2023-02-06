/* Celsius to Fahrenheit

Build an aplication who receive a string in celsiu or fahrenheit and transform from one unit of measurement to another.

C = ( F - 32 ) * 5/9

F = C * 9/5 + 32

*/

// my 1st solution:

function toCelsius(x) {
  let total = (x - 32) * (9 / 5)
  return total
}

function toFahrenheit(x) {
  let total = x * (9 / 5) + 32
  return total
}

let temperature = '12f'
temperature = temperature.toUpperCase()

if (temperature.includes('C') === true) {
  temperature = temperature.split('')
  temperature.pop()
  temperature = temperature.join('')
  temperature = Number(temperature)
  console.log(`Temperature in Fahrenheit: ${toFahrenheit(temperature)}F`)
} else if (temperature.includes('F') === true) {
  temperature = temperature.split('')
  temperature.pop()
  temperature = temperature.join('')
  temperature = Number(temperature)
  console.log(`Temperature in Celsius: ${toCelsius(temperature)}C`)
} else {
  console.log('Insert a valid Celsius(C) or Fahrenheit(F) temperature.')
}

//  //my 2nd solution:

// function transformDegree(degree) {
//   const celsiusExists = degree.toUpperCase().includes('C')
//   const fahrenheitExists = degree.toUpperCase().includes('F')

//   //error flow
//   if (!celsiusExists && !fahrenheitExists) {
//     throw new Error('Not identified degree')
//   }

//   //ideal flow F -> C
//   let updatedDegree = Number(degree.toUpperCase().replace('F', ''))
//   let formula = fahrenheit => ((fahrenheit - 32) * 5) / 9
//   let degreeSign = 'C'

//   //alternative flow C -> F
//   if (celsiusExists) {
//     updatedDegree = Number(degree.toUpperCase().replace('C', ''))
//     formula = celsius => celsius * (9 / 5) + 32
//     degreeSign = 'F'
//   }
//   return formula(updatedDegree) + degreeSign
// }

// try {
//   console.log(transformDegree('10c'))
//   console.log(transformDegree('50F'))
//   console.log(transformDegree('100c'))
//   console.log(transformDegree('212f'))
// } catch (error) {
//   console.log(error)
// }
