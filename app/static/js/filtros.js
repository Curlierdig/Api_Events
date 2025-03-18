$(function () {
    // Manejar el envío del formulario
    $("#filterForm").on("submit", function (e) {
        e.preventDefault();
        
        // Recoger datos del formulario correctamente
        const formData = {
            fechaInicio: $("#fechaInicio").val(),
            fechaFin: $("#fechaFin").val(),
            presupuesto: $("#presupuesto").val(),
            tipo: $("input[name='tipo']:checked").map(function() {
                return $(this).val();
            }).get()
        };

        // Limpiar parámetros vacíos
        const cleanParams = Object.fromEntries(
            Object.entries(formData).filter(([_, v]) => v !== '' && v !== null && v.length !== 0)
        );

        $.ajax({
            url: "/api/events/filter",
            type: "GET",
            data: cleanParams,
            beforeSend: function() {
                $("#eventosCarousel").addClass("loading");
            },
            success: function (response) {
                updateCarousel(response);
            },
            error: function (xhr) {
                handleAjaxError(xhr);
            },
            complete: function() {
                $("#eventosCarousel").removeClass("loading");
            }
        });
    });

    // Función para actualizar el carrusel
    function updateCarousel(events) {
        const carouselInner = $("#eventosCarousel .carousel-inner");
        carouselInner.empty();

        if (events.length === 0) {
            carouselInner.html(noEventsTemplate());
            resetCarouselIndicators(0);
            return;
        }

        const totalGroups = Math.ceil(events.length / 3);
        const carouselItems = events.reduce((acc, event, index) => {
            if (index % 3 === 0) {
                acc.push({
                    active: index === 0,
                    events: [event]
                });
            } else {
                acc[acc.length - 1].events.push(event);
            }
            return acc;
        }, []);

        carouselInner.html(carouselItems.map(createCarouselItem).join(''));
        resetCarouselIndicators(totalGroups);
        initializeCarousel();
    }

    // Plantilla para cuando no hay eventos
    function noEventsTemplate() {
        return `
            <div class="carousel-item active">
                <div class="row">
                    <div class="col-12">
                        <div class="alert alert-info text-center shadow-sm">
                            No se encontraron eventos que coincidan con los filtros.
                        </div>
                    </div>
                </div>
            </div>`;
    }

    // Crear item del carrusel
    function createCarouselItem(group, index) {
        return `
            <div class="carousel-item ${group.active ? 'active' : ''}">
                <div class="row g-4">
                    ${group.events.map(event => createEventCard(event)).join('')}
                </div>
            </div>`;
    }

    // Función para crear tarjeta de evento
    function createEventCard(event) {
        const safeData = {
            name: event.name || 'Evento sin nombre',
            description: event.description || 'Descripción no disponible',
            date: formatEventDate(event.date),
            budget: event.budget ? `$${event.budget} MXN` : 'Gratis',
            image: event.image || 'default.jpg',
            type: event.type?.name || 'General',
            address: event.location?.address ? 
                truncateText(event.location.address, 20) : 'Ubicación no especificada',
            time: event.time || '--:--',
            id: event.id || '#'
        };

        return `
            <div class="col-md-4">
                <div class="card h-100 border-0 shadow-lg rounded-3">
                    <div class="position-relative">
                        <img class="card-img-top rounded-top" 
                             src="/static/img/events/${safeData.image}" 
                             alt="${safeData.name}" 
                             style="height: 220px; object-fit: cover">
                        <span class="position-absolute top-0 end-0 m-2 badge rounded-pill fs-6" 
                              style="background-color: #5e35b1; color: white">
                            ${safeData.type}
                        </span>
                    </div>
                    <div class="card-body d-flex flex-column p-3">
                        <h4 class="card-title h5 fw-bold text-dark mb-2">${safeData.name}</h4>
                        <p class="card-text text-secondary small flex-grow-1">${safeData.description}</p>
                        
                        <div class="mt-auto pt-3">
                            <div class="d-flex flex-wrap gap-2 mb-3">
                                <span class="badge rounded-pill" style="background-color: #00796b; color: white">
                                    <i class="fa-solid fa-calendar-days me-1"></i>
                                    ${safeData.date}
                                </span>
                                <span class="badge rounded-pill" style="background-color: #e65100; color: white">
                                    <i class="fa-solid fa-money-bill me-1"></i>
                                    ${safeData.budget}
                                </span>
                            </div>
                            
                            <div class="d-flex justify-content-between align-items-center text-muted small">
                                <span>
                                    <i class="fas fa-map-marker-alt me-1"></i>${safeData.address}
                                </span>
                                <span>
                                    <i class="fas fa-clock me-1"></i>${safeData.time}
                                </span>
                            </div>
                        </div>
                    </div>
                    <div class="card-footer bg-white border-0 py-3 text-center">
                        <a href="/event/${safeData.id}" 
                           class="btn text-white" 
                           style="background-color: #5e35b1">
                            Ver detalles
                        </a>
                    </div>
                </div>
            </div>`;
    }

    // Formatear fecha
    function formatEventDate(dateString) {
        try {
            if (!dateString) return "Fecha no disponible";
            const dateObj = new Date(dateString);
            if (isNaN(dateObj)) return "Fecha inválida";
            return dateObj.toLocaleDateString('es-ES', { 
                day: 'numeric', 
                month: 'short', 
                year: 'numeric' 
            });
        } catch (e) {
            console.error("Error formatting date:", e);
            return "Fecha no disponible";
        }
    }

    // Acortar texto
    function truncateText(text, maxLength) {
        return text.length > maxLength ? 
            `${text.substring(0, maxLength)}...` : text;
    }

    // Reiniciar indicadores
    function resetCarouselIndicators(totalGroups) {
        const indicators = $('.carousel-indicators');
        indicators.empty().toggle(totalGroups > 0);
        
        if (totalGroups === 0) return;
        
        indicators.append(Array.from({length: totalGroups}, (_, i) => `
            <button type="button" 
                    data-bs-target="#eventosCarousel" 
                    data-bs-slide-to="${i}"
                    class="${i === 0 ? 'active' : ''} bg-white"
                    style="width: 10px; height: 10px; border-radius: 50%; opacity: 0.8;">
            </button>
        `).join(''));
    }

    // Inicializar/reiniciar carrusel
    function initializeCarousel() {
        const carousel = $('#eventosCarousel');
        carousel.carousel('dispose').carousel({
            interval: 5000,
            wrap: true
        });
    }

    // Manejar errores AJAX
    function handleAjaxError(xhr) {
        console.error("Error:", xhr.responseJSON?.error || "Error desconocido");
        const errorMsg = xhr.status === 0 ? 
            "Error de conexión" : 
            "Ha ocurrido un error. Por favor, intenta de nuevo.";
        
        $("#eventosCarousel .carousel-inner").html(`
            <div class="carousel-item active">
                <div class="row">
                    <div class="col-12">
                        <div class="alert alert-danger shadow-sm">${errorMsg}</div>
                    </div>
                </div>
            </div>
        `);
        resetCarouselIndicators(0);
    }
});