# ОСТОРОЖНО, ГРАФЫ СГЕНЕРИРОВАНЫ CHATGPT И МОГУТ НЕ СОВПАДАТЬ С РЕАЛЬНОСТЬЮ

cities = {
    'Moscow': {'St. Petersburg': 635, 'Kazan': 815, 'Nizhny Novgorod': 410},
    'St. Petersburg': {'Moscow': 635, 'Kazan': 1208},
    'Kazan': {'St. Petersburg': 1208, 'Yekaterinburg': 892, 'Moscow': 815},
    'Yekaterinburg': {'Kazan': 892, 'Novosibirsk': 1498, 'Omsk': 1417},
    'Novosibirsk': {'Yekaterinburg': 1498, 'Vladivostok': 6147, 'Krasnoyarsk': 1569},
    'Vladivostok': {'Novosibirsk': 6147, 'Irkutsk': 4789},
    'Irkutsk': {'Vladivostok': 4789, 'Krasnoyarsk': 1060},
    'Krasnoyarsk': {'Novosibirsk': 1569, 'Irkutsk': 1060, 'Omsk': 1422},
    'Omsk': {'Krasnoyarsk': 1422, 'Yekaterinburg': 1417, 'Novosibirsk': 641},
    'Nizhny Novgorod': {'Moscow': 410, 'Kazan': 419, 'Kirov': 453},
    'Kirov': {'Nizhny Novgorod': 453}
}