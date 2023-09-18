
// for toggleBtn
const toggleBtn = document.querySelector('.toggle_btn')
const toggleBtnIcon = document.querySelector('.toggle_btn i')
const dropDownMenu = document.querySelector('.dropdown-menu')

toggleBtn.onclick = function(){
    dropDownMenu.classList.toggle('open');
    const isOpen = dropDownMenu.classList.contains('open')

    toggleBtnIcon.classList = isOpen
        ? "fa-solid fa-xmark"
        : "fa-solid fa-bars"

}


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





