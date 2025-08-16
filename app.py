import streamlit as st
from groq_rag import generate_answer

# Set page configuration with jewelry theme
st.set_page_config(
    page_title="Kalyan Jewellers FAQ Assistant", 
    layout="wide",
    page_icon="💎",
    initial_sidebar_state="expanded"
)

# Custom CSS for jewelry-themed design
st.markdown("""
<style>
    /* Main background with elegant gradient */
    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    
    /* Header styling */
    .header-container {
        background: linear-gradient(90deg, #FFD700, #FFA500, #FF8C00);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        box-shadow: 0 8px 32px rgba(255, 215, 0, 0.3);
        text-align: center;
    }
    
    .header-title {
        color: #2C1810;
        font-size: 2.5rem;
        font-weight: bold;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    .header-subtitle {
        color: #5D4E37;
        font-size: 1.2rem;
        margin-top: 0.5rem;
        font-style: italic;
    }
    
    /* Chat container styling */
    .chat-container {
        background: white;
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        border: 2px solid #FFD700;
    }
    
    /* FAQ categories styling */
    .faq-category {
        background: linear-gradient(45deg, #fff8dc, #f0f8ff);
        border-left: 4px solid #FFD700;
        padding: 1rem;
        margin: 0.5rem 0;
        border-radius: 8px;
        transition: all 0.3s ease;
    }
    
    .faq-category:hover {
        transform: translateX(5px);
        box-shadow: 0 5px 15px rgba(255, 215, 0, 0.3);
    }
    
    /* Input styling */
    .stSelectbox > div > div {
        background: linear-gradient(45deg, #fff, #f8f9fa);
        border: 2px solid #FFD700;
        border-radius: 10px;
    }
    
    .stTextInput > div > div > input {
        background: linear-gradient(45deg, #fff, #f8f9fa);
        border: 2px solid #FFD700;
        border-radius: 10px;
        color: #2C1810;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(45deg, #FFD700, #FFA500);
        color: #2C1810;
        border: none;
        border-radius: 25px;
        padding: 0.5rem 2rem;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        background: linear-gradient(45deg, #FFA500, #FF8C00);
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(255, 165, 0, 0.4);
    }
    
    /* Radio button styling */
    .stRadio > div {
        background: rgba(255, 215, 0, 0.1);
        padding: 1rem;
        border-radius: 10px;
        border: 1px solid #FFD700;
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background: linear-gradient(180deg, #2C1810, #5D4E37);
    }
    
    /* Answer container styling */
    .answer-container {
        background: linear-gradient(135deg, #fff 0%, #f8f9fa 100%);
        border: 2px solid #FFD700;
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 5px 20px rgba(255, 215, 0, 0.2);
    }
    
    /* Jewelry icons */
    .jewelry-icon {
        font-size: 1.5rem;
        margin: 0 0.5rem;
        color: #FFD700;
    }
</style>
""", unsafe_allow_html=True)

# Header section
st.markdown("""
<div class="header-container">
    <h1 class="header-title">💎 Kalyan Jewellers FAQ Assistant 💎</h1>
    <p class="header-subtitle">✨ Your trusted guide to all jewelry queries ✨</p>
</div>
""", unsafe_allow_html=True)

# List of exact section titles
titles = [
    "Rate Enquiry",
    "Making Charges / Wastage Query (VADD)",
    "Current offers",
    "Certification & Hallmarking Details",
    "Product Availability",
    "Product Customization Requests",
    "Availability Status at Specific Stores",
    "Online Purchase",
    "Scheme & Scheme Enquiry",
    "Scheme Enrolment Details",
    "Scheme Maturity",
    "Scheme Withdrawal",
    "Exchange Policy",
    "Selling Policy",
    "Billing Requests",
    "Payment Mode",
    "Regional Price Variation",
    "Store contact request",
    "Store Locator",
    "Gun Shot",
    "Goldsmith",
    "Working Hours",
    "Job / Career Enquiry",
    "Franchise/BusinessEnquiry",
    "Matrimony",
    "Gift Card / Voucher Enquiry",
    "Pre -Booking(wedding, anniversary, baby shower)",
    "Jewellery Maintenance ",
    "Donation ",
    "Customer Complaint ",
    "Gold Loan",
    "Jewel Insurance"
]

