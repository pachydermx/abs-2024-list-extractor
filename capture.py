import csv, os
from bs4 import BeautifulSoup

def get_table_data(html_file_path):
# Read the HTML file
    with open(html_file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    # Find the main div containing the table
    table_div = soup.select('.ais-Hits.grid')[0]

    # Extract rows
    rows = table_div.select('.grid.grid-cols-subgrid.col-span-full')

    # Extract data from each row
    table_data = []
    for row in rows:
        row_data = [field.get_text(strip=True) for field in row.select('.ajg-column')]
        table_data.append(row_data)
    
    return table_data

# Get all HTML files under tables directory
html_files = [f for f in os.listdir('tables') if f.endswith('.html')]
csv_file_path = 'captured.csv'
table_data = []

for html_file in html_files:
    html_file_path = os.path.join('tables', html_file)
    table_data += get_table_data(html_file_path)

# Save the data to a CSV file
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(table_data)

print(f'Table data has been saved to {csv_file_path}')