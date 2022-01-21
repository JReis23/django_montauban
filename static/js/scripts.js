document.addEventListener('DOMContentLoaded', function() {

  
    var calendarEl = document.getElementById('calendar');
  
    var xmlhttp = new XMLHttpRequest()
    
    xmlhttp.onreadystatechange = () => {
      if(xmlhttp.readyState = 4){
        if(xmlhttp.status = 200){
          var evenements = JSON.parse(xmlhttp.responseText)
          
          var calendar = new FullCalendar.Calendar(calendarEl, {
            initialView: 'dayGridMonth',
            googleCalendarApiKey: 'AIzaSyBg0Ukmg0-AqZ7sq79h1K5CMmeHxz1ymsM',
            events: {
              googleCalendarId: '32527171615-sh2gkp9tk9gd6tgtttohiqmht2b9ijg6.apps.googleusercontent.com'
            },
            locale: 'fr',
            themeSystem: 'bootstrap',
            headerToolbar:{
              start: "prev prevYear nextYear next today",
              center: 'title',
              right: 'dayGridMonth,timeGridWeek,timeGridDay',
            },
            titleFormat:{
              year: 'numeric', 
              month: 'long', 
            },
            buttonText:{
              today: "Aujourd\'hui",
              month: 'Mois',
              week: 'Semaine',
              day: 'Jour',
            },
            bootstrapFontAwesome:{
              close: 'fa-times',
              prev: 'fa-chevron-left',
              next: 'fa-chevron-right',
              prevYear: 'fa-angle-double-left',
              nextYear: 'fa-angle-double-right',
            },
            events: evenements,
            nowIndicator: true,
            editable: true,
            eventStartEditable: true,
            dayMaxEvents: true,
            

        
        
          });
          calendar.render();
        }
      }
    }
    
    xmlhttp.open('get', 'http://localhost/montauban/Calendar/node_modules/calenda.json', true)
    xmlhttp.send(null)
  
  });