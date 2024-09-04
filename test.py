import xmltodict
import json

def readXML():
    with open("./dados2modified.xml") as xmldir:
        res = xmltodict.parse(xmldir.read())
    print(res)
    return True

def readJSON():
    with open("./dados.json") as jsondir:
        res = json.load(jsondir)
    print(res)
    return True

def main():
    opt = input("What would you like to do?\n1: Read JSON\n2: Read XML\n> ")
    if opt != "1" and opt != "2":
        print("Invalid input.")
        return False
    
    if opt == "1":
        readJSON()
    else:
        readXML()
    
main()