import ldap3
import logging
import json
import tkinter as tk
from tkinter import messagebox
from ldap3 import Server, Connection, ALL, MODIFY_REPLACE

# Configure Logging
logging.basicConfig(filename="ad_integration.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Active Directory Server Settings
AD_SERVER = "ldap://your-ad-server.com"
AD_BASE_DN = "DC=yourdomain,DC=com"
AD_ADMIN_USER = "admin@yourdomain.com"
AD_ADMIN_PASS = "your_password"

# Function to connect to AD
def connect_to_ad():
    try:
        server = Server(AD_SERVER, get_info=ALL)
        conn = Connection(server, AD_ADMIN_USER, AD_ADMIN_PASS, auto_bind=True)
        logging.info("Connected to Active Directory")
        return conn
    except Exception as e:
        logging.error(f"Failed to connect to AD: {e}")
        return None

# Function to authenticate a user
def authenticate_user(username, password):
    user_dn = f"CN={username},{AD_BASE_DN}"
    try:
        conn = Connection(AD_SERVER, user_dn, password, auto_bind=True)
        logging.info(f"User {username} authenticated successfully")
        return True
    except Exception as e:
        logging.warning(f"Authentication failed for {username}: {e}")
        return False

# Function to list users in AD
def list_users():
    conn = connect_to_ad()
    if conn:
        conn.search(AD_BASE_DN, "(objectClass=person)", attributes=["cn", "mail"])
        users = [{"name": entry["attributes"]["cn"], "email": entry["attributes"].get("mail", "N/A")} for entry in conn.entries]
        return users
    return []

# Function to reset a user password
def reset_password(username, new_password):
    conn = connect_to_ad()
    if conn:
        user_dn = f"CN={username},{AD_BASE_DN}"
        conn.modify(user_dn, {"unicodePwd": [(MODIFY_REPLACE, [new_password])]})
        if conn.result["description"] == "success":
            logging.info(f"Password reset for {username}")
            return True
        else:
            logging.error(f"Password reset failed for {username}: {conn.result}")
    return False

# GUI Interface for AD User Management
def run_gui():
    def authenticate():
        username = user_entry.get()
        password = pass_entry.get()
        if authenticate_user(username, password):
            messagebox.showinfo("Login Success", f"User {username} authenticated")
        else:
            messagebox.showerror("Login Failed", f"Authentication failed for {username}")

    root = tk.Tk()
    root.title("Active Directory Authentication")

    tk.Label(root, text="Username:").grid(row=0, column=0)
    user_entry = tk.Entry(root)
    user_entry.grid(row=0, column=1)

    tk.Label(root, text="Password:").grid(row=1, column=0)
    pass_entry = tk.Entry(root, show="*")
    pass_entry.grid(row=1, column=1)

    tk.Button(root, text="Authenticate", command=authenticate).grid(row=2, column=0, columnspan=2)

    root.mainloop()

# Run GUI if script is executed
if __name__ == "__main__":
    run_gui()
