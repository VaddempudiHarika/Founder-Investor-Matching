# Founder-Investor Matching AI Model

## Overview
This project implements an AI-driven system to match startup founders with potential investors based on compatibility criteria. The model analyzes investor preferences and founder requirements to generate a match score and ranks investors accordingly.

## Features
- Loads investor data from a JSON or Excel file.
- Utilizes Google Gemini AI for advanced data processing.
- Matches investors with founders based on industry, startup stage, and funding requirements.
- Displays ranked investors along with their match scores and details.

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.x
- Google Generative AI SDK
- Pandas

### Install Dependencies
```sh
pip install google-generativeai pandas
```

## Usage
### Upload Dataset
Run the script and upload a dataset in JSON or Excel format containing investor information.

### Execute Matching
The script automatically:
1. Loads and preprocesses the dataset.
2. Matches founders with investors.
3. Ranks and displays results based on match scores.

### Running the Script
```sh
python founder_investor_matching.py
```

## Input Format
The dataset should contain investor details such as:
- Name
- Industry
- Stage
- Cheque_range (Investment range)
- Website

Example JSON Structure:
```json
[
  {
    "Name": "Investor A",
    "Industry": "Technology",
    "Stage": "Seed",
    "Cheque_range": "$100K - $500K",
    "Website": "https://investora.com"
  }
]
```

## Output
The script returns a ranked list of investors with the following details:
- Name
- Match Score
- Website
- Cheque Size
- Stage
- Industry

Example Output:
```
Investor: Investor A
Match Score: 3
Website: https://investora.com
Cheque Size: $100K - $500K
Stage: Seed
Industry: Technology
---------------------------------
```

## Future Improvements
- Improve AI-driven scoring with more advanced natural language processing.
- Integrate a web-based interface for user-friendly interactions.
- Enhance data validation and handling of complex investment structures.

## License
This project is open-source under the MIT License.

## Contributors
- Your Name

## Contact
For any inquiries, reach out at [your.email@example.com](mailto:your.email@example.com).

