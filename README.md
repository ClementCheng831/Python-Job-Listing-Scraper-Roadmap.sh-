# Fake-Jobs Scraper

A lightweight Python web scraper designed to extract job listings from the Real Python fake jobs test site. The script fetches the HTML content, parses relevant data points using BeautifulSoup, and exports the structured data into a clean CSV file.

This project is built as a solution to the [Job Listings Scraper](https://roadmap.sh/projects/job-listings-scraper) challenge on roadmap.sh.

## Features

* **Robust Connection Handling:** Utilizes `requests` with exception handling to ensure seamless connectivity.
* **Targeted Data Extraction:** Extracts 4 key data fields per job listing:
    * Job Title
    * Company Name
    * Location (cleaned of whitespace and newlines)
    * Job Detail Page URL
* **Error Tolerance:** Individual try-except blocks ensure that if a single field is missing from a card, the scraper defaults to `"Not Given"` instead of crashing.
* **Automated Export:** Organizes the data using `pandas` and exports it directly to a `job_listing.csv` file.

---

## Project Info & Context

This project is part of the backend/scripting developer challenges. 
* **Project Specifications:** [roadmap.sh - Job Listings Scraper](https://roadmap.sh/projects/job-listings-scraper)
* **Target Scraping URL:** [Real Python Fake Jobs](https://realpython.github.io/fake-jobs/)

---

## Prerequisites

Before running the script, ensure you have Python 3.x installed. You will also need to install the required external libraries.

### Required Libraries:
* `requests` — To send HTTP requests and fetch page content.
* `beautifulsoup4` — To parse HTML data.
* `pandas` — To structure data into a DataFrame and export it to CSV.

---

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git)
   cd YOUR_REPOSITORY_NAME
