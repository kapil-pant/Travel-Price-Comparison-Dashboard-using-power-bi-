import requests
import time
import csv
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

# Define the URL
url = "https://www.makemytrip.com/hotels/hotel-listing/?checkin=01312025&city=CTKUU&checkout=02012025&roomStayQualifier=1e0e&locusId=CTKUU&country=IN&locusType=city&searchText=Manali&regionNearByExp=3&rsc=1e1e0e"

# Create a session
session = requests.Session()

# Set up headers with a dynamic User-Agent
headers = {
    'User-Agent': UserAgent().random,  # Randomized user agent
    'accept-encoding': 'gzip, deflate, br, zstd',
    'accept-language': 'en-US,en;q=0.9',
    'referer': 'https://www.makemytrip.com/',
}

# Delay to avoid rate-limiting
time.sleep(2)

# Make the request
response = session.get(url, headers=headers)

# Check if the response is successful
if response.status_code == 200:
    print("Successfully accessed the website.")
    
    # Save HTML response to a file
    with open("file.html", "w", encoding="utf-8") as f:
        f.write(response.text)
    print("HTML content saved to file.html")
else:
    print(f"Error accessing website. Status code: {response.status_code}")
    exit()

# -------- Step 2: Parse the saved HTML file with BeautifulSoup -------- #

# Read the saved HTML file
with open("file.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Extract hotel details
hotels = soup.find_all("div", class_="latoBlack font16 blackText appendRight10 listingHotelName")  # Update class name based on actual HTML structure

# Open a CSV file to save the extracted data
with open("hotels.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Hotel Name", "Price", "Rating"])  # CSV Headers

    for hotel in hotels:
        # Extract hotel name
        name = hotel.find("h3", class_="latoBlack font16 blackText appendRight10 listingHotelName")
        name = name.text.strip() if name else "N/A"

        # Extract price
        price = hotel.find("p", class_="latoBlack blackText appendBottom3 font20")
        price = price.text.strip() if price else "N/A"

        # Extract rating
        rating = hotel.find("span", class_="blueBg whiteText font12 latoBlack padding3_5 appendRight5")
        rating = rating.text.strip() if rating else "N/A"

        # Write to CSV file
        writer.writerow([name, price, rating])

print("Data successfully saved to hotels.csv!")
