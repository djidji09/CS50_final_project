let dark = document.getElementById('dark');
let light = document.getElementById('light');
let swatch = document.getElementById('swatch')
let body = document.body;


//dark.onclick = () => {
//    body.classList.remove('light');
//    body.classList.add('dark');
//};
//light.onclick = () => {
//    body.classList.replace('dark', 'light');
//};
swatch.onclick = ( ) => {
    body.classList.toggle('dark');
};