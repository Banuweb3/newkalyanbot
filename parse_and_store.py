# import re
# import pickle
# from PyPDF2 import PdfReader

# def extract_sections(pdf_path):
#     reader = PdfReader(pdf_path)
#     full_text = "\n".join(page.extract_text() for page in reader.pages if page.extract_text())

#     # Print a portion of the text for debugging
#     print("----- RAW TEXT PREVIEW -----")
#     print(full_text[:2000])
#     print("----------------------------")

#     # More flexible pattern: handles titles with or without space, colon, or newline
#     pattern = r"([A-Z][A-Za-z /&()-]{4,}Queries)(?::|\s)?\s*\n?(.*?)(?=\n[A-Z][A-Za-z /&()-]{4,}Queries(?::|\s)?\s*\n|\Z)"

#     matches = re.findall(pattern, full_text, re.DOTALL)

#     section_dict = {title.strip(): content.strip() for title, content in matches}

#     # Save for inspection
#     with open("data/debug_sections.txt", "w", encoding="utf-8") as f:
#         for title, content in section_dict.items():
#             f.write(f"{title}\n{'-'*40}\n{content}\n\n")

#     return section_dict

# if __name__ == "__main__":
#     pdf_path = "data/QueriesRateEnquiryQueries.pdf"
#     section_dict = extract_sections(pdf_path)

#     with open("data/section_dict.pkl", "wb") as f:
#         pickle.dump(section_dict, f)

#     print(f"✅ Stored {len(section_dict)} sections.")




# import re
# import pickle
# from PyPDF2 import PdfReader

# def extract_sections(pdf_path):
#     reader = PdfReader(pdf_path)
#     full_text = "\n".join(page.extract_text() for page in reader.pages if page.extract_text())

#     print("----- RAW TEXT PREVIEW -----")
#     print(full_text[:2000])
#     print("----------------------------")

#     # Use all known titles to match manually (safer than guessing by regex)
#     titles = [
#         "Rate Enquiry Queries",
#         "Making Charges / Wastage Query",
#         "Current offers Queries",
#         "Certification & Hallmarking Details Queries",
#         "Product Availability Queries",
#         "Product Customization RequestsQueries",
         
#         "Availability Status at Specific StoresQueries",
#         "Online PurchaseQueries",
#         "Scheme queries",
#         "Scheme Enquiry - General questions regarding available gold saving or jewellery purchase schemes",
#         "Scheme Enrolment Details - Requests related to joining a scheme, required documents, or eligibility",
#         "Scheme Maturity - Enquiries about the completion date, benefits, and redemption process of an ongoing scheme",
#         "Scheme Withdrawal - Questions about early exit, cancellation, or premature closure of an enrolled scheme",
#         "Exchange PolicyQueries",
#         "Selling PolicyQueries",
#         "Billing RequestsQueries",
#         "Payment ModeQueries",
#         "Regional Price Variation Queries",
#         "Store contact requestQueries",
#         "Store Locator Queries",
#         "Gun Shot Queries",
#         "GoldsmithQueries",
#         "Working HoursQueries",
#         "Job / Career EnquiryQueries",
#         "Franchise/BusinessEnquiryQueries",
#         "MatrimonyQueries",
#         "Gift Card / Voucher EnquiryQueries",
#         "Pre -Booking(wedding, anniversary, baby shower)Queries",
#         "Jewellery Maintenance queries",
#         "Donation queries",
#         "Customer Complaint queries",
#         "Gold LoanQueries"
#     ]

#     section_dict = {}
#     for i, title in enumerate(titles):
#         # Escape special regex characters in title
#         start_pattern = re.escape(title)
#         start_match = re.search(start_pattern, full_text)
#         if not start_match:
#             continue

#         start_index = start_match.start()
#         end_index = len(full_text)

#         for next_title in titles[i + 1:]:
#             next_match = re.search(re.escape(next_title), full_text[start_index + 1:])
#             if next_match:
#                 end_index = start_index + 1 + next_match.start()
#                 break

#         section_content = full_text[start_index + len(title):end_index].strip()
#         section_dict[title] = section_content

#     return section_dict

# if __name__ == "__main__":
#     pdf_path = "data/QueriesRateEnquiryQueries.pdf"
#     section_dict = extract_sections(pdf_path)

#     with open("data/section_dict.pkl", "wb") as f:
#         pickle.dump(section_dict, f)

#     print(f"✅ Stored {len(section_dict)} sections.")










# import pickle
# from PyPDF2 import PdfReader

