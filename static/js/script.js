function notifyMe() {
  if (!("Notification" in window)) {
    alert("This browser does not support system notifications");
  }
  else if (Notification.permission === "granted") {
    notify();
  }
  else if (Notification.permission !== 'denied') {
    Notification.requestPermission(function (permission) {
      if (permission === "granted") {
        notify();
      }
    });
  }
  
  function notify() {
    var notification = new Notification('VOUS AVEZ UN POST-IT', {
      body: "Salut! Regarde ton post-it!",
    });

    notification.onclick = function () {
      window.open("http://carnes.cc");      
    };
    setTimeout(notification.close.bind(notification), 40000); 
  }

}