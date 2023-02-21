const btn = document.querySelector('button')
const div = document.querySelector('div')
const body = document.querySelector('body')
const esc = document.querySelector('#esc')

function change() {
  div.classList.toggle('invisible')
}

btn.addEventListener('click', change)
esc.addEventListener('click', change)

body.onkeydown = function (event) {
  let keyPressed = event.key
  if (keyPressed === 'Escape') {
    change()
  }
}
