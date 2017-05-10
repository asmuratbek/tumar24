/**
 * Created by erlan on 5/10/17.
 */
var map = null;
var markers = [];
function initMap() {
    map = new google.maps.Map(document.getElementById('map_canvas'), {
        center: haightAshbury,
        zoom: 13,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    });
    addMarker(haightAshbury);
}
function addMarker(location) {
    var marker = new google.maps.Marker({
        position: new google.maps.LatLng(location.lat,location.lng),
        map: map
    });
}