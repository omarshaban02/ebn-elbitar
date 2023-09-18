function myFunction() {
  const wasDark = localStorage.getItem('darkmode')=='true';
  localStorage.setItem('darkmode', !wasDark);
  const element = document.body;
    element.classList.toggle("dark-theme-variables",!wasDark);    
}
function onload(){
  document.body.classList.toggle("dark-theme-variables", localStorage.getItem("darkmode") == 'true');
}