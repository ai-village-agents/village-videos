from bs4 import BeautifulSoup
import os

if os.path.exists("index.html"):
    with open("index.html", "r") as f:
        soup = BeautifulSoup(f, "html.parser")
        
    cards = soup.find_all("div", class_="video-card")
    print(f"Found {len(cards)} video cards in the showcase HTML.")
    for card in cards:
        title = card.find("h2").text
        link = card.find("a")["href"]
        print(f"Verified: {title} -> {link}")
else:
    print("index.html not found.")
