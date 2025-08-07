



import streamlit as st
from groq_rag import generate_answer

# Set layout and title only once
# port = int(os.environ.get("PORT", 8501))
st.set_page_config(page_title="Kalyan FAQ Chatbot", layout="centered")
st.title("💬 Kalyan Jewellers FAQ Chatbot")

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
    "Scheme queries",
    "Scheme Enquiry",
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
    "Gold Loan"
]

# User chooses how to search
mode = st.radio("🔎 Choose input method:", ["Select from list", "Type your own"])

if mode == "Select from list":
    selected_title = st.selectbox("📂 Select a section title to view FAQs:", titles)
    if selected_title:
        with st.spinner("Fetching FAQs..."):
            answer = generate_answer(selected_title.strip())
            st.markdown(answer)
else:
    query = st.text_input("💬 Enter section title manually:")
    if query:
        with st.spinner("Searching..."):
            answer = generate_answer(query.strip())
            st.markdown(answer)



























# import streamlit as st
# from groq_rag import generate_answer

# st.set_page_config(page_title="Kalyan FAQ Chatbot", layout="centered")
# st.title("📒 Kalyan Jewellers Section FAQ Bot")
# st.markdown("Ask by title: _e.g._ `Scheme Queries`, `Goldsmith Queries`, `Product Availability`")

# query = st.text_input("🔍 Enter section title:")
# if query:
#     with st.spinner("Searching..."):
#         answer = generate_answer(query.strip())
#         st.markdown(answer)







# import streamlit as st
# from groq_rag import generate_answer

# # Exact section titles from the PDF
# titles = [
#     "Rate Enquiry",
#     "Making Charges / Wastage Query (VADD)",
#     "Current offers",
#     "Certification & Hallmarking Details",
#     "Product Availability",
#     "Product Customization Requests",
#     "Availability Status at Specific Stores",
#     "Online Purchase",
#     "Scheme queries",
#     "Scheme Enquiry",
#     "Scheme Enrolment Details",
#     "Scheme Maturity",
#     "Scheme Withdrawal",
#     "Exchange Policy",
#     "Selling Policy",
#     "Billing Requests",
#     "Payment Mode",
#     "Regional Price Variation",
#     "Store contact request",
#     "Store Locator",
#     "Gun Shot",
#     "Goldsmith",
#     "Working Hours",
#     "Job / Career Enquiry",
#     "Franchise/BusinessEnquiry",
#     "Matrimony",
#     "Gift Card / Voucher Enquiry",
#     "Pre -Booking(wedding, anniversary, baby shower)",
#     "Jewellery Maintenance ",
#     "Donation ",
#     "Customer Complaint ",
#     "Gold Loan"
# ]

# st.set_page_config(page_title="Kalyan FAQ Chatbot", layout="centered")
# st.title("💬 Kalyan Jewellers FAQ Chatbot")

# # Dropdown selection
# selected_title = st.selectbox("📂 Select a section title to view FAQs:", titles)

# if selected_title:
#     with st.spinner("Fetching FAQs..."):
#         answer = generate_answer(selected_title.strip())
#         st.markdown(answer)








# # import streamlit as st
# # from sentence_transformers import SentenceTransformer
# # import numpy as np
# # from groq_rag import generate_answer

# # # Load embedding model
# # model = SentenceTransformer("all-MiniLM-L6-v2")

