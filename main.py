from pyscript import display, document

def order_summary(e=None):
    # Customer info
    first_name = document.getElementById('fname').value
    last_name = document.getElementById('lname').value
    address_info = document.getElementById('addr').value
    contact_info = document.getElementById('contact-num').value

    # Menu items: (checkbox id, qty id, price)
    menu = {
        "Strawberry jam parfait": ("jam", "jam_qty", 180),
        "Mixed berry yogurt": ("yogurt", "yogurt_qty", 170),
        "Strawberry shortcake": ("shortcake", "shortcake_qty", 150),
        "Strawberry flan": ("flan", "flan_qty", 130),
        "Strawberry ice-cream bars": ("bars", "bars_qty", 135),
        "Strawberry cream cheese cupcakes": ("cupcake", "cupcake_qty", 120),
        "Strawberry cream sando": ("sando", "sando_qty", 135),
    }

    # default order summary
    total = 0
    items_selected = False
    summary = ""
    
    # when items are checked, it will give the order summary (gets data from the checkbox and the quantity id) for item, (checkbox_id, qty_id, price) in menu.items(): checkbox = document.getElementById(checkbox_id) qty_value = document.getElementById(qty_id).value # checks id the quantity entered by the user is a positive number. so the amount of orders is the quantity value and it checks if it is greater than 0 in order for the summary to be given

    for item, (checkbox_id, qty_id, price) in menu.items():
        checkbox = document.getElementById(checkbox_id)
        qty_value = document.getElementById(qty_id).value

        if checkbox.checked and qty_value.isdigit() and int(qty_value) > 0:
            qty = int(qty_value)
            cost = price * qty
            summary += f"{item} x {qty} = ₱{cost}.00 " 
            total += cost
            items_selected = True

# checks id the quantity entered by the user is a positive number. so the amount of orders is the quantity value and it checks if it is greater than 0 in order for the summary to be given # assigning string and numeric values


    # final summary
    if items_selected:
        summary += f"Total: ₱{total}.00"
    else:
        summary = "No items selected."

    # display in one f-string
    display(f"🧺 Order Summary for {first_name} {last_name} | Address: {address_info} | Contact number: {contact_info} | {summary}",target="output")