# Create main chat interface
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("### 🔍 How would you like to search?")
    
    # Search mode selection with jewelry theme
    mode = st.radio(
        "",
        ["💎 Browse Categories", "✨ Ask Directly"],
        help="Choose your preferred way to find information"
    )
    
    # Popular categories sidebar
    st.markdown("### 🌟 Popular Categories")
    popular_categories = [
        "💰 Rate Enquiry",
        "🎁 Current offers", 
        "💍 Product Availability",
        "🏪 Store Locator",
        "💳 Scheme Enquiry"
    ]
    
    for category in popular_categories:
        if st.button(category, key=f"pop_{category}"):
            # Remove emoji for actual query
            clean_category = category.split(" ", 1)[1]
            with col2:
                with st.spinner("✨ Fetching information..."):
                    answer = generate_answer(clean_category.strip())
                    st.markdown(f'<div class="answer-container">{answer}</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    
    if mode == "💎 Browse Categories":
        st.markdown("### 📂 Select a Category")
        
        # Group categories for better organization
        category_groups = {
            "💰 Pricing & Rates": ["Rate Enquiry", "Making Charges / Wastage Query (VADD)", "Regional Price Variation"],
            "🛍️ Shopping & Products": ["Current offers", "Product Availability", "Product Customization Requests", "Online Purchase"],
            "🏪 Store Services": ["Store Locator", "Store contact request", "Working Hours", "Availability Status at Specific Stores"],
            "💎 Schemes & Policies": ["Scheme & Scheme Enquiry", "Scheme Enrolment Details", "Scheme Maturity", "Scheme Withdrawal", "Exchange Policy", "Selling Policy"],
            "📋 Documentation & Billing": ["Certification & Hallmarking Details", "Billing Requests", "Payment Mode"],
            "🎯 Special Services": ["Gift Card / Voucher Enquiry", "Pre -Booking(wedding, anniversary, baby shower)", "Jewellery Maintenance", "Gold Loan", "Jewel Insurance"],
            "👥 Other Inquiries": ["Job / Career Enquiry", "Franchise/BusinessEnquiry", "Matrimony", "Gun Shot", "Goldsmith", "Donation", "Customer Complaint"]
        }
        
        selected_group = st.selectbox("Choose a category group:", list(category_groups.keys()))
        
        if selected_group:
            selected_title = st.selectbox(
                f"Select from {selected_group}:",
                category_groups[selected_group],
                help="Choose the specific topic you need help with"
            )
            
            if selected_title:
                if st.button("🔍 Get Information", key="get_info_btn"):
                    with st.spinner("✨ Fetching your answer..."):
                        answer = generate_answer(selected_title.strip())
                        st.markdown(f'<div class="answer-container">{answer}</div>', unsafe_allow_html=True)
    
    else:  # Ask Directly mode
        st.markdown("### 💬 Ask Your Question")
        st.markdown("Type any jewelry-related question or topic:")
        
        query = st.text_input(
            "",
            placeholder="e.g., gold rates, scheme details, store timings...",
            help="Enter your question in natural language"
        )
        
        if query:
            if st.button("🔍 Search", key="search_btn"):
                with st.spinner("🔍 Searching for answers..."):
                    answer = generate_answer(query.strip())
                    st.markdown(f'<div class="answer-container">{answer}</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Footer section
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 2rem; background: linear-gradient(90deg, #FFD700, #FFA500); border-radius: 10px; margin-top: 2rem;">
    <h4 style="color: #2C1810; margin: 0;">💎 Kalyan Jewellers - Trusted Since 1993 💎</h4>
    <p style="color: #5D4E37; margin: 0.5rem 0 0 0;">✨ Making your jewelry dreams come true ✨</p>
</div>
""", unsafe_allow_html=True)
