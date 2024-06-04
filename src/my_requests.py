# Disney character data via rest api from https://disneyapi.dev/docs/
# There is no authentication required for this api

# Hint: For better debugging use jupyter extension in vscode
# Go to the settings and turn on Jupyter › Interactive Window › Text Editor: Execute Selection/Line
# After that you can run the code by selecting the code and pressing Shift+Enter
# More info: https://code.visualstudio.com/docs/python/jupyter-support-py

import requests

# Root URL for the Disney API
ROOT_URL = "https://api.disneyapi.dev"

# Use GET method to retrieve data from the API and store the response in a variable
# Using the ROOT URL it will return all the characters regarding the Disney API Documentation
# Nevertheless it will return only 50 characters per default
response = requests.get(f"{ROOT_URL}/character")
print(response.status_code)
# >>> 200

# Response headers
print(response.headers)
# >>> {'Server': 'Cowboy', 'Report-To': '{"group":"heroku-nel","max_age":3600,"endpoints":[{"url":"https://nel.heroku.com/reports?ts=1717441240&sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d&s=0RYbNaLOm38%2Bmur9Nph%2Fjs6ej32KGcP8sfK3pa%2FGaWI%3D"}]}', 'Reporting-Endpoints': 'heroku-nel=https://nel.heroku.com/reports?ts=1717441240&sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d&s=0RYbNaLOm38%2Bmur9Nph%2Fjs6ej32KGcP8sfK3pa%2FGaWI%3D', 'Nel': '{"report_to":"heroku-nel","max_age":3600,"success_fraction":0.005,"failure_fraction":0.05,"response_headers":["Via"]}', 'Connection': 'keep-alive', 'X-Powered-By': 'Express', 'Access-Control-Allow-Origin': '*', 'Content-Type': 'application/json; charset=utf-8', 'Content-Length': '23641', 'Etag': 'W/"5c59-y1rqYZi0ko5Xd/hYfQr6cOFpc7Y"', 'Date': 'Mon, 03 Jun 2024 19:00:40 GMT', 'Via': '1.1 vegur'}

# Response is a JSON object, so we can use the .json() method to convert it to a Python dictionary
disney_data = response.json()
print(disney_data.keys())
# >>> dict_keys(['info', 'data'])

# You can inspect the info key to see how many characters are available
print(disney_data["info"])
# >>> {'count': 50, 'totalPages': 149, 'previousPage': None, 'nextPage': 'http://api.disneyapi.dev/character?page=2&pageSize=50'}
# You can see that there are 50 characters in the first page and a total of 149 pages

# You can also inspect the data key to see the actual characters
# The data key is a list of dictionaries, where each dictionary represents a character
print(disney_data["data"])
# >>> [{'_id': 112, 'films': ['Hercules (film)'], 'shortFilms': [], 'tvShows': ['Hercules (TV series)'], 'videoGames': ['Kingdom Hearts III'], 'parkAttractions': [], 'allies': [], 'enemies': [], 'sourceUrl': 'https://disney.fandom.com/wiki/Achilles_(Hercules)', 'name': 'Achilles', 'imageUrl': 'https://static.wikia.nocookie.net/disney/images/d/d3/Vlcsnap-2015-05-06-23h04m15s601.png', 'createdAt': '2021-04-12T01:31:30.547Z', 'updatedAt': '2021-12-20T20:39:18.033Z', 'url': 'https://api.disneyapi.dev/characters/112', '__v': 0},
# >>> {'_id': 18, 'films': ['The Fox and the Hound', 'The Fox and the Hound 2'], 'shortFilms': [], 'tvShows': [], 'videoGames': [], 'parkAttractions': [], 'allies': [], 'enemies': [], 'sourceUrl': 'https://disney.fandom.com/wiki/Abigail_the_Cow', 'name': 'Abigail the Cow', 'imageUrl': 'https://static.wikia.nocookie.net/disney/images/0/05/Fox-disneyscreencaps_com-901.jpg', 'createdAt': '2021-04-12T01:26:03.413Z', 'updatedAt': '2021-12-20T20:39:18.032Z', 'url': 'https://api.disneyapi.dev/characters/18', '__v': 0},
# >>> ...]

# To verify the number of characters in the data key, you can use the len() function
print(len(disney_data["data"]))
# >>> 50

# To get the next page of characters, you can use the nextPage key in the info key to get the URL
print(disney_data["info"]["nextPage"])
# >>> http://api.disneyapi.dev/character?page=2&pageSize=50
response = requests.get(disney_data["info"]["nextPage"])

# As you can see to use specific information from the API you can use query parameters like page and pageSize
# Usually the query parameters are separated by a question mark and the parameters are separated by an ampersand
# In this case the query parameters are page=2 and pageSize=50
# You can also define params as a dictionary and pass it to the GET method

# Params dictionary
params = {"page": 4, "pageSize": 20}

response = requests.get(f"{ROOT_URL}/character", params=params)
characters_from_page_4_with_20_characters = response.json()

# URL with query parameters
print(response.url)
# >>> https://api.disneyapi.dev/character/character?page=4&pageSize=20

# Verify that the number of characters is 20 and the page is 4
print(characters_from_page_4_with_20_characters["info"])
# >>> {'count': 20, 'totalPages': 372, 'previousPage': 'http://api.disneyapi.dev/character?page=3&pageSize=20', 'nextPage': 'http://api.disneyapi.dev/character?page=5&pageSize=20'}

