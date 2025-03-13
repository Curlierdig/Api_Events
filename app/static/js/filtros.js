$(function () {
	// Manejar el envío del formulario
	$("#filterForm").on("submit", function (filter) {
		filter.preventDefault(); // Evitar que el formulario se envíe de forma tradicional

		// Recopilar los datos del formulario
		var formData = $(this).serialize();

		// Realizar la solicitud AJAX a tu endpoint
		$.ajax({
			url: "/api/events/filter", // Ajusta esta ruta según tu configuración
			type: "GET",
			data: formData,
			success: function (response) {
				// Limpiar los resultados
				$("#eventResults").empty();

				// Si no hay eventos, mostrar mensaje
				if (response.length === 0) {
					$("#eventResults").html('<div class="col-12"><div class="alert alert-info">No se encontraron eventos con los filtros seleccionados.</div></div>');
					return;
				}

				// Recorrer la lista de eventos y mostrarlos
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
});