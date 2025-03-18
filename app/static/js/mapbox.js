document.addEventListener("DOMContentLoaded", function () {
    const mapboxToken = document.getElementById("mapbox-token").getAttribute("data-token");
    mapboxgl.accessToken = mapboxToken;
});