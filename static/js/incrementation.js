
function incrementQuantity() {
    var quantityElement = document.getElementById("product-quantity");
    valeur=quantityElement.innerText
    var currentQuantity = parseInt(valeur);
    // console.log(currentQuantity)
    quantityElement.innerText = currentQuantity + 1;
}

function decrementQuantity() {   
    var quantityElement = document.getElementById("product-quantity");
    var currentQuantity = parseInt(quantityElement.textContent);
    if (currentQuantity > 0) {
        quantityElement.textContent = currentQuantity - 1;
    }
}
