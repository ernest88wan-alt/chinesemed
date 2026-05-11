import streamlit as st

# Data: Prices per 10 grams
PRICES_PER_10G = {
    "茯苓": 0.10,
    "黄芩": 0.50,
    "山药": 1.00,
    "山楂": 0.70,
    "生地": 0.80,
    "熟地": 0.90,
    "山茱萸": 1.10,
    "薏仁": 0.40,
    "白花蛇舌草": 0.60,
    "半枝莲": 0.80
}

def calculate_price(herb_name, weight_grams):
    price_per_10g = PRICES_PER_10G.get(herb_name, 0)
    # Formula: (Weight / 10) * Price_per_10g
    return (weight_grams / 10) * price_per_10g

# --- Website Layout ---
st.set_page_config(page_title="TCM Pharmacy Calculator", page_icon="🌿")

st.title("🌿 Chinese Medicine Price Calculator")
st.markdown("---")

# Session state to keep track of the prescription items
if 'prescription' not in st.session_state:
    st.session_state.prescription = []

# Sidebar for Input
with st.sidebar:
    st.header("Add Herb to Packet")
    selected_herb = st.selectbox("Select Herb (药材名称)", options=list(PRICES_PER_10G.keys()))
    weight = st.number_input("Weight in Grams (克数)", min_value=0.0, step=1.0)
    
    if st.button("Add to List"):
        if weight > 0:
            price = calculate_price(selected_herb, weight)
            st.session_state.prescription.append({
                "Herb": selected_herb,
                "Weight (g)": weight,
                "Price (RM)": round(price, 2)
            })
            st.success(f"Added {selected_herb}")

# Main Display
st.subheader("Current Packet Composition")
if st.session_state.prescription:
    # Display the list as a table
    st.table(st.session_state.prescription)
    
    # Calculate Grand Total
    total_price = sum(item["Price (RM)"] for item in st.session_state.prescription)
    
    st.markdown("---")
    st.metric(label="Total Price (总额)", value=f"RM {total_price:.2f}")
    
    if st.button("Clear Packet"):
        st.session_state.prescription = []
        st.rerun()
else:
    st.info("The packet is currently empty. Use the sidebar to add herbal medicines.")

st.markdown("""
<style>
    .stMetric { background-color: #f0f2f6; padding: 10px; border-radius: 10px; }
</style>
""", unsafe_allow_html=True)