from src.semantic_network import semantic_network
from src.nlp_processor import process_text
from src.extractor import extract_entities_relations
import streamlit as st

st.set_page_config(
    page_title="Banking AI Assistant",
    page_icon="🏦",
    layout="wide"
)

st.title("🏦 Banking Knowledge Representation System")

menu = st.sidebar.selectbox(
    "Select Module",
    [
        "Home",
        "Dashboard",
        "NLP Analyzer",
        "Semantic Network",
        "Customer Frame",
        "Eligibility Checker",
        "Banking Knowledge Base",
        "Chatbot"
    ]
)

# HOME
if menu == "Home":

    st.header("Welcome")

    st.write("""
    This project demonstrates:

    • Natural Language Processing (NLP)

    • Semantic Network

    • Frame Representation

    • Logic Based Reasoning

    • Banking Expert System

    • AI Banking Chatbot
    """)
#Dashboard
elif menu == "Dashboard":

    st.header("📊 Banking Dashboard")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Customers", "10,000")

    with col2:
        st.metric("Loans", "3,500")

    with col3:
        st.metric("Transactions", "25,000")
#Frame
elif menu == "Customer Frame":

    st.header("👤 Customer Frame Representation")

    customer_frame = {
        "Customer Name": "Ashish",
        "Account Type": "Savings Account",
        "ATM Card": "Active",
        "Credit Card": "Available",
        "Loan Status": "Approved",
        "Mobile Banking": "Enabled",
        "Internet Banking": "Enabled",
        "Transaction Limit": "50000",
        "Branch": "Mumbai Branch",
        "Insurance": "Active"
    }

    st.json(customer_frame)
#Eligibility
elif menu == "Eligibility Checker":

    st.header("🧠 Banking Expert System")

    balance = st.number_input(
        "Enter Account Balance",
        min_value=0
    )

    kyc = st.selectbox(
        "KYC Status",
        ["Verified", "Not Verified"]
    )

    if st.button("Check Eligibility"):

        st.subheader("Results")

        if balance >= 20000 and kyc == "Verified":
            st.success("✅ Loan Eligible")
        else:
            st.error("❌ Loan Not Eligible")

        if balance >= 10000:
            st.success("✅ Fixed Deposit Eligible")
        else:
            st.error("❌ Fixed Deposit Not Eligible")

        if balance >= 50000 and kyc == "Verified":
            st.success("✅ Credit Card Approved")
        else:
            st.error("❌ Credit Card Rejected")
