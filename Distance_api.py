import requests
import argparse

API_KEY = "AIzaSyB7Ynu2Ee_Bnr3oOUUhQ2V2rqlL8yE_jy0"

def get_distance(start_location, end_location):
    url = f"https://maps.googleapis.com/maps/api/distancematrix/json?origins={start_location}&destinations={end_location}&units=imperial&key={API_KEY}"

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    distance = response.json()["rows"][0]["elements"][0]["distance"]["text"]

    return distance

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get the distance between two locations.")
    parser.add_argument("start_location", type=str, help="The starting location.")
    parser.add_argument("end_location", type=str, help="The ending location.")
    args = parser.parse_args()

    distance = get_distance(args.start_location, args.end_location)
    print(f"{distance}")
