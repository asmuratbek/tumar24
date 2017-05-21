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

    var input = /** @type {HTMLInputElement} */(
      document.getElementById('pac-input'));

    // Create the autocomplete helper, and associate it with
    // an HTML text input box.
    var autocomplete = new google.maps.places.Autocomplete(input);
    autocomplete.bindTo('bounds', map);

    map.controls[google.maps.ControlPosition.TOP_LEFT].push(input);
    var infowindow = new google.maps.InfoWindow();
    var marker = new google.maps.Marker({
      map: map,
      anchorPoint: new google.maps.Point(0, -29)
    });
    autocomplete.addListener('place_changed', function() {
        infowindow.close();
        marker.setVisible(false);
        var place = autocomplete.getPlace();
        if (!place.geometry) {
            // User entered the name of a Place that was not suggested and
            // pressed the Enter key, or the Place Details request failed.
            window.alert("No details available for input: '" + place.name + "'");
            return;
        }

        // If the place has a geometry, then present it on a map.
        if (place.geometry.viewport) {
            map.fitBounds(place.geometry.viewport);
        } else {
            map.setCenter(place.geometry.location);
            map.setZoom(17);  // Why 17? Because it looks good.
        }
        marker.setIcon(/** @type {google.maps.Icon} */({
            url: place.icon,
            size: new google.maps.Size(71, 71),
            origin: new google.maps.Point(0, 0),
            anchor: new google.maps.Point(17, 34),
            scaledSize: new google.maps.Size(35, 35)
        }));
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