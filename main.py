import google.generativeai as genai
import pandas as pd
import io
from google.colab import files

print("Upload dataset (JSON or Excel).")
uploaded = files.upload()
file_name = list(uploaded.keys())[0]

if file_name.endswith('.json'):
    investors_data = pd.read_json(io.BytesIO(uploaded[file_name]))
elif file_name.endswith('.xlsx'):
    investors_data = pd.read_excel(io.BytesIO(uploaded[file_name]), sheet_name='Sheet1')
else:
    raise ValueError("Unsupported format. Upload JSON or Excel.")

print("Dataset Loaded:")
print(investors_data.head())

genai.configure(api_key='YOUR_GEMINI_API_KEY')

founder_profile = {
    "Industry": "Information Technology & Services",
    "Startup Stage": "Seed",
    "Funding Required": "$500K",
    "Traction": "Early revenue",
    "Business Model": "SaaS"
}

def calculate_match_score(founder, investor):
    score = 0
    if founder["Industry"] in investor["Industry"]:
        score += 1
    if founder["Startup Stage"] in investor["Stage"]:
        score += 1
    try:
        funding_range = investor["Cheque_range"].replace('$', '').strip()
        if not funding_range:
            return score
        investor_min, investor_max = map(lambda x: int(x.replace('K', '000').replace('M', '000000')), funding_range.split(' - '))
        founder_funding = int(founder["Funding Required"].replace('$', '').replace('K', '000').replace('M', '000000'))
        if investor_min <= founder_funding <= investor_max:
            score += 1
    except Exception as e:
        print(f"Error processing {investor['Name']}: {e}")
    return score

def find_matching_investors(founder, investors):
    matches = []
    for _, investor in investors.iterrows():
        match_score = calculate_match_score(founder, investor)
        if match_score > 0:
            matches.append({
                "Name": investor["Name"],
                "Match Score": match_score,
                "Website": investor["Website"],
                "Cheque Size": investor["Cheque_range"],
                "Stage": investor["Stage"],
                "Industry": investor["Industry"]
            })
    return sorted(matches, key=lambda x: x["Match Score"], reverse=True)

matching_investors = find_matching_investors(founder_profile, investors_data)

print("\nMatching Investors:")
for investor in matching_investors:
    print(f"Investor: {investor['Name']}")
    print(f"Match Score: {investor['Match Score']}")
    print(f"Website: {investor['Website']}")
    print(f"Cheque Size: {investor['Cheque Size']}")
    print(f"Stage: {investor['Stage']}")
    print(f"Industry: {investor['Industry']}")
    print("-" * 40)
