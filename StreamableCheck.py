from zlib import DEFLATED
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import sys

def check_link(url):
    headers = {"User-Agent": "Mozilla/5.0"}  # User-Agent
    try:
        res = requests.get(url, headers=headers, timeout=10)
    except Exception:
        # Network Errors or Timeouts (408) will be treated as VALID 
        return url, "VALID"

    if res.status_code == 404:
        return url, "DELETED"
    if res.status_code != 200:
        return url, "VALID"
    
    soup = BeautifulSoup(res.text, 'html.parser')
    text = soup.get_text(separator=' ').lower()
    
    # Error Phrases 
    phrases = [
        "this video isn't available", 
        "video not found", 
        "is not available", 
        "not available", 
        "video has been deleted", 
        "has been deleted", 
        "removed for violating", 
        "video unavailable", 
    ]
    for phrase in phrases:
        if phrase in text:
            return url, "DELETED"
    
    return url, "VALID"

def main(input_file):
    with open(input_file, 'r') as f:
        urls = [line.strip() for line in f if line.strip()]
    if not urls:
        print("No URLs found.")
        return
    
    active_links = []
    deleted_links = []
    
    # ThreadPoolExecutor (Parallel Processing)
    with ThreadPoolExecutor(max_workers=3) as executor: # Workers (Higher Values might cause Timeouts)
        for url, status in executor.map(check_link, urls):
            print(f"{url} -> {status}")
            if status == "VALID":
                active_links.append(url + "\n")
            else:
                deleted_links.append(url + "\n")
    
    # Write Outputs
    with open('Valid_Streamables.txt', 'w') as fa:
        fa.writelines(active_links)
    with open('Deleted_Streamables.txt', 'w') as fd:
        fd.writelines(deleted_links)

    print(f"\n✅  Done! | {len(active_links)} out of {len(urls)} URLs seem to be valid, while the other {len(deleted_links)} URLs seem to be deleted.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python StreamableCheck.py <Input_File>")
        sys.exit(1)
    main(sys.argv[1])
