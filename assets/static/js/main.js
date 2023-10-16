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
        source: function(request, response) {
            if (request.term.startsWith("@")) {
                var term = request.term.slice(1).toLowerCase();
                var suggestions = availableTags.filter(tag => tag.toLowerCase().startsWith(term));
                response(suggestions);
            } else {
                response([]);
            }
        }
    });
}

