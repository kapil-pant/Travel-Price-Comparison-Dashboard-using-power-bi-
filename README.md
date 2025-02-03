# Travel-Price-Comparison-Dashboard-using-power-bi-

 #Slide 1: Title Slide
Title: Travel Price Comparison Dashboard Using Power BI
Subtitle: Data Extraction & Visualization from Multiple Travel Websites
Presented by: kapil pant 


#Slide 2: Introduction
Objective of the Project:

To analyze and compare hotel prices across multiple travel websites.
Provide users with the best possible deals using data-driven insights.
Key Technologies Used:

Web Scraping: Requests, BeautifulSoup
Data Processing: Pandas, SQL
Visualization: Power BI

 #Slide 3: Data Collection Process
Sources of Data:
Data scraped from MakeMyTrip, Booking.com, Expedia, Agoda, Airbnb, etc.
Method Used:
Web Scraping: Extracted hotel names, prices, locations, ratings, and availability.
Challenges Faced:
Handling dynamic websites with BeautifulSoup
Avoiding bans using rotating user agents & proxies.
Data Storage:
Cleaned and stored in SQL Database / CSV files.

 #Slide 4: Data Cleaning & Transformation
Handling Missing Data:
Filled missing values and standardized price formats.
Data Transformation:
Converted multi-currency pricing into a common currency (e.g., INR/USD).
Created calculated columns (e.g., price per night, rating-weighted score).
ETL Process:
Extract → Transform → Load into Power BI.

#Slide 5: Power BI Dashboard Overview
Dashboard Features:
Interactive Filters (City, Check-in Date, Room Type, Price Range).
Dynamic Pricing Trends (Compare different websites).
Top 10 Best Deals Based on Ratings & Price.
KPI Scorecards for Price Variance & Trends.


#Slide 6: Data Visualization - Price Comparison
Key Insights:
Significant price variations across different platforms.
Seasonal pricing fluctuations.
Website with the most competitive pricing.
Visuals Used:
Bar Charts: Website-wise price comparison.
Line Charts: Price trends over time.
Table View: Hotel-wise price details across websites.

 #Slide 7: Dynamic Analysis with DAX & Measures
DAX Queries Used:
Dynamic Ranking of Websites by Price.
Average Price Calculation Per City.
Discount % Computation (Based on highest & lowest prices).
Example Measures in Power BI:
Lowest Price = MIN(Hotels[Price])
Price Variance = MAX(Hotels[Price]) - MIN(Hotels[Price])

#Slide 8: Business Impact & Use Cases
Who Can Benefit?
Travelers: Find the best hotel deals easily.
Hotel Owners: Price positioning against competitors.
Travel Agencies: Data-backed decision-making.
Potential Future Enhancements:
Predictive pricing analysis using machine learning.
AI-driven recommendations based on past bookings.

 #Slide 9: Challenges & Learnings
Challenges Faced:
Handling CAPTCHA & anti-scraping mechanisms.
Ensuring data accuracy with real-time updates.
Key Learnings:
Efficient data scraping using Selenium for dynamic websites.
Advanced Power BI techniques for enhanced visualization.

#Slide 10: Conclusion & Next Steps
Summary of Findings:
Pricing across platforms varies by 15-40%.
Some platforms offer better deals based on seasonal trends.
Next Steps:
Implement real-time price monitoring.
Expand the project to include flight price comparison.
