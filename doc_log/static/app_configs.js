var map_options = {
    center: new google.maps.LatLng(-2.548926, 118.0148634),
    zoom: 4,
    mapTypeId: google.maps.MapTypeId.ROADMAP
};

var map = new google.maps.Map(document.getElementById("map_canvas"), map_options);

var input = document.getElementById("keyword");
var autocomplete = new google.maps.places.Autocomplete(input);
autocomplete.bindTo("bounds", map);

var marker = new google.maps.Marker({
    map: map,
    zoom: 14,
    animation: google.maps.Animation.BOUNCE
});

google.maps.event.addListener(autocomplete, "place_changed", function () {
    var place = autocomplete.getPlace();

    if (place.geometry.viewport) {
        map.fitBounds(place.geometry.viewport);
    } else {
        map.setCenter(place.geometry.location);
        map.setZoom(15);
    }

    marker.setPosition(place.geometry.location);
});

google.maps.event.addListener(map, "click", function (event) {
    marker.setPosition(event.latLng);
});