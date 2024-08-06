import requests
from bs4 import BeautifulSoup
import os
from support import extract_between
def extract_text_from_webpage(url):
    # Fetch the webpage content
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code != 200:
        return f"Failed to fetch the webpage. Status code: {response.status_code}"
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract all text from the parsed HTML
    text = soup.get_text()
    
    return text

# URL of the webpage to extract text from




sutras = [47,72,43,42,29,47,30,28,34,42,55,20,35,27,20,24,28,78] 
for i in range(0,len(sutras)) :
    os.makedirs(f"{i+1}", exist_ok=True)
    for j in range(0,sutras[i]) :
        file_path = os.path.join(f"{i+1}", f"{i+1}-{j+1}.txt")
        url = f"https://www.gitasupersite.iitk.ac.in/srimad?language=dv&field_chapter_value={i+1}&field_nsutra_value={j+1}&show_mool=1"
        webpage_text = extract_text_from_webpage(url)
        with open(file_path, "w",encoding='utf-8') as file:
    
            file.write(str(extract_between(webpage_text,"Display Selected Translations","Copyright © 2024,    Design by  Zymphonies")))


    print(f"{i+1} -> Done")
