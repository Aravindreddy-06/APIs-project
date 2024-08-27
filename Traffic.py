import requests

# OSRM API settings
BASE_URL = 'http://router.project-osrm.org/route/v1/driving'

class TrafficMonitoringSystem:
    def __init__(self):
        self.base_url = BASE_URL

    def get_route_data(self, origin, destination):
        # Construct the URL for OSRM API
        url = f"{self.base_url}/{origin};{destination}?overview=false"
        response = requests.get(url)
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: Unable to fetch data (status code: {response.status_code})")
            return None

    def display_route_data(self, data):
        if data and 'routes' in data and data['routes']:
            route = data['routes'][0]
            duration = route['duration'] / 60  # Convert seconds to minutes
            distance = route['distance'] / 1000  # Convert meters to kilometers
            
            print("Current Route Information:")
            print("--------------------------")
            print(f"Estimated Travel Time: {duration:.2f} minutes")
            print(f"Total Distance: {distance:.2f} kilometers")
            print(f"Encoded Polyline (for route): {route['geometry']}")
        else:
            print("No route data available.")

def main():
    tms = TrafficMonitoringSystem()
    
    # Get user input for origin and destination
    origin = input("Enter your starting point : ")
    destination = input("Enter your destination : ")
    
    # Get route data from the OSRM API
    data = tms.get_route_data(origin, destination)
    
    # Display the route data
    tms.display_route_data(data)

if __name__ == "__main__":
    main()
