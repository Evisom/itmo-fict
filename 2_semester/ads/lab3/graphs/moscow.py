# ОСТОРОЖНО, ГРАФЫ СГЕНЕРИРОВАНЫ CHATGPT И МОГУТ НЕ СОВПАДАТЬ С РЕАЛЬНОСТЬЮ

graph = {
    'Tverskaya Street': {'Strastnoy Boulevard': 0.6, 'Okhotny Ryad': 1.2},
    'Strastnoy Boulevard': {'Tverskaya Street': 0.6, 'Pushkinskaya Square': 0.9},
    'Pushkinskaya Square': {'Strastnoy Boulevard': 0.9, 'Tverskaya Street': 1.4, 'Chekhovskaya Street': 1.2},
    'Chekhovskaya Street': {'Pushkinskaya Square': 1.2, 'Arbat Street': 1.4},
    'Arbat Street': {'Chekhovskaya Street': 1.4, 'Smolenskaya Square': 1.1},
    'Smolenskaya Square': {'Arbat Street': 1.1, 'Kutuzovsky Prospekt': 1.5},
    'Kutuzovsky Prospekt': {'Smolenskaya Square': 1.5, 'Novy Arbat Street': 1.3},
    'Novy Arbat Street': {'Kutuzovsky Prospekt': 1.3, 'Okhotny Ryad': 1.7},
    'Okhotny Ryad': {'Tverskaya Street': 1.2, 'Novy Arbat Street': 1.7}
}