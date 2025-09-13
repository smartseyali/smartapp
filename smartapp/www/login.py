import frappe
from frappe.auth import LoginManager

def get_context(context):
    return {}

@frappe.whitelist(allow_guest=True)
def custom_login(usr, pwd):
    try:
        login_manager = LoginManager()
        login_manager.authenticate(usr, pwd)
        login_manager.post_login()
        return {"status": "success"}
    except Exception as e:
        return {"status": "failed", "message": str(e)}

