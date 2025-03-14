$("#filterForm").on("submit", function (filter) {
    filter.preventDefault(); // Evitar envío tradicional

    // Recopilar los checkboxes manualmente
    let checkboxes = [];
    $(".form-check-input:checked").each(function () {
        checkboxes.push($(this).val());
    });

    // Recopilar los otros datos del formulario
    let formData = $(this).serializeArray(); 

    // Agregar los checkboxes seleccionados al formData
    formData.push({ name: "eventTypes", value: checkboxes });

    // Convertir a formato adecuado para AJAX
    let queryString = $.param(formData);

    // Hacer la petición AJAX
    $.ajax({
        url: "/api/events/filter",
        type: "GET",
        data: queryString,
        success: function (response) {
            $("#eventResults").empty();

            if (response.length === 0) {
                $("#eventResults").html('<div class="col-12"><div class="alert alert-info">No se encontraron eventos con los filtros seleccionados.</div></div>');
                return;
            }

            $.each(response, function (index, event) {
                var eventCard = `
                    <div class="col-md-4 mb-4">
                        <div class="card h-100">
                        <img src="${event.image}" class="card-img-top" alt="${event.name}">
                        <div class="card-body">
                            <h5 class="card-title">${event.name}</h5>
                            <p class="card-text">${event.description}</p>
                            <p class="card-text">
                            <small class="text-muted">
                                <i class="fa-solid fa-calendar-days"></i> ${event.date}
                                <br>
                                <i class="fa-solid fa-money-bill"></i> $${event.budget} MXN
                            </small>
                            </p>
                        </div>
                        <div class="card-footer d-flex justify-content-end">
                            <a href="/event/${event.id}" class="btn btn-warning">Ver detalles</a>
                        </div>
                        </div>
                    </div>
                `;

                $("#eventResults").append(eventCard);
            });
        },
        error: function (error) {
            console.error("Error al filtrar eventos:", error);
            $("#eventResults").html('<div class="col-12"><div class="alert alert-danger">Ocurrió un error al buscar eventos. Por favor, intenta nuevamente.</div></div>');
        },
    });
});
