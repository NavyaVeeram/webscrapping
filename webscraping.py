#import 
import requests
import pandas as pd
from bs4 import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler

def scrape_website():
    # Scraping the data
    response = requests.get("https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=phones&_sacat=0")
    soup = BeautifulSoup(response.content, 'html.parser')

    names = soup.find_all('div', class_="s-item__title")
    name = []
    for i in names[0:30]:
        d = i.get_text()
        name.append(d)
    print(name)

    prices = soup.find_all('span', class_="s-item__price")
    price = []
    for i in prices[0:30]:
        d = i.get_text()
        price.append(d)
    print(price)

    reviews = soup.find_all('span', class_="s-item__reviews-count")
    review = []
    for i in reviews[0:30]:
        d = i.get_text()
        review.append(d)
    print(review)

    solded = soup.find_all('span', class_="BOLD")
    sold = []
    for i in solded[0:30]:
        d = i.get_text()
        sold.append(d)
    print(sold)

    features = soup.find_all('div', class_="s-item__subtitle")
    feature = []
    for i in features[0:30]:
        d = i.get_text()
        feature.append(d)
    print(feature)

    links = soup.find_all('a')
    link = []
    for i in links[0:30]:
        d = i['href']
        link.append(d)
    print(link)

    images = soup.find_all('img')
    image = []
    for i in images[0:30]:
        d = i['src']
        image.append(d)
    print(image)

    data = {
        'Names': name,
        "Prices": price,
        "Reviews": review,
        "Solded": sold,
        "Features": feature,
        "Links": link,
        "Images": image,
    }
    print(data)
    df = pd.DataFrame(data)
    df.to_csv("Mobiles_data.csv")
    print("Dataset updated successfully.")

# Create a scheduler
scheduler = BlockingScheduler()

# Schedule the scraping job to run every day at a specific time (adjust as needed)
scheduler.add_job(scrape_website, 'cron', hour=12, minute=0)

try:
    print("Press Ctrl+C to exit.")
    scheduler.start()
except KeyboardInterrupt:
    print("Scheduler stopped manually.")

