Court-Data Fetcher & Mini-Dashboard

A simple Flask-based web app that allows users to fetch metadata and the latest order/judgment PDF for Indian court cases by entering the **case type**, **case number**, and **filing year**.

---

 Demo

🎥 Watch the full screen-capture walkthrough:  
👉 [Court-Data Fetcher – Demo on Loom](https://www.loom.com/share/1be4e84eaeac43fb9f0af6a54dfa7d9f?sid=2e7ad942-3d99-4276-9d8e-eaeca9e50419)

---

 🧠 Objective

Build a mini-dashboard to query Indian court case data using public portals.

This project fetches:
- Parties’ names
- Filing and next hearing dates
- Link to the latest Order/Judgment PDF

Currently supports:
- **Faridabad District Court (Haryana)**
- Uses: [eCourts Portal](https://districts.ecourts.gov.in/faridabad)

---

## 🖼 Features

✅ Simple web UI for court case lookup  
✅ Displays parties, dates, and PDF order links  
✅ Logs every query to SQLite for traceability  
✅ Handles invalid inputs with friendly messages  
✅ Clean HTML templates (no frontend framework needed)

---

💻 Tech Stack

| Layer        | Tech Stack             |
|--------------|------------------------|
| Frontend     | HTML, Flask Templates |
| Backend      | Python (Flask)         |
| Scraping     | `requests`, `BeautifulSoup` |
| Storage      | SQLite                 |
| Deployment   | Run locally or via Render |

---
 ⚙️ Setup Instructions
 1. Clone the Repository

```bash
git clone https://github.com/jonnagaddalamohansai/Court-Data-Fetcher-Mini-Dashboard.git
cd Court-Data-Fetcher-Mini-Dashboard
2. Create Virtual Environment
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate  # for Windows
# or
source venv/bin/activate  # for macOS/Linux
3. Install Requirements
bash
Copy
Edit
pip install -r requirements.txt
4. Run the Flask App
bash
Copy
Edit
python main.py
Then open http://127.0.0.1:5000 in your browser.

🧪 Sample Input
Field	Sample Value
Case Type	CS
Case Number	123
Filing Year	2023

🛠 CAPTCHA Strategy
✅ No CAPTCHA used — this project queries the eCourts backend directly via their POST endpoint:

bash
Copy
Edit
https://services.ecourts.gov.in/ecourtindia_v6/getCaseStatus
No CAPTCHA bypassing or token extraction was necessary.

📁 Project Structure
pgsql
Copy
Edit
court-data-fetcher/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── scraper.py
│   ├── db.py
│   └── templates/
│       ├── index.html
│       └── result.html
├── database.db
├── main.py
├── requirements.txt
├── .env
└── README.md