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
        text: 'Top batsman'
    },
    subtitle: {
        text: 'Plot the total runs scored by all or by teams over the history of IPL.'
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
        name: 'Batsman Runs',
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


})
}