
const calculator_fom = document.getElementById("calculator-form")
const csrf = calculator_fom.querySelector("[name='csrfmiddlewaretoken']")
const weight =  document.getElementById("id_weight")
const grade = document.getElementById("grade")
const pricing = document.getElementById("pricing")

console.log(weight.value)

const url = "http://127.0.0.1:8000/shop/calculate-price"

calculator_fom.addEventListener("submit", e=>{
    e.preventDefault()

    const fd = new FormData()
    fd.append("csrfmiddlewaretoken", csrf.value)
    fd.append("weight", weight.value)
    fd.append("grade", grade.value)


    $.ajax({
        type: "POST",
        url: url,
        data: fd,

        success: function(response){
            pricing.innerHTML =`<p id="pricing"> wycna: ${response.metal_pricing}zł </p>`
        },

        error: function(response){
            console.log(response)
        },
        cache: false,
        contentType: false,
        processData: false,

    })
})

