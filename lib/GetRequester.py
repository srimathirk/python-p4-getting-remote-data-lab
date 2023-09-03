import requests
import json

class GetRequester:
    #url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
    def __init__(self, url="https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        #objs=[]
        obj=json.loads(self.get_response_body())
        return obj

results = GetRequester().get_response_body()
print(results)
results2 = GetRequester().load_json()
print(results2)