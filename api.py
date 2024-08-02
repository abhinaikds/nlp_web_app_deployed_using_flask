def ner(text):    
    
    import requests

    url = "https://named-entity-extraction1.p.rapidapi.com/api/lingo"

    payload = {
        "extractor": "en",
        "text": text
    }
    headers = {
        "x-rapidapi-key": "6a6406b76emshc3b25cb812859b4p1addd1jsn1f16b46554eb",
        "x-rapidapi-host": "named-entity-extraction1.p.rapidapi.com",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    return response.json()
