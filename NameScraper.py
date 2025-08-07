import requests
from bs4 import BeautifulSoup 
from rich.progress import track
from rich.console import Console

console = Console()

print("""
  ▄████  ██▓     ▒█████   ▄▄▄▄    ▄▄▄       ██▓        ███▄    █  ▄▄▄       ███▄ ▄███▓▓█████   ██████ 
 ██▒ ▀█▒▓██▒    ▒██▒  ██▒▓█████▄ ▒████▄    ▓██▒        ██ ▀█   █ ▒████▄    ▓██▒▀█▀ ██▒▓█   ▀ ▒██    ▒ 
▒██░▄▄▄░▒██░    ▒██░  ██▒▒██▒ ▄██▒██  ▀█▄  ▒██░       ▓██  ▀█ ██▒▒██  ▀█▄  ▓██    ▓██░▒███   ░ ▓██▄   
░▓█  ██▓▒██░    ▒██   ██░▒██░█▀  ░██▄▄▄▄██ ▒██░       ▓██▒  ▐▌██▒░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄   ▒   ██▒
░▒▓███▀▒░██████▒░ ████▓▒░░▓█  ▀█▓ ▓█   ▓██▒░██████▒   ▒██░   ▓██░ ▓█   ▓██▒▒██▒   ░██▒░▒████▒▒██████▒▒
 ░▒   ▒ ░ ▒░▓  ░░ ▒░▒░▒░ ░▒▓███▀▒ ▒▒   ▓▒█░░ ▒░▓  ░   ░ ▒░   ▒ ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░▒ ▒▓▒ ▒ ░
  ░   ░ ░ ░ ▒  ░  ░ ▒ ▒░ ▒░▒   ░   ▒   ▒▒ ░░ ░ ▒  ░   ░ ░░   ░ ▒░  ▒   ▒▒ ░░  ░      ░ ░ ░  ░░ ░▒  ░ ░
░ ░   ░   ░ ░   ░ ░ ░ ▒   ░    ░   ░   ▒     ░ ░         ░   ░ ░   ░   ▒   ░      ░      ░   ░  ░  ░  
      ░     ░  ░    ░ ░   ░            ░  ░    ░  ░            ░       ░  ░       ░      ░  ░      ░                                                                                                
               ██████  ▄████▄   ██▀███   ▄▄▄       ██▓███   ██▓███  ▓█████  ██▀███  
            ▒██    ▒ ▒██▀ ▀█  ▓██ ▒ ██▒▒████▄    ▓██░  ██▒▓██░  ██▒▓█   ▀ ▓██ ▒ ██▒
            ░ ▓██▄   ▒▓█    ▄ ▓██ ░▄█ ▒▒██  ▀█▄  ▓██░ ██▓▒▓██░ ██▓▒▒███   ▓██ ░▄█ ▒
              ▒   ██▒▒▓▓▄ ▄██▒▒██▀▀█▄  ░██▄▄▄▄██ ▒██▄█▓▒ ▒▒██▄█▓▒ ▒▒▓█  ▄ ▒██▀▀█▄  
            ▒██████▒▒▒ ▓███▀ ░░██▓ ▒██▒ ▓█   ▓██▒▒██▒ ░  ░▒██▒ ░  ░░▒████▒░██▓ ▒██▒
            ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░▒▓▒░ ░  ░▒▓▒░ ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░
            ░ ░▒  ░ ░  ░  ▒     ░▒ ░ ▒░  ▒   ▒▒ ░░▒ ░     ░▒ ░      ░ ░  ░  ░▒ ░ ▒░
            ░  ░  ░  ░          ░░   ░   ░   ▒   ░░       ░░          ░     ░░   ░ 
                  ░  ░ ░         ░           ░  ░                     ░  ░   ░     
                     ░                                                                  
                                                                                  By NobleLip
""")



### Names Scraping ####



console.print("[[dark_orange]![/dark_orange]] :magnifying_glass_tilted_right: Checking how many pages to scrape")
response = requests.get('https://www.behindthename.com/names/')
soup = BeautifulSoup(response.text, 'html.parser')
soup = soup.find_all('a', class_='pgcanhide')
NumberOfPages = int(soup[-1].text.strip())
console.print("    [[green]+[/green]] There are " + soup[-1].text.strip() + " pages to scrape.")


console.print("[[dark_orange]![/dark_orange]] :magnifying_glass_tilted_right: Initializing Names scrape process :magnifying_glass_tilted_left:")
NameDictionary = {}
for i in track(range(1, NumberOfPages+1), description="Scrapping Names..."):
    response = requests.get('https://www.behindthename.com/names/'+str(i))

    soup = BeautifulSoup(response.text, 'html.parser')

    for l in soup.find_all('div', class_='browsename'):
        GenderVal = l.find('span', class_='listgender').text.strip('1234567890')
        NameToAdd = l.find('span', class_='listname').text.strip('1234567890')
        for j in l.find('span', class_='listusage').text.strip('1234567890').split(', '):
            if str(j) not in NameDictionary:
                NameDictionary[str(j)] = {'Male': [], 'Female': []}

            if GenderVal == 'f':
                NameDictionary[str(j)]['Female'].append(NameToAdd)
            else:
                NameDictionary[str(j)]['Male'].append(NameToAdd)

console.print("[[green]+[/green]] Scraping Names completed successfully!")



##### Surnames Scraping #####

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    # You can add more headers if needed
}

console.print("[[dark_orange]![/dark_orange]] :magnifying_glass_tilted_right: Initializing Surnames scrape process :magnifying_glass_tilted_left:")
ArrayOfLetter = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
SurNameDictionary = {}
for i in track(ArrayOfLetter, description="Scrapping Surnames..."):
    response = requests.get('https://surnam.es/surnames-with-'+str(i), headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    for l in soup.find_all('li', class_='list-item'):
        if str(i) not in SurNameDictionary:
            SurNameDictionary[str(i)] = []

        SurNameDictionary[str(i)].append(l.text.strip('()1234567890 '))

console.print("[[green]+[/green]] Scraping completed successfully!")


### Saving the data to JSON files ###

console.print("[[green]+[/green]] :file_folder: Saving data to Names.json...")
with open('Names.json', 'w', encoding='utf-8') as f:
    import json
    json.dump(NameDictionary, f, ensure_ascii=False, indent=4)


console.print("[[green]+[/green]] :file_folder: Saving data to Surames.json...")
with open('Surnames.json', 'w', encoding='utf-8') as f:
    json.dump(SurNameDictionary, f, ensure_ascii=False, indent=4)