# # # Known section titles
# # titles = [
# #     "Queries Rate Enquiry Queries",
# #     "Making Charges / Wastage Query (VADD) Queries",
# #     "Current offers Queries",
# #     "Certification & Hallmarking Details Queries",
# #     "Product Availability Queries",
# #     "Product Customization RequestsQueries",
# #     "Availability Status at Specific StoresQueries",
# #     "Online PurchaseQueries",
# #     "Scheme queries",
# #     "Scheme Enquiry - General questions regarding available gold saving or jewellery purchase schemes",
# #     "Scheme Enrolment Details - Requests related to joining a scheme, required documents, or eligibility",
# #     "Scheme Maturity - Enquiries about the completion date, benefits, and redemption process of an ongoing scheme",
# #     "Scheme Withdrawal - Questions about early exit, cancellation, or premature closure of an enrolled scheme",
# #     "Exchange PolicyQueries",
# #     "Selling PolicyQueries",
# #     "Billing RequestsQueries",
# #     "Payment ModeQueries",
# #     "Regional Price Variation Queries",
# #     "Store contact requestQueries",
# #     "Store Locator Queries",
# #     "Gun Shot Queries",
# #     "GoldsmithQueries",
# #     "Working HoursQueries",
# #     "Job / Career EnquiryQueries",
# #     "Franchise/BusinessEnquiryQueries",
# #     "MatrimonyQueries",
# #     "Gift Card / Voucher EnquiryQueries",
# #     "Pre -Booking(wedding, anniversary, baby shower)Queries",
# #     "Jewellery Maintenance queries",
# #     "Donation queries",
# #     "Customer Complaint queries",
# #     "Gold LoanQueries"
# # ]

# # # Precompute embeddings
# # title_embeddings = model.encode(titles)

# # # UI setup
# # st.set_page_config(page_title="Kalyan FAQ Chatbot", layout="centered")
# # st.title("💬 Kalyan Jewellers FAQ Chatbot")

# # # Search input
# # search_input = st.text_input("🔍 Enter any keyword or query:").strip()

# # matched_title = None
# # if search_input:
# #     # Embed the search query
# #     query_emb = model.encode([search_input])[0]
# #     sims = np.dot(title_embeddings, query_emb) / (
# #         np.linalg.norm(title_embeddings, axis=1) * np.linalg.norm(query_emb)
# #     )

# #     # Get best match
# #     best_idx = int(np.argmax(sims))
# #     if sims[best_idx] > 0.5:
# #         matched_title = titles[best_idx]
# #         st.success(f"✅ Matched section: **{matched_title}** (score: {sims[best_idx]:.2f})")
# #     else:
# #         st.warning("❌ No relevant section found based on keyword.")

# # # Manual dropdown fallback
# # st.markdown("Or select a section manually:")
# # selected_title = st.selectbox("📂 FAQ Section Titles:", sorted(titles))

# # # Final query (search match takes priority)
# # final_query_title = matched_title if matched_title else selected_title

# # if final_query_title:
# #     with st.spinner("📄 Fetching answer..."):
# #         answer = generate_answer(final_query_title)
# #         st.markdown(answer)





# # import streamlit as st
# # import pickle
# # import numpy as np
# # from sentence_transformers import SentenceTransformer
# # from groq_rag import generate_answer

# # # Load embedding model
# # model = SentenceTransformer("all-MiniLM-L6-v2")

# # # Load section titles + content
# # with open("data/section_dict.pkl", "rb") as f:
# #     section_dict = pickle.load(f)

# # titles = list(section_dict.keys())
# # texts = list(section_dict.values())
# # text_embeddings = model.encode(texts)

# # # UI setup
# # st.set_page_config(page_title="Kalyan FAQ Chatbot", layout="centered")
# # st.title("💬 Kalyan Jewellers FAQ Chatbot")

# # # Search bar
# # search_input = st.text_input("🔍 Enter any keyword or query:").strip()
# # matched_title = None

# # if search_input:
# #     query_emb = model.encode([search_input])[0]
# #     sims = np.dot(text_embeddings, query_emb) / (
# #         np.linalg.norm(text_embeddings, axis=1) * np.linalg.norm(query_emb)
# #     )
# #     best_idx = int(np.argmax(sims))
# #     best_score = sims[best_idx]

# #     if best_score > 0.6:
# #         matched_title = titles[best_idx]
# #         st.success(f"✅ Matched section: **{matched_title}** (score: {best_score:.2f})")
# #     else:
# #         st.warning("❌ No highly relevant section found. Try another keyword or use the dropdown.")

# # # Manual dropdown fallback
# # st.markdown("Or select a section manually:")
# # selected_title = st.selectbox("📂 FAQ Section Titles:", sorted(titles))

# # # Final query (search result has priority)
# # final_query_title = matched_title if matched_title else selected_title

# # if final_query_title:
# #     with st.spinner("📄 Fetching answer..."):
# #         answer = generate_answer(final_query_title)
# #         st.markdown(answer)








