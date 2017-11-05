import json
import requests

url = 'http://127.0.0.1:5000/api/news'
headers = {'Accept': 'application/vnd.api+json'}
post_headers = {'Accept': 'application/vnd.api+json',
                'Content-Type': 'application/vnd.api+json'}

# Make a POST request to create an object in the database.
news = {
    'data': {
        'type': 'news',
        'attributes': {
            'link': 'aaa',
            'status': 'status!!',
            'info': 'information'
        }
    }
}
response = requests.post(url, data=json.dumps(news), headers=post_headers)
print response
assert response.status_code == 201

# Make a GET request for the entire collection.
response = requests.get(url, headers=headers)
assert response.status_code == 200
print(response.json())

# Make a GET request for an individual instance of the model.
response = requests.get(url + '/1', headers=headers)
assert response.status_code == 200
print(response.json())

# Use query parameters to make a search. `requests.get` doesn't like
# arbitrary query parameters, so be sure that you pass a dictionary
# whose values are strings to the keyword argument `params`.
filters = [dict(name='name', op='like', val='%y%')]
params = {'filter[objects]': json.dumps(filters)}
response = requests.get(url, params=params, headers=headers)
assert response.status_code == 200
print(response.json())
