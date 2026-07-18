import networkx as nx
import matplotlib.pyplot as plt

from src.nlp_processor import process_text
from src.extractor import extract_entities_relations


# -------------------------------
# 0. NLP Processing
# -------------------------------
def nlp_input():

    text = input("\nEnter banking text: ")

    tokens, pos_tags = process_text(text)

    entities, relations = extract_entities_relations(pos_tags)

    print("\n---------------- NLP OUTPUT ----------------")
    print("\nTokens:")
    print(tokens)

    print("\nPOS Tags:")
    print(pos_tags)

    print("\nExtracted Entities:")
    print(entities)

    print("\nExtracted Relations:")
    print(relations)

    return entities, relations


# -------------------------------
# 1. Advanced Semantic Network
# -------------------------------
def semantic_network():

    G = nx.DiGraph()

    # -------------------------------
    # ADD BANKING ENTITIES
    # -------------------------------
    nodes = [
    "Customer",
    "Savings Account",
    "Current Account",
    "Fixed Deposit",
    "Recurring Deposit",
    "ATM Card",
    "Debit Card",
    "Credit Card",
    "Loan",
    "Home Loan",
    "Education Loan",
    "Personal Loan",
    "Bank",
    "ATM Machine",
    "Mobile Banking",
    "Internet Banking",
    "Transaction",
    "Money",
    "Employee",
    "Manager",
    "Branch",
    "Insurance",
    "UPI Payment",
    "Cheque",
    "Security System",
    "Passbook",
    "KYC",
    "Locker",
    "Interest",
    "Customer Service",
    "RTGS",
    "NEFT",
    "IMPS",
    "Nominee",
    "Statement",
    "Cash Deposit",
    "Cash Withdrawal"
]

    G.add_nodes_from(nodes)

    # -------------------------------
    # ADD RELATIONSHIPS
    # -------------------------------
    edges = [

    ("Customer", "Savings Account", "has"),
    ("Customer", "Current Account", "owns"),
    ("Customer", "Fixed Deposit", "opens"),
    ("Customer", "Recurring Deposit", "opens"),

    ("Customer", "ATM Card", "uses"),
    ("Customer", "Debit Card", "uses"),
    ("Customer", "Credit Card", "uses"),

    ("Customer", "Loan", "applies for"),
    ("Customer", "Home Loan", "applies for"),
    ("Customer", "Education Loan", "applies for"),
    ("Customer", "Personal Loan", "applies for"),

    ("Customer", "Money", "withdraws"),
    ("Customer", "UPI Payment", "performs"),
    ("Customer", "RTGS", "performs"),
    ("Customer", "NEFT", "performs"),
    ("Customer", "IMPS", "performs"),

    ("Customer", "Internet Banking", "accesses"),
    ("Customer", "Mobile Banking", "uses"),

    ("Customer", "Passbook", "receives"),
    ("Customer", "Locker", "rents"),
    ("Customer", "Nominee", "assigns"),

    ("Savings Account", "Bank", "managed by"),
    ("Current Account", "Bank", "managed by"),
    ("Fixed Deposit", "Bank", "managed by"),
    ("Recurring Deposit", "Bank", "managed by"),

    ("Savings Account", "Interest", "earns"),
    ("Fixed Deposit", "Interest", "earns"),
    ("Recurring Deposit", "Interest", "earns"),

    ("ATM Card", "ATM Machine", "accesses"),

    ("Transaction", "Money", "transfers"),
    ("UPI Payment", "Money", "transfers"),
    ("RTGS", "Money", "transfers"),
    ("NEFT", "Money", "transfers"),
    ("IMPS", "Money", "transfers"),

    ("Employee", "Branch", "works in"),
    ("Manager", "Branch", "manages"),

    ("Employee", "Customer Service", "provides"),

    ("Bank", "Insurance", "provides"),

    ("Cheque", "Bank", "processed by"),

    ("Statement", "Transaction", "records"),

    ("KYC", "Customer", "verifies"),

    ("Cash Deposit", "Money", "adds"),
    ("Cash Withdrawal", "Money", "removes"),

    ("Security System", "Transaction", "verifies"),
    ("Security System", "UPI Payment", "authenticates"),
    ("Security System", "Internet Banking", "protects")
]
    for source, target, relation in edges:
        G.add_edge(source, target, label=relation)

    # -------------------------------
    # GRAPH DESIGN
    # -------------------------------
    plt.figure(figsize=(18, 12))

    pos = nx.spring_layout(G, k=2, seed=42)

    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color="lightblue",
        node_size=4000,
        font_size=9,
        font_weight="bold",
        arrows=True
    )

    edge_labels = nx.get_edge_attributes(G, 'label')

    nx.draw_networkx_edge_labels(
        G,
        pos,
        edge_labels=edge_labels,
        font_size=8
    )

    plt.title("Advanced Banking Semantic Network", fontsize=18)

    plt.savefig("output/advanced_banking_semantic_network.png")

    plt.show()

    print("\nSemantic Network Generated Successfully!")
    print("Graph saved in output folder.")


# -------------------------------
# 2. Advanced Frame Representation
# -------------------------------
def frame_representation():

    customer_frame = {

    "Customer ID": "C1001",
    "Customer Name": "Ashish",
    "Age": 22,
    "Gender": "Male",

    "Account Type": "Savings Account",
    "Account Number": "123456789",
    "Branch": "Mumbai Branch",

    "Balance": 25000,

    "ATM Card": "Active",
    "Debit Card": "Active",
    "Credit Card": "Available",

    "Loan Status": "Approved",
    "Loan Type": "Personal Loan",

    "Mobile Banking": "Enabled",
    "Internet Banking": "Enabled",

    "UPI ID": "ashish@upi",

    "Transaction Limit": 50000,

    "Insurance": "Active",

    "Nominee": "Rahul",

    "KYC Status": "Verified"
}

    print("\n---------------- FRAME REPRESENTATION ----------------\n")

    for key, value in customer_frame.items():
        print(f"{key} : {value}")


