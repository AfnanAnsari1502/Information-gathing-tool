import sys
import requests
import socket
import json

if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + " <url>")
    sys.exit(1)

url = sys.argv[1]
print(f"Attempting to gather information for: {url}")

try:
    req = requests.get("https://" + url)
    print("\n" + str(req.headers))
except requests.exceptions.RequestException as e:
    print(f"Error fetching headers for {url}: {e}")
    sys.exit(1)

try:
    gethostby_ = socket.gethostbyname(url)
    print("\nThe IP address of " + url + " is: " + gethostby_ + "\n")
except socket.gaierror as e:
    print(f"Error resolving IP address for {url}: {e}")
    sys.exit(1)

try:
    req_two = requests.get("https://ipinfo.io/" + gethostby_ + "/json")
    resp_ = json.loads(req_two.text)
    print("IP:", resp_["ip"])
    print("Hostname:", resp_.get("hostname", "N/A"))
    print("City:", resp_.get("city", "N/A"))
    print("Region:", resp_.get("region", "N/A"))
    print("Country:", resp_.get("country", "N/A"))
    print("Location:", resp_["loc"])
    print("Organization:", resp_.get("org", "N/A"))
    print("Timezone:", resp_.get("timezone", "N/A"))
except requests.exceptions.RequestException as e:
    print(f"Error fetching geolocation data: {e}")
