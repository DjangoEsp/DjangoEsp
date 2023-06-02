function Reloj() {
    var date = new Date();
    var options = {
        weekday: "long",
        year: "numeric",
        month: "long",
        day: "numeric",
        hour: "numeric",
        minute: "numeric",
        second: "numeric",
    };
    return date.toLocaleDateString("es-gt", options);
}

function ActualizarTiempo() {
    var currentDateElement = document.getElementById("currentDate");
    if (currentDateElement) {
        currentDateElement.innerHTML = Reloj();
    }
}

// Se actualiza cada segundo
setInterval(ActualizarTiempo, 1000);