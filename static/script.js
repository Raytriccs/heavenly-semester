let cart = [];

function addToCart(name, price) {
    let item = cart.find(product => product.name === name);

    if (item) {
        item.quantity += 1;
    } else {
        cart.push({
            name: name,
            price: Number(price),
            quantity: 1
        });
    }

    updateCart();
}

function updateCart() {
    let totalCount = 0;
    let totalPrice = 0;
    let html = "";

    for (let item of cart) {
        totalCount += item.quantity;
        totalPrice += item.price * item.quantity;

        html += `
            <div class="cart-item">
                <p>${item.name}</p>
                <p>${item.quantity} stk</p>
            </div>
        `;
    }

    document.getElementById("cart-count").textContent = totalCount + " varer";
    document.getElementById("cart-total").textContent = totalPrice.toFixed(2) + " kr";
    document.getElementById("cart-items").innerHTML = html || "<p>Handlekurven er tom</p>";
}

function toggleCart() {
    let cartBox = document.getElementById("cart-dropdown");

    if (cartBox.style.display === "block") {
        cartBox.style.display = "none";
    } else {
        cartBox.style.display = "block";
    }
}

function placeOrder() {
    if (cart.length === 0) {
        alert("Handlekurven er tom");
        return;
    }

    fetch("/place_order", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ items: cart })
    })
    .then(response => response.json())
    .then(data => {
        if (data.message === "ok") {
            alert("Bestilling lagret!");
            cart = [];
            updateCart();
            location.reload();
        }
    })
    .catch(error => {
        alert("Noe gikk galt med bestillingen");
        console.log(error);
    });
}
