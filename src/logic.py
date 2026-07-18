# Logic-based reasoning for banking

customer = {
    "has_atm_card": True,
    "account_type": "savings"
}

def can_withdraw(customer):
    if customer["has_atm_card"] and customer["account_type"] == "savings":
        return "Withdrawal Allowed"
    else:
        return "Withdrawal Not Allowed"

print("Logic Inference Result:")
print(can_withdraw(customer))