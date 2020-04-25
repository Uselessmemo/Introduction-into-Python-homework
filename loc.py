import requests

def get_loc():
    return requests.get("https://freegeoip.live/json/").json()

if __name__=="__main__":
    print(get_loc())