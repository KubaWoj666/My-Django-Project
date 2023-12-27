console.log("opa")

const counterDiv = document.querySelector(".counter")
const checkboxes = document.querySelectorAll("#checkbox")




let count = checkboxes.length
console.log(count)

counterDiv.innerHTML+=`<h1>${count}</h1>`

checkboxes.forEach((checkbox) => checkbox.addEventListener('change', function(){
    if (checkbox.checked){
        console.log("chekd")
        count --
    }else{
        console.log("ozdznaczony")
        count ++
    }

    counterDiv.innerHTML = `<h1>${count}</h1>`
}))












