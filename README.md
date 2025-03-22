# Jewelry & Ceramics Studio – Web Design (Part A + B)

This project was designed and implemented as part of a web development course, for a real client who owns a boutique ceramics and jewelry studio.  
We created the site according to her needs, with attention to quality, responsiveness, and standards similar to professional websites in Israel.  
The website is fully responsive and works across desktop, tablet, and mobile devices.

---

## Assumptions
- The target audience is Israeli; the site is in Hebrew and accepts only valid Israeli phone numbers.
- Backend integration and object storage will be implemented in Part C.
- Minimum user age for registration is 12.

---

## User Experience
- A fixed top navigation (`nav`) and bottom footer appear on all pages for easy access to all sections of the site.
- On mobile and tablet, a sidebar menu replaces the top nav for better usability.

---

## Pages Overview

### Home
- Includes navigation to all other pages.
- Users can choose between two product categories: **Ceramics** and **Jewelry**.
- Newsletter sign-up form is available with email input and a submission button.

---

### Login
- Users can log in to their account or reset their password.
- After login, users are redirected to their personal account page (`purchase_history`).
- Google login will be implemented after deployment using a valid Google Client ID.

---

### Registration
- New users can create an account.
- Email uniqueness validation will be implemented in Part B.
- Success and error messages are displayed in green and red, respectively.

---

### Password Reset
- For existing users who wish to reset their password via email.

---

### Shopping Cart
- Accessible to both guest and registered users.
- Users can remove items and view current items in their cart.

---

### Purchase History (User Account)
- Accessible only to logged-in users.
- Displays a list of previous orders.
- The account icon in the nav bar redirects to this page for authenticated users.

---

### Catalog (Jewelry & Ceramics)
- All users can browse products and view item details.
- Only the first product (on the left) has a full product page for demonstration.
- Products can be added directly to the cart from the catalog.
- Sorting/filtering features are **not** implemented in this phase.

---

### Product Page
- Displays images and detailed info for a selected product.
- **Ceramic items are limited to one unit each** due to their uniqueness.
- Quantity restrictions apply only to ceramics, not to jewelry.

---

### Contact
- Users can send messages via a contact form.
- An embedded map shows the studio’s location for in-person visits.

---

### About
- Provides background info about the business.
- Links to social media and WhatsApp.
- Embedded videos showcase the ceramic-making process at the studio.

