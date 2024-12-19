import json

def getServerConfig():
    with open ('config/server.json', 'r') as server:
        jsonserverdata = json.load(server)
        return jsonserverdata
    
    
