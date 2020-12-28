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
            data: count_umpire,
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



    })
});
