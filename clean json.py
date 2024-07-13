import json
jsonFile = '''

{
    "levels": [
        {
            "title": "CYCLOLCYC",
            "creator": "by eightos & more, uploaded by TeamPoopfish [2P]",
            "fps": "1974",
            "id": "76372236",
            "wr": "0.23% (Declandude25)",
            "place": "1"
        },
        {
            "title": "Formosa",
            "creator": "by eightos, uploaded by HectorSalamanca",
            "fps": "20000",
            "id": "92796375",
            "wr": "N/A",
            "place": "2"
        },
        {
            "title": "Lunar Empress",
            "creator": "by Tendart & more [2P]",
            "fps": "2000",
            "id": "89423130",
            "wr": "2.86% (Igna1035)",
            "place": "3"
        },
        {
            "title": "Ballistic wistfully",
            "creator": "by eightos & more [2P] [FIT1]",
            "fps": "3000",
            "id": "70371046",
            "wr": "0.60% (mikoshii)",
            "place": "4"
        },
        {
            "title": "RAIN",
            "creator": "by Skyyee, uploaded by 641",
            "fps": "7200",
            "id": "92339884",
            "wr": "0.77% (snowspike)",
            "place": "5"
        },
        {
            "title": "CUM",
            "creator": "by AuraXalaiv & Glitchy [2P] [Unreleased]",
            "fps": "1242",
            "id": "N/A (GMD)",
            "wr": "1.51% (erzor)",
            "place": "6"
        },
        {
            "title": "wistfully",
            "creator": "by Xiaolumi & Misogi [2P] [Old Version] [FIT1]",
            "fps": "720",
            "id": "65844817",
            "wr": "1.30% (Koozoo2000)",
            "place": "7"
        },
        {
            "title": "METH DEATH X",
            "creator": "by AuraXalaiv & erzor [2P]",
            "fps": "480",
            "id": "84311079",
            "wr": "3.1% (zeus91)",
            "place": "8"
        },
        {
            "title": "arcturus unnerfed",
            "creator": "by maxfs, uploaded by Wuro [2P] [Old Version] [FIT1]",
            "fps": "1440",
            "id": "67059113",
            "wr": "8.6% (KPGDylan)",
            "place": "9"
        },
        {
            "title": "Shipping",
            "creator": "by Apocalipse, uploaded by epsilonner [2P]",
            "fps": "2022",
            "id": "86525854",
            "wr": "0.33% (IAmNot60Hz)",
            "place": "10"
        },
        {
            "title": "Joke Resubmission",
            "creator": "by Relayne & more [2P]",
            "fps": "1440",
            "id": "74189247",
            "wr": "3.0% (Jalongames)",
            "place": "11"
        },
        {
            "title": "MUTEclub",
            "creator": "by gqc & TenDart",
            "fps": "1616",
            "id": "92460803",
            "wr": "1.00% (skeletonlol)",
            "place": "12"
        },
        {
            "title": "Deadly Deimos",
            "creator": "by Andra86 [2P]",
            "fps": "1250",
            "id": "88587390",
            "wr": "0.7% (zeus91)",
            "place": "13"
        },
        {
            "title": "Singularity",
            "creator": "by 070 [2P] [FIT1]",
            "fps": "3000",
            "id": "67432669",
            "wr": "53.4% (SeptaGon7)",
            "place": "14"
        },
        {
            "title": "Cyberphobia",
            "creator": "by 2A0L0I3 [2P]",
            "fps": "500",
            "id": "81062161",
            "wr": "2.3% (IAmNot60hz)",
            "place": "15"
        },
        {
            "title": "Silent Circles",
            "creator": "by TheRealSailent & Cyrillic, uploaded by 860 [2P] [FIT1]",
            "fps": "720",
            "id": "84316225",
            "wr": "40.3% (UFokinWotM8)",
            "place": "16"
        },
        {
            "title": "The Golden",
            "creator": "by HipoAR & more, uploaded by 043 [2P]",
            "fps": "1440",
            "id": "91914385",
            "wr": "N/A (≥1.6%)",
            "place": "17"
        },
        {
            "title": "THE LIMIT",
            "creator": "by realhutoew, uploaded by Y7N",
            "fps": "3000",
            "id": "88757643",
            "wr": "1.44% (dudodo)",
            "place": "18"
        },
        {
            "title": "Fear Factory",
            "creator": "by etermias & more, uploaded by Tendart",
            "fps": "1200",
            "id": "96127056",
            "wr": "0.36% (xaura2k)",
            "place": "19"
        },
        {
            "title": "Six Paths of Pain",
            "creator": "by GionniBlood",
            "fps": "666",
            "id": "17777889",
            "wr": "1.4% (IgnaXi0)",
            "place": "20"
        },
        {
            "title": "MINUStheory",
            "creator": "by HaydenDom & more, uploaded by HipoAR [2P]",
            "fps": "1200",
            "id": "70473532",
            "wr": "1.0% (halapenie)",
            "place": "21"
        },
        {
            "title": "Horrible Draw",
            "creator": "by Skyyee",
            "fps": "720",
            "id": "93453750",
            "wr": "1.4% (erzor)",
            "place": "22"
        },
        {
            "title": "Ghost",
            "creator": "by Apocalipse",
            "fps": "480",
            "id": "101068588",
            "wr": "0.8% (NotVeryGood)",
            "place": "23"
        },
        {
            "title": "Kingdom of Miracalis",
            "creator": "by GDMiracle & more, uploaded by skeletonlol [FIT1]",
            "fps": "1200",
            "id": "77452038",
            "wr": "0.13% (aelzfr)",
            "place": "24"
        },
        {
            "title": "Last Memories",
            "creator": "by Satoumatsuzaka, Nxaelevend & Kooto [2P]",
            "fps": "662",
            "id": "105496693",
            "wr": "N/A (≥0.8%)",
            "place": "25"
        },
        {
            "title": "MINUSclub",
            "creator": "by xVOLUMNIUS [2P] [FIT1]",
            "fps": "1872",
            "id": "65476277",
            "wr": "2.0% (sincos)",
            "place": "26"
        },
        {
            "title": "The Hell Heaven",
            "creator": "by maus999",
            "fps": "6969",
            "id": "69083618",
            "wr": "2.7% (IAmNot60Hz)",
            "place": "27"
        },
        {
            "title": "The Squall",
            "creator": "by Pieguy57 & RezerdPrime [2P]",
            "fps": "600",
            "id": "90859590",
            "wr": "1.14% (erzor)",
            "place": "28"
        },
        {
            "title": "regularity",
            "creator": "by Starz879 [2P]",
            "fps": "1200",
            "id": "74455372",
            "wr": "1.1% (skeletonlol), 58-100% (HipoAR)",
            "place": "29"
        }
    ]
}


'''
data = json.loads(jsonFile)

for i in range(29):
    data["levels"][i].pop("wr")
    link = input("Enter link for " + data["levels"][i]["title"] + ": ")
    data["levels"][i].update({"link": link})
    print(data["levels"][i])


with open("list2.json", "w") as f:
    json.dump(data, f)