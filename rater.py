from dotenv import load_dotenv
load_dotenv()

import os
import base64
import requests
import json


def main():

    #hides api key, gets key from os
    key = os.environ.get("api-token")
    imageURLCropped = "https://i.imgur.com/YJBL4gX.png"
    imageURL = "https://i.imgur.com/vNEcJ4i.png"

    #data for post request
    payload = {
        'apiKey':key,
        'url':imageURL,
        'language':'eng',
        'OCREngine':2,
        'isOverlayRequired':True
    }
    # result = requests.post(url="https://api.ocr.space/parse/image", data=payload)
    # result = json.loads(result.content)
    
    #temporary so i dont spam api calls
    result = {'ParsedResults': [{'TextOverlay': {'Lines': [{'LineText': "Thunderbird's", 'Words': [{'WordText': "Thunderbird's", 'Left': 16.0, 'Top': 20.0, 'Height': 28.0, 'Width': 234.0}], 'MaxHeight': 28.0, 'MinTop': 20.0}, {'LineText': 'Mercy', 'Words': [{'WordText': 'Mercy', 'Left': 15.0, 'Top': 60.0, 'Height': 34.0, 'Width': 106.0}], 'MaxHeight': 34.0, 'MinTop': 60.0}, {'LineText': 'Flower of Life', 'Words': [{'WordText': 'Flower', 'Left': 16.0, 'Top': 115.0, 'Height': 17.0, 'Width': 73.0}, {'WordText': 'of', 'Left': 97.0, 'Top': 114.0, 'Height': 17.0, 'Width': 23.0}, {'WordText': 'Life', 'Left': 127.0, 'Top': 114.0, 'Height': 17.0, 'Width': 41.0}], 'MaxHeight': 18.0, 'MinTop': 114.0}, {'LineText': 'HP', 'Words': [{'WordText': 'HP', 'Left': 28.0, 'Top': 157.0, 'Height': 20.0, 'Width': 32.0}], 'MaxHeight': 20.0, 'MinTop': 157.0}, {'LineText': '3,967', 'Words': [{'WordText': '3,967', 'Left': 247.0, 'Top': 154.0, 'Height': 30.0, 'Width': 86.0}], 'MaxHeight': 30.0, 'MinTop': 154.0}, {'LineText': '+16', 'Words': [{'WordText': '+16', 'Left': 24.0, 'Top': 251.0, 'Height': 20.0, 'Width': 38.0}], 'MaxHeight': 20.0, 'MinTop': 251.0}, {'LineText': 'CRIT Rate+10.1%', 'Words': [{'WordText': 'CRIT', 'Left': 18.0, 'Top': 287.0, 'Height': 33.0, 'Width': 67.0}, {'WordText': 'Rate+10.1%', 'Left': 105.0, 'Top': 287.0, 'Height': 33.0, 'Width': 138.0}], 'MaxHeight': 33.0, 'MinTop': 287.0}, {'LineText': 'CRIT DMG+5.4%', 'Words': [{'WordText': 'CRIT', 'Left': 19.0, 'Top': 322.0, 'Height': 31.0, 'Width': 76.0}, {'WordText': 'DMG+5.4%', 'Left': 108.0, 'Top': 322.0, 'Height': 31.0, 'Width': 141.0}], 'MaxHeight': 31.0, 'MinTop': 322.0}, {'LineText': 'Energy Recharge+11.7%', 'Words': [{'WordText': 'Energy', 'Left': 19.0, 'Top': 357.0, 'Height': 31.0, 'Width': 98.0}, {'WordText': 'Recharge+11.7%', 'Left': 130.0, 'Top': 357.0, 'Height': 31.0, 'Width': 192.0}], 'MaxHeight': 31.0, 'MinTop': 357.0}, {'LineText': 'DEF+42', 'Words': [{'WordText': 'DEF+42', 'Left': 24.0, 'Top': 392.0, 'Height': 30.0, 'Width': 113.0}], 'MaxHeight': 30.0, 'MinTop': 392.0}, {'LineText': 'Thundering Fury:(0)', 'Words': [{'WordText': 'Thundering', 'Left': 15.0, 'Top': 432.0, 'Height': 25.0, 'Width': 140.0}, {'WordText': 'Fury:(0)', 'Left': 164.0, 'Top': 431.0, 'Height': 26.0, 'Width': 99.0}], 'MaxHeight': 26.0, 'MinTop': 431.0}, {'LineText': '2-Pieee Set: Electro', 'Words': [{'WordText': '2-Pieee', 'Left': 17.0, 'Top': 460.0, 'Height': 21.0, 'Width': 120.0}, {'WordText': 'Set:', 'Left': 146.0, 'Top': 461.0, 'Height': 19.0, 'Width': 45.0}, {'WordText': 'Electro', 'Left': 201.0, 'Top': 461.0, 'Height': 20.0, 'Width': 88.0}], 'MaxHeight': 21.0, 'MinTop': 460.0}, {'LineText': 'DMG Bonus +15%', 'Words': [{'WordText': 'DMG', 'Left': 45.0, 'Top': 490.0, 'Height': 19.0, 'Width': 59.0}, {'WordText': 'Bonus', 'Left': 113.0, 'Top': 490.0, 'Height': 19.0, 'Width': 74.0}, {'WordText': '+15%', 'Left': 196.0, 'Top': 490.0, 'Height': 23.0, 'Width': 60.0}], 'MaxHeight': 23.0, 'MinTop': 490.0}, {'LineText': '4-Piece Set: Increases', 'Words': [{'WordText': '4-Piece', 'Left': 16.0, 'Top': 518.0, 'Height': 21.0, 'Width': 123.0}, {'WordText': 'Set:', 'Left': 148.0, 'Top': 519.0, 'Height': 19.0, 'Width': 45.0}, {'WordText': 'Increases', 'Left': 203.0, 'Top': 519.0, 'Height': 19.0, 'Width': 116.0}], 'MaxHeight': 24.0, 'MinTop': 517.0}, {'LineText': 'damage catised by,', 'Words': [{'WordText': 'damage', 'Left': 45.0, 'Top': 548.0, 'Height': 25.0, 'Width': 91.0}, {'WordText': 'catised', 'Left': 145.0, 'Top': 548.0, 'Height': 29.0, 'Width': 83.0}, {'WordText': 'by,', 'Left': 238.0, 'Top': 548.0, 'Height': 26.0, 'Width': 35.0}], 'MaxHeight': 29.0, 'MinTop': 548.0}, {'LineText': '** Overloaded,', 'Words': [{'WordText': '**', 'Left': 13.0, 'Top': 576.0, 'Height': 3.0, 'Width': 16.0}, {'WordText': 'Overloaded,', 'Left': 44.0, 'Top': 575.0, 'Height': 28.0, 'Width': 146.0}], 'MaxHeight': 28.0, 'MinTop': 575.0}, {'LineText': 'Electro-Charged and', 'Words': [{'WordText': 'Electro-Charged', 'Left': 20.0, 'Top': 604.0, 'Height': 28.0, 'Width': 210.0}, {'WordText': 'and', 'Left': 254.0, 'Top': 604.0, 'Height': 28.0, 'Width': 44.0}], 'MaxHeight': 28.0, 'MinTop': 604.0}, {'LineText': 'Superconduct by 40%.', 'Words': [{'WordText': 'Superconduct', 'Left': 45.0, 'Top': 634.0, 'Height': 26.0, 'Width': 170.0}, {'WordText': 'by', 'Left': 224.0, 'Top': 633.0, 'Height': 27.0, 'Width': 28.0}, {'WordText': '40%.', 'Left': 261.0, 'Top': 635.0, 'Height': 19.0, 'Width': 64.0}], 'MaxHeight': 27.0, 'MinTop': 633.0}, {'LineText': 'Triggering such effects', 'Words': [{'WordText': 'Triggering', 'Left': 45.0, 'Top': 664.0, 'Height': 26.0, 'Width': 127.0}, {'WordText': 'such', 'Left': 179.0, 'Top': 664.0, 'Height': 20.0, 'Width': 57.0}, {'WordText': 'effects', 'Left': 244.0, 'Top': 664.0, 'Height': 20.0, 'Width': 89.0}], 'MaxHeight': 26.0, 'MinTop': 664.0}, {'LineText': 'decreases Elemental', 'Words': [{'WordText': 'decreases', 'Left': 45.0, 'Top': 695.0, 'Height': 18.0, 'Width': 121.0}, {'WordText': 'Elemental', 'Left': 174.0, 'Top': 695.0, 'Height': 26.0, 'Width': 122.0}], 'MaxHeight': 26.0, 'MinTop': 695.0}, {'LineText': 'Skill CD by 1s. Can only', 'Words': [{'WordText': 'Skill', 'Left': 44.0, 'Top': 722.0, 'Height': 20.0, 'Width': 56.0}, {'WordText': 'CD', 'Left': 107.0, 'Top': 722.0, 'Height': 20.0, 'Width': 35.0}, {'WordText': 'by', 'Left': 151.0, 'Top': 722.0, 'Height': 25.0, 'Width': 28.0}, {'WordText': '1s.', 'Left': 188.0, 'Top': 722.0, 'Height': 27.0, 'Width': 27.0}, {'WordText': 'Can', 'Left': 224.0, 'Top': 722.0, 'Height': 26.0, 'Width': 45.0}, {'WordText': 'only', 'Left': 277.0, 'Top': 721.0, 'Height': 26.0, 'Width': 53.0}], 'MaxHeight': 28.0, 'MinTop': 721.0}, {'LineText': 'occur once every 0.8s.', 'Words': [{'WordText': 'occur', 'Left': 44.0, 'Top': 757.0, 'Height': 19.0, 'Width': 71.0}, {'WordText': 'once', 'Left': 122.0, 'Top': 757.0, 'Height': 23.0, 'Width': 57.0}, {'WordText': 'every', 'Left': 187.0, 'Top': 753.0, 'Height': 27.0, 'Width': 72.0}, {'WordText': '0.8s.', 'Left': 264.0, 'Top': 751.0, 'Height': 27.0, 'Width': 60.0}], 'MaxHeight': 29.0, 'MinTop': 751.0}, {'LineText': 'A lightning-infused flower,', 'Words': [{'WordText': 'A', 'Left': 14.0, 'Top': 789.0, 'Height': 17.0, 'Width': 15.0}, {'WordText': 'lightning-infused', 'Left': 35.0, 'Top': 789.0, 'Height': 22.0, 'Width': 187.0}, {'WordText': 'flower,', 'Left': 230.0, 'Top': 789.0, 'Height': 19.0, 'Width': 79.0}], 'MaxHeight': 22.0, 'MinTop': 789.0}, {'LineText': 'somehow spared the fate of', 'Words': [{'WordText': 'somehow', 'Left': 15.0, 'Top': 816.0, 'Height': 16.0, 'Width': 99.0}, {'WordText': 'spared', 'Left': 122.0, 'Top': 816.0, 'Height': 21.0, 'Width': 70.0}, {'WordText': 'the', 'Left': 200.0, 'Top': 816.0, 'Height': 16.0, 'Width': 34.0}, {'WordText': 'fate', 'Left': 239.0, 'Top': 816.0, 'Height': 25.0, 'Width': 46.0}, {'WordText': 'of', 'Left': 292.0, 'Top': 816.0, 'Height': 16.0, 'Width': 23.0}], 'MaxHeight': 25.0, 'MinTop': 816.0}], 'HasOverlay': True, 'Message': 'Total lines: 24'}, 'TextOrientation': '0', 'FileParseExitCode': 1, 'ParsedText': "Thunderbird's\nMercy\nFlower of Life\nHP\n3,967\n+16\nCRIT Rate+10.1%\nCRIT DMG+5.4%\nEnergy Recharge+11.7%\nDEF+42\nThundering Fury:(0)\n2-Pieee Set: Electro\nDMG Bonus +15%\n4-Piece Set: Increases\ndamage catised by,\n** Overloaded,\nElectro-Charged and\nSuperconduct by 40%.\nTriggering such effects\ndecreases Elemental\nSkill CD by 1s. Can only\noccur once every 0.8s.\nA lightning-infused flower,\nsomehow spared the fate of", 'ErrorMessage': '', 'ErrorDetails': ''}], 'OCRExitCode': 1, 'IsErroredOnProcessing': False, 'ProcessingTimeInMilliseconds': '890'}

    process_parsed_text(result)

