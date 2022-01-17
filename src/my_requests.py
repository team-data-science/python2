# Beer recipes data via rest api from https://punkapi.com/documentation/v2
# There is no authentication and it relies on rate limits from IP addresses 1 req/sec; 3600 requests per hour so be mindful :)
import requests
# Root Endpoint
BASE_URL = "https://api.punkapi.com/v2/"
# query data with GET - get all beers as json
response = requests.get(f'{BASE_URL}/beers')
print(response.status_code)
# > 200

# Response's headers
print(response.headers)
# > {'Date': 'Sun, 05 Dec 2021 19:13:10 GMT', 'Content-Type': 'application/json; charset=utf-8', 'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive', 'access-control-allow-origin': '*', 'cache-control': 'public, max-age=14400, must-revalidate', 'x-dns-prefetch-control': 'off', 'etag': 'W/"b763-uq9mCpw3GfGLWVDAEjtO7T6F6Ng"', 'x-download-options': 'noopen', 'strict-transport-security': 'max-age=15552000; includeSubDomains', 'x-xss-protection': '1; mode=block', 'x-ratelimit-limit': '3600', 'access-control-allow-credentials': 'true', 'x-content-type-options': 'nosniff', 'x-frame-options': 'SAMEORIGIN', 'x-ratelimit-remaining': '3455', 'x-ratelimit-reset': '1638702739', 'access-control-expose-headers': 'x-ratelimit-limit,x-ratelimit-remaining,content-length,origin,content-type,accept', 'x-vercel-cache': 'MISS', 'age': '30070','x-vercel-id': 'arn1::sfo1::vzxk7-1638701519956-7a018e92b5a5', 'content-encoding': 'gzip', 'CF-Cache-Status': 'HIT', 'Expect-CT': 'max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"', 'Report-To': '{"endpoints":[{"url":"https:\\/\\/a.nel.cloudflare.com\\/report\\/v3?s=mwe4F2a60%2BrZm2KCfY5%2Fcx7yLUmSYw6Zs7HQ2pSVqkE909oeVlj4vsQlrr2tLbwL5NrMJAu%2BNdyIyVA22yqcUMUueZKTSLgUCq%2BGvLpxGFAPZ6WLFCw4hANOp55OJ9xg50w%3D"}],"group":"cf-nel","max_age":604800}', 'NEL': '{"success_fraction":0,"report_to":"cf-nel","max_age":604800}','Vary': 'Accept-Encoding', 'Server': 'cloudflare', 'CF-RAY': '6b8f971ad9950b61-OSL', 'alt-svc': 'h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400'}

# there is a builtin JSON decoder, in case you are dealing with JSON data
all_beers = response.json()

# example of first dictionary entity in a list of beers
print(all_beers[0])
# > { 'abv': 4.5,
# >   'attenuation_level': 75,
# >   'boil_volume': {'unit': 'litres', 'value': 25},
# >   'brewers_tips': 'The earthy and floral aromas from the hops can be '
# >                   'overpowering. Drop a little Cascade in at the end of the '
# >                   'boil to lift the profile with a bit of citrus.',
# >   'contributed_by': 'Sam Mason <samjbmason>',
# >   'description': 'A light, crisp and bitter IPA brewed with English and '
# >                  'American hops. A small batch brewed only once.',
# >   'ebc': 20,
# >   'first_brewed': '09/2007',
# >   'food_pairing': [ 'Spicy chicken tikka masala',
# >                     'Grilled chicken quesadilla',
# >                     'Caramel toffee cake'],
# >   'ibu': 60,
# >   'id': 1,
# >   'image_url': 'https://images.punkapi.com/v2/keg.png',
# >   'ingredients': { 'hops': [ { 'add': 'start',
# >                                'amount': {'unit': 'grams', 'value': 25},
# >                                'attribute': 'bitter',
# >                                'name': 'Fuggles'},
# >                              { 'add': 'start',
# >                                'amount': {'unit': 'grams', 'value': 25},
# >                                'attribute': 'bitter',
# >                                'name': 'First Gold'},
# >                              { 'add': 'middle',
# >                                'amount': {'unit': 'grams', 'value': 37.5},
# >                                'attribute': 'flavour',
# >                                'name': 'Fuggles'},
# >                              { 'add': 'middle',
# >                                'amount': {'unit': 'grams', 'value': 37.5},
# >                                'attribute': 'flavour',
# >                                'name': 'First Gold'},
# >                              { 'add': 'end',
# >                                'amount': {'unit': 'grams', 'value': 37.5},
# >                                'attribute': 'flavour',
# >                                'name': 'Cascade'}],
# >                    'malt': [ { 'amount': {'unit': 'kilograms', 'value': 3.3},
# >                                'name': 'Maris Otter Extra Pale'},
# >                              { 'amount': {'unit': 'kilograms', 'value': 0.2},
# >                                'name': 'Caramalt'},
# >                              { 'amount': {'unit': 'kilograms', 'value': 0.4},
# >                                'name': 'Munich'}],
# >                    'yeast': 'Wyeast 1056 - American Ale™'},
# >   'method': { 'fermentation': {'temp': {'unit': 'celsius', 'value': 19}},
# >               'mash_temp': [ { 'duration': 75,
# >                                'temp': {'unit': 'celsius', 'value': 64}}],
# >               'twist': None},
# >   'name': 'Buzz',
# >   'ph': 4.4,
# >   'srm': 10,
# >   'tagline': 'A Real Bitter Experience.',
# >   'target_fg': 1010,
# >   'target_og': 1044,
# >   'volume': {'unit': 'litres', 'value': 20}}

