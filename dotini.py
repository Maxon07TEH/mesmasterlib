content = ""
def readini(filepath, linenumber):
    with open(filepath, "r") as file:
        text = file.readlines()[linenumber]
        content = text.split(" = ")[1]
    return content

#print(readini("setting.ini", 0))
