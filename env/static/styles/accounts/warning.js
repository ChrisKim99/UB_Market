const first_name = document.getElementById('first_name')
const last_name = document.getElementById('last_name')
const email = document.getElementById('email')
const password = document.getElementById('password')
const confirm_password = document.getElementById('confirm password')
const form = document.getElementById('form')

form.addEventListener('submit', (e) => {
    let messages = []
    if (fisrt_name.value === '' || name.value == null) {
        messages.push('First name is required')
    }

    if (last_name.value === '' || name.value == null) {
        messages.push('Last name is required')
    }
    if (email.value === '' || name.value == null) {
        messages.push('Email is required')
    }
    if (password.value === '' || name.value == null) {
        messages.push('Password is required')
    }
    if (confirm_password.value === '' || name.value == null) {
        messages.push('Confirm password is required')
    }

    if (messages.length > 0) {
        e.preventDefault()
        errorElement.innerText = messages.join(',')
    }


})

