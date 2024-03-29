


window.addEventListener('beforeunload', function (e) {
    var confirmationMessage = 'Czy na pewno chcesz opuścić stronę? Wprowadzone dane mogą zostać utracone.';
    (e || window.e).returnValue = confirmationMessage;
    return confirmationMessage;
});
    


const counterDiv = document.querySelector(".counter");
const checkboxes = document.querySelectorAll("#checkbox");
const tableBody = document.querySelector(".table-group-divider");

let count = checkboxes.length;

counterDiv.innerHTML += `<h1>${count}</h1>`;

checkboxes.forEach((checkbox) =>
  checkbox.addEventListener("change", function () {
    if (checkbox.checked) {
      count--;
    } else {
      count++;
    }

    counterDiv.innerHTML = `<h1>${count}</h1>`;

    // Sorting rows based on checkbox status
    const rows = Array.from(tableBody.children);
    rows.sort((a, b) => {
      const checkboxA = a.querySelector("#checkbox");
      const checkboxB = b.querySelector("#checkbox");
      return checkboxA.checked - checkboxB.checked;
    });

    // Deleting existing rows from a table
    tableBody.innerHTML = "";

    // Adding sorted rows back to the table
    rows.forEach((row) => {
      tableBody.appendChild(row);
    });
  })
);


const saveButton = document.querySelector(".btn-primary");
const form = document.querySelector("form");

saveButton.addEventListener("click", function () {
  // Zbierz zaznaczone checkboxy
  const selectedItems = Array.from(checkboxes).filter((checkbox) => checkbox.checked);

  // Zaktualizuj formularz, aby przesłać tylko zaznaczone elementy
  selectedItems.forEach((item) => {
    const hiddenInput = document.createElement("input");
    hiddenInput.type = "hidden";
    hiddenInput.name = "selected_items";
    hiddenInput.value = item.value;
    form.appendChild(hiddenInput);
    console.log(item)
  });
});


