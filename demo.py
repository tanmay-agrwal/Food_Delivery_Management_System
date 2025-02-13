import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Function to display order details
def display_order_details():
    oid = oid_entry.get()

    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="manager",
            database="demo"
        )
        cursor = conn.cursor()

        cursor.callproc("OrderDetails", (oid,))
        
        for result in cursor.stored_results():
            order_details = result.fetchall()

        if order_details:
            order_window = tk.Toplevel(root)
            order_window.title("Order Details")

            for detail in order_details:
                tk.Label(order_window, text=f"Customer Name: {detail[0]}").pack()
                tk.Label(order_window, text=f"City: {detail[1]}").pack()
                tk.Label(order_window, text=f"Seller: {detail[2]}").pack()
                tk.Label(order_window, text=f"Item: {detail[3]}").pack()
                tk.Label(order_window, text=f"Amount: {detail[4]}").pack()
                tk.Label(order_window, text=f"Payment Mode: {detail[5]}").pack()
                tk.Label(order_window, text=f"Delivery Partner: {detail[6]}").pack()
                tk.Label(order_window, text=f"Delivery Phone Number: {detail[7]}").pack()
                tk.Label(order_window, text=f"Order Status: {detail[8]}").pack()

        else:
            messagebox.showinfo("Info", "No order found with the given OID")

        cursor.close()
        conn.close()

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

# Function to place new order
def place_order():
    cid = place_order_cid_entry.get()
    sel_id = place_order_sel_id_entry.get()
    item = place_order_item_entry.get()
    quantity = place_order_quantity_entry.get()

    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="manager",
            database="demo"
        )
        cursor = conn.cursor()

        cursor.callproc("NewOrder", (cid, sel_id, item, quantity))
        conn.commit()

        messagebox.showinfo("Success", "Order placed successfully")

        cursor.close()
        conn.close()

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

# Function to delete order
def delete_order():
    oid = delete_oid_entry.get()

    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="manager",
            database="demo"
        )
        cursor = conn.cursor()

        query = "DELETE FROM ORDERS WHERE OID = %s"
        data = (oid,)

        cursor.execute(query, data)
        conn.commit()

        messagebox.showinfo("Success", "Order deleted successfully")

        cursor.close()
        conn.close()

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

# Function to delete seller
def delete_seller():
    sel_id = delete_sel_id_entry.get()

    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="manager",
            database="demo"
        )
        cursor = conn.cursor()

        query = "DELETE FROM SELLER WHERE SID = %s"
        data = (sel_id,)

        cursor.execute(query, data)
        conn.commit()

        messagebox.showinfo("Success", "Seller deleted successfully")

        cursor.close()
        conn.close()

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

# Main GUI
root = tk.Tk()
root.title("Customer and Order Management")
root.configure(bg="#f0f0f0")
root.geometry("280x330")

# Styling Configuration
button_bg = "#0078D7"  # Blue buttons
button_fg = "white"  # White text

# Order Entry Field
tk.Label(root, text="Enter Order OID:").grid(row=0, column=0)
oid_entry = tk.Entry(root)
oid_entry.grid(row=0, column=1)

# Display Order Details Button
display_btn = tk.Button(root, text="Display Order Details", command=display_order_details, bg=button_bg, fg=button_fg)
display_btn.grid(row=1, column=0, columnspan=2, pady=10)

# Place Order Entry Fields
tk.Label(root, text="CID:").grid(row=2, column=0)
place_order_cid_entry = tk.Entry(root)
place_order_cid_entry.grid(row=2, column=1)

tk.Label(root, text="Seller ID:").grid(row=3, column=0)
place_order_sel_id_entry = tk.Entry(root)
place_order_sel_id_entry.grid(row=3, column=1)

tk.Label(root, text="Item Name:").grid(row=4, column=0)
place_order_item_entry = tk.Entry(root)
place_order_item_entry.grid(row=4, column=1)

tk.Label(root, text="Quantity:").grid(row=5, column=0)
place_order_quantity_entry = tk.Entry(root)
place_order_quantity_entry.grid(row=5, column=1)

# Place Order Button
place_order_btn = tk.Button(root, text="Place Order", command=place_order, bg=button_bg, fg=button_fg)
place_order_btn.grid(row=6, column=0, columnspan=2, pady=10)

# Delete Order Entry Field
tk.Label(root, text="Enter Order OID to Delete:").grid(row=7, column=0)
delete_oid_entry = tk.Entry(root)
delete_oid_entry.grid(row=7, column=1)

# Delete Order Button
delete_order_btn = tk.Button(root, text="Delete Order", command=delete_order, bg=button_bg, fg=button_fg)
delete_order_btn.grid(row=8, column=0, columnspan=2, pady=10)

# Delete Seller Entry Field
tk.Label(root, text="Enter Seller ID to Delete:").grid(row=9, column=0)
delete_sel_id_entry = tk.Entry(root)
delete_sel_id_entry.grid(row=9, column=1)

# Delete Seller Button
delete_seller_btn = tk.Button(root, text="Delete Seller", command=delete_seller, bg=button_bg, fg=button_fg)
delete_seller_btn.grid(row=10, column=0, columnspan=2, pady=10)

root.mainloop()