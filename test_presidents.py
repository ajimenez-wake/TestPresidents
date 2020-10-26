import pytest
import requests
import json


def test_president():
    # We're only testing last names.
    presidents_answer = ['Washington', 'Adams', 'Jefferson', 'Madison', 'Monroe', 'Adams', 'Jackson', 'Van Buren',
                         'Henry Harrison', 'Tyler', 'Polk', 'Taylor', 'Fillmore', 'Pierce', 'Buchanan', 'Lincoln',
                         'Johnson', 'Grant', 'Hayes', 'Garfield', 'Cleveland', 'McKinley', 'Roosevelt', 'Taft',
                         'Wilson', 'Harding', 'Coolidge', 'Hoover', 'Roosevelt', 'Truman', 'Eisenhower', 'Kennedy',
                         'Johnson', 'Nixon', 'Ford', 'Carter', 'Reagan', 'Bush', 'Clinton', 'Bush', 'Obama', 'Trump']

    url = 'https://api.duckduckgo.com/?q=presidents+of+the+united+states&format=json&pretty=1'
    response = requests.get(url)
    presidents_dict = json.loads(response.text)
    presidents_response = []
    for key in presidents_dict['RelatedTopics']:
        presidents_response.append(key['Text'])
    for president in presidents_answer:
        assert president in str(presidents_response)

