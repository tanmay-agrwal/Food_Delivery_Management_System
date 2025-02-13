# 🛒 Online Food Delivery Management System
A **Database Management System (DBMS) project** that provides an efficient and user-friendly **Online Food Ordering & Delivery System** for customers, sellers, and delivery partners.

---

## 📌 Project Overview
This project aims to build a centralized **Online Food Delivery Management System** that connects **customers, restaurants (sellers), and delivery personnel**, streamlining the entire ordering and delivery process.

- Customers can **place orders**, track deliveries, and make payments.
- Sellers (restaurants) can **list their food items** and **manage orders**.
- Delivery partners are assigned automatically based on their availability to fulfill orders within their **respective cities**.
- The system supports both **online transactions** and **cash on delivery (COD)**.

---

## 🚀 Features
✅ **Customer Management** - Add and manage customers with personal details.  
✅ **Seller Management** - Sellers can list food items and receive orders.  
✅ **Order Management** - Customers can place, view, and delete orders.  
✅ **Payment Processing** - Handles transactions using online banking or cash on delivery.  
✅ **Delivery Partner Management** - Assigns orders to delivery partners based on location.  
✅ **GUI-Based Interface** - User-friendly GUI built with **Tkinter** for managing orders.  
✅ **MySQL Integration** - The database stores all customer, order, payment, and delivery details.  

---

## 🏗 Database Schema & ER Model
### 📌 ER Diagram
This Entity-Relationship (ER) Diagram visualizes the key entities and their relationships.

<img src="https://github.com/tanmay-agrwal/Food_Delivery_Management_System/blob/main/diagrams/ER_Model.jpg" alt="ER Model" width="600"/>

### 📌 Relational Mapping
The Relational Mapping of the project demonstrates the table structure.

<img src="https://github.com/tanmay-agrwal/Food_Delivery_Management_System/blob/main/diagrams/Relational_Mapping.jpg" alt="Relational Mapping" width="600"/>

---

## 🖥 Graphical User Interface (GUI)
The project includes a **Tkinter-based GUI** for order and customer management.

<img src="https://github.com/tanmay-agrwal/Food_Delivery_Management_System/blob/main/diagrams/GUI.png" alt="GUI Screenshot" width="600"/>

### GUI Functionalities
- **Display Order Details** - Retrieve details of a specific order.
- **Place Order** - Customers can place new food orders.
- **Delete Order** - Remove an existing order.
- **Delete Seller** - Remove a seller from the system.

---

## 🗄 Database Tables & Business Rules
The system follows **proper relational database design**, ensuring data consistency and integrity.

### Main Tables
| **Table Name**       | **Description** |
|----------------------|---------------|
| `CUSTOMER`          | Stores customer details like name, phone number, city, etc. |
| `SELLER`            | Stores restaurant details, including ratings and locations. |
| `ORDER`             | Stores order information, including customer, seller, and delivery partner IDs. |
| `PRODUCT`           | Contains menu items listed by sellers, categorized with pricing details. |
| `PAYMENT`           | Tracks transactions, linking payments with orders. |
| `DELIVERY_PARTNER`  | Stores details of delivery personnel. |

### Key Business Rules
1. **Customers** can only place orders from sellers within the same **city**.
2. **Orders** must have a **unique order ID (OID)** and should contain only **one type of item** per order.
3. **Payments** are either **online** (with transaction numbers) or **cash on delivery** (with `NULL` transaction IDs).
4. **Each order** is assigned to a **single delivery partner** based on location.
5. **Products** can be listed by multiple sellers, but the **seller ID + item name** is the unique key.

---


## ⚙ Installation & Setup
### 1️⃣ Prerequisites
Ensure you have the following installed:
- **Python** (version 3.7+)
- **MySQL Server**
- **Tkinter** (for GUI)

### 2️⃣ Database Setup
1. Open MySQL and create a new database:
   ```sql
   CREATE DATABASE demo;
   ```
2. Run the provided SQL script to create tables and procedures:
   ```sql
   SOURCE demo.sql;
   ```

### 3️⃣ Running the Application
1. Install required Python modules:
   ```python
   pip install mysql-connector-pythonCREATE DATABASE demo;
   ```
2. Run the GUI application:
   ```python
   python demo.py
   ```
   
