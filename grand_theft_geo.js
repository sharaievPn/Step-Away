function anotherPage(){
    window.location.replace("./map")
}

function success(position){
    const crd = position.coords;
    var lat = crd.latitude;
    var lng = crd.longitude;
    console.log(`Latitude : ${lat}`);
    console.log(`Longitude : ${lng}`);
    fetch("/", {
        method:'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({'latitude': lat, 'longitude': lng})
    })
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(error => console.log(error))
        .then(anotherPage)
}

function error(err) {
    alert('We could not get your geolocation')
    console.warn(`ERROR(${err.code}): ${err.message}`);
    window.location.replace("./")
}

function grabLocation(){
    if (navigator.geolocation){
        navigator.geolocation.getCurrentPosition(success, error, {
            enableHighAccuracy: true,
            timeout: 5000,
            maximumAge: 0
        });
    } else {
        alert('Your browser does not support geolocation \n Or it is just turned off')
        window.location.replace("./")
    }
}