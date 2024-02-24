from serpapi import GoogleSearch

SERPAPI_API_KEY = "" # your api_key

def get_web(question):
    params = {
      "q": question,
      "hl": "en",
      "gl": "us",
      "google_domain": "google.com",
      "api_key": SERPAPI_API_KEY
    }
    search = GoogleSearch(params)
    results = search.get_dict()["organic_results"]
    sum = ""
    for i in range(len(results)):
        sum= sum +  results[i]["snippet"] 
    return sum
