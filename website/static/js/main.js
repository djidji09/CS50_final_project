let dark = document.getElementById('dark');
let light = document.getElementById('light');
let swatch = document.getElementById('swatch')
let body = document.body;

//applying the cashed theme 
const theme = localStorage.getItem('theme');
if (theme){
    body.classList.add(theme);
}

//dark.onclick = () => {
//    body.classList.remove('light');
//    body.classList.add('dark');
//};
//light.onclick = () => {
//    body.classList.replace('dark', 'light');
//};
swatch.onclick = ( ) => {
    if (body.classList.contains('light')) {
        body.classList.replace('light', 'dark');
        localStorage.setItem('theme', 'dark');
    } else if (body.classList.contains('dark')) {
        body.classList.replace('dark', 'light');
        localStorage.setItem('theme', 'light');
    }
    
};