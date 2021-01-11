from dotenv import load_dotenv
load_dotenv()

from weight_calculator import get_scores, calculate_rolls
from data import artifact_pieces, mainstat_names, substat_names

import os
import base64
import requests
import json
import re


def main():

    #hides api key, gets key from os
    key = os.environ.get("api-token")

    #imageURL = "https://i.imgur.com/5ohv3yV.png"
    #imageURL = "https://i.imgur.com/MsWUhqe.png"
    #imageURL = "https://i.imgur.com/C1XfwJ5.png"
    imageURL = "https://cdn.discordapp.com/attachments/787533173004173343/798118856040120340/unknown.png"

    #data for post request
    payload = {
        'apiKey':key,
        'url':imageURL,
        'language':'eng',
        'OCREngine':2,
        'isOverlayRequired':True
    }
    result = requests.post(url="https://api.ocr.space/parse/image", data=payload)
    result = json.loads(result.content)
    print(result)
    
    #temporary so i dont spam api calls
    #result = {'ParsedResults': [{'TextOverlay': {'Lines': [{'LineText': 'Thunder', 'Words': [{'WordText': 'Thunder', 'Left': 15.0, 'Top': 15.0, 'Height': 24.0, 'Width': 123.0}], 'MaxHeight': 24.0, 'MinTop': 15.0}, {'LineText': "Summoner's", 'Words': [{'WordText': "Summoner's", 'Left': 20.0, 'Top': 52.0, 'Height': 22.0, 'Width': 173.0}], 'MaxHeight': 22.0, 'MinTop': 52.0}, {'LineText': 'Crown', 'Words': [{'WordText': 'Crown', 'Left': 6.0, 'Top': 84.0, 'Height': 27.0, 'Width': 106.0}], 'MaxHeight': 27.0, 'MinTop': 84.0}, {'LineText': 'Circlet of Logos', 'Words': [{'WordText': 'Circlet', 'Left': 19.0, 'Top': 128.0, 'Height': 16.0, 'Width': 62.0}, {'WordText': 'of', 'Left': 87.0, 'Top': 129.0, 'Height': 14.0, 'Width': 19.0}, {'WordText': 'Logos', 'Left': 112.0, 'Top': 130.0, 'Height': 17.0, 'Width': 52.0}], 'MaxHeight': 21.0, 'MinTop': 127.0}, {'LineText': 'DEF', 'Words': [{'WordText': 'DEF', 'Left': 30.0, 'Top': 166.0, 'Height': 16.0, 'Width': 40.0}], 'MaxHeight': 16.0, 'MinTop': 166.0}, {'LineText': '8.7%', 'Words': [{'WordText': '8.7%', 'Left': 222.0, 'Top': 163.0, 'Height': 22.0, 'Width': 63.0}], 'MaxHeight': 22.0, 'MinTop': 163.0}, {'LineText': '+0', 'Words': [{'WordText': '+0', 'Left': 30.0, 'Top': 243.0, 'Height': 16.0, 'Width': 26.0}], 'MaxHeight': 16.0, 'MinTop': 243.0}, {'LineText': 'Elemental Mastery+19', 'Words': [{'WordText': 'Elemental', 'Left': 23.0, 'Top': 275.0, 'Height': 26.0, 'Width': 110.0}, {'WordText': 'Mastery+19', 'Left': 146.0, 'Top': 275.0, 'Height': 26.0, 'Width': 122.0}], 'MaxHeight': 26.0, 'MinTop': 275.0}, {'LineText': 'ATK+5.3%', 'Words': [{'WordText': 'ATK+5.3%', 'Left': 26.0, 'Top': 304.0, 'Height': 20.0, 'Width': 117.0}], 'MaxHeight': 20.0, 'MinTop': 304.0}, {'LineText': ':Energy Recharge+6.5%', 'Words': [{'WordText': ':Energy', 'Left': 22.0, 'Top': 329.0, 'Height': 26.0, 'Width': 96.0}, {'WordText': 'Recharge+6.5%', 'Left': 115.0, 'Top': 329.0, 'Height': 26.0, 'Width': 161.0}], 'MaxHeight': 26.0, 'MinTop': 329.0}], 'HasOverlay': True, 'Message': 'Total lines: 10'}, 'TextOrientation': '0', 'FileParseExitCode': 1, 'ParsedText': "Thunder\nSummoner's\nCrown\nCirclet of Logos\nDEF\n8.7%\n+0\nElemental Mastery+19\nATK+5.3%\n:Energy Recharge+6.5%", 'ErrorMessage': '', 'ErrorDetails': ''}], 'OCRExitCode': 1, 'IsErroredOnProcessing': False, 'ProcessingTimeInMilliseconds': '390'}

    #processed parsed text into usable data
    p, l, m, s = process_parsed_text(result)

    #how much main and sub are weighted
    main_sub_weight = [0.5, 0.5]

    #weights correspond to the index of the weight tiers
    dps_weights_main = {
        'Flower of Life': [1],
        'Plume of Death': [1],
        'Sands of Eon': [0, 0, 1, 0, 0],
        'Goblet of Eonothem': [0, 0, 0.5, 0, 1, 1, 1, 1, 1, 1, 1],
        'Circlet of Logos': [0, 0, 0.5, 0, 1, 1, 0]
    }
    dps_weights_sub = [0, 0.2, 0, 0, 0.2, 0, 0, 0, 0.3, 0.3]

    print("Piece: " + p)
    print("Level: " + str(l))
    print("Mainstat: " + m)
    print("Substats: ")
    print(s)
    print("Rolls: ")
    print(calculate_rolls('5 star', s))
    print("Scores: ")
    print(get_scores(p, m, s, l, '5 star', main_sub_weight, dps_weights_main, dps_weights_sub))

