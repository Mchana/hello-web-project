# Tests for your routes go here

"""when i make a GET request to /names
and i send nothing
then i should get a 200 response """

def test_get_names_nothing(web_client):
    response = web_client.get('/names')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "please give a name"

"""when i make a GET request to names
and i send names=Dana
then i should get a 200 response and "Julia, Alice, Karim,Dana"""

def test_get_names(web_client):
    response = web_client.get('/names?name=Dana')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Julia,Alice,Karim,Dana"

"""when i make a GET request to names
and i send names=Matt,John
then i should get a 200 response and "Alice,John,Julia,Karim,Matt"""

"""when i make a POST request to /sort-names
and i send names=Joe,Alice,Zoe,Julia,Kieran
then i should get a 200 reponse with the list of names sorted"""

def test_post_sort_names(web_client):
    response = web_client.post('/sort-names', data={'names':"Joe,Alice,Zoe,Julia,Kieran"})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Alice,Joe,Julia,Kieran,Zoe"

"""
When: I make a POST request to /count_vowels
And: I send "eee" as the body parameter text
Then: I should get a 200 response with 3 in the message
"""
def test_post_count_vowels_eee(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eee'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 3 vowels in "eee"'

"""
When: I make a POST request to /count_vowels
And: I send "eunoia" as the body parameter text
Then: I should get a 200 response with 5 in the message
"""
def test_post_count_vowels_eunoia(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eunoia'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 5 vowels in "eunoia"'

"""
When: I make a POST request to /count_vowels
And: I send "mercurial" as the body parameter text
Then: I should get a 200 response with 4 in the message
"""
def test_post_count_vowels_mercurial(web_client):
    response = web_client.post('/count_vowels', data={'text': 'mercurial'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 4 vowels in "mercurial"'

# === Example Code Below ===

"""
GET /emoji
"""
def test_get_emoji(web_client):
    response = web_client.get("/emoji")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ":)"

# === End Example Code ===
