# ОСТОРОЖНО, ГРАФЫ СГЕНЕРИРОВАНЫ CHATGPT И МОГУТ НЕ СОВПАДАТЬ С РЕАЛЬНОСТЬЮ

graph = {
    'Nevsky Prospect': {'Liteyny Prospekt': 1.2, 'Sadovaya Street': 0.9},
    'Liteyny Prospekt': {'Nevsky Prospect': 1.2, 'Griboedova Canal': 0.8},
    'Griboedova Canal': {'Liteyny Prospekt': 0.8, 'Kazanskaya Street': 0.9},
    'Kazanskaya Street': {'Griboedova Canal': 0.9, 'Nevsky Prospect': 1.1, 'Ligovsky Prospekt': 1.3},
    'Ligovsky Prospekt': {'Kazanskaya Street': 1.3, 'Moskovsky Prospekt': 2.2},
    'Moskovsky Prospekt': {'Ligovsky Prospekt': 2.2, 'Vosstaniya Square': 0.8},
    'Vosstaniya Square': {'Moskovsky Prospekt': 0.8, 'Sadovaya Street': 1.5},
    'Sadovaya Street': {'Vosstaniya Square': 1.5, 'Nevsky Prospect': 0.9}
}