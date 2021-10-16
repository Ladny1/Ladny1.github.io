---
layout: post
title: What's Jekyll?
---

[Jekyll](https://jekyllrb.com) is a static site generator, an open-source tool for creating simple yet powerful websites of all shapes and sizes. From [the project's readme](https://github.com/jekyll/jekyll/blob/master/README.markdown):

> Jekyll is a simple, blog aware, static site generator. It takes a template directory [...] and spits out a complete, static website suitable for serving with Apache or your favorite web server. This is also the engine behind GitHub Pages, which you can use to host your project’s page or blog right here from GitHub.

It's an immensely useful tool. Find out more by [visiting the project on GitHub](https://github.com/jekyll/jekyll).


<div id="smart-button-container">
<div style="text-align: center;">
<div style="margin-bottom: 1.25rem;">
<p>Enhanced Matte Art Paper: matte finish, shallow tooth
Hahnemühle German Etching Paper:  matte finish, deep tooth</p>
<select id="item-options"><option value="9"x12" Enhanced Matte Art Print" price="1.00">9"x12" Enhanced Matte Art Print - 1.00 USD</option><option value="9"x12"Hahnemühle German Etching Print" price="1.00">9"x12"Hahnemühle German Etching Print - 1.00 USD</option><option value="12"x16" Enhanced Matte Art Print" price="2.00">12"x16" Enhanced Matte Art Print - 2.00 USD</option><option value="12"x16" Hahnemühle German Etching Print" price="2.00">12"x16" Hahnemühle German Etching Print - 2.00 USD</option></select>
<select style="visibility: hidden" id="quantitySelect"><option value="1">1</option><option value="2">2</option><option value="3">3</option><option value="4">4</option><option value="5">5</option><option value="6">6</option><option value="7">7</option><option value="8">8</option><option value="9">9</option><option value="10">10</option><option value="11">11</option><option value="12">12</option><option value="13">13</option><option value="14">14</option><option value="15">15</option><option value="16">16</option><option value="17">17</option><option value="18">18</option><option value="19">19</option><option value="20">20</option><option value="21">21</option><option value="22">22</option><option value="23">23</option><option value="24">24</option><option value="25">25</option><option value="26">26</option><option value="27">27</option><option value="28">28</option><option value="29">29</option><option value="30">30</option><option value="31">31</option><option value="32">32</option><option value="33">33</option><option value="34">34</option><option value="35">35</option><option value="36">36</option><option value="37">37</option><option value="38">38</option><option value="39">39</option><option value="40">40</option><option value="41">41</option><option value="42">42</option><option value="43">43</option><option value="44">44</option><option value="45">45</option><option value="46">46</option><option value="47">47</option><option value="48">48</option><option value="49">49</option><option value="50">50</option><option value="51">51</option><option value="52">52</option><option value="53">53</option><option value="54">54</option><option value="55">55</option><option value="56">56</option><option value="57">57</option><option value="58">58</option><option value="59">59</option><option value="60">60</option><option value="61">61</option><option value="62">62</option><option value="63">63</option><option value="64">64</option><option value="65">65</option><option value="66">66</option><option value="67">67</option><option value="68">68</option><option value="69">69</option><option value="70">70</option><option value="71">71</option><option value="72">72</option><option value="73">73</option><option value="74">74</option><option value="75">75</option></select>
</div>
<div id="paypal-button-container"></div>
</div>
</div>
<script src="https://www.paypal.com/sdk/js?client-id=sb&enable-funding=venmo&currency=USD" data-sdk-integration-source="button-factory"></script>
<script>
function initPayPalButton() {
var shipping = 2.99;
var itemOptions = document.querySelector("#smart-button-container #item-options");
var quantity = parseInt(75);
var quantitySelect = document.querySelector("#smart-button-container #quantitySelect");
if (!isNaN(quantity)) {
quantitySelect.style.visibility = "visible";
}
var orderDescription = 'Enhanced Matte Art Paper: matte finish, shallow tooth
Hahnemühle German Etching Paper:  matte finish, deep tooth';
if(orderDescription === '') {
orderDescription = 'Item';
}
paypal.Buttons({
style: {
shape: 'rect',
color: 'gold',
layout: 'vertical',
label: 'buynow',

},
createOrder: function(data, actions) {
var selectedItemDescription = itemOptions.options[itemOptions.selectedIndex].value;
var selectedItemPrice = parseFloat(itemOptions.options[itemOptions.selectedIndex].getAttribute("price"));
var tax = (0 === 0 || false) ? 0 : (selectedItemPrice * (parseFloat(0)/100));
if(quantitySelect.options.length > 0) {
quantity = parseInt(quantitySelect.options[quantitySelect.selectedIndex].value);
} else {
quantity = 1;
}

tax *= quantity;
tax = Math.round(tax * 100) / 100;
var priceTotal = quantity * selectedItemPrice + parseFloat(shipping) + tax;
priceTotal = Math.round(priceTotal * 100) / 100;
var itemTotalValue = Math.round((selectedItemPrice * quantity) * 100) / 100;

return actions.order.create({
purchase_units: [{
description: orderDescription,
amount: {
currency_code: 'USD',
value: priceTotal,
breakdown: {
item_total: {
currency_code: 'USD',
value: itemTotalValue,
},
shipping: {
currency_code: 'USD',
value: shipping,
},
tax_total: {
currency_code: 'USD',
value: tax,
}
}
},
items: [{
name: selectedItemDescription,
unit_amount: {
currency_code: 'USD',
value: selectedItemPrice,
},
quantity: quantity
}]
}]
});
},
onApprove: function(data, actions) {
return actions.order.capture().then(function(orderData) {

// Full available details
console.log('Capture result', orderData, JSON.stringify(orderData, null, 2));

// Show a success message within this page, e.g.
const element = document.getElementById('paypal-button-container');
element.innerHTML = '';
element.innerHTML = '<h3>Thank you for your payment!</h3>';

// Or go to another URL:  actions.redirect('thank_you.html');

});
},
onError: function(err) {
console.log(err);
},
}).render('#paypal-button-container');
}
initPayPalButton();
</script>