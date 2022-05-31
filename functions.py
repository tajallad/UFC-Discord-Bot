import requests
from bs4 import BeautifulSoup

fights = []

def fetch():
    s = requests.Session()
    site = 'www.ufc.com'
    event_url = f'https://{site}/events'
    response = s.get(event_url)
    soup = BeautifulSoup(response.text,'html.parser')
    total = soup.find_all("div",attrs={"class", "althelete-total"})
    total = int(total[0].text.split()[0])
    name_elements = soup.findAll("h3",attrs={"class", "c-card-event--result__headline"})
    names = []
    for i in range(8):
        names.append(name_elements[i].text)

    time_elements = soup.findAll("div",attrs={"class", "c-card-event--result__date tz-change-data"})
    dates = []
    times = []
    cards = []
    for element in time_elements:
        strips = element.text.split("/")
        dates.append(strips[0].strip())
        times.append(strips[1].strip())
        cards.append(strips[2].strip())
    
    global fights
    counter = 0
    for i in range(len(names)):
        data = {
            "names" : names[i],
            "date" : dates[i],
            "time" : times[i],
            "card" : cards[i]
        }
        if data not in fights:
            fights.append(data)
            counter += 1
    
    return counter

def list_fights():
    if not fights:
        return None
    fight_list = []
    for fight in fights:
        data = [fight["names"], fight["date"], fight["time"], fight["card"]]
        fight_list.append(data)
    return fight_list

def refresh_list():
    fights.clear()
    return fetch()