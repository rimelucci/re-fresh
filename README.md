# Re-fresh

Live at: *http://104.236.207.202/*

Our project aims to reduce waste from places that have to sell their leftover food by the end of the day. 
  - Many stores and restaurants offer discounts at the end of the day on foods that would spoil or lose quality overnight.
  - With Re-Fresh, stores can post food that they need to sell by the end of the day and the discounted price they are selling for.


##With Re-Fresh, you save money, stores make more money, and less food goes to waste
###It's a win-win-win!

## Overview

| Role        | Name            |
|-------------|--------------   |
| Leader + UX | Rick Melucci    |
| Backend     |  Young Kim      |
| Middleware  |  Derrick Lui    |
| Middleware  |  Aaron Wang     |

## Tools

Fully implemented:
- Materialize
- Python
  - Flask
  
Ready for implementation, but not yet integrated in current version:
- Geo API
- Stripe API

##Functions:

###Customers:
  - View a live feed of posts from food institutions nearby.
  - Add food items to cart.
  - Purchase items (implementing Stripe API later)
  - Feed and user cart are dynamically updated.
  - User can change settings.

###Stores:
  - Add items to live feed for sale.
  - Receive payments from Stripe API (implemented later)

