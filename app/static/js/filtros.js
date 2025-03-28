$(function () {
    // Función para manejar el envío del formulario
    $("#filterForm").on("submit", function (e) {
        e.preventDefault();

        /* // Procesar el rango de fechas
        var dateRange = $('#daterange').val();
        var startDate = $('#startDate').val();
        var endDate = $('#endDate').val(); */


        // Recoger todos los parámetros del formulario
        /* var formData = {
            start_date: startDate,
            end_date: endDate,
            type_id: $('input[name="tipo"]:checked').map(function() {
                return this.value;
            }).get(),
            budget: $('#presupuesto').val() || null
        }; */

        var formData = $(this).serialize();

        // Limpiar parámetros vacíos
        /* var cleanParams = {};
        Object.keys(formData).forEach(function(key) {
            cleanParams[key] = formData[key];
        }); */

        // Realizar la petición AJAX
        $.ajax({
            url: "/api/events/filter",
            type: "GET",
            data: formData,
            success: function(response) {
                handleFilterResponse(response);
            },
            error: function(error) {
                console.error("Error al filtrar eventos:", error);
                $("#eventResults").html(
                    '<div class="col-12">'+
                    '<div class="alert alert-danger text-center">Error al buscar eventos. Intenta nuevamente.</div>'+
                    '</div>'
                );
                scrollToResults();
            }
        });
    });

    // Función para manejar la respuesta exitosa
    function handleFilterResponse(events) {
        $(".carousel-inner .carousel-item .row").empty();

        if (events.length === 0) {
            $(".carousel-inner .carousel-item .row").html(
                '<div class="col-12">'+
                '<div class="alert alert-info text-center">No se encontraron eventos con los filtros seleccionados</div>'+
                '</div>'
            );
            scrollToResults();
            return;
        }

        // Generar tarjetas de eventos
        events.forEach(function(event) {
            var eventCard = `
                <div class="col-12 col-md-6 col-lg-4 mb-4">
                    <div class="card h-100 shadow-sm">
                        <div class="position-relative">
                            <img class="card-img-top" src="/static/img/events/${event.image}" alt="${event.name}" style="min-height: 280px; object-fit: cover;">
                            <span class="position-absolute top-0 end-0 m-2 px-2 py-1 rounded-pill fs-6" style="background-color: #19c6db; color: #324b4f;">
                                ${event.type.name}
                            </span>
                        </div>
                        <div class="card-body d-flex flex-column">
                            <div class="d-flex flex-wrap justify-content-between align-items-center mb-2">
                                <span class="px-2 py-1 rounded-2 mb-1" style="background-color: #005c83; color: white;">
                                    <i class="fa-solid fa-calendar-days me-1"></i>
                                    ${event.date}
                                </span>
                                <span class="px-2 py-1 rounded-3 fw-bold" style="background-color: #348774; color: white;">
                                    <i class="fa-solid fa-money-bill me-2"></i>
                                    $${event.budget} MXN
                                </span>
                            </div>
                            <h3 class="card-title h5 fw-bold">${event.name}</h3>
                            <p class="card-text text-muted mb-3">
                                <i class="fas fa-map-marker-alt me-1"></i>
                                ${event.location.address}
                            </p>
                            <p class="card-text">${event.description}</p>
                            <div class="d-flex justify-content-between mt-auto">
                                <span class="text-muted">
                                    <i class="fas fa-clock me-1"></i>
                                    ${event.time}
                                </span>
                                <a href="/event/${event.id}" class="btn btn-sm" style="border-color: #005c83; color: #005c83;">
                                    Ver detalles
                                </a>
                            </div>
                        </div>
                    </div>
                </div>`;
            
            $(".carousel-inner .carousel-item .row").append(eventCard);
        });

        scrollToResults();
    }

    // Función para formatear fechas
    function formatEventDate(dateString) {
        try {
            if (!dateString) return "Fecha no disponible";
            const options = { 
                weekday: 'short', 
                year: 'numeric', 
                month: 'short', 
                day: 'numeric' 
            };
            return new Date(dateString).toLocaleDateString('es-MX', options);
        } catch (e) {
            console.error("Error formateando fecha:", e);
            return "Fecha inválida";
        }
    }

    // Función para scroll a los resultados
    function scrollToResults() {
        $('html, body').animate({
            scrollTop: $("#eventResults").offset().top - 100
        }, 500);
    }

    // Reset del formulario
    $("#filterForm").on("reset", function() {
        setTimeout(function() {
            $("#eventResults").empty();
            scrollToResults();
        }, 100);
    });
});