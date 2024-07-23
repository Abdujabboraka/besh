import json
def fargona():
    with open("viloyatlar.json", "r", encoding='utf-8') as file:
        loader = json.load(file)
    return json.dumps(loader["Ozbekiston"]["Farg'ona viloyati"], indent=4, ensure_ascii=False)



def andijon():
    with open("viloyatlar.json", "r", encoding='utf-8') as file:
        loader = json.load(file)
    return json.dumps(loader["Ozbekiston"]["Andijon viloyati"], indent=4, ensure_ascii=False)


def buxoro():
    with open("viloyatlar.json", "r", encoding='utf-8') as file:
        loader = json.load(file)
    return json.dumps(loader["Ozbekiston"]["Buxoro viloyati"], indent=4, ensure_ascii=False)


def jizzax():
    with open("viloyatlar.json", "r", encoding='utf-8') as file:
        loader = json.load(file)
    return json.dumps(loader["Ozbekiston"]["Jizzax viloyati"], indent=4, ensure_ascii=False)


def namangan():
    with open("viloyatlar.json", "r", encoding='utf-8') as file:
        loader = json.load(file)
    return json.dumps(loader["Ozbekiston"]["Namangan viloyati"], indent=4, ensure_ascii=False)

def navoiy():
    with open("viloyatlar.json", "r", encoding='utf-8') as file:
        loader = json.load(file)
    return json.dumps(loader["Ozbekiston"]["Navoiy viloyati"], indent=4, ensure_ascii=False)

def qashqadaryo():
    with open("viloyatlar.json", "r", encoding='utf-8') as file:
        loader = json.load(file)
    return json.dumps(loader["Ozbekiston"]["Qashqadaryo viloyati"], indent=4, ensure_ascii=False)

def Qoraqalpogiston_Respublikasi():
    with open("viloyatlar.json", "r", encoding='utf-8') as file:
        loader = json.load(file)
    return json.dumps(loader["Ozbekiston"]["Qoraqalpog'iston Respublikasi"], indent=4, ensure_ascii=False)


def samarqand():
    with open("viloyatlar.json", "r", encoding='utf-8') as file:
        loader = json.load(file)
    return json.dumps(loader["Ozbekiston"]["Samarqand viloyati"], indent=4, ensure_ascii=False)

def sirdaryo():
    with open("viloyatlar.json", "r", encoding='utf-8') as file:
        loader = json.load(file)
    return json.dumps(loader["Ozbekiston"]["Sirdaryo viloyati"], indent=4, ensure_ascii=False)

def surxondaryo():
    with open("viloyatlar.json", "r", encoding='utf-8') as file:
        loader = json.load(file)
    return json.dumps(loader["Ozbekiston"]["Surxondaryo viloyati"], indent=4, ensure_ascii=False)

def toshkent():
    with open("viloyatlar.json", "r", encoding='utf-8') as file:
        loader = json.load(file)
    return json.dumps(loader["Ozbekiston"]["Toshkent viloyati".join()], indent=4, ensure_ascii=False)




def xorazm():
    with open("viloyatlar.json", "r") as file:
        loader = json.load(file)
        return json.dumps(loader["Ozbekiston"]["Xorazm viloyati"], indent=4, ensure_ascii=False)


