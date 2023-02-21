const btnOpenModal = document.querySelector('#openModal')
const modalWrapper = document.querySelector('.modal-wrapper')
const body = document.querySelector('body')
const scape = document.querySelector('#esc')

function invisibleToggle() {
  modalWrapper.classList.toggle('invisible')
}

btnOpenModal.addEventListener('click', invisibleToggle)
esc.addEventListener('click', invisibleToggle)

body.onkeydown = function (event) {
  let keyPressed = event.key
  if (keyPressed === 'Escape') {
    invisibleToggle()
  }
}
