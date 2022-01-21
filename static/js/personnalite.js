// k_changer_personnalite

function changerPersonnalite() {
    var perso = document.getElementById("k_changer_perso")

    if(perso.style.display == "none"){
        perso.style.display = "inherit";
    } else {
        perso.style.display = "none";
    }
}
function personnaliteRouge() {
    var perso = document.getElementById("k_changer_personnalite")
    var perso2 = document.getElementById("k_changer_perso")

    perso.style.background = "Red";
    perso2.style.display = "none";
}
function personnaliteGreen() {
    var perso = document.getElementById("k_changer_personnalite")
    var perso2 = document.getElementById("k_changer_perso")

    perso.style.background = "Green";
    perso2.style.display = "none";
}
function personnaliteYellow() {
    var perso = document.getElementById("k_changer_personnalite")
    var perso2 = document.getElementById("k_changer_perso")

    perso.style.background = "Yellow";
    perso2.style.display = "none";
}