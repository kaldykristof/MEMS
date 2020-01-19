import requests
import io
import json

def validator(license_plate):
    if (len(license_plate) != 7):
        return False
    
    for character in license_plate[0:3:1]:
        if (character.isalpha() == False):
            return False
    
    if (license_plate[3] != "-"):
        return False
    
    for character in license_plate[4:7:1]:
        if (character.isnumeric() == False):
            return False
    
    return True

def ocr(api_key, file_name):
    api_url = "https://api.ocr.space/parse/image"
    
    with open(file="images/{0}.png".format(file_name), mode="rb") as image_binary:
        result = requests.post(url=api_url, files={"b.png" : image_binary}, data={"apikey" : api_key})

    result = result.content.decode()
    result = json.loads(result)

    license_plate = result.get("ParsedResults")[0].get("ParsedText")

    license_plate = license_plate.replace(" ", "")

    return license_plate.rstrip()