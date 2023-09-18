
const wrapper = document.querySelector('.wrapper')
const loginLink = document.querySelector('.login-link')
const registerLink = document.querySelector('.register-link')


registerLink.addEventListener('click', ()=>{
    wrapper.classList.add('active-register')
})
loginLink.addEventListener('click', ()=>{
    wrapper.classList.remove('active-register')
})
function toLoginPage(){
    location.reload()
    // location.href=''
}
function toHomePage(){
    location.reload()
}
window.onload = function() {
    var e = document.getElementById('Id').value;
    if (e ==1 ) {
        wrapper.classList.add('active-register');
    }
    }




