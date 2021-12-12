
    var psArray = [];
    
    var a = Math.floor(Math.random() * 25) + 1;
    var b = Math.floor(Math.random() * 25) + 1;
    var c = Math.floor(Math.random() * 25) + 1;
    var d = Math.floor(Math.random() * 25) + 1;
    var e = Math.floor(Math.random() * 25) + 1;

    fetch('https://retoolapi.dev/DmVDy5/propdata/' + a)
    .then(response=>{
    return response.json();

    }).then(json=>{

    var data = json;

    var { PropagandaScore } = data;

    var prop = parseInt(PropagandaScore);

    psArray.push(prop);

    console.log(psArray);

    });

    fetch('https://retoolapi.dev/DmVDy5/propdata/' + b)
    .then(response=>{
    return response.json();

    }).then(json=>{

    var data = json;

    var { PropagandaScore } = data;

    var prop = parseInt(PropagandaScore);

    psArray.push(prop);

    console.log(psArray);

    });

    fetch('https://retoolapi.dev/DmVDy5/propdata/' + c)
    .then(response=>{
    return response.json();

    }).then(json=>{

    var data = json;

    var { PropagandaScore } = data;

    var prop = parseInt(PropagandaScore);

    psArray.push(prop);

    console.log(psArray);

    });

    fetch('https://retoolapi.dev/DmVDy5/propdata/' + d)
    .then(response=>{
    return response.json();

    }).then(json=>{

    var data = json;

    var { PropagandaScore } = data;

    var prop = parseInt(PropagandaScore);

    psArray.push(prop);

    console.log(psArray);

    });

    fetch('https://retoolapi.dev/DmVDy5/propdata/' + e)
    .then(response=>{
    return response.json();

    }).then(json=>{

    var data = json;

    var { PropagandaScore } = data;

    var prop = parseInt(PropagandaScore);

    psArray.push(prop);

    sum = psArray[0] + psArray[1] + psArray[2] + psArray[3] + psArray[4]

    avg = sum / 5;

    var Low = document.createElement("img");
    Low.src = "LOW.png";
    var Caution = document.createElement("img");
    Caution.src = "CAUTION.png";
    var Elevated = document.createElement("img");
    Elevated.src = "ELEVATED.png";
    var High = document.createElement("img");
    High.src = "HIGH.png";
   
    if (avg > -1 && avg < 4) {
        document.getElementById("gr").innerHTML = avg;
        document.getElementById("Low").appendChild(Low);
        document.getElementById("caution_info").innerHTML = "The content on this page has been rated GREEN, indicating that people viewing this page frequent sites that contain low amounts of propaganda"
    }

    else if (avg > 3 && avg < 6) {
        document.getElementById("kh").innerHTML = avg;
        document.getElementById("Caution").appendChild(Caution);
        document.getElementById("caution_info").innerHTML = "The content on this page has been rated YELLOW, indicating that people viewing this page frequent sites that contain moderate amounts of propaganda"
    }

    else if (avg > 5 && avg < 8) {
        document.getElementById("or").innerHTML = avg;
        document.getElementById("Elevated").appendChild(Elevated);
        document.getElementById("caution_info").innerHTML = "The content on this page has been rated ORANGE, indicating that people viewing this page frequent sites that contain significant amounts of propaganda"
    }

    else if (avg > 7 && avg < 12) {
        document.getElementById("re").innerHTML = avg;
        document.getElementById("High").appendChild(High);
        document.getElementById("caution_info").innerHTML = "The content on this page has been rated RED, indicating that people viewing this page frequent sites that contain High amounts of propaganda"
    }

    else  {
        document.getElementById("na").innerHTML = avg;
    }


});

