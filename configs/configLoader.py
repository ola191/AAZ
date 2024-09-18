import json 

def loadConfig(configPath):
    with open(f"{configPath}", "r") as cF:
        config = json.load(cF)
    return config
    