# def extract_sections(pdf_path):
#     reader = PdfReader(pdf_path)
#     full_text = "\n".join(page.extract_text() for page in reader.pages if page.extract_text())

#     print("----- RAW TEXT PREVIEW -----")
#     print(full_text[:2000])
#     print("----------------------------")

#     # Exact section titles in order from the PDF
#     titles = [
#         "Rate Enquiry Queries",
#         "Making Charges / Wastage Query",
#         "Current offers Queries",
#         "Certification & Hallmarking Details Queries",
#         "Product Availability Queries and Product Customization RequestsQueries",
#         "Availability Status at Specific StoresQueries",
#         "Online PurchaseQueries",
#         "Scheme queries",
#         "Scheme Enquiry - General questions regarding available gold saving or jewellery purchase schemes",
#         "Scheme Enrolment Details - Requests related to joining a scheme, required documents, or eligibility",
#         "Scheme Maturity - Enquiries about the completion date, benefits, and redemption process of an ongoing scheme",
#         "Scheme Withdrawal - Questions about early exit, cancellation, or premature closure of an enrolled scheme",
#         "Exchange PolicyQueries",
#         "Selling PolicyQueries",
#         "Billing RequestsQueries",
#         "Payment ModeQueries",
#         "Regional Price Variation Queries",
#         "Store contact requestQueries",
#         "Store Locator Queries",
#         "Gun Shot Queries",
#         "GoldsmithQueries",
#         "Working HoursQueries",
#         "Job / Career EnquiryQueries",
#         "Franchise/BusinessEnquiryQueries",
#         "MatrimonyQueries",
#         "Gift Card / Voucher EnquiryQueries",
#         "Pre -Booking(wedding, anniversary, baby shower)Queries",
#         "Jewellery Maintenance queries",
#         "Donation queries",
#         "Customer Complaint queries",
#         "Gold LoanQueries"
#     ]

#     section_dict = {}
#     for i, title in enumerate(titles):
#         start_index = full_text.find(title)
#         if start_index == -1:
#             print(f"❌ Title not found: {title}")
#             continue

#         # Find where this section ends
#         end_index = len(full_text)
#         for next_title in titles[i + 1:]:
#             next_index = full_text.find(next_title, start_index + len(title))
#             if next_index != -1:
#                 end_index = next_index
#                 break

#         content = full_text[start_index + len(title):end_index].strip()
#         section_dict[title] = content

#     # Optional: Save as debug TXT
#     with open("data/debug_sections.txt", "w", encoding="utf-8") as f:
#         for title, content in section_dict.items():
#             f.write(f"{title}\n{'='*40}\n{content}\n\n")

#     return section_dict

# if __name__ == "__main__":
#     pdf_path = "data/QueriesRateEnquiryQueries.pdf"
#     section_dict = extract_sections(pdf_path)

#     with open("data/section_dict.pkl", "wb") as f:
#         pickle.dump(section_dict, f)

#     print(f"✅ Stored {len(section_dict)} sections.")























# import pickle
# from PyPDF2 import PdfReader
# import difflib

# def extract_sections(pdf_path):
#     reader = PdfReader(pdf_path)
#     full_text = "\n".join(page.extract_text() for page in reader.pages if page.extract_text())

#     print("----- RAW TEXT PREVIEW -----")
#     print(full_text[:2000])
#     print("----------------------------")

#     # Normalize spacing
#     full_text = full_text.replace('\r', '').replace('  ', ' ').replace('\n\n', '\n')

#     # Split into lines for fuzzy matching
#     lines = full_text.split('\n')

#     # Official section titles to find
#     titles = [
#         "Queries Rate Enquiry Queries",
#         "Making Charges / Wastage Query (VADD) Queries",
#         "Current offers Queries",
#         "Certification & Hallmarking Details Queries",
#         "Product Availability Queries",
#         "Product Customization RequestsQueries",
#         "Availability Status at Specific StoresQueries",
#         "Online PurchaseQueries",
#         "Scheme queries",
#         "Scheme Enquiry - General questions regarding available gold saving or jewellery purchase schemes",
#         "Scheme Enrolment Details - Requests related to joining a scheme, required documents, or eligibility",
#         "Scheme Maturity - Enquiries about the completion date, benefits, and redemption process of an ongoing scheme",
#         "Scheme Withdrawal - Questions about early exit, cancellation, or premature closure of an enrolled scheme",
#         "Exchange PolicyQueries",
#         "Selling PolicyQueries",
#         "Billing RequestsQueries",
#         "Payment ModeQueries",
#         "Regional Price Variation Queries",
#         "Store contact requestQueries",
#         "Store Locator Queries",
#         "Gun Shot Queries",
#         "GoldsmithQueries",
#         "Working HoursQueries",
#         "Job / Career EnquiryQueries",
#         "Franchise/BusinessEnquiryQueries",
#         "MatrimonyQueries",
#         "Gift Card / Voucher EnquiryQueries",
#         "Pre -Booking(wedding, anniversary, baby shower)Queries",
#         "Jewellery Maintenance queries",
#         "Donation queries",
#         "Customer Complaint queries",
#         "Gold LoanQueries"
#     ]

