import requests
from bs4 import  BeautifulSoup
import re

def parse_text(url):
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html5lib')
        title = soup.title.get_text()
        search_ingredients = soup.find(class_= re.compile(".*ingredients.*"))
        search_instructions = soup.find(class_=re.compile(".*instructions.*"))
        ingredients = search_ingredients.prettify()
        instructions = search_instructions.prettify()
        recipe = {
                "title": title,
                "ingredients": ingredients,
                "instructions": instructions
                }
        return recipe