# GET with parameters in query string
# One common way to customize a GET request is to pass values through query string parameters in the URL. API Query parameters can be defined as the optional key-value pairs that appear after the question mark in the URL
# Query parameters are used to sort/filter resources

# One of the parameter name is abv_gt number Returns all beers with ABV greater than the supplied number
# Second parameter name is abv_lt       number  Returns all beers with ABV less than the supplied number
# So return me beer between 15 and 20 ABV

payload = {
    'abv_gt': 15,
    'abv_lt': 20
}
response = requests.get(f'{BASE_URL}/beers', params=payload)
print(response)
# > <Response [200]>
beers_between_20_and_15_percent = response.json()

# Url that we sent in a request
response.url
# > 'https://api.punkapi.com/v2/beers?abv_gt=15&abv_lt=20'

# 9 beers
print(len(beers_between_20_and_15_percent))
# > 9

# List of all the keys
print(beers_between_20_and_15_percent[0].keys())
# > dict_keys(['id', 'name', 'tagline', 'first_brewed', 'description', 'image_url', 'abv', 'ibu', 'target_fg', 'target_og', 'ebc', 'srm', 'ph', 'attenuation_level', 'volume', 'boil_volume', 'method', 'ingredients', 'food_pairing', 'brewers_tips', 'contributed_by'])

# Lets get their names and alcohol percentages
short_summary_of_beers = [
    {
        "beer_name": beer.get("name"),
        "beer_alcohol": beer.get("abv")
    }
    for beer in beers_between_20_and_15_percent
]

short_summary_of_beers
# > [ {'beer_alcohol': 16.5, 'beer_name': 'Anarchist Alchemist'},
# >   {'beer_alcohol': 15.2, 'beer_name': 'Lumberjack Stout'},
# >   {'beer_alcohol': 18.3, 'beer_name': "Bowman's Beard - B-Sides"},
# >   {'beer_alcohol': 16.2, 'beer_name': 'Tokyo*'},
# >   {'beer_alcohol': 18, 'beer_name': 'AB:02'},
# >   { 'beer_alcohol': 17.2,
# >     'beer_name': 'Black Tokyo Horizon (w/Nøgne Ø & Mikkeller)'},
# >   {'beer_alcohol': 16.1, 'beer_name': 'Dog D'},
# >   {'beer_alcohol': 16.1, 'beer_name': 'Dog E'},
# >   {'beer_alcohol': 17, 'beer_name': 'Dog G'}]

# GET with path parameter
# path parameters come before the question mark sign
# path parameters are used to identify a specific resource or resources.

# Our path parameter will be the beer id
# Gets a beer from the api using the beers id

beer_id = 1

