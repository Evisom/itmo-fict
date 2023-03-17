# ОСТОРОЖНО, ГРАФЫ СГЕНЕРИРОВАНЫ CHATGPT И МОГУТ НЕ СОВПАДАТЬ С РЕАЛЬНОСТЬЮ

graph = {
    'Baker Street': {'Marylebone': 0.9, 'Regent\'s Park': 0.7, 'Bond Street': 0.6, 'St. John\'s Wood': 1.2},
    'Marylebone': {'Baker Street': 0.9, 'Edgware Road': 1.1},
    'Regent\'s Park': {'Baker Street': 0.7, 'Oxford Circus': 1.1},
    'Bond Street': {'Baker Street': 0.6, 'Oxford Circus': 0.6, 'Green Park': 0.7},
    'St. John\'s Wood': {'Baker Street': 1.2, 'Swiss Cottage': 0.9},
    'Edgware Road': {'Marylebone': 1.1, 'Paddington': 0.9, 'Baker Street': 1.1},
    'Oxford Circus': {'Regent\'s Park': 1.1, 'Bond Street': 0.6, 'Tottenham Court Road': 0.9, 'Green Park': 0.8},
    'Swiss Cottage': {'St. John\'s Wood': 0.9, 'Finchley Road': 1.3},
    'Paddington': {'Edgware Road': 0.9, 'Bayswater': 0.9},
    'Bayswater': {'Paddington': 0.9, 'Queensway': 0.6},
    'Queensway': {'Bayswater': 0.6, 'Notting Hill Gate': 0.7},
    'Notting Hill Gate': {'Queensway': 0.7, 'Holland Park': 0.9, 'High Street Kensington': 1.0},
    'Holland Park': {'Notting Hill Gate': 0.9, 'Shepherd\'s Bush': 1.3},
    'Shepherd\'s Bush': {'Holland Park': 1.3, 'Goldhawk Road': 0.9},
    'Goldhawk Road': {'Shepherd\'s Bush': 0.9, 'Hammersmith': 1.2},
    'Hammersmith': {'Goldhawk Road': 1.2, 'Barons Court': 1.1},
    'Barons Court': {'Hammersmith': 1.1, 'Earl\'s Court': 1.2},
    'Earl\'s Court': {'Barons Court': 1.2, 'Gloucester Road': 1.0, 'West Brompton': 1.3},
    'Gloucester Road': {'Earl\'s Court': 1.0, 'South Kensington': 0.8, 'High Street Kensington': 1.3},
    'South Kensington': {'Gloucester Road': 0.8, 'Sloane Square': 1.0, 'Knightsbridge': 1.1},
    'Sloane Square': {'South Kensington': 1.0, 'Victoria': 1.0},
    'Victoria': {'Sloane Square': 1.0, 'Green Park': 1}
}