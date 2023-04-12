import lzma
import json
import pprint

def get_keys(data, prefix="", keys=[]):
    if isinstance(data, dict):
        for key in data.keys():
            get_keys(data[key], prefix + key + ".", keys)
    else:
        keys.append(prefix[:-1])  # Remove the trailing period
    return keys

# Open the xz file
with lzma.open('2022-12-30_10-53-18_UTC.json.xz', 'r') as myfile:

    # Read the JSON file
    data = json.load(myfile)
    

    #print(data)
    #for i in keys:
    #    print(data['node']['comments_disabled'])
    #print(keys)

    # Delete a key and its value
    del data['node']['display_url']
    del data['node']['thumbnail_src']
    del data['node']['thumbnail_resources']
    del data['instaloader']
    
    print(data)
    print(get_keys(data))