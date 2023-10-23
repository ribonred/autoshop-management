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
    Alpine.data('AlpineData', () => ({
        entityFormLoading: false,
        instrumentModal: false,
        propertiesModal: false,
        successToast: false,
        errorToast: false,
        propertiesData: {},
        resetEntityData() {
            this.entityData = {
                code: '',
                name: '',
                instrument: '',
                properties: {}
            }
        },
        entityResult: {
            name: null,
            id: null
        },
        transactionFormData: {
            entity_name: '',
            entity: '',
            amount_display: '',
            amount: '',
        },
        entityData: {
            code: '',
            name: '',
            instrument: null,
        },
        instrumentData: {
            name: ''
        },
        formData: {
            labelProp: '',
            valueProp: ''
        },
        clearTransactionFormData() {
            this.transactionFormData = {
                entity_name: '',
                entity: '',
                amount_display: '',
                amount: '',
            }
        },
        formatRupiah(value) {
            const formatter = new Intl.NumberFormat('id-ID', {
                style: 'currency',
                currency: 'IDR',
                minimumFractionDigits: 2
            });
            const display = formatter.format(value)
            this.transactionFormData.amount = value
            if (value) {
                this.transactionFormData.amount_display = display
            } else {
                this.transactionFormData.amount_display = ''
            }
        },
        getPropContainer() {
            return document.getElementById('entity-prop-container')
        },
        clearPropContainer() {
            const entityPropContainer = this.getPropContainer()
            entityPropContainer.innerHTML = ''
        },
        clearEntityResult() {
            this.entityResult.name = null
            this.entityResult.id = null
        },
        selectedEntity() {
            this.transactionFormData.entity_name = this.entityResult.name
            this.transactionFormData.entity = this.entityResult.id
            this.clearEntityResult()
        },
        async submitTransaction(url, csrftoken) {
            payload = {
                entity: this.transactionFormData.entity,
                amount: this.transactionFormData.amount,
                trx_type: this.transactionFormData.trx_type,
                trx_category: this.transactionFormData.trx_category,
                trx_date: this.transactionFormData.trx_date,
                description: this.transactionFormData.description,
            }
            const response = await fetch(url, {
                method: 'POST',
                body: JSON.stringify(payload),
                headers: {
                    "Content-type": "application/json",
                    "X-CSRFToken": csrftoken
                }
            })
            if (response.ok) {
                this.successToast = true
                setTimeout(() => {
                    this.successToast = false
                }, 2000);
            } else {
                this.errorToast = true
                setTimeout(() => {
                    this.errorToast = false
                }, 2000);
            }
            this.clearTransactionFormData()

        },
        async handleKey(e, url) {
            if (e.target.value.length >= 2) {

                const response = await fetch(`${url}?search=${e.target.value}`, {
                    method: 'GET',
                    headers: {
                        "Accept": "application/json",
                        "Content-type": "application/json",
                    }
                })
                if (response.ok) {
                    const data = await response.json()
                    if (data.entities.length > 0) {
                        entityData = data.entities[0]
                        this.entityResult.name = entityData.name
                        this.entityResult.id = entityData.id
                    } else {
                        this.clearEntityResult()
                    }
                }

            } else {
                this.clearEntityResult()
            }
        }, async submitInstrument(url, csrftoken) {
            this.instrumentFormLoading = true
            const response = await fetch(url, {
                method: 'POST',
                body: JSON.stringify(this.instrumentData),
                headers: {
                    "Content-type": "application/json",
                    "X-CSRFToken": csrftoken
                }
            })
            setTimeout(() => {
                this.instrumentFormLoading = false
                if (response.ok) {
                    this.successToast = true
                    setTimeout(() => {
                        this.successToast = false
                    }, 2000);
                } else {
                    this.errorToast = true
                    setTimeout(() => {
                        this.errorToast = false
                    }, 2000);
                }
            }, 1000);
            this.instrumentData.name = ''
        },
        async submitEntity(url, csrftoken) {
            this.entityFormLoading = true
            this.getProperties()
            this.entityData['properties'] = this.propertiesData
            const response = await fetch(url, {
                method: 'POST',
                body: JSON.stringify(this.entityData),
                headers: {
                    "Content-type": "application/json",
                    "X-CSRFToken": csrftoken
                }
            })
            setTimeout(() => {
                this.entityFormLoading = false
                if (response.ok) {
                    this.successToast = true
                    setTimeout(() => {
                        this.successToast = false
                    }, 2000);
                } else {
                    this.errorToast = true
                    setTimeout(() => {
                        this.errorToast = false
                    }, 2000);
                }
            }, 1000);

            this.resetEntityData()
            this.clearPropContainer()

        },
        getProperties() {
            const entityPropContainer = this.getPropContainer()
            for (let i = 0; i < entityPropContainer.children.length; i++) {
                const element = entityPropContainer.children[i];
                const label = element.querySelector('label').innerText
                const value = element.querySelector('input').value
                this.propertiesData[label] = value
            }
        },
        propertiesAdd() {
            // "labelProp" "valueProp"
            var removeButton = document.createElement('button');
            removeButton.className = 'absolute right-0 top-0 shadow bg-gray-500- hover:bg-gray-700  focus:shadow-outline focus:outline-none text-white font-bold py-2 px-4 rounded';
            removeButton.innerHTML = '<span style="color: red;">X</span>';
            const labelProp = this.formData['labelProp']
            const valueProp = this.formData['valueProp']
            const template = `<div class="md:flex md:items-center mb-6">
            <div class="md:w-1/3">
                <label class="block text-gray-500 font-bold md:text-right mb-1 md:mb-0 pr-4" for="${valueProp}">
                    ${labelProp}
                </label>
            </div>
            <div class="relative md:w-2/3" id="parent-${labelProp}">
                <input class="bg-gray-200 
                appearance-none border-2 
                border-gray-200 rounded 
                w-full py-2 px-4 text-gray-700 
                leading-tight focus:outline-none 
                focus:bg-white focus:border-purple-500" id="${valueProp}" type="text" value=${valueProp} disabled>
            </div>
            </div>`
            var tempDiv = document.createElement('div');
            tempDiv.innerHTML = template;
            tempDiv.querySelector(`#parent-${labelProp}`).appendChild(removeButton);
            const entityPropContainer = this.getPropContainer()
            entityPropContainer.appendChild(tempDiv)
            removeButton.addEventListener('click', function () {
                entityPropContainer.removeChild(tempDiv);
            });
            this.formData['labelProp'] = ''
            this.formData['valueProp'] = ''
            this.propertiesModalToggle()
        },
        instrumentModalToggle(e) {
            this.instrumentModal = !this.instrumentModal

        },
        propertiesModalToggle(e) {
            this.propertiesModal = !this.propertiesModal

        },

    }))
})


