# Xcel--Ecommerce-store

To use this app paypal checkout feature you have to add signup to paypal developer and use your API in blog>blog>templates>blog>checkout.html

Our project is a fully functional full stack ecommerce website with user and guest checkout capabilities. Users will have the ability to add multiple products to cart, 
varying from physical to digital products. After we completed basic checkout with a logged in user, we added in the ability for users to checkout as a guest using cookies.
Users can create and update their accounts and can add or remove items to their cart and complete their checkout process using paypal integration.


# Project Database
We are used SQLite for our project because SQLite database is implemented on a single file with no additional server process or the need for complicated RDBMS to install.
SQLite comes with zero server-side software installation and minimum maintenance.

# Models:
 This project will consist of 6 Models, so let's summarize each one:
  1. USER - Built in Django user model, instance created for each customer who registers.
  2. CUSTOMER - Along with a User model, each customer contains a customer model that holds a one-to-one relationship to each user. (OneToOneFied)
  3. PRODUCT - The product model represents product types we have in store.
  4. ORDER - The order model represents a transaction that is placed or pending. The model holds information such as the transaction ID, data completed and order status. 
   This model will be a child or the customer model but a parent to Order Items.
  5. ORDERITEM - An order Item is one item with an order. For example, a shopping cart may consist of many items but is all part of one order.


# Guest/User checkout:
The main focus of this ECommerce project will be to integrate guest checkout ability along with user accounts.
Any E-Commerce webapp should always give user the ability to checkout without creating the account.


# Authenticated User Vs Guest Checkout
Authenticated users & guests have virtually the same process with slight differences. Users with accounts will have the ability to view pending and previous orders 
while guests will have items stored in cookies and will have the option to create account after a successful purchase.

  # Authenticated User Process:
   1. Add item to cart → Edit Order → Checkout
   2. View pending and previous orders + Order details
  # Guest Checkout Process:
   1. Add item to cart → Edit Order → Checkout
   2. Create Account to view Order
