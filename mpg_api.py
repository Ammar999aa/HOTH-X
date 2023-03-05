import pandas as pd
from fuzzywuzzy import fuzz, process
import argparse

# Read the vehicle data into a pandas DataFrame
vehicle_data = pd.read_csv('vehicles.csv', low_memory=False)
vehicle_data['make_model_year'] = vehicle_data['make'] + ' ' + vehicle_data['model'] + ' ' + vehicle_data['year'].astype(str)

# Create a command-line argument parser
parser = argparse.ArgumentParser(description='Search for the average MPG of a car make and model.')
parser.add_argument('make', type=str, help='the make of the car')
parser.add_argument('model', type=str, help='the model of the car')
parser.add_argument('year', type=int, help='the year of the car')

# Parse the arguments
args = parser.parse_args()

# Perform a fuzzy search on the vehicle data to find the closest match
vehicle_search = process.extractOne(f"{args.make} {args.model} {args.year}", vehicle_data['make_model_year'], scorer=fuzz.token_sort_ratio)

# Check if a match was found
if vehicle_search:
    # Get the index of the closest match
    vehicle_index = vehicle_data.index[vehicle_data['make_model_year'] == vehicle_search[0]][0]

    # Get the average MPG of the car
    avg_mpg = vehicle_data.loc[vehicle_index, 'highway08U']

    if avg_mpg == 0:
        # Search for the next 5 years
        for year in range(args.year+1, args.year+6):
            next_vehicle_search = process.extractOne(f"{args.make} {args.model} {year}", vehicle_data['make_model_year'], scorer=fuzz.token_sort_ratio)
            if next_vehicle_search:
                next_vehicle_index = vehicle_data.index[vehicle_data['make_model_year'] == next_vehicle_search[0]][0]
                next_avg_mpg = vehicle_data.loc[next_vehicle_index, 'highway08U']
                if next_avg_mpg != 0:
                    print(f"0 {year} {next_avg_mpg:.2f}")
                    break
        else:
            # If not found in next 5 years, search in previous 5 years
            for year in range(args.year-1, args.year-6, -1):
                prev_vehicle_search = process.extractOne(f"{args.make} {args.model} {year}", vehicle_data['make_model_year'], scorer=fuzz.token_sort_ratio)
                if prev_vehicle_search:
                    prev_vehicle_index = vehicle_data.index[vehicle_data['make_model_year'] == prev_vehicle_search[0]][0]
                    prev_avg_mpg = vehicle_data.loc[prev_vehicle_index, 'highway08U']
                    if prev_avg_mpg != 0:
                        print(f"0 {year} {prev_avg_mpg:.2f}")
                        break
            else:
                # If not found in previous 5 years, print "No mpg data found"
                print("-1 No mpg data found")
    elif vehicle_data.loc[vehicle_index, 'year'] == args.year:
        print(f"1 {avg_mpg:.2f}")
    else:
        print(f"0 {vehicle_data.loc[vehicle_index, 'year']} {avg_mpg:.2f}")
else:
    print("-1 No model found.")
