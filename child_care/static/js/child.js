function myFunction(){
    var x = document.getElementById("menuList");
    if (x.className === "navbar-collapse") {
        x.className += "show";
    } else {
        x.className = "navbar-collapse"
    }

}
// var menuList = document.getElementById('menuList');
// var mainMenu = document.getElementById('nav-ul');

// $(menuList).addEventListener('onclick', () => {
//     $(mainMenu).classList.toggle("show");
// })