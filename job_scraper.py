def job_scraper():
    # Use requests to connect to the url and get the data
    url = "https://realpython.github.io/fake-jobs/"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Connect Successfully")
        else:
            print(response.status_code)

    except Exception as e:
        print(e)

    # Use beautifulsoup to parse the html, make it easier to read
    job_scraper_bs = bs(response.content, 'html.parser')

    # find all the cards that have the needed information
    job_scraper_bs_card = job_scraper_bs.find_all('div', {"class":"column is-half"})


    # Create empty list to store the results (There are 4 targets we need find)
    job_title, company_name, location, job_detail_page_url = [], [], [] ,[]

    for item in job_scraper_bs_card:
        try:
            title = item.find_all("h2", {"class": "title is-5"})[0].text
        except:
            title = "Not Given"
        job_title.append(title)

        try:
            name = item.find_all("h3", {"class": "subtitle is-6 company"})[0].text
        except:
            name = "Not Given"
        company_name.append(name)

        try:
            loc = item.find_all("p", {"class": "location"})[0].text.replace("\n", "").strip()
        except:
            loc = "Not Given"
        location.append(loc)

        try:
            link = item.find_all("a", {"class": "card-footer-item"})[1]['href']
        except:
            link = "Not Given"
        job_detail_page_url.append(link)


    # Creating pandas dataframe for further analysis and export
    job_dict = {
    'job_title': job_title,
    'company_name': company_name,
    'location': location,
    'job_detail_page_url': job_detail_page_url
    }

    job_list = pd.DataFrame(job_dict)

    # Export the dataframe to csv

    job_list.to_csv('job_listing.csv')


if __name__ == "__main__":
    import requests
    from bs4 import BeautifulSoup as bs
    import pandas as pd

    job_scraper()