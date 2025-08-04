import requests
from bs4 import BeautifulSoup

def fetch_case_details(case_type, case_number, year):
    try:
        url = "https://services.ecourts.gov.in/ecourtindia_v6/getCaseStatus"
        payload = {
            "stateCode": "HR",        # Haryana
            "distCode": "FB",         # Faridabad
            "courtCode": "",          # leave empty to search all courts
            "caseType": case_type,
            "caseNo": case_number,
            "caseYear": year
        }

        headers = {
            "User-Agent": "Mozilla/5.0",
            "Content-Type": "application/x-www-form-urlencoded"
        }

        response = requests.post(url, data=payload, headers=headers, timeout=10)

        if response.status_code != 200:
            return {"error": "Could not reach court portal. Status code: " + str(response.status_code)}

        soup = BeautifulSoup(response.text, "html.parser")

        parties = soup.find(id="petitionerRespondent")
        case_dates = soup.find(id="caseHistoryTable")
        order_link = soup.find("a", string="View Order")

        return {
            "parties": parties.text.strip() if parties else "Not found",
            "dates": case_dates.text.strip() if case_dates else "Not available",
            "order_link": order_link["href"] if order_link else "No PDF found"
        }

    except Exception as e:
        return {"error": str(e)}
