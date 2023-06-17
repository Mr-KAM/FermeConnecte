
function incrementQuantity(productName) {
    var quantityElement = document.getElementById(productName + "-quantity");
    var currentQuantity = parseInt(quantityElement.textContent);
    quantityElement.textContent = currentQuantity + 1;
}

function decrementQuantity(productName) {   
    var quantityElement = document.getElementById(productName + "-quantity");
    var currentQuantity = parseInt(quantityElement.textContent);
    if (currentQuantity > 0) {
        quantityElement.textContent = currentQuantity - 1;
    }
}
