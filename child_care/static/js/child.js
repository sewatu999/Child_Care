function myFunction(){
    var x = document.getElementById("mainMenu");
    if (x.className === "navbar-collapse") {
        x.className += " responsive";
    } else {
        x.className = "navbar-collapse"
    }

}
// var menuList = document.getElementById('menuList');
// var mainMenu = document.getElementById('nav-ul');

// $(menuList).addEventListener('onclick', () => {
//     $(mainMenu).classList.toggle("show");
// })