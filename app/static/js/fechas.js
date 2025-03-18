$(function () {
	// Fecha actual para mínimo
	var hoy = moment();

	// Fecha máxima (último día de 2025)
	var fechaMaxima = moment("2025-12-31");

	// Inicializar el daterangepicker
	$("#daterange").daterangepicker(
		{
			opens: "left",
			startDate: hoy,
			endDate: moment().add(7, "days"),
			minDate: hoy, // Restringir fechas anteriores a hoy
			maxDate: fechaMaxima, // Restringir fechas posteriores a 2025
			ranges: {
				Hoy: [moment(), moment()],
				Mañana: [moment().add(1, "days"), moment().add(1, "days")],
				"Próximos 7 días": [moment(), moment().add(6, "days")],
				"Próximos 30 días": [moment(), moment().add(29, "days")],
				"Este mes": [moment().startOf("month"), moment().endOf("month")],
				"Próximo mes": [moment().add(1, "month").startOf("month"), moment().add(1, "month").endOf("month")],
			},
		},
		function (start, end, label) {
			// Cuando el usuario seleccione fechas, actualizar los campos hidden
			$("#fechaInicio").val(start.format("YYYY-MM-DD"));
			$("#fechaFin").val(end.format("YYYY-MM-DD"));
		}
	);

	// Establecer valores iniciales para los campos ocultos
	$("#fechaInicio").val(moment().format("YYYY-MM-DD"));
	$("#fechaFin").val(moment().add(7, "days").format("YYYY-MM-DD"));
});