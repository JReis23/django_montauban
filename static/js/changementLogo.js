function afficherLogo() {
    var listelogo = document.getElementById("k_liste_logo");
    if (listelogo.style.display=="flex") {
        listelogo.style.display="none";
    } else {
        listelogo.style.display="flex";
    }
}
function changerLogo2() {
    var listelogo = document.getElementById("k_liste_logo");
    var logoDeux = document.getElementById("k_logo2").src
    document.getElementById("k_logo2").src = document.getElementById("k_logo1").src
    document.getElementById("k_logo1").src = logoDeux
    console.log("Logo 2", k_logo2)
    console.log("Logo 1",  k_logo1)
    listelogo.style.display = "none";
    
}
function changerLogo3() {
    var listelogo = document.getElementById("k_liste_logo");
    var logoDeux = document.getElementById("k_logo3").src
    document.getElementById("k_logo3").src = document.getElementById("k_logo1").src
    document.getElementById("k_logo1").src = logoDeux
    console.log("Logo 3", k_logo2)
    console.log("Logo 1",  k_logo1)
    listelogo.style.display = "none";
}
function changerLogo4() {
    var listelogo = document.getElementById("k_liste_logo");
    var logoDeux = document.getElementById("k_logo4").src
    document.getElementById("k_logo4").src = document.getElementById("k_logo1").src
    document.getElementById("k_logo1").src = logoDeux
    console.log("Logo 4", k_logo2)
    console.log("Logo 1",  k_logo1)
    listelogo.style.display = "none";
}