def process_parsed_text(parsedInfo):
    #word bank of pieces, mainstats, and substats
    artifact_pieces = ['Flower of Life', 'Plume of Death', 'Sands of Eon', 'Goblet of Eonothem', 'Circlet of Logos']
    mainstat_names = ['HP', 'ATK', 'HP%', 'DEF%', 'ATK%', 'Elementary Mastery', 'Physical DMG Bonus', 'Geo DMG Bonus', 'Anemo DMG Bonus', 'Cryo DMG Bonus', 'Pyro DMG Bonus', 'Hydro DMG Bonus', 'Electro DMG Bonus' 'Energy Recharge', 'CRIT Rate', 'CRIT DMG']
    substat_names = ['HP', 'ATK', 'DEF', 'HP%', 'ATK%', 'DEF%', 'Elemental Mastery', 'Energy Recharge', 'CRIT Rate', 'CRIT DMG']

    #gets the lines of parsed info
    lines = parsedInfo['ParsedResults'][0]['TextOverlay']['Lines']

    main_count = 0
    sub_count = 0

    piece = ''
    main_stat = ''
    sub_stats = []

    for line in lines:
        line = line['LineText']
        if line in artifact_pieces:
            piece = line

        if main_count == 1 and sub_count < 4:
            for substat in substat_names:
                if substat in line:
                    sub_stats.append(line)
                    sub_count += 1

        if main_count == 0:
            for mainstat in mainstat_names:
                if mainstat in line:
                    main_stat = line
                    main_count += 1
    
    return piece, main_stat, sub_stats


if __name__ == "__main__":
    main()