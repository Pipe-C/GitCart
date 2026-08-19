# 🛒 GitCart - Mini Shopping System

> A lightweight CLI-based shopping cart application developed to practice collaborative Git/GitHub workflows, feature branching, Conventional Commits, Code Reviews, and Pull Requests.

---

## 📌 Features

### 📦 Product Management Module (`productos.py`)
Developed on branch: `feature/productos`

* **Dynamic Catalog Generation:** Automatically populates a catalog of products with randomized names, realistic prices, and initial stock quantities.
* **Product Listing:** Formats and displays all available products in a clean console table.
* **ID Lookup:** Utility function to retrieve product details by ID (used by the purchase module).
* **Manual Registration:** Allows users to add new products to the catalog with proper validation.

### 🛍️ Purchase Process Module (`compras.py`)
Developed on branch: `feature/compras`

* **Cart Management:** Enables adding available products to the active shopping cart while tracking quantity and stock.
* **Cart View & Calculation:** Summarizes selected items, subtotal, and total cost with currency formatting.
* **Checkout System:** Finalizes the purchase, confirms transaction success, and resets the active cart.

---

## 📂 Project Structure

```text
GitCart/
├── .gitignore          # Ignores bytecode and cache files
├── README.md           # Project documentation
├── main.py             # CLI menu & system entry point
├── productos.py        # Product catalog logic
└── compras.py          # Shopping cart logic