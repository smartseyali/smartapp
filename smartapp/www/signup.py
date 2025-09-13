import frappe

def get_context(context):
    return {}

@frappe.whitelist(allow_guest=True)
def create_user(email, password):
    if frappe.db.exists("User", email):
        return {"status": "failed", "message": "User already exists"}

    user = frappe.get_doc({
        "doctype": "User",
        "email": email,
        "first_name": email.split("@")[0],
        "enabled": 1,
        "new_password": password
    })
    user.insert(ignore_permissions=True)
    frappe.db.commit()
    return {"status": "success", "message": "User created"}
