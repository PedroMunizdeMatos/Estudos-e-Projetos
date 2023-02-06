/* 

Exercise: Transform school grade.

Build an aplication that transforms school grade from numeric sistem to characters like A B C

* 90 or higher - A
* between 80 - 89 - B
* between 70 - 79 - c
* between 60 - 69 - D
* less than 60 - F

*/

// Resolution:

function getScore(score) {
  if (score >= 90 && score <= 100) {
    console.log('Student score: A')
  } else if (score < 90 && score > 79) {
    console.log('Student score: B')
  } else if (score < 80 && score > 69) {
    console.log('Student score: C')
  } else if (score < 70 && score >= 60) {
    console.log('Student score: D')
  } else if (score < 60) {
    console.log('Student score: F')
  } else {
    console.log('Invalid score.')
  }
  console.log(score)
  return score
}

getScore(101)
getScore(75)
getScore(80)
getScore(95)
getScore(67)
getScore(59)
