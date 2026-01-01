import requests
import json

BASE_URL = "http://127.0.0.1:8000/api"

def test_entry_flow():
    # 1. Register/Login
    username = "debug_entry_user_02"
    password = "password123"
    
    # Try login first to see if user exists, else register
    token_url = f"{BASE_URL}/token/"
    token_resp = requests.post(token_url, json={"username": username, "password": password})
    
    token = None
    if token_resp.status_code == 200:
        token = token_resp.json()['access']
    else:
        # Register
        reg_url = f"{BASE_URL}/user/register/"
        requests.post(reg_url, json={"username": username, "password": password})
        # Login again
        token_resp = requests.post(token_url, json={"username": username, "password": password})
        if token_resp.status_code == 200:
            token = token_resp.json()['access']
    
    if not token:
        print("Could not get token. Aborting.")
        return

    # 2. Try Create Entry
    entry_url = f"{BASE_URL}/entries/"
    headers = {"Authorization": f"Bearer {token}"}
    payload = {
        "title": "Debug Entry",
        "content": "This is a test content.",
        "mood": "Happy"
    }
    
    print(f"Testing Create Entry...")
    try:
        resp = requests.post(entry_url, json=payload, headers=headers)
        print(f"Status: {resp.status_code}")
        if resp.status_code == 500:
            print("Captured 500 Error HTML.")
            with open("entry_error.html", "w", encoding="utf-8") as f:
                f.write(resp.text)
            
             # Try to grab traceback from Django debug page
            if "Traceback" in resp.text:
                 # Find the exception line
                 import re
                 match = re.search(r"<th>Exception Value:</th>\s*<td><pre>(.*?)</pre>", resp.text, re.DOTALL)
                 if match:
                     print(f"Exception Value: {match.group(1)}")
                 else:
                     print("Could not parse exception value.")
                     print("First 500 chars of response:")
                     print(resp.text[:500])
        elif resp.status_code == 201:
            print("Success! Entry created.")
        else:
            print(f"Failed with {resp.status_code}")
            print(resp.text)

    except Exception as e:
        print(f"Test Exception: {e}")

if __name__ == "__main__":
    test_entry_flow()
