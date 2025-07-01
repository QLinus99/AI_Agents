"""
from duckduckgo_search import DDGS
import time

def simple_search(query, max_results=5):
    tries = 3
    delay = 2 

    for attempt in range(tries):
        try:
            with DDGS() as ddgs:
                results = ddgs.text(query, max_results=max_results)
                for result in results:
                    print(f"Title: {result['title']}")
                    print(f"Link: {result['href']}\n")
            return
        except Exception as e:
            print(f"Attempt {attempt+1} failed: {e}")
            time.sleep(delay)

simple_search("How many countries have a king?")
"""

# --------------------------------------------------------------------------------------------------------------------
# second approach

"""
from bs4 import BeautifulSoup
import requests


URL = 'https://www.e-works.co.uk/'
response = requests.get(URL)
html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')

rows = soup.find_all('tr', class_='athing')

for row in rows:
    titleline = row.find('span', class_='titleline')
    link_tag = titleline.find('a', href=True)

    title = link_tag.text
    link = link_tag['href']

    visible_link_tag = row.find('span', class_='sitestr')
    visible_link = visible_link_tag.text if visible_link_tag else "No visible link"

    print("Title:", title)
    print("")
    print("Link:", link)
    print("")
    print("Visible Link:", visible_link)
    print('---')
"""


# ------------------------------------------------------------------------------------------------------------------------
# thrid approach via API key
# SerpAPI, free plan with 100 searches/month

import os
from dotenv import load_dotenv
from serpapi import GoogleSearch


load_dotenv(dotenv_path="/home/linus/Documents/VS_Code/AI_Agents/keys.env")

def get_search_results(query):
    params = {
        "q": query,
        "location": "Germany",
        "hl": "en",
        "gl": "de",
        "google_domain": "google.com",
        "api_key": os.getenv("SERPAPI_API_KEY")
    }
    search = GoogleSearch(params)
    return search.get_dict()

results = get_search_results("Rostock")
print(results)

