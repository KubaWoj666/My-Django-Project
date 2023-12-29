console.log("opa")

const input = document.getElementById("id_image")
const image_box = document.getElementById("image_box")
const csrf = document.getElementsByName("csrfmiddelwaretoken")

input.addEventListener("change", ()=>{
    const image_data = input.files[0]
    const url = URL.createObjectURL(image_data)
    image_box.innerHTML = `<img id="image" src="${url}" class="card-img-top" alt="...">`
})
