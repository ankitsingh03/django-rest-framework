function getOption1() {
    var obj = document.getElementById("mySelect1");
    var top = document.getElementById("mySelect2")
  
      // data to be sent to the POST request
      let _data = {
      'year': obj.options[obj.selectedIndex].text,
      'top': top.options[top.selectedIndex].text
      // 'top':2
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
                  data: runs
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


  function getOption2(){
    let year = document.getElementById("dd-1");
    let team = document.getElementById("dd-2");
    let top = document.getElementById("dd-3");
    let _data = {
        'year': year.options[year.selectedIndex].text,
        'team': team.options[team.selectedIndex].text,
        'top': top.options[top.selectedIndex].text
    }

    fetch('http://127.0.0.1:8000/batsman/', {
    method: "POST",
    body: JSON.stringify(_data),
    headers: {"Content-type": "application/json; charset=UTF-8"}
    })
    .then(response => response.json())
    .then(data => {
      document.getElementById("demo1").innerHTML = JSON.stringify(data);
    console.log(data);
    let batsman = []
    let runs = []
    for (var i of data){
        batsman.push(i['batsman'])
        runs.push(i['runs'])
    }

    Highcharts.chart('container_2', {
    chart: {
        type: 'column'
    },
    title: {
        text: 'Top batsman for Royal Challengers Bangalore'
    },
    subtitle: {
        text: 'plot the total runs scored by every batsman playing for Royal Challengers Bangalore over the history of IPL.'
    },
    xAxis: {
        categories: batsman
    },
    yAxis: {
        labels: {
            x: -15
        },
        title: {
            text: 'Total Runs Scored'
        }
    },
    series: [{
        name: 'Batsman Playing for Royal Challengers Bangalore',
        data: runs
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


})
}


// plot 3

function getSelectedCheckboxValues(name) {
    // code help https://www.javascripttutorial.net/javascript-dom/javascript-checkbox/
    const checkboxes = document.querySelectorAll(`input[name="${name}"]:checked`);
    let values = [];
    checkboxes.forEach((checkbox) => {
        values.push(checkbox.value);
    });
    return values;
    }

    const btn = document.querySelector('#btn');
    btn.addEventListener('click', (event) => {

        let _data = {
            'umpire' : getSelectedCheckboxValues('color')
        }
    
        fetch('http://127.0.0.1:8000/umpire/', {
        method: "POST",
        body: JSON.stringify(_data),
        headers: {"Content-type": "application/json; charset=UTF-8"}
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById("demo1").innerHTML = JSON.stringify(data);
            console.log(data);
            let country = []
            let count_umpire = []
            for (var i of data){
                country.push(i['nationality'])
                count_umpire.push(i['total'])
          }


        Highcharts.chart('container_3', {
        chart: {
            type: 'column'
        },
        title: {
            text: 'Foreign umpire analysis'
        },
        subtitle: {
            text: 'chart of the total runs scored by each teams over the history of IPL.'
        },
        xAxis: {
            categories: country
        },
        yAxis: {
            labels: {
                x: -15
            },
            title: {
                text: 'Number of Umpires'
            }
        },
        series: [{
            name: 'Country',
            data: count_umpire
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



    })
});


// plot 4
