# Frame Representation using Python Dictionary

customer_frame = {
    "Customer": {
        "account_type": "Savings Account",
        "card_type": "ATM Card",
        "action": "Withdraw Money",
        "channel": "ATM Machine"
    }
}

print("Customer Frame Representation:\n")

for key, value in customer_frame["Customer"].items():
    print(f"{key} : {value}")