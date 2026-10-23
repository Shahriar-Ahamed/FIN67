import pandas as pd
import streamlit as st

st.set_page_config(page_title="Money Brain Dashboard", page_icon="💸", layout="wide")

# TEAM TODO: change this title to your team name
st.title("💸 Money Brain Dashboard")
st.caption("FinTech Club | All data on this page is fake")

# ---------- Fake data (nothing here is real) ----------
accounts = pd.DataFrame(
    {
        "Account": ["Checking", "Savings", "Credit Card", "Investments"],
        "Type": ["Bank", "Bank", "Credit", "Investment"],
        "Balance": [1250.40, 3400.00, -420.75, 2150.30],
    }
)

transactions = pd.DataFrame(
    {
        "Date": [
            "2026-10-01", "2026-10-02", "2026-10-03", "2026-10-05",
            "2026-10-06", "2026-10-08", "2026-10-09", "2026-10-11",
            "2026-10-12", "2026-10-14", "2026-10-15", "2026-10-17",
        ],
        "Merchant": [
            "Campus Cafe", "Streamly", "Grocery Mart", "Gas Station",
            "Pizza Place", "Textbook Store", "Streamly", "Grocery Mart",
            "Coffee Shop", "Ride Share", "Pizza Place", "Gym Membership",
        ],
        "Category": [
            "Food", "Subscriptions", "Groceries", "Transport",
            "Food", "School", "Subscriptions", "Groceries",
            "Food", "Transport", "Food", "Health",
        ],
        "Amount": [
            6.50, 11.99, 54.20, 38.00,
            18.75, 129.99, 11.99, 47.10,
            5.25, 14.80, 21.40, 25.00,
        ],
    }
)

# ---------- Summary numbers ----------
net_total = accounts["Balance"].sum()
total_spent = transactions["Amount"].sum()

col1, col2, col3 = st.columns(3)
col1.metric("Net total", f"${net_total:,.2f}")
col2.metric("Spent this month", f"${total_spent:,.2f}")
col3.metric("Number of transactions", len(transactions))

# ---------- Screens ----------
tab_accounts, tab_transactions, tab_ai, tab_security = st.tabs(
    ["Accounts", "Transactions", "Ask AI", "Security"]
)

with tab_accounts:
    st.subheader("Accounts")
    st.dataframe(accounts, use_container_width=True, hide_index=True)

with tab_transactions:
    st.subheader("Transactions")
    st.dataframe(transactions, use_container_width=True, hide_index=True)

with tab_ai:
    st.subheader("Ask AI")
    st.info("Coming in Event 3: ask questions about your spending in plain language.")

with tab_security:
    st.subheader("Security")
    st.info("Coming in Event 4: a checklist of security checks and fixes.")
