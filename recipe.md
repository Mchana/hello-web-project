# Request:
GET /names?add=Eddie

# This route should return a list of pre-defined names, plus the name given.

# Expected response (2OO OK):
Julia, Alice, Karim, Eddie
You should assert that the response status code is 200 and that the response body is the correct string.

For an extra challenge, add multiple names and sort them alphabetically.

# Request:
GET /names?add=Eddie,Leo

# Expected response (2OO OK):
Alice, Eddie, Julia, Karim, Leo

1. route

GET /names
name = string

2. examples:



get /names?name=Dana
response (200)

"Julia, Alice, Karim,Dana"

GET /names
response (400)

"please provide a name"

extended:

GET /names?name=Matt,John
respose(200)

"Alice,John,Julia,Karim,Matt"