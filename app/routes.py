from flask import Blueprint, render_template, request
from .scraper import fetch_case_details
from .db import log_query

main = Blueprint("main", __name__)

@main.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@main.route("/fetch", methods=["POST"])
def fetch():
    case_type = request.form["case_type"]
    case_number = request.form["case_number"]
    filing_year = request.form["filing_year"]

    result = fetch_case_details(case_type, case_number, filing_year)
    log_query(case_type, case_number, filing_year, result)
    
    return render_template("result.html", data=result)
