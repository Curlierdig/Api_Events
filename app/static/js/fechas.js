$(document).ready(function () {
    console.log("Daterangepicker versión:", typeof $.fn.daterangepicker); // Verifica si está cargado

    if (typeof $.fn.daterangepicker === "undefined") {
        console.error("Error: daterangepicker no está definido.");
        return;
    }

    // Inicializar el daterangepicker
    $("#daterange").daterangepicker({
        opens: "left",
        startDate: moment(),
        endDate: moment().add(7, "days"),
        minDate: moment(), // Restringir fechas anteriores a hoy
        maxDate: moment("2025-12-31"),
        ranges: {
            Hoy: [moment(), moment()],
            Mañana: [moment().add(1, "days"), moment().add(1, "days")],
            "Próximos 7 días": [moment(), moment().add(6, "days")],
            "Próximos 30 días": [moment(), moment().add(29, "days")],
            "Este mes": [moment().startOf("month"), moment().endOf("month")],
            "Próximo mes": [moment().add(1, "month").startOf("month"), moment().add(1, "month").endOf("month")],
        }
    }, function (start, end) {
        $("#fechaInicio").val(start.format("YYYY-MM-DD"));
        $("#fechaFin").val(end.format("YYYY-MM-DD"));
    });

    console.log("Daterangepicker inicializado correctamente.");
});
