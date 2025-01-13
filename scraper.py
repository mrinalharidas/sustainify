import os
import csv
from serpapi import GoogleSearch
import requests
from bs4 import BeautifulSoup
import google.generativeai as genai

# Configure Google Generative AI
genai.configure(api_key="AIzaSyA5CE1G5QOM5NuWbum8ZTJ8FudHYeIEuYk")
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}
model = genai.GenerativeModel(
    model_name="gemini-2.0-flash-exp",
    generation_config=generation_config,
)

# Function to scrape the product title
def scrape_title(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.find("title").text.strip()
        return title
    except Exception as e:
        return f"Error: {str(e)}"

# Function to process data with Generative AI and Google Shopping
def process_product_data(url):
    # Step 1: Scrape the product title
    title = scrape_title(url)
    if "Error" in title:
        return title, None

    # Step 2: Use Generative AI to determine the product type
    chat_session = model.start_chat(
        history=[
            {
                "role": "user",
                "parts": [
                    "product type or genre recognition from a given title from a shopping website \n"
                    "only want a single word or at max two word answer",
                ],
            }
        ]
    )
    ai_response = chat_session.send_message(title).text.strip()

    # Step 3: Use AI response to perform a Google Shopping search
    params = {
        "engine": "google_shopping",
        "q": ai_response + " sustainable",
        "api_key": "5b670ebad651ae61669bb24465ba3b0a58d4b38db17dd45ae9378d4edf6b3457",
    }
    search = GoogleSearch(params)
    results = search.get_dict().get("shopping_results", [])

    # Step 4: Write results to a CSV file
    csv_file = "results.csv"
    csv_header = ['product_name', 'product_price', 'product_link']
    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=csv_header)
        writer.writeheader()
        for product in results:
            writer.writerow({
                'product_name': product.get('title', 'N/A'),
                'product_price': product.get('price', 'N/A'),
                'product_link': product.get('product_link', 'N/A'),
            })

    return title, csv_file
