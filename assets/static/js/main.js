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

    $("#search-input").autocomplete({
        source: availableTags
    });
}

