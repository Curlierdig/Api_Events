document.addEventListener("DOMContentLoaded", function () {
    const mapboxToken = document.getElementById("mapbox-token").dataset.token;
    
    // Verificar si el token existe
    if (!mapboxToken) {
        console.error("Mapbox token no encontrado");
        return;
    }

    // Inicializar el mapa
    const map = new mapboxgl.Map({
        container: 'map', // ID del contenedor HTML
        style: 'mapbox://styles/mapbox/streets-v12', // Estilo del mapa
        center: [-106.0691, 28.6353], // Coordenadas de Chihuahua
        zoom: 12 // Nivel de zoom inicial
    });

    // Añadir controles de navegación
    map.addControl(new mapboxgl.NavigationControl());
});