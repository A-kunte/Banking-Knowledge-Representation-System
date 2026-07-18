import networkx as nx
import matplotlib.pyplot as plt

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


    plt.savefig(
        "output/advanced_banking_semantic_network.png"
    )

    plt.close()