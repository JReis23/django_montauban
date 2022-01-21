const ongletsProjetClient = document.querySelectorAll('.ongletsProjetClient');
const contenuProjetClient = document.querySelectorAll('.contenuProjetClient');
let index = 0;

ongletsProjetClient.forEach(ongletProjetClient => {
    
    
    ongletProjetClient.addEventListener('click', () => {
        
        if(ongletProjetClient.classList.contains('activeProjetClient')){
            return;
        } else {
            ongletProjetClient.classList.add('activeProjetClient');
        }
        
        index = ongletProjetClient.getAttribute('data-anim');
        console.log(index);
        
        for(i = 0; i < ongletsProjetClient.length; i++) {
            
            if(ongletsProjetClient[i].getAttribute('data-anim') != index) {
                ongletsProjetClient[i].classList.remove('activeProjetClient');
            }
            
        }
        
        for(j = 0; j < contenuProjetClient.length; j++){
            
            if(contenuProjetClient[j].getAttribute('data-anim') == index) {
                contenuProjetClient[j].classList.add('activeContenuProjetClient');
            } else {
                contenuProjetClient[j].classList.remove('activeContenuProjetClient');
            }
            
            
        }
        
        
    })
    
})