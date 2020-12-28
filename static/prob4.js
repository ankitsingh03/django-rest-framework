function getSelectedCheckboxValues(name) {
    // code help https://www.javascripttutorial.net/javascript-dom/javascript-checkbox/
    const checkboxes = document.querySelectorAll(`input[name="${name}"]:checked`);
    let values = [];
    checkboxes.forEach((checkbox) => {
        values.push(checkbox.value);
    });
    return values;
    }

    const btn1 = document.querySelector('#btn1');
    btn1.addEventListener('click', (event) => {
    
    let value = {
        'year': getSelectedCheckboxValues('year'),
        'team': getSelectedCheckboxValues('name')
    } 
    fetch('http://127.0.0.1:8000/stacked/', {
    method: "POST",
    body: JSON.stringify(value),
    headers: {"Content-type": "application/json; charset=UTF-8"}
    })
    .then(response => response.json())
    .then(data => {
    //   document.getElementById("demo1").innerHTML = JSON.stringify(data);
    //   console.log(data)
      let year = value.year
      year.sort()
        let total_data = [];
        for (i of value.team){
            let list = [];
            for (j of year){
                let check = 0;
                for (k of data){
                    if (i == k.team1 && j == k.season){
                        check = k.total;
                        break;
                    }
                }
                list.push(check)
            }
            total_data.push({"name": i, "data": list})
        }
        
        // console.log(total_data)
        Highcharts.chart('container_4', {
        chart: {
            type: 'bar'
        },
        title: {
            text: 'Stacked chart of matches played by team by season'
        },
        xAxis: {
            categories: year
        },
        yAxis: {
            min: 0,
            title: {
                text: 'Matches Played by Team'
            }
        },
        legend: {
            reversed: true
        },
        plotOptions: {
            series: {
                stacking: 'normal'
            }
        },
        series: total_data
        });
    });
    });