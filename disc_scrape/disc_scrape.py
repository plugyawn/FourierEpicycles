
import time
from urllib import request
import requests
from bs4 import BeautifulSoup
import re
import os
from config.definitions import ROOT_DIR


fac_link = "iitgn.ac.in/faculty/"
fac_dict = {
    "Computer Science and Engineering" : "cse",
    "Chemistry" : "chemistry",
    "Distinguished" : "dhp",
    "Civil Engineering" : "civil",
    "Mechanical Engineering" : "me",
    "Creative Learning" : "cl",
    "Physics" : "phy",
    "Design" : "design",
    "Mathematics" : "math",
    "Electrical Engineering" : "ee",
    "Earth Sciences" : "earths",
    "Biological Engineering" : "bioe",
    "Chemical Engineering" : "chemical",
    "Materials Engineering" : "mse"
}

class discipline_scrape:
    """
    Enter a discipline name to scrape it, through given functions.
    """

    def __init__(self, disc = "Computer Science and Engineering"):
        print(f"Scraper initiated. Default discipline is set to {disc}")
        print(f"Dumping scraped data to {ROOT_DIR}")
        self.fac_link = "https://" + fac_link + fac_dict[disc]

    
    def set_discipline(self, disc = "Computer Science and Engineering"):
        self.fac_link = fac_link + fac_dict[dict]

    def scrape_and_dump(self, path = ROOT_DIR):
        path_to_dump = os.path.join(path, 'data')
        soup = BeautifulSoup(requests.get(self.fac_link).text, "html.parser")
        img_tags = soup.find_all('img')
        url_list = []

        for img in img_tags:
            try:
                if img["alt"] == "Image":
                    url_list.append(img["src"])
            except:
                pass

        for url in url_list:
            filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', url)
            try:
                with open(ROOT_DIR+"/data/"+filename.group(1), 'wb') as file:
                    print(filename.group(1))
                    response = requests.get(url)
                    file.write(response.content)
            except:
                print("Skipped.")
