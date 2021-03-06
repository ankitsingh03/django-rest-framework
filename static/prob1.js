function getOption1() {
    // taking data from the html page
    var year = document.getElementById("mySelect1");
    var top = document.getElementById("mySelect2")
  
      let _data = {
      'year': year.options[year.selectedIndex].text,
      'top': top.options[top.selectedIndex].text
      }
  
      fetch('http://127.0.0.1:8000/team/', {
      method: "POST",
      body: JSON.stringify(_data),
      headers: {"Content-type": "application/json; charset=UTF-8"}
      })
      .then(response => response.json())
      .then(data => {
        //   document.getElementById("demo1").innerHTML = "cool " + JSON.stringify(data);
        //   console.log(data);
          let teams = []
          let runs = []
          for (var i of data){
              teams.push(i['batting_team'])
              runs.push(i['dsum'])
          }
  
          Highcharts.chart('container_1', {
              chart: {
                  type: 'column'
              },
              title: {
                  text: 'Total runs scored by team'
              },
              subtitle: {
                  text: 'chart of the total runs scored by each teams over the history of IPL.'
              },
              xAxis: {
                  categories: teams
              },
              yAxis: {
                  labels: {
                      x: -15
                  },
                  title: {
                      text: 'total runs scored '
                  }
              },
              series: [{
                  name: 'Teams',
                  data: runs,
                  pointWidth: 40
              }],
              responsive: {
                  rules: [{
                      condition: {
                          maxWidth: 500
                      },
                      // Make the labels less space demanding on mobile
                      chartOptions: {
                          xAxis: {
                              labels: {
                                  formatter: function () {
                                      return this.value.charAt(0);
                                  }
                              }
                          },
                          yAxis: {
                              labels: {
                                  align: 'left',
                                  x: 0,
                                  y: -2
                              },
                              title: {
                                  text: ''
                              }
                          }
                      }
                  }]
              }
          });
          
          document.getElementById('small').addEventListener('click', () => {
              chart.setSize(400, 300);
          });
          
          document.getElementById('large').addEventListener('click', () => {
              chart.setSize(800, 300);
              });
      });
  }

