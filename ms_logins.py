from bs4 import BeautifulSoup
from pprint import pprint

list_id = 0
events = []

soup = BeautifulSoup(open("microsoft_login_history.txt", encoding="utf8"), features="html.parser")

for event in soup.find_all("div", {"data-nuid": "ActivityGroup"}):
    new_event = {}
    new_event['id'] = list_id
    
    new_event['date'] = event.find("div", {"data-nuid": "GroupDate"}).text
    new_event['type'] = event.find("span", {"data-nuid": "GroupType"}).text
    if new_event['type'] != "Automatic Sync":
        new_event['location'] = event.find("div", {"data-nuid": "GroupLocation"}).text
        new_event['os'] = event.find("span", {"data-bind": "text: os"}).text
        new_event['browser'] = event.find("span", {"data-bind": "text: browser"}).text
        new_event['ip'] = event.find("span", {"data-bind": "text: ip"}).text
        try:
            new_event['desc'] = event.find("span", {"data-bind": "text: desc"}).text
        except:
            new_event['desc'] = ""
        if new_event['type'] == "Successful sign-in":
            new_event['activity'] = event.find("span", {"data-nuid": "ActivityList"}).text
        elif new_event['type'] == "Unsuccessful sign-in":
            new_event['activity'] = event.find("span", {"data-nuid": "ActivityType"}).text
        events.append(new_event)
        
    list_id += 1

locations = {}
oses = {}
browsers = {}
ips = {}
activities = {}

for event in events:
    if event['type'] == 'Unsuccessful sign-in':
        if event['location'] not in locations:
            locations[event['location']] = 1
        else:
            locations[event['location']] += 1
        if event['os'] not in oses:
            oses[event['os']] = 1
        else:
            oses[event['os']] += 1
        if event['browser'] not in browsers:
            browsers[event['browser']] = 1
        else:
            browsers[event['browser']] += 1
        if event['ip'] not in ips:
            ips[event['ip']] = 1
        else:
            ips[event['ip']] += 1
        if event['activity'] not in activities:
            activities[event['activity']] = 1
        else:
            activities[event['activity']] += 1

print("====================================================")
print(f"Total events: {len(events)+1}")
print("====================================================")
print("Locations")
print("---------")
#for k, v in locations.items():
for k, v in sorted(locations.items(), key=lambda item: item[1], reverse=True):
    print(f"{k}: {v}")
print("====================================================")
print("Operating systems")
print("-----------------")
#for k, v in oses.items():
for k, v in sorted(oses.items(), key=lambda item: item[1], reverse=True):
    print(f"{k}: {v}")
print("====================================================")
print("Browsers")
print("--------")
#for k, v in browsers.items():
for k, v in sorted(browsers.items(), key=lambda item: item[1], reverse=True):
    print(f"{k}: {v}")
print("====================================================")
print("IP addresses")
print("------------")
#for k, v in ips.items():
for k, v in sorted(ips.items(), key=lambda item: item[1], reverse=True):
    print(f"{k}: {v}")
print("====================================================")
print("Activities")
print("----------")
#for k, v in activities.items():
for k, v in sorted(activities.items(), key=lambda item: item[1], reverse=True):
    print(f"{k}: {v}")
print("====================================================")