#Banking Knowledge Base
elif menu == "Banking Knowledge Base":

    st.header("📚 Banking Knowledge Repository")

    knowledge_base = {

    "ATM Card":
    "ATM Card allows customers to withdraw cash, check balances, transfer funds, and perform banking transactions through ATM machines.",

    "Debit Card":
    "A Debit Card allows direct access to funds from a customer's bank account for purchases and cash withdrawals.",

    "Credit Card":
    "A Credit Card allows customers to borrow money from the bank up to a specified limit and repay it later.",

    "Savings Account":
    "A Savings Account is a deposit account that helps customers save money while earning interest.",

    "Current Account":
    "A Current Account is designed for businesses and individuals who perform frequent transactions.",

    "Fixed Deposit":
    "A Fixed Deposit allows customers to deposit money for a fixed period and earn higher interest rates.",

    "Recurring Deposit":
    "A Recurring Deposit allows customers to save a fixed amount every month and earn interest.",

    "Loan":
    "A Loan is borrowed money provided by a bank that must be repaid with interest over a specific period.",

    "Home Loan":
    "A Home Loan helps customers purchase, construct, or renovate residential property.",

    "Personal Loan":
    "A Personal Loan can be used for personal financial needs without providing collateral.",

    "Education Loan":
    "An Education Loan helps students finance higher education expenses.",

    "Vehicle Loan":
    "A Vehicle Loan is used to purchase cars, bikes, or commercial vehicles.",

    "Gold Loan":
    "A Gold Loan is secured by pledging gold ornaments as collateral.",

    "UPI":
    "UPI (Unified Payments Interface) enables instant bank-to-bank money transfers using mobile devices.",

    "NEFT":
    "NEFT (National Electronic Funds Transfer) enables electronic fund transfers between banks.",

    "RTGS":
    "RTGS (Real Time Gross Settlement) supports instant high-value fund transfers.",

    "IMPS":
    "IMPS (Immediate Payment Service) provides instant money transfer services 24x7.",

    "Cheque":
    "A Cheque is a written instruction directing a bank to pay a specified amount.",

    "Demand Draft":
    "A Demand Draft is a prepaid negotiable instrument issued by a bank.",

    "Passbook":
    "A Passbook records all transactions associated with a bank account.",

    "Bank Statement":
    "A Bank Statement provides a summary of account transactions over a period.",

    "Interest":
    "Interest is the amount earned on deposits or paid on loans.",

    "Simple Interest":
    "Simple Interest is calculated only on the principal amount.",

    "Compound Interest":
    "Compound Interest is calculated on both principal and accumulated interest.",

    "Nominee":
    "A Nominee is a person authorized to receive account benefits when required.",

    "KYC":
    "KYC (Know Your Customer) verifies customer identity and prevents fraud.",

    "PAN Card":
    "PAN Card is used for tax identification and financial transactions.",

    "Aadhaar":
    "Aadhaar is a unique identification number used for KYC verification.",

    "Mobile Banking":
    "Mobile Banking allows customers to perform banking operations through smartphones.",

    "Internet Banking":
    "Internet Banking provides online access to banking services through websites.",

    "SMS Banking":
    "SMS Banking allows customers to receive account updates through text messages.",

    "Net Banking":
    "Net Banking enables customers to access banking services over the internet.",

    "Bank":
    "A Bank is a financial institution that accepts deposits, provides loans, and offers financial services.",

    "Branch":
    "A Branch is a local office of a bank where customers can perform transactions.",

    "Manager":
    "A Bank Manager supervises banking operations and customer services.",

    "Cash Deposit":
    "Cash Deposit refers to adding money into a bank account.",

    "Cash Withdrawal":
    "Cash Withdrawal refers to removing money from a bank account.",

    "Balance":
    "Balance is the amount of money available in a bank account.",

    "Minimum Balance":
    "Minimum Balance is the required amount customers must maintain in certain accounts.",

    "Transaction":
    "A Transaction is any financial activity involving deposits, withdrawals, or transfers.",

    "Fund Transfer":
    "Fund Transfer refers to moving money between accounts.",

    "Beneficiary":
    "A Beneficiary is a person or account that receives transferred funds.",

    "IFSC Code":
    "IFSC Code uniquely identifies a bank branch for electronic transactions.",

    "MICR Code":
    "MICR Code helps banks process cheques efficiently.",

    "Account Number":
    "An Account Number uniquely identifies a customer's bank account.",

    "Customer":
    "A Customer is an individual or organization using banking services.",

    "Employee":
    "A Bank Employee assists customers and performs banking operations.",

    "Insurance":
    "Insurance provides financial protection against specified risks.",

    "Life Insurance":
    "Life Insurance offers financial support to beneficiaries after the policyholder's death.",

    "Health Insurance":
    "Health Insurance covers medical and hospitalization expenses.",

    "Premium":
    "Premium is the amount paid to maintain an insurance policy.",

    "Policy":
    "A Policy is a contract between the insurer and the insured.",

    "Locker":
    "A Bank Locker provides secure storage for valuables and documents.",

    "Security":
    "Bank Security protects customer accounts and financial data.",

    "OTP":
    "OTP (One Time Password) provides additional authentication for transactions.",

    "Fraud":
    "Fraud refers to unauthorized or deceptive financial activities.",

    "Cyber Security":
    "Cyber Security protects banking systems from digital attacks.",

    "EMI":
    "EMI (Equated Monthly Installment) is a fixed monthly loan repayment amount.",

    "Credit Score":
    "A Credit Score measures an individual's creditworthiness.",

    "CIBIL":
    "CIBIL Score is a commonly used credit score in India.",

    "Mortgage":
    "A Mortgage is a loan secured against property.",

    "Collateral":
    "Collateral is an asset pledged to secure a loan.",

    "Principal":
    "Principal is the original amount deposited or borrowed.",

    "Maturity":
    "Maturity is the date when a deposit or investment completes its term.",

    "Overdraft":
    "An Overdraft allows customers to withdraw more money than available in their account.",

    "Cash Credit":
    "Cash Credit provides short-term funding for businesses.",

    "Treasury":
    "Treasury manages a bank's investments and financial assets.",

    "Mutual Fund":
    "A Mutual Fund pools money from investors and invests in securities.",

    "Investment":
    "Investment refers to allocating money to generate future returns.",

    "Stock":
    "A Stock represents ownership in a company.",

    "Bond":
    "A Bond is a debt instrument issued by governments or companies.",

    "Dividend":
    "A Dividend is a share of profits distributed to shareholders.",

    "Demat Account":
    "A Demat Account stores securities electronically.",

    "Trading Account":
    "A Trading Account enables buying and selling of securities.",

    "Foreign Exchange":
    "Foreign Exchange involves currency conversion and international payments.",

    "Forex":
    "Forex is the global market for trading currencies.",

    "SWIFT":
    "SWIFT facilitates secure international banking communications.",

    "Merchant Banking":
    "Merchant Banking provides financial advisory and investment services.",

    "Retail Banking":
    "Retail Banking serves individual customers.",

    "Corporate Banking":
    "Corporate Banking provides services to businesses and organizations.",

    "Private Banking":
    "Private Banking offers personalized financial services to high-net-worth individuals.",

    "Digital Banking":
    "Digital Banking delivers banking services through digital channels.",

    "FinTech":
    "FinTech uses technology to improve financial services and banking operations.",

    "Wallet":
    "A Digital Wallet stores funds electronically for online payments.",

    "QR Code":
    "QR Codes enable quick digital payments and transactions.",

    "POS":
    "Point of Sale terminals process card-based transactions.",

    "Merchant":
    "A Merchant accepts payments for goods and services.",

    "Payment Gateway":
    "A Payment Gateway securely processes online transactions.",

    "E-Commerce":
    "E-Commerce refers to buying and selling products online.",

    "Reconciliation":
    "Reconciliation verifies and matches financial records.",

    "Audit":
    "An Audit examines financial records and transactions.",

    "Tax":
    "Tax is a mandatory contribution imposed by governments.",

    "GST":
    "GST is a Goods and Services Tax applied to goods and services.",

    "Financial Planning":
    "Financial Planning helps individuals achieve long-term financial goals.",

    "Wealth Management":
    "Wealth Management combines investment, tax, and financial advisory services.",

    "Pension":
    "A Pension provides regular income after retirement.",

    "Retirement Planning":
    "Retirement Planning helps individuals prepare financially for retirement."
}

    topic = st.selectbox(
        "Select Topic",
        list(knowledge_base.keys())
    )

    st.info(knowledge_base[topic])

