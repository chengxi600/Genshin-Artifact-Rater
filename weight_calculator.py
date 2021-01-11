from data import sub_stats_values, main_stats, sub_stats

#this should return the weights of main and sub assuming best stats are perfect rolls
def calculate_stat_weights(piece, main, sub, main_weights, sub_weights, main_weight_tiers, sub_weight_tiers):
    stat_sub_weights = {}
    stat_weights = []

    #finds the index of main stat then assigns corresponding weight
    mainstat_index = main_stats[piece].index(main)
    mainstat_weight_index = main_weights[piece][mainstat_index]
    stat_weights.append(main_weight_tiers[mainstat_weight_index])


    #iterate through sub, finds index of the sub in sub_stats, then get corresponding weight
    for subKey, substat in sub.items():
        substat_index = sub_stats.index(subKey)
        substat_weight_index = sub_weights[substat_index]
        stat_sub_weights[subKey] = sub_weight_tiers[substat_weight_index]
    
    stat_weights.append(stat_sub_weights)

    return stat_weights
        
def calculate_rolls(star, sub):
    subrolls = {}
    for subKey, substat in sub.items():
        avg_roll_val = sum(sub_stats_values[star][subKey])/len(sub_stats_values[star][subKey])
        subrolls[subKey] = round(substat/avg_roll_val)

    return subrolls

def calculate_stat_score(star, main_sub_weight, weighted_main, sub, weighted_sub, subrolls):
    score = []
    substat_score = 0
    for subKey, substat in sub.items():
        max_roll = subrolls[subKey]*sub_stats_values[star][subKey][-1]
        substat_score += (substat/max_roll)*weighted_sub[subKey]
    
    score.append(weighted_main)
    score.append(substat_score)
    score.append(weighted_main*main_sub_weight[0] + substat_score*main_sub_weight[1])

    return score
        
def get_scores(piece, main, sub, level, star, main_sub_weight, main_weights, sub_weights, main_weight_tiers, sub_weight_tiers):
    stat_weights = calculate_stat_weights(piece, main, sub, main_weights, sub_weights, main_weight_tiers, sub_weight_tiers)
    rolls = calculate_rolls(star, sub)
    return calculate_stat_score(star, main_sub_weight, stat_weights[0], sub, stat_weights[1], rolls)