# Retrieve all information keys from the first character in the list
characters_from_page_4_with_20_characters["data"][0].keys()
# >>> dict_keys(['_id', 'films', 'shortFilms', 'tvShows', 'videoGames', 'parkAttractions', 'allies', 'enemies', 'sourceUrl', 'name', 'imageUrl', 'createdAt', 'updatedAt', 'url', '__v'])

# Filter only the id and the name of all characters
characters = [
    {"id": character["_id"], "name": character["name"]}
    for character in characters_from_page_4_with_20_characters["data"]
]
print(characters)
# >>> [{'id': 555, 'name': 'Becky Gibson'}, {'id': 47, 'name': 'Adonis'}, {'id': 133, 'name': 'Agent Gordon'}, {'id': 137, 'name': 'Aggro'}, {'id': 145, 'name': 'Ajay'}, {'id': 146, 'name': 'Ajed Al-Gebraic'}, {'id': 150, 'name': 'Al'}, {'id': 151, 'name': 'Al Muddy'}, {'id': 158, 'name': 'Alan-A-Dale'}, {'id': 169, 'name': 'Alex Morrow'}, {'id': 190, 'name': 'Lorraine Almaden'}, {'id': 193, 'name': 'Alonzo'}, {'id': 199, 'name': 'Amara'}, {'id': 220, 'name': 'Anansi'}, {'id': 248, 'name': 'Angelica'}, {'id': 252, 'name': 'Angler'}, {'id': 276, 'name': 'Antonio Agama'}, {'id': 319, 'name': 'Armstrong'}, {'id': 343, 'name': 'Asteroth'}, {'id': 358, 'name': 'Audrey'}]

# You can also use path parameters to get specific characters with the character ID
# Path parameters are defined by curly braces in the URL
character_id = 156
response = requests.get(f"{ROOT_URL}/character/{character_id}")
character_156 = response.json()["data"]
print(character_156)
# >>> {'_id': 156, 'films': ['Aladdin (film)', 'The Return of Jafar', 'Aladdin and the King of Thieves', "Mickey's Magical Christmas: Snowed in at the House of Mouse", "Mickey's House of Villains", 'The Lion King 1½', 'Once Upon a Halloween', 'Descendants 2', 'Aladdin (2019 film)', 'Aladdin 2 (live-action film)'], 'shortFilms': [], 'tvShows': ['Aladdin (TV series)', 'Hercules (TV series)', 'House of Mouse', 'A Poem Is...', 'Once Upon a Time'], 'videoGames': ['Aladdin (video game)', "Disney's Aladdin Chess Adventures", 'Aladdin Magic Carpet Racing', "Disney's MathQuest With Aladdin", "Disney's ReadingQuest With Aladdin", "Disney's Aladdin in Nasira's Revenge", 'Kingdom Hearts (series)', 'Disney Universe', 'Kinect Disneyland Adventures', 'Epic Mickey: Power of Illusion', 'Disney Magical World', 'Hidden Worlds', 'Disney Infinity (series)', 'Disney Villains Challenge', 'Disney Tsum Tsum (game)', 'Disney Crossy Road', 'Disney Emoji Blitz', 'Disney Magical Dice', 'Disney Magic Kingdoms', 'Disney Heroes: Battle Mode', 'Disney Getaway Blast', 'Disney Princess Majestic Quest', "Disney Sorcerer's Arena", 'w:c:justdance:Just Dance 2014', 'w:c:justdance:Just Dance Now', 'w:c:justdance:Just Dance Unlimited'], 'parkAttractions': ["Mickey's PhilharMagic", "Mickey's Soundsational Parade", "It's a Small World", 'World of Color', 'Fantasmic!', "Mickey's Boo-to-You Halloween Parade", "Mickey's Once Upon a Christmastime Parade", "Aladdin's Royal Caravan", 'A Christmas Fantasy Parade', 'Mickey and the Wondrous Book', 'Golden Fairytale Fanfare', 'Voyage to the Crystal Grotto', 'Happily Ever After (fireworks show)', 'Wishes', 'Remember... Dreams Come True'], 'allies': [], 'enemies': [], 'sourceUrl': 'https://disney.fandom.com/wiki/Aladdin_(character)', 'name': 'Aladdin', 'imageUrl': 'https://static.wikia.nocookie.net/disney/images/b/bb/Profile_-_Aladdin.png', 'createdAt': '2021-04-12T01:31:57.819Z', 'updatedAt': '2021-12-20T20:39:18.877Z', 'url': 'https://api.disneyapi.dev/characters/156', '__v': 0}

# Lets change to a hosted REST-API ready to respond to your AJAX requests, so we can test POST requests
# API documentation = https://reqres.in/

# Lets first test one more GET request to request a single fake user
BASE_URL = "https://reqres.in/api"

response = requests.get(f"{BASE_URL}/users/2")
print(response.json())
# >>> {'data': {'id': 2, 'email': 'janet.weaver@reqres.in', 'first_name': 'Janet', 'last_name': 'Weaver', 'avatar': 'https://reqres.in/img/faces/2-image.jpg'}, 'support': {'url': 'https://reqres.in/#support-heading', 'text': 'To keep ReqRes free, contributions towards server costs are appreciated!'}}


# write data with POST parameters in query string

# write data with POST (json data in body)

new_user = {"name": "New User", "job": "Data Engineer"}

# Create a new user
response = requests.post(f"{BASE_URL}/users", data=new_user)
print(response)
# >>> <Response [201]>

# Created user
print(response.json())
# >>> {'name': 'New User', 'job': 'Data Engineer', 'id': '434', 'createdAt': '2024-06-03T19:47:19.674Z'}