# -------------------------------
# 3. Advanced Logic-Based Reasoning
# -------------------------------
def logic_inference():

    customer = {
    "has_atm_card": True,
    "account_balance": 25000,
    "loan_approved": True,
    "internet_banking": True,
    "security_verified": True,
    "kyc_verified": True
}

    print("\n---------------- LOGIC INFERENCE ----------------")

    # Withdrawal Rule
    if customer["has_atm_card"] and customer["account_balance"] > 0:
        print("\nWithdrawal Status: Allowed")
    else:
        print("\nWithdrawal Status: Not Allowed")

    # Loan Rule
    if customer["loan_approved"]:
        print("Loan Status: Loan Approved")
    else:
        print("Loan Status: Loan Rejected")

    # Banking Access Rule
    if customer["internet_banking"] and customer["security_verified"]:
        print("Internet Banking Access: Granted")
    else:
        print("Internet Banking Access: Denied")

    # Fixed Deposit Eligibility
    if customer["account_balance"] >= 10000:
        print("FD Eligibility: Eligible")
    else:
        print("FD Eligibility: Not Eligible")

    # Credit Card Eligibility
    if customer["account_balance"] >= 50000:
        print("Credit Card Eligibility: Approved")
    else:
        print("Credit Card Eligibility: Rejected")

    # Premium Banking
    if customer["account_balance"] >= 100000:
        print("Premium Banking Status: Eligible")
    else:
        print("Premium Banking Status: Standard Customer")

    # KYC Verification
    if customer["kyc_verified"]:
        print("KYC Status: Verified")
    else:
        print("KYC Status: Pending")

    # Loan Eligibility
    if customer["account_balance"] >= 20000:
        print("Loan Eligibility: Eligible")
    else:
        print("Loan Eligibility: Not Eligible")    


# -------------------------------
# 4. Advanced Query System
# -------------------------------
def query_system():

    knowledge_base = {

    "ATM Card":
        "ATM card is used for cash withdrawal and ATM transactions.",

    "Debit Card":
        "Debit card allows direct access to money from a bank account.",

    "Credit Card":
        "Credit card allows customers to borrow money temporarily.",

    "Savings Account":
        "Savings account allows money storage and earns interest.",

    "Current Account":
        "Current account supports business transactions.",

    "Fixed Deposit":
        "Fixed Deposit offers higher interest for a fixed period.",

    "Recurring Deposit":
        "Recurring Deposit allows monthly savings with interest.",

    "Loan":
        "Loan is borrowed money that must be repaid with interest.",

    "Home Loan":
        "Home loan helps customers purchase residential property.",

    "Education Loan":
        "Education loan supports higher education expenses.",

    "Personal Loan":
        "Personal loan can be used for personal financial needs.",

    "UPI Payment":
        "UPI enables instant digital money transfer.",

    "RTGS":
        "RTGS enables real-time high-value money transfers.",

    "NEFT":
        "NEFT supports electronic fund transfers across banks.",

    "IMPS":
        "IMPS provides instant fund transfer services.",

    "Mobile Banking":
        "Mobile banking allows banking operations through smartphones.",

    "Internet Banking":
        "Internet banking supports online banking services.",

    "Bank":
        "Bank manages customer accounts, loans and transactions.",

    "Insurance":
        "Insurance provides financial protection against risks.",

    "Cheque":
        "Cheque is a written payment instruction to the bank.",

    "Transaction":
        "Transaction refers to transfer, deposit or withdrawal of money.",

    "Locker":
        "Bank locker provides secure storage for valuables.",

    "Passbook":
        "Passbook records all account transactions.",

    "KYC":
        "Know Your Customer is a process used to verify customer identity.",

    "Nominee":
        "Nominee receives account benefits when required.",

    "Statement":
        "Bank statement contains transaction history."
}
    print("\n---------------- QUERY SYSTEM ----------------")

    print("\nAvailable Queries:")
    for key in knowledge_base.keys():
        print("-", key)

    query = input("\nEnter your banking query: ")

    if query in knowledge_base:
        print("\nAnswer:")
        print(knowledge_base[query])
    else:
        print("\nNo knowledge available for this query.")

# -------------------------------
# MAIN PROGRAM
# -------------------------------
def banking_expert_system():

    print("\n---------------- BANKING EXPERT SYSTEM ----------------")

    customer_balance = int(input("Enter Customer Balance: "))

    print("\n1. Loan Eligibility")
    print("2. Fixed Deposit Eligibility")
    print("3. Credit Card Eligibility")

    choice = int(input("\nEnter Choice: "))

    if choice == 1:

        if customer_balance >= 20000:
            print("Result: Loan Eligible")
        else:
            print("Result: Loan Not Eligible")

    elif choice == 2:

        if customer_balance >= 10000:
            print("Result: FD Eligible")
        else:
            print("Result: FD Not Eligible")

    elif choice == 3:

        if customer_balance >= 50000:
            print("Result: Credit Card Approved")
        else:
            print("Result: Credit Card Rejected")

    else:
        print("Invalid Choice")
if __name__ == "__main__":

    print("\n==============================================")
    print(" BANKING KNOWLEDGE REPRESENTATION SYSTEM ")
    print("==============================================")

    entities, relations = nlp_input()

    semantic_network()

    frame_representation()

    logic_inference()

    banking_expert_system()

    query_system()


    print("\nProject Execution Completed Successfully!")