navigator.geolocation.getCurrentPosition(
    function (position) {
       initMap(position.coords.latitude, position.coords.longitude)
    },
    function errorCallback(error) {
       console.log(error)
    }
  );
  
  function initMap(lat, lng) {
  
    var myLatLng = {
       lat,
       lng
    };
  
    var map = new google.maps.Map(document.getElementById('map'), {
       zoom: 15,
       center: myLatLng
       
    });
  
    var marker = new google.maps.Marker({
       position: myLatLng,
       map: map,
    })
 
 
   fetch('https://maps.googleapis.com/maps/api/geocode/json?latlng='+lat+','+lng+'&key=APIKEY')
    .then(response=>{
       return response.json();
  
    }).then(json=>{
 
       console.log(json.plus_code.compound_code);
 
       var jsVariable = json.plus_code.compound_code;
 
       var cityName = jsVariable.split(' ');
 
       console.log(cityName[2]);
 
 
       if(cityName[2].includes("AL")){
 
          fetch('https://retoolapi.dev/ClBIjw/statedata/1')
          .then(response=>{
             return response.json();
      
          }).then(json=>{
      
             var data = json;
 
             var { Conservative, Moderate, Liberal, DoNotKnow } = data;
 
             document.getElementById('polistats').innerHTML= "The users in your state are " +Conservative+ " Conservative, " +Moderate+ " Moderate, " +Liberal+ " Liberal, and " +DoNotKnow+ " Do Not Know ";
 
 
      
      });
      
       }
       
       if(cityName[2].includes("AK")){
 
         fetch('https://retoolapi.dev/ClBIjw/statedata/2')
         .then(response=>{
            return response.json();
     
         }).then(json=>{
     
            var data = json;

            var { Conservative, Moderate, Liberal, DoNotKnow } = data;

            document.getElementById('polistats').innerHTML= "The users in your state are " +Conservative+ " Conservative, " +Moderate+ " Moderate, " +Liberal+ " Liberal, and " +DoNotKnow+ " Do Not Know ";


     
     });
     
      } 
  
      if(cityName[2].includes("AZ")){
 
         fetch('https://retoolapi.dev/ClBIjw/statedata/3')
         .then(response=>{
            return response.json();
     
         }).then(json=>{
     
            var data = json;

            var { Conservative, Moderate, Liberal, DoNotKnow } = data;

            document.getElementById('polistats').innerHTML= "The users in your state are " +Conservative+ " Conservative, " +Moderate+ " Moderate, " +Liberal+ " Liberal, and " +DoNotKnow+ " Do Not Know ";


     
     });
     
      }

      if(cityName[2].includes("AR")){
 
         fetch('https://retoolapi.dev/ClBIjw/statedata/4')
         .then(response=>{
            return response.json();
     
         }).then(json=>{
     
            var data = json;

            var { Conservative, Moderate, Liberal, DoNotKnow } = data;

            document.getElementById('polistats').innerHTML= "The users in your state are " +Conservative+ " Conservative, " +Moderate+ " Moderate, " +Liberal+ " Liberal, and " +DoNotKnow+ " Do Not Know ";


     
     });
     
      }
      
      if(cityName[2].includes("CA")){
 
         fetch('https://retoolapi.dev/ClBIjw/statedata/5')
         .then(response=>{
            return response.json();
     
         }).then(json=>{
     
            var data = json;

            var { Conservative, Moderate, Liberal, DoNotKnow } = data;

            document.getElementById('polistats').innerHTML= "The users in your state are " +Conservative+ " Conservative, " +Moderate+ " Moderate, " +Liberal+ " Liberal, and " +DoNotKnow+ " Do Not Know ";


     
     });
     
      } 

      if(cityName[2].includes("CO")){
 
         fetch('https://retoolapi.dev/ClBIjw/statedata/6')
         .then(response=>{
            return response.json();
     
         }).then(json=>{
     
            var data = json;

            var { Conservative, Moderate, Liberal, DoNotKnow } = data;

            document.getElementById('polistats').innerHTML= "The users in your state are " +Conservative+ " Conservative, " +Moderate+ " Moderate, " +Liberal+ " Liberal, and " +DoNotKnow+ " Do Not Know ";


     
     });
     
      } 

      if(cityName[2].includes("CT")){
 
         fetch('https://retoolapi.dev/ClBIjw/statedata/7')
         .then(response=>{
            return response.json();
     
         }).then(json=>{
     
            var data = json;

            var { Conservative, Moderate, Liberal, DoNotKnow } = data;

            document.getElementById('polistats').innerHTML= "The users in your state are " +Conservative+ " Conservative, " +Moderate+ " Moderate, " +Liberal+ " Liberal, and " +DoNotKnow+ " Do Not Know ";


     
     });
     
      } 

      if(cityName[2].includes("DE")){
 
         fetch('https://retoolapi.dev/ClBIjw/statedata/8')
         .then(response=>{
            return response.json();
     
         }).then(json=>{
     
            var data = json;

            var { Conservative, Moderate, Liberal, DoNotKnow } = data;

            document.getElementById('polistats').innerHTML= "The users in your state are " +Conservative+ " Conservative, " +Moderate+ " Moderate, " +Liberal+ " Liberal, and " +DoNotKnow+ " Do Not Know ";


     
     });
     
      } 

      if(cityName[2].includes("FL")){
 
         fetch('https://retoolapi.dev/ClBIjw/statedata/9')
         .then(response=>{
            return response.json();
     
         }).then(json=>{
     
            var data = json;

            var { Conservative, Moderate, Liberal, DoNotKnow } = data;

            document.getElementById('polistats').innerHTML= "The users in your state are " +Conservative+ " Conservative, " +Moderate+ " Moderate, " +Liberal+ " Liberal, and " +DoNotKnow+ " Do Not Know ";


     
     });
     
      } 

      if(cityName[2].includes("GA")){
 
         fetch('https://retoolapi.dev/ClBIjw/statedata/10')
         .then(response=>{
            return response.json();
     
         }).then(json=>{
     
            var data = json;

            var { Conservative, Moderate, Liberal, DoNotKnow } = data;

            document.getElementById('polistats').innerHTML= "The users in your state are " +Conservative+ " Conservative, " +Moderate+ " Moderate, " +Liberal+ " Liberal, and " +DoNotKnow+ " Do Not Know ";


     
     });
     
      } 

      if(cityName[2].includes("HI")){
 
         fetch('https://retoolapi.dev/ClBIjw/statedata/11')
         .then(response=>{
            return response.json();
     
         }).then(json=>{
     
            var data = json;

            var { Conservative, Moderate, Liberal, DoNotKnow } = data;

            document.getElementById('polistats').innerHTML= "The users in your state are " +Conservative+ " Conservative, " +Moderate+ " Moderate, " +Liberal+ " Liberal, and " +DoNotKnow+ " Do Not Know ";


     
     });
     
      } 

      if(cityName[2].includes("ID")){
 
         fetch('https://retoolapi.dev/ClBIjw/statedata/12')
         .then(response=>{
            return response.json();
     
         }).then(json=>{
     
            var data = json;

            var { Conservative, Moderate, Liberal, DoNotKnow } = data;

            document.getElementById('polistats').innerHTML= "The users in your state are " +Conservative+ " Conservative, " +Moderate+ " Moderate, " +Liberal+ " Liberal, and " +DoNotKnow+ " Do Not Know ";


     
     });
     
      } 

      if(cityName[2].includes("IL")){
 
         fetch('https://retoolapi.dev/ClBIjw/statedata/13')
         .then(response=>{
            return response.json();
     
         }).then(json=>{
     
            var data = json;

            var { Conservative, Moderate, Liberal, DoNotKnow } = data;

            document.getElementById('polistats').innerHTML= "The users in your state are " +Conservative+ " Conservative, " +Moderate+ " Moderate, " +Liberal+ " Liberal, and " +DoNotKnow+ " Do Not Know ";


     
     });
     
      }
      
      if(cityName[2].includes("IN")){
 
         fetch('https://retoolapi.dev/ClBIjw/statedata/14')
         .then(response=>{
            return response.json();
     
         }).then(json=>{
     
            var data = json;

            var { Conservative, Moderate, Liberal, DoNotKnow } = data;

            document.getElementById('polistats').innerHTML= "The users in your state are " +Conservative+ " Conservative, " +Moderate+ " Moderate, " +Liberal+ " Liberal, and " +DoNotKnow+ " Do Not Know ";


     
     });
     
      }

      if(cityName[2].includes("IA")){
 
         fetch('https://retoolapi.dev/ClBIjw/statedata/15')
         .then(response=>{
            return response.json();
     
         }).then(json=>{
     
            var data = json;

            var { Conservative, Moderate, Liberal, DoNotKnow } = data;

            document.getElementById('polistats').innerHTML= "The users in your state are " +Conservative+ " Conservative, " +Moderate+ " Moderate, " +Liberal+ " Liberal, and " +DoNotKnow+ " Do Not Know ";


     
     });
     
      }

      if(cityName[2].includes("KS")){
 
         fetch('https://retoolapi.dev/ClBIjw/statedata/16')
         .then(response=>{
            return response.json();
     
         }).then(json=>{
     
            var data = json;

            var { Conservative, Moderate, Liberal, DoNotKnow } = data;

            document.getElementById('polistats').innerHTML= "The users in your state are " +Conservative+ " Conservative, " +Moderate+ " Moderate, " +Liberal+ " Liberal, and " +DoNotKnow+ " Do Not Know ";


     
     });
     
      }

      if(cityName[2].includes("KY")){
 
         fetch('https://retoolapi.dev/ClBIjw/statedata/17')
         .then(response=>{
            return response.json();
     
         }).then(json=>{
     
            var data = json;

            var { Conservative, Moderate, Liberal, DoNotKnow } = data;

            document.getElementById('polistats').innerHTML= "The users in your state are " +Conservative+ " Conservative, " +Moderate+ " Moderate, " +Liberal+ " Liberal, and " +DoNotKnow+ " Do Not Know ";


     
     });
     
      }

      if(cityName[2].includes("LA")){
 
         fetch('https://retoolapi.dev/ClBIjw/statedata/18')
         .then(response=>{
            return response.json();
     
         }).then(json=>{
     
            var data = json;

            var { Conservative, Moderate, Liberal, DoNotKnow } = data;

            document.getElementById('polistats').innerHTML= "The users in your state are " +Conservative+ " Conservative, " +Moderate+ " Moderate, " +Liberal+ " Liberal, and " +DoNotKnow+ " Do Not Know ";


     
     });
     
      }

      if(cityName[2].includes("ME")){
 
         fetch('https://retoolapi.dev/ClBIjw/statedata/19')
         .then(response=>{
            return response.json();
     
         }).then(json=>{
     
            var data = json;

            var { Conservative, Moderate, Liberal, DoNotKnow } = data;

            document.getElementById('polistats').innerHTML= "The users in your state are " +Conservative+ " Conservative, " +Moderate+ " Moderate, " +Liberal+ " Liberal, and " +DoNotKnow+ " Do Not Know ";


     
     });
     
      }

      if(cityName[2].includes("MD")){
 
         fetch('https://retoolapi.dev/ClBIjw/statedata/20')
         .then(response=>{
            return response.json();
     
         }).then(json=>{
     
            var data = json;

            var { Conservative, Moderate, Liberal, DoNotKnow } = data;

            document.getElementById('polistats').innerHTML= "The users in your state are " +Conservative+ " Conservative, " +Moderate+ " Moderate, " +Liberal+ " Liberal, and " +DoNotKnow+ " Do Not Know ";


     
     });
     
      }

      if(cityName[2].includes("MA")){
 
         fetch('https://retoolapi.dev/ClBIjw/statedata/21')
         .then(response=>{
            return response.json();
     
         }).then(json=>{
     
            var data = json;

            var { Conservative, Moderate, Liberal, DoNotKnow } = data;

            document.getElementById('polistats').innerHTML= "The users in your state are " +Conservative+ " Conservative, " +Moderate+ " Moderate, " +Liberal+ " Liberal, and " +DoNotKnow+ " Do Not Know ";


     
     });
     
      }

      if(cityName[2].includes("MI")){
 
         fetch('https://retoolapi.dev/ClBIjw/statedata/22')
         .then(response=>{
            return response.json();
     
         }).then(json=>{
     
            var data = json;

            var { Conservative, Moderate, Liberal, DoNotKnow } = data;

            document.getElementById('polistats').innerHTML= "The users in your state are " +Conservative+ " Conservative, " +Moderate+ " Moderate, " +Liberal+ " Liberal, and " +DoNotKnow+ " Do Not Know ";


     
     });
     
      }

      if(cityName[2].includes("MN")){
 
         fetch('https://retoolapi.dev/ClBIjw/statedata/23')
         .then(response=>{
            return response.json();
     
         }).then(json=>{
     
            var data = json;

            var { Conservative, Moderate, Liberal, DoNotKnow } = data;

            document.getElementById('polistats').innerHTML= "The users in your state are " +Conservative+ " Conservative, " +Moderate+ " Moderate, " +Liberal+ " Liberal, and " +DoNotKnow+ " Do Not Know ";


     
     });
     
      }

      if(cityName[2].includes("MS")){
 
         fetch('https://retoolapi.dev/ClBIjw/statedata/24')
         .then(response=>{
            return response.json();
     
         }).then(json=>{
     
            var data = json;

            var { Conservative, Moderate, Liberal, DoNotKnow } = data;

            document.getElementById('polistats').innerHTML= "The users in your state are " +Conservative+ " Conservative, " +Moderate+ " Moderate, " +Liberal+ " Liberal, and " +DoNotKnow+ " Do Not Know ";


     
     });
     
      }

      if(cityName[2].includes("MO")){
 
         fetch('https://retoolapi.dev/ClBIjw/statedata/25')
         .then(response=>{
            return response.json();
     
         }).then(json=>{
     
            var data = json;

            var { Conservative, Moderate, Liberal, DoNotKnow } = data;

            document.getElementById('polistats').innerHTML= "The users in your state are " +Conservative+ " Conservative, " +Moderate+ " Moderate, " +Liberal+ " Liberal, and " +DoNotKnow+ " Do Not Know ";


     
     });
     
      }

      if(cityName[2].includes("MT")){
 
         fetch('https://retoolapi.dev/ClBIjw/statedata/26')
         .then(response=>{
            return response.json();
     
         }).then(json=>{
     
            var data = json;

            var { Conservative, Moderate, Liberal, DoNotKnow } = data;

            document.getElementById('polistats').innerHTML= "The users in your state are " +Conservative+ " Conservative, " +Moderate+ " Moderate, " +Liberal+ " Liberal, and " +DoNotKnow+ " Do Not Know ";


     
     });
     
      }

      if(cityName[2].includes("NE")){
 
         fetch('https://retoolapi.dev/ClBIjw/statedata/27')
         .then(response=>{
            return response.json();
     
         }).then(json=>{
     
            var data = json;

            var { Conservative, Moderate, Liberal, DoNotKnow } = data;

            document.getElementById('polistats').innerHTML= "The users in your state are " +Conservative+ " Conservative, " +Moderate+ " Moderate, " +Liberal+ " Liberal, and " +DoNotKnow+ " Do Not Know ";


     
     });
     
      }

      if(cityName[2].includes("NV")){
 
         fetch('https://retoolapi.dev/ClBIjw/statedata/28')
         .then(response=>{
            return response.json();
     
         }).then(json=>{
     
            var data = json;

            var { Conservative, Moderate, Liberal, DoNotKnow } = data;

            document.getElementById('polistats').innerHTML= "The users in your state are " +Conservative+ " Conservative, " +Moderate+ " Moderate, " +Liberal+ " Liberal, and " +DoNotKnow+ " Do Not Know ";


     
     });
     
      }

      if(cityName[2].includes("NH")){
 
         fetch('https://retoolapi.dev/ClBIjw/statedata/29')
         .then(response=>{
            return response.json();
     
         }).then(json=>{
     
            var data = json;

            var { Conservative, Moderate, Liberal, DoNotKnow } = data;

            document.getElementById('polistats').innerHTML= "The users in your state are " +Conservative+ " Conservative, " +Moderate+ " Moderate, " +Liberal+ " Liberal, and " +DoNotKnow+ " Do Not Know ";


     
     });
     
      }

      if(cityName[2].includes("NJ")){
 
         fetch('https://retoolapi.dev/ClBIjw/statedata/30')
         .then(response=>{
            return response.json();
     
         }).then(json=>{
     
            var data = json;

            var { Conservative, Moderate, Liberal, DoNotKnow } = data;

            document.getElementById('polistats').innerHTML= "The users in your state are " +Conservative+ " Conservative, " +Moderate+ " Moderate, " +Liberal+ " Liberal, and " +DoNotKnow+ " Do Not Know ";


     
     });
     
      }

      if(cityName[2].includes("NM")){
 
         fetch('https://retoolapi.dev/ClBIjw/statedata/31')
         .then(response=>{
            return response.json();
     
         }).then(json=>{
     
            var data = json;

            var { Conservative, Moderate, Liberal, DoNotKnow } = data;

            document.getElementById('polistats').innerHTML= "The users in your state are " +Conservative+ " Conservative, " +Moderate+ " Moderate, " +Liberal+ " Liberal, and " +DoNotKnow+ " Do Not Know ";


     
     });
     
      }

      if(cityName[2].includes("NY")){
 
         fetch('https://retoolapi.dev/ClBIjw/statedata/32')
         .then(response=>{
            return response.json();
     
         }).then(json=>{
     
            var data = json;

            var { Conservative, Moderate, Liberal, DoNotKnow } = data;

            document.getElementById('polistats').innerHTML= "The users in your state are " +Conservative+ " Conservative, " +Moderate+ " Moderate, " +Liberal+ " Liberal, and " +DoNotKnow+ " Do Not Know ";


     
     });
     
      }

      if(cityName[2].includes("NC")){
 
         fetch('https://retoolapi.dev/ClBIjw/statedata/33')
         .then(response=>{
            return response.json();
     
         }).then(json=>{
     
            var data = json;

            var { Conservative, Moderate, Liberal, DoNotKnow } = data;

            document.getElementById('polistats').innerHTML= "The users in your state are " +Conservative+ " Conservative, " +Moderate+ " Moderate, " +Liberal+ " Liberal, and " +DoNotKnow+ " Do Not Know ";


     
     });
     
      }

      if(cityName[2].includes("ND")){
 
         fetch('https://retoolapi.dev/ClBIjw/statedata/34')
         .then(response=>{
            return response.json();
     
         }).then(json=>{
     
            var data = json;

            var { Conservative, Moderate, Liberal, DoNotKnow } = data;

            document.getElementById('polistats').innerHTML= "The users in your state are " +Conservative+ " Conservative, " +Moderate+ " Moderate, " +Liberal+ " Liberal, and " +DoNotKnow+ " Do Not Know ";


     
     });
     
      }

      if(cityName[2].includes("OH")){
 
         fetch('https://retoolapi.dev/ClBIjw/statedata/35')
         .then(response=>{
            return response.json();
     
         }).then(json=>{
     
            var data = json;

            var { Conservative, Moderate, Liberal, DoNotKnow } = data;

            document.getElementById('polistats').innerHTML= "The users in your state are " +Conservative+ " Conservative, " +Moderate+ " Moderate, " +Liberal+ " Liberal, and " +DoNotKnow+ " Do Not Know ";


     
     });
     
      }

      if(cityName[2].includes("OK")){
 
         fetch('https://retoolapi.dev/ClBIjw/statedata/36')
         .then(response=>{
            return response.json();
     
         }).then(json=>{
     
            var data = json;

            var { Conservative, Moderate, Liberal, DoNotKnow } = data;

            document.getElementById('polistats').innerHTML= "The users in your state are " +Conservative+ " Conservative, " +Moderate+ " Moderate, " +Liberal+ " Liberal, and " +DoNotKnow+ " Do Not Know ";


     
     });
     
      }

      if(cityName[2].includes("OR")){
 
         fetch('https://retoolapi.dev/ClBIjw/statedata/37')
         .then(response=>{
            return response.json();
     
         }).then(json=>{
     
            var data = json;

            var { Conservative, Moderate, Liberal, DoNotKnow } = data;

            document.getElementById('polistats').innerHTML= "The users in your state are " +Conservative+ " Conservative, " +Moderate+ " Moderate, " +Liberal+ " Liberal, and " +DoNotKnow+ " Do Not Know ";


     
     });
     
      }

      if(cityName[2].includes("PA")){
 
         fetch('https://retoolapi.dev/ClBIjw/statedata/38')
         .then(response=>{
            return response.json();
     
         }).then(json=>{
     
            var data = json;

            var { Conservative, Moderate, Liberal, DoNotKnow } = data;

            document.getElementById('polistats').innerHTML= "The users in your state are " +Conservative+ " Conservative, " +Moderate+ " Moderate, " +Liberal+ " Liberal, and " +DoNotKnow+ " Do Not Know ";


     
     });
     
      }

      if(cityName[2].includes("RI")){
 
         fetch('https://retoolapi.dev/ClBIjw/statedata/39')
         .then(response=>{
            return response.json();
     
         }).then(json=>{
     
            var data = json;

            var { Conservative, Moderate, Liberal, DoNotKnow } = data;

            document.getElementById('polistats').innerHTML= "The users in your state are " +Conservative+ " Conservative, " +Moderate+ " Moderate, " +Liberal+ " Liberal, and " +DoNotKnow+ " Do Not Know ";


     
     });
     
      }

      if(cityName[2].includes("SC")){
 
         fetch('https://retoolapi.dev/ClBIjw/statedata/40')
         .then(response=>{
            return response.json();
     
         }).then(json=>{
     
            var data = json;

            var { Conservative, Moderate, Liberal, DoNotKnow } = data;

            document.getElementById('polistats').innerHTML= "The users in your state are " +Conservative+ " Conservative, " +Moderate+ " Moderate, " +Liberal+ " Liberal, and " +DoNotKnow+ " Do Not Know ";


     
     });
     
      }

      if(cityName[2].includes("SD")){
 
         fetch('https://retoolapi.dev/ClBIjw/statedata/40')
         .then(response=>{
            return response.json();
     
         }).then(json=>{
     
            var data = json;

            var { Conservative, Moderate, Liberal, DoNotKnow } = data;

            document.getElementById('polistats').innerHTML= "The users in your state are " +Conservative+ " Conservative, " +Moderate+ " Moderate, " +Liberal+ " Liberal, and " +DoNotKnow+ " Do Not Know ";


     
     });
     
      }

      if(cityName[2].includes("TN")){
 
         fetch('https://retoolapi.dev/ClBIjw/statedata/41')
         .then(response=>{
            return response.json();
     
         }).then(json=>{
     
            var data = json;

            var { Conservative, Moderate, Liberal, DoNotKnow } = data;

            document.getElementById('polistats').innerHTML= "The users in your state are " +Conservative+ " Conservative, " +Moderate+ " Moderate, " +Liberal+ " Liberal, and " +DoNotKnow+ " Do Not Know ";


     
     });
     
      }

      if(cityName[2].includes("TX")){
 
         fetch('https://retoolapi.dev/ClBIjw/statedata/42')
         .then(response=>{
            return response.json();
     
         }).then(json=>{
     
            var data = json;

            var { Conservative, Moderate, Liberal, DoNotKnow } = data;

            document.getElementById('polistats').innerHTML= "The users in your state are " +Conservative+ " Conservative, " +Moderate+ " Moderate, " +Liberal+ " Liberal, and " +DoNotKnow+ " Do Not Know ";


     
     });
     
      }

      if(cityName[2].includes("UT")){
 
         fetch('https://retoolapi.dev/ClBIjw/statedata/43')
         .then(response=>{
            return response.json();
     
         }).then(json=>{
     
            var data = json;

            var { Conservative, Moderate, Liberal, DoNotKnow } = data;

            document.getElementById('polistats').innerHTML= "The users in your state are " +Conservative+ " Conservative, " +Moderate+ " Moderate, " +Liberal+ " Liberal, and " +DoNotKnow+ " Do Not Know ";


     
     });
     
      }

      if(cityName[2].includes("VT")){
 
         fetch('https://retoolapi.dev/ClBIjw/statedata/44')
         .then(response=>{
            return response.json();
     
         }).then(json=>{
     
            var data = json;

            var { Conservative, Moderate, Liberal, DoNotKnow } = data;

            document.getElementById('polistats').innerHTML= "The users in your state are " +Conservative+ " Conservative, " +Moderate+ " Moderate, " +Liberal+ " Liberal, and " +DoNotKnow+ " Do Not Know ";


     
     });
     
      }

      if(cityName[2].includes("VA")){
 
         fetch('https://retoolapi.dev/ClBIjw/statedata/45')
         .then(response=>{
            return response.json();
     
         }).then(json=>{
     
            var data = json;

            var { Conservative, Moderate, Liberal, DoNotKnow } = data;

            document.getElementById('polistats').innerHTML= "The users in your state are " +Conservative+ " Conservative, " +Moderate+ " Moderate, " +Liberal+ " Liberal, and " +DoNotKnow+ " Do Not Know ";


     
     });
     
      }

      if(cityName[2].includes("VI")){
 
         fetch('https://retoolapi.dev/ClBIjw/statedata/46')
         .then(response=>{
            return response.json();
     
         }).then(json=>{
     
            var data = json;

            var { Conservative, Moderate, Liberal, DoNotKnow } = data;

            document.getElementById('polistats').innerHTML= "The users in your state are " +Conservative+ " Conservative, " +Moderate+ " Moderate, " +Liberal+ " Liberal, and " +DoNotKnow+ " Do Not Know ";


     
     });
     
      }

      if(cityName[2].includes("WA")){
 
         fetch('https://retoolapi.dev/ClBIjw/statedata/47')
         .then(response=>{
            return response.json();
     
         }).then(json=>{
     
            var data = json;

            var { Conservative, Moderate, Liberal, DoNotKnow } = data;

            document.getElementById('polistats').innerHTML= "The users in your state are " +Conservative+ " Conservative, " +Moderate+ " Moderate, " +Liberal+ " Liberal, and " +DoNotKnow+ " Do Not Know ";


     
     });
     
      }

      if(cityName[2].includes("WV")){
 
         fetch('https://retoolapi.dev/ClBIjw/statedata/48')
         .then(response=>{
            return response.json();
     
         }).then(json=>{
     
            var data = json;

            var { Conservative, Moderate, Liberal, DoNotKnow } = data;

            document.getElementById('polistats').innerHTML= "The users in your state are " +Conservative+ " Conservative, " +Moderate+ " Moderate, " +Liberal+ " Liberal, and " +DoNotKnow+ " Do Not Know ";


     
     });
     
      }

      if(cityName[2].includes("WI")){
 
         fetch('https://retoolapi.dev/ClBIjw/statedata/49')
         .then(response=>{
            return response.json();
     
         }).then(json=>{
     
            var data = json;

            var { Conservative, Moderate, Liberal, DoNotKnow } = data;

            document.getElementById('polistats').innerHTML= "The users in your state are " +Conservative+ " Conservative, " +Moderate+ " Moderate, " +Liberal+ " Liberal, and " +DoNotKnow+ " Do Not Know ";


     
     });
     
      }

      if(cityName[2].includes("WY")){
 
         fetch('https://retoolapi.dev/ClBIjw/statedata/50')
         .then(response=>{
            return response.json();
     
         }).then(json=>{
     
            var data = json;

            var { Conservative, Moderate, Liberal, DoNotKnow } = data;

            document.getElementById('polistats').innerHTML= "The users in your state are " +Conservative+ " Conservative, " +Moderate+ " Moderate, " +Liberal+ " Liberal, and " +DoNotKnow+ " Do Not Know ";


     
     });
     
      }
  
    });
 
 };




