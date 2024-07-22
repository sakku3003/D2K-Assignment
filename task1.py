import os
import requests
from retrying import retry

BASE_URL = "https://example.com/2019/"
SAVE_DIR = "/path/to/save/directory/"

MONTHS = [
    "01_Jan.csv", "02_Feb.csv", "03_Mar.csv", "04_Apr.csv",
    "05_May.csv", "06_Jun.csv", "07_Jul.csv", "08_Aug.csv",
    "09_Sep.csv", "10_Oct.csv", "11_Nov.csv", "12_Dec.csv"
]

retry_kwargs = {
    "wait_exponential_multiplier": 1000,  
    "wait_exponential_max": 10000,        
    "stop_max_attempt_number": 3          
}

@retry(**retry_kwargs)
def download_csv(url, save_path):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
    else:
        raise Exception(f"Failed to download {url}")

def main():
    os.makedirs(SAVE_DIR, exist_ok=True)
    
    for month_file in MONTHS:
        file_url = BASE_URL + month_file
        save_path = os.path.join(SAVE_DIR, month_file)
        
        try:
            download_csv(file_url, save_path)
            print(f"Downloaded {month_file} successfully")
        except Exception as e:
            print(f"Error downloading {month_file}: {str(e)}")
            continue

if __name__ == "__main__":
    main()
