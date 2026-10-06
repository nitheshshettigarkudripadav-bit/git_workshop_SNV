let quantity = 1;
const price = 200;
const delivery = 100;

function updateCart() {
    const itemTotal = quantity * price;
    const total = itemTotal + delivery;

    document.getElementById("quantity").textContent = quantity;
    document.getElementById("itemPrice").textContent =
        itemTotal.toLocaleString("en-IN");

    document.getElementById("subtotal").textContent =
        itemTotal.toLocaleString("en-IN");

    document.getElementById("total").textContent =
        total.toLocaleString("en-IN");
}

function increase() {
    quantity++;
    updateCart();
}

function decrease() {
    if (quantity > 1) {
        quantity--;
        updateCart();
    }
}

updateCart();
