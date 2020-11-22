var sortOption = document.getElementById("sort");
var list = document.querySelector('#list_container');
var price = document.querySelectorAll('#list_container .col-md-4 .price');
var area = document.querySelectorAll('#list_container .col-md-4 #area');
var prices = Array.prototype.slice.call(price);
var areas = Array.prototype.slice.call(area);
var temp;

for (var i = 0; i<prices.length - 1;i++) {
    if (parseFloat(prices[i].textContent) > parseFloat(prices[i+1].textContent)) {
        temp = prices[i];
        prices[i] = prices[i+1];
        prices[i+1] = temp;
        if (i > 0) 
            i-=2;
    }
}

for (var i = 0; i<areas.length - 1;i++) {
    if (parseFloat(areas[i].textContent) > parseFloat(areas[i+1].textContent)) {
        temp = areas[i+1];
        areas[i+1] = areas[i];
        areas[i] = temp;
        if (i > 0) 
            i-=2;
    }
}

sortOption.onchange = function() {
    console.log(this.value)
    if (sortOption.value == "low") {
        for (var i = 0;i<prices.length;i++) {
            list.removeChild(prices[i].parentNode.parentNode.parentNode.parentNode.parentNode.parentNode.parentNode)
            list.appendChild(prices[i].parentNode.parentNode.parentNode.parentNode.parentNode.parentNode.parentNode)
        }
    }
    else if (sortOption.value == 'high') {
        for (var i = prices.length - 1;i>=0;i--) {
            list.removeChild(prices[i].parentNode.parentNode.parentNode.parentNode.parentNode.parentNode.parentNode)
            list.appendChild(prices[i].parentNode.parentNode.parentNode.parentNode.parentNode.parentNode.parentNode)
        }
    }
    else if (sortOption.value == 'small') {
        for (var i = 0;i<areas.length;i++) {
            list.removeChild(areas[i].parentNode.parentNode.parentNode.parentNode.parentNode.parentNode.parentNode.parentNode)
            list.appendChild(areas[i].parentNode.parentNode.parentNode.parentNode.parentNode.parentNode.parentNode.parentNode)
        }
    }
    else if (sortOption.value == 'big') {
        for (var i = areas.length - 1;i>=0;i--) {
            list.removeChild(areas[i].parentNode.parentNode.parentNode.parentNode.parentNode.parentNode.parentNode.parentNode)
            list.appendChild(areas[i].parentNode.parentNode.parentNode.parentNode.parentNode.parentNode.parentNode.parentNode)
        }
    }
}


