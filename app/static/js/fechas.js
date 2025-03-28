$(function () {
	/* Function to set the date range picker plugin */
	// Actual date
	var hoy = moment();

	// Maximum date
	var fechaMaxima = moment("2025-12-31");

	// Initializer
	$("#daterange").daterangepicker(
		{
			opens: "left",
			startDate: hoy,
			endDate: moment().add(7, "days"),
			minDate: hoy,
			maxDate: fechaMaxima,
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
			// When the user selects dates it will update the hidden fields 
			$("#startDate").val(start.format("YYYY-MM-DD"));
			$("#endDate").val(end.format("YYYY-MM-DD"));
		}
	);

	// Establish initial values for hidden fields
	$("#startDate").val(moment().format("YYYY-MM-DD"));
	$("#endDate").val(moment().add(7, "days").format("YYYY-MM-DD"));
});