/**
 * Created by erlan on 5/10/17.
 */

var map = null;
var markers = [];
var haightAshbury = {lat: 55.750549, lng: 37.617939};

function initMap() {
    map = new google.maps.Map(document.getElementById('choose-mark'), {
        center: haightAshbury,
        zoom: 15,
        mapTypeId: google.maps.MapTypeId.TERRAIN
    });

    if(ad_location != null) {
        var ad_map = new google.maps.Map(document.getElementById('map_canvas'), {
            center: ad_location,
            zoom: 15,
            mapTypeId: google.maps.MapTypeId.TERRAIN
        });
        addAdMarker(ad_location, ad_map);
    }

    map.addListener('click', function (event) {
        addMarker(event.latLng);
    });

    // Adds a marker at the center of the map.
}

function addAdMarker(location, map) {
    var marker = new google.maps.Marker({
        position: location,
        map: map
    });
    markers.push(marker);
}

function addMarker(location) {
    var marker = new google.maps.Marker({
        position: location,
        map: map
    });
    var markerString = {
        lat: marker.position.lat(),
        lng: marker.position.lng(),
        zoom: map.zoom
    };
    var input = $('#id_location');
    $(input).val(JSON.stringify(markerString));
    deleteMarkers();
    markers.push(marker);
    console.log($(input).val());
}

// Sets the map on all markers in the array.
function setMapOnAll(map) {
    for (var i = 0; i < markers.length; i++) {
        markers[i].setMap(map);
    }
}

// Removes the markers from the map, but keeps them in the array.
function clearMarkers() {
    setMapOnAll(null);
}

// Shows any markers currently in the array.
function showMarkers() {
    setMapOnAll(map);
}

// Deletes all markers in the array by removing references to them.
function deleteMarkers() {
    clearMarkers();
    markers = [];
}