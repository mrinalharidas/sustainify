from flask import Flask, render_template, request, send_file
from scraper import process_product_data
import csv

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/scrape", methods=["POST"])
def scrape():
    url = request.form.get("url")
    if not url:
        return "Error: No URL provided!"
    
    title, csv_file = process_product_data(url)
    if "Error" in title:
        return title

    # Read CSV data for display
    csv_data = []
    if csv_file:
        with open(csv_file, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            csv_data = [row for row in reader]

    return render_template("result.html", title=title, csv_data=csv_data)

if __name__ == "__main__":
    app.run(debug=True)