# NLP ANALYZER
elif menu == "NLP Analyzer":

    st.header("NLP Analyzer")

    text = st.text_area(
        "Enter Banking Text"
    )

    if st.button("Analyze"):

        tokens, pos_tags = process_text(text)

        entities, relations = extract_entities_relations(
            pos_tags
        )

        st.subheader("Tokens")
        st.write(tokens)

        st.subheader("POS Tags")
        st.write(pos_tags)

        st.subheader("Entities")
        st.write(entities)

        st.subheader("Relations")
        st.write(relations)

# SEMANTIC NETWORK
elif menu == "Semantic Network":

    st.header("Semantic Network")

    if st.button("Generate Semantic Network"):
        semantic_network()

        st.success(
            "Semantic Network Generated"
        )

        st.image(
            "output/advanced_banking_semantic_network.png"
        )

# EXPERT SYSTEM
elif menu == "Expert System":

    st.header("Banking Expert System")

    balance = st.number_input(
        "Enter Account Balance",
        min_value=0
    )

    if st.button("Check Eligibility"):

        if balance >= 20000:
            st.success("Loan Eligible")
        else:
            st.error("Loan Not Eligible")

        if balance >= 10000:
            st.success("FD Eligible")
        else:
            st.error("FD Not Eligible")

        if balance >= 50000:
            st.success("Credit Card Approved")
        else:
            st.error("Credit Card Rejected")

