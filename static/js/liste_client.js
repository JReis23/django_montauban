// const ongletsInfoClient = document.querySelectorAll('.ongletsInfoClient');
// const contenuInfoClient = document.querySelectorAll('.contenuInfoClient');
// let index = 0;

// ongletsInfoClient.forEach(ongletInfoClient => {
    
    
//     ongletInfoClient.addEventListener('click', () => {
        
//         if(ongletInfoClient.classList.contains('activeInfoClient')){
//             return;
//         } else {
//             ongletInfoClient.classList.add('activeInfoClient');
//         }
        
//         index = ongletInfoClient.getAttribute('data-anim');
//         console.log(index);
        
//         for(i = 0; i < ongletsInfoClient.length; i++) {
            
//             if(ongletsInfoClient[i].getAttribute('data-anim') != index) {
//                 ongletsInfoClient[i].classList.remove('activeInfoClient');
//             }
            
//         }
        
//         for(j = 0; j < contenuInfoClient.length; j++){
            
//             if(contenuInfoClient[j].getAttribute('data-anim') == index) {
//                 contenuInfoClient[j].classList.add('activeContenuInfoClient');
//             } else {
//                 contenuInfoClient[j].classList.remove('activeContenuInfoClient');
//             }
            
            
//         }
        
        
//     })
    
// })

$(document).ready(function(){
	$('[data-toggle="tooltip"]').tooltip();
});