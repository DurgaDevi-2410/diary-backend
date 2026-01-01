import requests

BASE_URL = "http://127.0.0.1:8000/api"

def test_registration():
    url = f"{BASE_URL}/user/register/"
    import random
    suffix = random.randint(10000, 99999)
    payload = {
        "username": f"debuguser_{suffix}",
        "password": "debugpassword123"
    }
    print(f"Testing Register with {payload['username']}...")
    try:
        response = requests.post(url, json=payload)
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 500:
            with open("error.html", "w", encoding="utf-8") as f:
                f.write(response.text)
            print("Saved error content to error.html")
            
            # Try to grab header
            try:
                from html.parser import HTMLParser
                class TitleParser(HTMLParser):
                    def __init__(self):
                        super().__init__()
                        self.title = ""
                        self.in_title = False
                    def handle_starttag(self, tag, attrs):
                        if tag == "title": self.in_title = True
                    def handle_endtag(self, tag):
                        if tag == "title": self.in_title = False
                    def handle_data(self, data):
                        if self.in_title: self.title += data
                
                parser = TitleParser()
                parser.feed(response.text)
                print(f"Error Page Title: {parser.title}")
            except:
                pass

        elif response.status_code == 201:
            print("SUCCESS")
        else:
             print(f"FAILURE: {response.text}")

    except Exception as e:
        print(f"Exception: {e}")

if __name__ == "__main__":
    test_registration()
