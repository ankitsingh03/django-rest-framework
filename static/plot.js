fetch('http://127.0.0.1:8000/api')
  .then(response => response.json())
  .then(data => {
    //   let country = Object.keys(data);
    //   let count_umpire = Object.values(data);
      console.log(data)
    });