#Parameters: raw parsed info from OCR
#returns piece name, artifact level, mainstat name, substat name/value dict
def process_parsed_text(parsedInfo):
    #gets the lines of parsed info
    lines = parsedInfo['ParsedResults'][0]['TextOverlay']['Lines']

    main_count = 0
    sub_count = 0
    level_count = 0

    piece = ''
    main_stat = ''
    mainstat_val = 0
    level = 0
    sub_stats = []

    #iterate through lines, look for piece name, main stat name, and substats and their values.
    for line in lines:
        line = line['LineText']
        
        #look for a valid piece name
        for piecename in artifact_pieces:
            if piecename in line:
                piece = piecename

        #main_count increments when mainstat name is found, increments again when the value is found
        #only start looking for substats when mainstat and value is found
        if main_count == 2 and sub_count < 4:
            for substat in substat_names:
                if substat in line:
                    sub_stats.append(line)
                    sub_count += 1

        #looks for level that starts with +
        if line.startswith('+') and level_count == 0:
            level = int(line[1:])
            level_count += 1

        #regex looks for numbers 0-16 in case level doesn't come with +
        if bool(re.search("^([0-1]?[0-9]|20)$", line)) and level_count == 0:
            level = int(re.search("^([0-1]?[0-9]|20)$", line).group(0))
            level_count += 1

        #after finding mainstat name, find mainstat value.
        #as HP/HP% ATK/ATK% only differentiate in the value, keep track of value to see if mainstat is HP or HP%, etc
        if main_count == 1:
            mainstat_val = line
            main_count += 1

        #special case as there is an hp/atk mainstat but no DEF mainstat
        if 'DEF' in line and main_count == 0:
            main_stat = 'DEF'
            main_count += 1

        #look for mainstat
        if main_count == 0:
            for mainstat in mainstat_names:
                if mainstat in line:
                    main_stat = mainstat
                    main_count += 1
                    break
    
    #if main stat value has a % and is HP/ATK/DEF
    if '%' in mainstat_val and main_stat in ['HP', 'ATK', 'DEF']:
        main_stat += '%'
                    
    return piece, level, main_stat, get_sub_stats(sub_stats)

#Parameters: array of raw substat string
#returns substat name/value dict
def get_sub_stats(sub_stats):
    parsed_subs = {}

    for sub in sub_stats:
        #iterate through substat_names in case the substat name comes with other characters
        #if hp%/def%/atk%, put in dict with % in name and cut off % symbol
        #regex looks for a word or two for stat name, a int or double for stat value
        for statname in substat_names:
            if statname in sub:
                if bool(re.match("(HP|DEF|ATK).*%$", sub)):
                    parsed_subs[statname + '%'] = float(re.search("\d+([.,]\d+)?", sub).group(0).replace(',', ''))
                    break
                else:
                    parsed_subs[statname] = float(re.search("\d+([.,]\d+)?", sub).group(0).replace(',', ''))
                    break

    return parsed_subs


if __name__ == "__main__":
    main()