window.onload = function () {
    document.body.addEventListener('htmx:configRequest', (event) => {
        event.detail.headers['X-CSRFToken'] = '{{ csrf_token }}';
    })

    var availableTags = [
        "ActionScript",
        "AppleScript",
        "Asp",
        // Add more tags as needed
    ];

    $("#search-input").on('keyup', function() {
        if (this.value.includes("@")) {
            console.log("email");
            $(this).autocomplete({
                source: availableTags
            });
        } else {
            $(this).autocomplete({
                source: []
            });
        }
    });
}

