testingmode = True
lnnumber = -1

if testingmode == True: #lkz ntcnbyuf b ghbvth vfccbdf
    settingbar = [
        setting1 := "adefault",
        setting2 := "define",
        setting3 := "def"
    ]

def count_lines(filepath, chunk_size=1<<13): #это говно скопировано, считает линии
    with open(filepath) as file:
        return sum(chunk.count('\n')
                   for chunk in iter(lambda: file.read(chunk_size), ''))

def getezsetting(settingmassive, filepath, returningmode): # основная функция
    #main script
    with open(filepath, "r+") as file:
        text = file.readlines()
        for repcount in range(count_lines(filepath)):
            settingbar[lnnumber + 1] = text.split(" = ")[1]
            repcount + 1
    #returning block
    if returningmode == "ps":
        print("setting getted, setting:")
        print(settingbar)
    elif returningmode == "pl":
        print("setting getted")
    elif returningmode == "np":
        print("\n")
    else:
        print("invalid returning mode")

if testingmode == True:
    getezsetting(settingbar, "setting.ini", "ps")