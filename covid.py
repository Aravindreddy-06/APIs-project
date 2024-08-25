import requests

# API settings
BASE_URL = "https://disease.sh/v3/covid-19"

class CovidStatsTracker:
    def __init__(self):
        self.base_url = BASE_URL

    def get_covid_data(self, region):
        # Construct the URL based on the region type
        url = f"{self.base_url}/countries/{region}" if not region.isalpha() else f"{self.base_url}/countries/{region}"
        response = requests.get(url)
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: Unable to fetch data (status code: {response.status_code})")
            return None

    def display_covid_data(self, data):
        if data:
            country = data.get('country', 'Unknown')
            cases = data.get('cases', 'N/A')
            recovered = data.get('recovered', 'N/A')
            deaths = data.get('deaths', 'N/A')
            
            print("Current COVID-19 Statistics:")
            print("----------------------------")
            print(f"Region: {country}")
            print(f"Total Cases: {cases}")
            print(f"Total Recoveries: {recovered}")
            print(f"Total Deaths: {deaths}")
        else:
            print("No COVID-19 data available.")

def main():
    tracker = CovidStatsTracker()
    
    # Get user input for region
    region = input("Enter a country name : ")
    
    # Fetch COVID-19 data
    data = tracker.get_covid_data(region)
    
    # Display the COVID-19 data
    tracker.display_covid_data(data)

if __name__ == "__main__":
    main()
