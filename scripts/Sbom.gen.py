import requests

OCTOPUS_SERVER = "https://octopus.company.com"
API_KEY = "API-XXXXXXXXXXXXXXXXX"
PROJECT_ID = "Projects-123"
FILE_PATH = "sbom.json"

url = f"{OCTOPUS_SERVER}/api/artifacts?overwriteMode=OverwriteExisting"
headers = {"X-Octopus-ApiKey": API_KEY}
files = {
    "file": open(FILE_PATH, "rb"),
    "project": (None, PROJECT_ID),
    "name": (None, "sbom.json")
}

response = requests.post(url, headers=headers, files=files)

if response.status_code == 201:
    print("✅ SBOM uploaded successfully to Octopus")
else:
    print(f"❌ Upload failed: {response.status_code} {response.text}")

