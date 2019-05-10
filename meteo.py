import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get(
    "https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
soup = BeautifulSoup(page.content, 'html.parser')
seven_day = soup.find(id="seven_day-forecast")
forecast_items = seven_day.find_all(class_="tombstone-container")
today = forecast_items[0]


period = today.find(class_="period-name").get_text()
short_desc = today.find(class_="short-desc").get_text()
temp = today.find(class_="temp").get_text()
print(period)

img = today.find("img")
print(img)
desc = img['title']

period_tags = seven_day.select(".tombstone-container .periode-name")
#pour chaque element pt de notre liste periode_tags on applique pt.get_text()
periods = [pt.get_text() for pt in period_tags]
short_desc = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
descs = [d['title'] for d in seven_day.select(".tombstone-container img")]
print(short_desc)


weather = pd.DataFrame({
    "periode" : periods,
    "short_desc": short_desc,
    "temp": temps,
    "desc": descs
})