#     section_dict = {}
#     for i, title in enumerate(titles):
#         # Fuzzy match title with lines from the document
#         match_line = difflib.get_close_matches(title, lines, n=1, cutoff=0.6)
#         if not match_line:
#             print(f"❌ Title not found: {title}")
#             continue

#         match_text = match_line[0]
#         start_index = full_text.find(match_text)

#         # Find end index using the next matched title
#         end_index = len(full_text)
#         for next_title in titles[i + 1:]:
#             next_match = difflib.get_close_matches(next_title, lines, n=1, cutoff=0.6)
#             if next_match:
#                 next_text = next_match[0]
#                 next_index = full_text.find(next_text)
#                 if next_index > start_index:
#                     end_index = next_index
#                     break

#         section_dict[title] = full_text[start_index + len(match_text):end_index].strip()
#         print(f"✅ Stored: {title}")

#     # Save extracted sections
#     with open("data/section_dict.pkl", "wb") as f:
#         pickle.dump(section_dict, f)

#     # Optional: Write out all extracted content for manual inspection
#     with open("data/debug_sections.txt", "w", encoding="utf-8") as f:
#         for title, content in section_dict.items():
#             f.write(f"{title}\n{'='*50}\n{content}\n\n")

#     print(f"\n✅ Stored {len(section_dict)} sections.")

# if __name__ == "__main__":
#     extract_sections("data/QueriesRateEnquiryQueries.pdf")








import pickle
from PyPDF2 import PdfReader
import difflib
import os

def extract_sections(pdf_path):
    reader = PdfReader(pdf_path)
    full_text = "\n".join(page.extract_text() for page in reader.pages if page.extract_text())

    print("----- RAW TEXT PREVIEW -----")
    print(full_text[:2000])
    print("----------------------------")

    # Normalize spacing and remove unwanted characters
    full_text = full_text.replace('\r', '').replace('  ', ' ').replace('\n\n', '\n')
    lines = [line.strip() for line in full_text.split('\n') if line.strip()]

    # Master list of titles
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
        "Jewellery Maintenance",
        "Donation",
        "Customer Complaint",
        "Gold Loan"
    ]

    # Optional fallback aliases (for known mismatches)
    aliases = {
        "Product Availability Queries": "Product Availability",
        "Making Charges / Wastage Query": "Making Charges / Wastage Query (VADD) Queries"
    }

    section_dict = {}
    for i, title in enumerate(titles):
        search_title = aliases.get(title, title)
        match_line = difflib.get_close_matches(search_title, lines, n=1, cutoff=0.5)

        if not match_line:
            print(f"❌ Title not found: {title}")
            continue

        matched_heading = match_line[0]
        start_index = full_text.find(matched_heading)
        end_index = len(full_text)

        for next_title in titles[i + 1:]:
            next_search = aliases.get(next_title, next_title)
            next_line_match = difflib.get_close_matches(next_search, lines, n=1, cutoff=0.5)
            if next_line_match:
                next_matched = next_line_match[0]
                next_idx = full_text.find(next_matched)
                if next_idx > start_index:
                    end_index = next_idx
                    break

        content = full_text[start_index + len(matched_heading):end_index].strip()
        section_dict[title] = content
        print(f"✅ Stored: {title}")

    os.makedirs("data", exist_ok=True)

    # Save as Pickle
    with open("data/section_dict.pkl", "wb") as f:
        pickle.dump(section_dict, f)

    # Save as debug file
    with open("data/debug_sections.txt", "w", encoding="utf-8") as f:
        for title, content in section_dict.items():
            f.write(f"{title}\n{'=' * 50}\n{content}\n\n")

    print(f"\n✅ Stored {len(section_dict)} sections.")

if __name__ == "__main__":
    extract_sections("data/QueriesRateEnquiryQueries.pdf")
