# ОСТОРОЖНО, ГРАФЫ СГЕНЕРИРОВАНЫ CHATGPT И МОГУТ НЕ СОВПАДАТЬ С РЕАЛЬНОСТЬЮ

graph = {
    'Sydney': {
        'Melbourne': 874,
        'Brisbane': 936,
        'Perth': 3280,
        'Adelaide': 1329,
        'Canberra': 286
    },
    'Melbourne': {
        'Sydney': 874,
        'Brisbane': 1686,
        'Perth': 2756,
        'Adelaide': 727,
        'Hobart': 609
    },
    'Brisbane': {
        'Sydney': 936,
        'Melbourne': 1686,
        'Perth': 4316,
        'Cairns': 1702,
        'Gold Coast': 81
    },
    'Perth': {
        'Sydney': 3280,
        'Melbourne': 2756,
        'Brisbane': 4316,
        'Adelaide': 2134,
        'Darwin': 4141
    },
    'Adelaide': {
        'Sydney': 1329,
        'Melbourne': 727,
        'Perth': 2134,
        'Canberra': 1165,
        'Alice Springs': 1539
    },
    'Canberra': {
        'Sydney': 286,
        'Adelaide': 1165,
        'Melbourne': 662,
        'Gold Coast': 1326,
        'Hobart': 1166
    },
    'Cairns': {
        'Brisbane': 1702,
        'Darwin': 2326
    },
    'Gold Coast': {
        'Brisbane': 81,
        'Canberra': 1326
    },
    'Hobart': {
        'Melbourne': 609,
        'Canberra': 1166
    },
    'Darwin': {
        'Perth': 4141,
        'Cairns': 2326
    },
    'Alice Springs': {
        'Adelaide': 1539
    }
}
