# Simple banking knowledge base

knowledge_base = {
    "ATM Card": "Used for cash withdrawal",
    "Savings Account": "Allows limited withdrawals and earns interest",
    "Customer": "An account holder in the bank",
    "Money": "Cash that can be withdrawn from the bank"
}

query = input("Enter your banking query: ")

if query in knowledge_base:
    print("Answer:", knowledge_base[query])
else:
    print("No knowledge available for this query.")