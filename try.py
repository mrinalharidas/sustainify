import csv
from serpapi import GoogleSearch

# Define the search parameters
params = {
    "engine": "google_shopping",
    "q": "Macbook M3",
    "api_key": "5b670ebad651ae61669bb24465ba3b0a58d4b38db17dd45ae9378d4edf6b3457"
}

# Initialize the GoogleSearch object and get the results
search = GoogleSearch(params)
results = search.get_dict()

# Extract shopping results from the response
shopping_results = results.get("shopping_results", [])

# Define the header for the CSV file
csv_header = ['product_name', 'product_price', 'product_link']

# Write the results to a CSV file
with open('shopping_results.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=csv_header)
    writer.writeheader()
    
    # Iterate over the shopping results and write them to the CSV
    for product in shopping_results:
        writer.writerow({
            'product_name': product.get('title', 'N/A'),
            'product_price': product.get('price', 'N/A'),
            'product_link': product.get('product_link', 'N/A'),
        })

print("Data has been written to shopping_results.csv")
