from data import sub_stats_values, main_stats, substat_names

#Parameters: takes in piece name, mainstat name, substat name/value dict, mainstat weights, substat weights
#returns weight of mainstat and substat name/weight dict
def calculate_stat_weights(piece, main, sub, main_weights, sub_weights):
    substat_weight = {}

    #finds the index of main stat then assigns corresponding weight
    mainstat_index = main_stats[piece].index(main)
    mainstat_weight = main_weights[piece][mainstat_index]


    #iterate through sub, finds index of the sub in substat_names, then get corresponding weight
    for subKey, substat in sub.items():
        substat_index = substat_names.index(subKey)
        substat_weight[subKey] = sub_weights[substat_index]

    return mainstat_weight, substat_weight

#Parameters: star of artifact, substat name/value dict
#returns a substat name/roll dict
def calculate_rolls(star, sub):
    subrolls = {}

    #divide each substat value by avg roll for that substat, then round to nearest integer
    for subKey, substat in sub.items():
        avg_roll_val = sum(sub_stats_values[star][subKey])/len(sub_stats_values[star][subKey])
        subrolls[subKey] = round(substat/avg_roll_val)
    
    return subrolls

#Parameters: star of artifact, mainstat/substat ratio, mainstat weight, substat name/value dict, substats weight, substat name/roll dict
#returns mainstat score, substat score, combined score
def calculate_stat_score(star, main_sub_ratio, weighted_main, sub, weighted_sub, subrolls):
    score = []
    substat_score = 0

    #divide each substat value by maximum possible roll substat value, multiple by substats weight
    for subKey, substat in sub.items():
        max_roll = subrolls[subKey]*sub_stats_values[star][subKey][-1]
        substat_score += (substat/max_roll)*weighted_sub[subKey]
    
    #weighted sum of mainstat score and substat score
    combined_score = weighted_main*main_sub_ratio[0] + substat_score*main_sub_ratio[1]

    #since mainstat is same for every artifact, we can just return the weight
    return weighted_main, substat_score, combined_score

#Parameters: piece name, mainstat name, substat name/value dict, star of artifact, mainstat/substat ratio, mainstat weights, substat weights
#returns mainstat score, substat score, combined score
def get_scores(piece, main, sub, level, star, main_sub_ratio, main_weights, sub_weights):
    mainstat_weight, substat_weight = calculate_stat_weights(piece, main, sub, main_weights, sub_weights)
    rolls = calculate_rolls(star, sub)
    return calculate_stat_score(star, main_sub_ratio, mainstat_weight, sub, substat_weight, rolls)