elif menu == "Chatbot":

    st.header("🤖 Banking AI Assistant")

    knowledge_base = {

    "ATM Card":
    "ATM Card allows customers to withdraw cash, check balances, transfer funds, and perform banking transactions through ATM machines.",

    "Debit Card":
    "A Debit Card allows direct access to funds from a customer's bank account for purchases and cash withdrawals.",

    "Credit Card":
    "A Credit Card allows customers to borrow money from the bank up to a specified limit and repay it later.",

    "Savings Account":
    "A Savings Account is a deposit account that helps customers save money while earning interest.",

    "Current Account":
    "A Current Account is designed for businesses and individuals who perform frequent transactions.",

    "Fixed Deposit":
    "A Fixed Deposit allows customers to deposit money for a fixed period and earn higher interest rates.",

    "Recurring Deposit":
    "A Recurring Deposit allows customers to save a fixed amount every month and earn interest.",

    "Loan":
    "A Loan is borrowed money provided by a bank that must be repaid with interest over a specific period.",

    "Home Loan":
    "A Home Loan helps customers purchase, construct, or renovate residential property.",

    "Personal Loan":
    "A Personal Loan can be used for personal financial needs without providing collateral.",

    "Education Loan":
    "An Education Loan helps students finance higher education expenses.",

    "Vehicle Loan":
    "A Vehicle Loan is used to purchase cars, bikes, or commercial vehicles.",

    "Gold Loan":
    "A Gold Loan is secured by pledging gold ornaments as collateral.",

    "UPI":
    "UPI (Unified Payments Interface) enables instant bank-to-bank money transfers using mobile devices.",

    "NEFT":
    "NEFT (National Electronic Funds Transfer) enables electronic fund transfers between banks.",

    "RTGS":
    "RTGS (Real Time Gross Settlement) supports instant high-value fund transfers.",

    "IMPS":
    "IMPS (Immediate Payment Service) provides instant money transfer services 24x7.",

    "Cheque":
    "A Cheque is a written instruction directing a bank to pay a specified amount.",

    "Demand Draft":
    "A Demand Draft is a prepaid negotiable instrument issued by a bank.",

    "Passbook":
    "A Passbook records all transactions associated with a bank account.",

    "Bank Statement":
    "A Bank Statement provides a summary of account transactions over a period.",

    "Interest":
    "Interest is the amount earned on deposits or paid on loans.",

    "Simple Interest":
    "Simple Interest is calculated only on the principal amount.",

    "Compound Interest":
    "Compound Interest is calculated on both principal and accumulated interest.",

    "Nominee":
    "A Nominee is a person authorized to receive account benefits when required.",

    "KYC":
    "KYC (Know Your Customer) verifies customer identity and prevents fraud.",

    "PAN Card":
    "PAN Card is used for tax identification and financial transactions.",

    "Aadhaar":
    "Aadhaar is a unique identification number used for KYC verification.",

    "Mobile Banking":
    "Mobile Banking allows customers to perform banking operations through smartphones.",

    "Internet Banking":
    "Internet Banking provides online access to banking services through websites.",

    "SMS Banking":
    "SMS Banking allows customers to receive account updates through text messages.",

    "Net Banking":
    "Net Banking enables customers to access banking services over the internet.",

    "Bank":
    "A Bank is a financial institution that accepts deposits, provides loans, and offers financial services.",

    "Branch":
    "A Branch is a local office of a bank where customers can perform transactions.",

    "Manager":
    "A Bank Manager supervises banking operations and customer services.",

    "Cash Deposit":
    "Cash Deposit refers to adding money into a bank account.",

    "Cash Withdrawal":
    "Cash Withdrawal refers to removing money from a bank account.",

    "Balance":
    "Balance is the amount of money available in a bank account.",

    "Minimum Balance":
    "Minimum Balance is the required amount customers must maintain in certain accounts.",

    "Transaction":
    "A Transaction is any financial activity involving deposits, withdrawals, or transfers.",

    "Fund Transfer":
    "Fund Transfer refers to moving money between accounts.",

    "Beneficiary":
    "A Beneficiary is a person or account that receives transferred funds.",

    "IFSC Code":
    "IFSC Code uniquely identifies a bank branch for electronic transactions.",

    "MICR Code":
    "MICR Code helps banks process cheques efficiently.",

    "Account Number":
    "An Account Number uniquely identifies a customer's bank account.",

    "Customer":
    "A Customer is an individual or organization using banking services.",

    "Employee":
    "A Bank Employee assists customers and performs banking operations.",

    "Insurance":
    "Insurance provides financial protection against specified risks.",

    "Life Insurance":
    "Life Insurance offers financial support to beneficiaries after the policyholder's death.",

    "Health Insurance":
    "Health Insurance covers medical and hospitalization expenses.",

    "Premium":
    "Premium is the amount paid to maintain an insurance policy.",

    "Policy":
    "A Policy is a contract between the insurer and the insured.",

    "Locker":
    "A Bank Locker provides secure storage for valuables and documents.",

    "Security":
    "Bank Security protects customer accounts and financial data.",

    "OTP":
    "OTP (One Time Password) provides additional authentication for transactions.",

    "Fraud":
    "Fraud refers to unauthorized or deceptive financial activities.",

    "Cyber Security":
    "Cyber Security protects banking systems from digital attacks.",

    "EMI":
    "EMI (Equated Monthly Installment) is a fixed monthly loan repayment amount.",

    "Credit Score":
    "A Credit Score measures an individual's creditworthiness.",

    "CIBIL":
    "CIBIL Score is a commonly used credit score in India.",

    "Mortgage":
    "A Mortgage is a loan secured against property.",

    "Collateral":
    "Collateral is an asset pledged to secure a loan.",

    "Principal":
    "Principal is the original amount deposited or borrowed.",

    "Maturity":
    "Maturity is the date when a deposit or investment completes its term.",

    "Overdraft":
    "An Overdraft allows customers to withdraw more money than available in their account.",

    "Cash Credit":
    "Cash Credit provides short-term funding for businesses.",

    "Treasury":
    "Treasury manages a bank's investments and financial assets.",

    "Mutual Fund":
    "A Mutual Fund pools money from investors and invests in securities.",

    "Investment":
    "Investment refers to allocating money to generate future returns.",

    "Stock":
    "A Stock represents ownership in a company.",

    "Bond":
    "A Bond is a debt instrument issued by governments or companies.",

    "Dividend":
    "A Dividend is a share of profits distributed to shareholders.",

    "Demat Account":
    "A Demat Account stores securities electronically.",

    "Trading Account":
    "A Trading Account enables buying and selling of securities.",

    "Foreign Exchange":
    "Foreign Exchange involves currency conversion and international payments.",

    "Forex":
    "Forex is the global market for trading currencies.",

    "SWIFT":
    "SWIFT facilitates secure international banking communications.",

    "Merchant Banking":
    "Merchant Banking provides financial advisory and investment services.",

    "Retail Banking":
    "Retail Banking serves individual customers.",

    "Corporate Banking":
    "Corporate Banking provides services to businesses and organizations.",

    "Private Banking":
    "Private Banking offers personalized financial services to high-net-worth individuals.",

    "Digital Banking":
    "Digital Banking delivers banking services through digital channels.",

    "FinTech":
    "FinTech uses technology to improve financial services and banking operations.",

    "Wallet":
    "A Digital Wallet stores funds electronically for online payments.",

    "QR Code":
    "QR Codes enable quick digital payments and transactions.",

    "POS":
    "Point of Sale terminals process card-based transactions.",

    "Merchant":
    "A Merchant accepts payments for goods and services.",

    "Payment Gateway":
    "A Payment Gateway securely processes online transactions.",

    "E-Commerce":
    "E-Commerce refers to buying and selling products online.",

    "Reconciliation":
    "Reconciliation verifies and matches financial records.",

    "Audit":
    "An Audit examines financial records and transactions.",

    "Tax":
    "Tax is a mandatory contribution imposed by governments.",

    "GST":
    "GST is a Goods and Services Tax applied to goods and services.",

    "Financial Planning":
    "Financial Planning helps individuals achieve long-term financial goals.",

    "Wealth Management":
    "Wealth Management combines investment, tax, and financial advisory services.",

    "Pension":
    "A Pension provides regular income after retirement.",

    "Retirement Planning":
    "Retirement Planning helps individuals prepare financially for retirement."
}
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:

        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    question = st.chat_input(
        "Ask a banking question..."
    )

    if question:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        answer = """
I don't have information about that topic yet.
Try asking about:

• Loan
• ATM
• UPI
• Credit Card
• Savings Account
• Insurance
• KYC
"""

        lower_question = question.lower()

        for key, value in knowledge_base.items():

            if key.lower() in lower_question:

                answer = value
                break

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

        st.rerun()
        # Search knowledge base
        for key, value in knowledge_base.items():

            if key in user_question:

                answer = value
                break

        # Save assistant response
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

        st.rerun()