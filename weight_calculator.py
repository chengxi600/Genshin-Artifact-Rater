main_stats = {
    'Flower of Life': ['HP'],
    'Plume of Death': ['ATK'],
    'Sands of Eon': ['HP%', 'DEF%', 'ATK%', 'Elementary Mastery', 'Energy Recharge%'],
    'Goblet of Eonothem': ['HP%', 'DEF%', 'ATK%', 'Elementary Mastery', 'Physical DMG Bonus%', 'Geo DMG Bonus%', 'Anemo DMG Bonus%', 'Cryo DMG Bonus%', 'Pyro DMG Bonus%', 'Hydro DMG Bonus%', 'Electro DMG Bonus%'],
    'Circlet of Logos': ['HP%', 'DEF%', 'ATK%', 'Elementary Mastery', 'CRIT Rate%', 'CRIT DMG%', 'Healing Bonus%']
}

sub_stats = ['HP', 'ATK', 'DEF', 'HP%', 'ATK%', 'DEF%', 'Elemental Mastery', 'Energy Recharge%', 'CRIT Rate%', 'CRIT DMG%']

sub_stats_values = {
    '3 star': {
        'HP': [100,  115,  129,  143],
        'ATK': [7,  8,  9],
        'DEF': [8,  9,  10,  11],
        'HP%': [2.5,  2.8,  3.2,  3.5],
        'ATK%': [2.5,  2.8,  3.2,  3.5],
        'DEF%': [3.1,  3.5,  3.9,  4.4],
        'Elemental Mastery': [10,  11,  13,  14],
        'Energy Recharge%': [2.7,  3.1,  3.5,  3.9],
        'CRIT Rate%': [1.6,  1.9,  2.1,  2.3],
        'CRIT DMG%': [3.3,  3.7,  4.2,  4.7]
    },
    '4 star': {
        'HP': [167,  191,  215,  239],
        'ATK': [11,  12,  14,  16],
        'DEF': [13,  15,  17,  19],
        'HP%': [3.3,  3.7,  4.2,  4.7],
        'ATK%': [3.3,  3.7,  4.2,  4.7],
        'DEF%': [4.1,  4.7,  5.3,  5.8],
        'Elemental Mastery': [13,  15,  17,  19],
        'Energy Recharge%': [3.6,  4.1,  4.7,  5.2],
        'CRIT Rate%': [2.2,  2.5,  2.8,  3.1],
        'CRIT DMG%': [4.4,  5,  5.6,  6.2]
    },
    '5 star': {
        'HP': [209,  239,  269,  299],
        'ATK': [14,  16,  18,  19],
        'DEF': [16,  19,  21,  23],
        'HP%': [4.1,  4.7,  5.3,  5.8],
        'ATK%': [4.1,  4.7,  5.3,  5.8],
        'DEF%': [5.1,  5.8,  6.6,  7.3],
        'Elemental Mastery': [16,  19,  21,  23],
        'Energy Recharge%': [4.5,  5.2,  5.8,  6.5],
        'CRIT Rate%': [2.7,  3.1,  3.5,  3.9],
        'CRIT DMG%': [5.4,  6.2,  7,  7.8]
    }
}

#each stat can be tier 1, 2, 3, and the weights correspond to their importance. Tier 3 is best.
main_weight_tiers = [0, 0.5, 1]
sub_weight_tiers = [0, 0.2, 0.3]

#how much main and sub are weighted
main_sub_weight = [0.5, 0.5]

#weights correspond to the index of the weight tiers
dps_weights_main = {
    'Flower of Life': [2],
    'Plume of Death': [2],
    'Sands of Eon': [0, 0, 2, 0, 0],
    'Goblet of Eonothem': [0, 0, 1, 0, 2, 2, 2, 2, 2, 2, 2],
    'Circlet of Logos': [0, 0, 1, 0, 2, 2, 0]
}

dps_weights_sub = [0, 1, 0, 0, 1, 0, 0, 0, 2, 2]

#this should return the weights of main and sub assuming best stats are perfect rolls
def calculate_stat_weights(piece, main, sub, main_weights, sub_weights, main_weight_tiers, sub_weight_tiers):
    stat_sub_weights = []
    stat_weights = []

    #finds the index of main stat then assigns corresponding weight
    mainstat_index = main_stats[piece].index(main)
    mainstat_weight_index = main_weights[piece][mainstat_index]
    stat_weights.append(main_weight_tiers[mainstat_weight_index])


    #iterate through sub, finds index of the sub in sub_stats, then get corresponding weight
    for subKey, substat in sub.items():
        substat_index = sub_stats.index(subKey)
        substat_weight_index = sub_weights[substat_index]
        stat_sub_weights.append(sub_weight_tiers[substat_weight_index])
    
    stat_weights.append(stat_sub_weights)

    return stat_weights
        