response = requests.get(f'{BASE_URL}/beers/{beer_id}')
response.status_code
# > 200
beer_no_1 = response.json()
len(beer_no_1)
# > 1
beer_no_1
# > [ { 'abv': 4.5,
# >     'attenuation_level': 75,
# >     'boil_volume': {'unit': 'litres', 'value': 25},
# >     'brewers_tips': 'The earthy and floral aromas from the hops can be '
# >                     'overpowering. Drop a little Cascade in at the end of '
# >                     'the boil to lift the profile with a bit of citrus.',
# >     'contributed_by': 'Sam Mason <samjbmason>',
# >     'description': 'A light, crisp and bitter IPA brewed with English and '
# >                    'American hops. A small batch brewed only once.',
# >     'ebc': 20,
# >     'first_brewed': '09/2007',
# >     'food_pairing': [ 'Spicy chicken tikka masala',
# >                       'Grilled chicken quesadilla',
# >                       'Caramel toffee cake'],
# >     'ibu': 60,
# >     'id': 1,
# >     'image_url': 'https://images.punkapi.com/v2/keg.png',
# >     'ingredients': { 'hops': [ { 'add': 'start',
# >                                  'amount': {'unit': 'grams', 'value': 25},
# >                                  'attribute': 'bitter',
# >                                  'name': 'Fuggles'},
# >                                { 'add': 'start',
# >                                  'amount': {'unit': 'grams', 'value': 25},
# >                                  'attribute': 'bitter',
# >                                  'name': 'First Gold'},
# >                                { 'add': 'middle',
# >                                  'amount': {'unit': 'grams', 'value': 37.5},
# >                                  'attribute': 'flavour',
# >                                  'name': 'Fuggles'},
# >                                { 'add': 'middle',
# >                                  'amount': {'unit': 'grams', 'value': 37.5},
# >                                  'attribute': 'flavour',
# >                                  'name': 'First Gold'},
# >                                { 'add': 'end',
# >                                  'amount': {'unit': 'grams', 'value': 37.5},
# >                                  'attribute': 'flavour',
# >                                  'name': 'Cascade'}],
# >                      'malt': [ { 'amount': { 'unit': 'kilograms',
# >                                              'value': 3.3},
# >                                  'name': 'Maris Otter Extra Pale'},
# >                                { 'amount': { 'unit': 'kilograms',
# >                                              'value': 0.2},
# >                                  'name': 'Caramalt'},
# >                                { 'amount': { 'unit': 'kilograms',
# >                                              'value': 0.4},
# >                                  'name': 'Munich'}],
# >                      'yeast': 'Wyeast 1056 - American Ale™'},
# >     'method': { 'fermentation': {'temp': {'unit': 'celsius', 'value': 19}},
# >                 'mash_temp': [ { 'duration': 75,
# >                                  'temp': {'unit': 'celsius', 'value': 64}}],
# >                 'twist': None},
# >     'name': 'Buzz',
# >     'ph': 4.4,
# >     'srm': 10,
# >     'tagline': 'A Real Bitter Experience.',
# >     'target_fg': 1010,
# >     'target_og': 1044,
# >     'volume': {'unit': 'litres', 'value': 20}}]

# Lets change to a hosted REST-API ready to respond to your AJAX requests, so we can test POST requests
# API documentation = https://reqres.in/

# Lets first test one more GET request to request a single fake user
BASE_URL = "https://reqres.in/api"

response = requests.get(f"{BASE_URL}/users/2")
print(response.json())
# > { 'data': { 'avatar': 'https://reqres.in/img/faces/2-image.jpg',
# >             'email': 'janet.weaver@reqres.in',
# >             'first_name': 'Janet',
# >             'id': 2,
# >             'last_name': 'Weaver'},
# >   'support': { 'text': 'To keep ReqRes free, contributions towards server '
# >                        'costs are appreciated!',
# >                'url': 'https://reqres.in/#support-heading'}}

# write data with POST parameters in query string

# write data with POST (json data in body)

new_user = {
    "name": "New User",
    "job": "Data Engineer"
}

# Create a new user
response = requests.post(f"{BASE_URL}/users", data=new_user)
response
# > <Response [201]>
# Created user
print(response.json())
# > { 'createdAt': '2021-12-05T19:13:11.710Z',
# >   'id': '247',
# >   'job': 'Data Engineer',
# >   'name': 'New User'}
