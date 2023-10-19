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
        source: function (request, response) {
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
// alpine js
document.addEventListener("alpine:init", function () {
    Alpine.data('modal', () => ({
        instrumentModal: false,
        propertiesModal: false,

        instrumentModalToggle(e) {
            this.instrumentModal = !this.instrumentModal

        },
        propertiesModalToggle(e) {
            this.propertiesModal = !this.propertiesModal

        },
        propertiesAdd(formdata){
            // "labelProp" "valueProp"
            var removeButton = document.createElement('button');
            removeButton.className = 'shadow bg-red-500 hover:bg-red-400 focus:shadow-outline focus:outline-none text-white font-bold py-2 px-4 rounded';
            removeButton.innerHTML = '<span style="color: red;">X</span>';
            removeButton.addEventListener('click', function() {
                propertiesContainer.removeChild(label);
                propertiesContainer.removeChild(input);
                propertiesContainer.removeChild(removeButton);
            });

            const template = `<div class="md:flex md:items-center mb-6" id="parent-${formdata.labelProp}">
            <div class="md:w-1/3">
                <label class="block text-gray-500 font-bold md:text-right mb-1 md:mb-0 pr-4" for="${formdata.valueProp}">
                    ${formdata.labelProp}
                </label>
            </div>
            <div class="md:w-2/3">
                <input class="bg-gray-200 
                appearance-none border-2 
                border-gray-200 rounded 
                w-full py-2 px-4 text-gray-700 
                leading-tight focus:outline-none 
                focus:bg-white focus:border-purple-500" id="${formdata.valueProp}" type="text" value=${formdata.valueProp} disabled>
            </div>
            </div>`
            var tempDiv = document.createElement('div');
            tempDiv.innerHTML = template;
            tempDiv.querySelector(`#parent-${formdata.labelProp}`).appendChild(removeButton);
           const entityPropContainer = document.getElementById('entity-prop-container')
            entityPropContainer.appendChild(tempDiv)
            this.propertiesModal = false
           console.log(this.valueProp)
           console.log(this.labelProp)
        }
    }))
})

const addProperty = (e) => {
    e.preventDefault()
    `<div class="md:flex md:items-center mb-6">
                <div class="md:w-1/3">
                    <label class="block text-gray-500 font-bold md:text-right mb-1 md:mb-0 pr-4" for="name">
                        nanana
                    </label>
                </div>
                <div class="md:w-2/3">
                    <input class="bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-purple-500" id="name" type="text" placeholder="Name">
                </div>
    </div>`
    console.log(e)
}


