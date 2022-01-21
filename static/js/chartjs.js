// Configuration chartjs Global
Chart.defaults.global.defaultFontColor = 'black';

new Chart(document.getElementById("devis_chart"), {
  type: 'line',
  data: {
    labels: ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Decembre"],
    datasets: [{
      data: [30, 42, 22, 23, 45, 2, 21, 21, 73, 24],
      label: "Devis signé",
      borderColor: "#2C8437",
      fill: false
    }, {
      data: [28, 35, 41, 50, 63, 9, 94, 140, 37, 57],
      label: "Devis en cours",
      borderColor: "#FA8D00",
      fill: false
    }, {
      data: [16, 17, 18, 19, 23, 76, 40, 54, 65, 34],
      label: "Devis annulé",
      borderColor: "#AA3939",
      fill: false
    },
    ]
  },
  options: {
    title: {
      display: true,
      text: 'Devis 2021',
      fontColor: 'black',
    },
    legend: {
      labels: {
        fontColor: 'black'
      }
    }
  }
});
new Chart(document.getElementById("projets_graph"), {
  type: 'doughnut',
  data: {
    labels: ["Montauban&Fils", "Gauthier", "Facade sud charente", "Funereraire sud charente"],
    datasets: [{
      label: "Projets en cours",
      backgroundColor: ["#E10C0C", "#bfbfbf", "#fbff00", "#e47fff"],
      data: [7, 2, 5, 1]
    }]
  },
  options: {
    responsive: true,
    title: {
      display: true,
      text: 'Répartition des chantier par entités',
      fontColor: 'black'
    },
    legend: {
      labels: {
        fontColor: 'black'
      }
    }
  },
});