import datetime
import requests

def get_google_today():
    response = requests.get("https://google.com")
    file = open("google.txt", mode="w")
    file.writelines([f"Today is {datetime.datetime.now()}\n", str(response.content)])
    


if __name__=="__main__":
    get_google_today()