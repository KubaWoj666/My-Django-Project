console.log("opa")

const input = document.getElementById("id_image")
const image_box = document.getElementById("image_box")

input.addEventListener("change", ()=>{
    const image_data = input.files[0]
    const url = URL.createObjectURL(image_data)
    image_box.innerHTML = `<img id="image" src="${url}" class="card-img-top" alt="...">`
})



const category_form = document.getElementById("category_form");
const category_input = document.getElementById("category_name");
const main_category_input = document.getElementById("main_cat_name");

const csrf = category_form.querySelector("[name='csrfmiddlewaretoken']")
console.log(category_form.elements)
var categoryUrl = "{% url 'get-categories' %}";

console.log(categoryUrl)

const select = document.getElementById("id_category")
console.log(category_input.length)



document.getElementById('save_btn').addEventListener('click', function() {
    // Close Modal
    $('#exampleModal').modal('hide');
});

const url = "http://127.0.0.1:8000/add-category"

category_form.addEventListener("submit", e=>{
    e.preventDefault()

    const fd = new FormData()
    fd.append("csrfmiddlewaretoken", csrf.value)
    fd.append("category_name", category_input.value)
    fd.append("main_cat_name", main_category_input.value)

    $.ajax({
        type: "POST",
        url: url,
        data: fd,
        success: function(response){
            console.log(response)
            // select.innerHTML += `<option value="1">${response.category_name}</option>`
            fetchCategoriesAndUpdateDropdown();
        },
        error: function(error){
            console.log(error)
        },
        cache: false,
        contentType: false,
        processData: false,
    })
})



function fetchCategoriesAndUpdateDropdown() {
    // Make an AJAX call to fetch categories
    $.ajax({
        type: "GET",
        url: "http://127.0.0.1:8000/get-categories",  
        success: function(categories) {
            // Update the dropdown list with the fetched categories
            updateDropdownList(categories);
        },
        error: function(error) {
            console.log(error);
        },
    });
}


function updateDropdownList(categories) {
    const select = document.getElementById("id_category");
    select.innerHTML = "";  // Clear existing options

    // Add options for each category
    categories.forEach(category => {
        const option = document.createElement("option");
        option.value = category.id;
        option.text = `${category.main_cat_name__main_name} - ${category.category_name}`
        // option.text = category.category_name;
        // option.text = category.main_cat_name
        select.appendChild(option);
    });
}


