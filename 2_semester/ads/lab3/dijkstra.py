from graphs.australia import graph 

test_graph = {
    1: {
        2: 10, 
        4: 30,
        5: 100
    },
    2: {3: 50},
    3: {
        5: 10,
    },
    4: {
        3: 20,
        5: 60
    },
    5: {},
    6: {}
}


def dijkstra(graph, start, end):

    vertices = list(graph.keys())

    inf = float('inf')

    P = [start] # Массив вершин P
    D = dict() # Словарь с минимальными длинами

    for i in vertices: # Инициализируем словарь с начальными значениями - inf 
        D[i] = inf 
    D[start] = 0 # Ставим кратчайший путь из стартовой точки в стартовую точку 0 (Логично)


    prev = 0 # Предыдущий ход, по умолчанию 0
    while P[-1] != end: # Пока не достигли конечной точки
        W = P[-1]
        nodes = list(graph[W].keys())

        for i in nodes: # Перебираем все соседние вершины
            if i not in P:
                D[i] = min(graph[W][i] + prev, D[i]) # Обновляем словарь минимальных вершин

        m_index = None # Ищем индекс с самым маленьким значением
        m_value = inf
        for i in list(D.keys()): # Ищем самый короткий путь
            if m_value > D[i] and i not in P:
                m_value = D[i]
                m_index = i 
        if m_index == None:
            return -1 
        P.append(m_index) # Переходим к вершине где самый короткий путь 
        prev = D[m_index] # Обновляем значение предыдущего пути


    # Ниже начинаем восстанавливать путь 
    route = [end]
    route_length = D[end]
    i = len(P)-1
    while route[-1] != start: # Пока не достигли начала, идем в обратном порядке
        for i in P: # Перебираем все вершины 
            if route[-1] in graph[i].keys(): # Проверяем есть ли путь от вершины из массива P в последнюю вершину в нашем пути 
                l = graph[i][route[-1]]
                if l+D[i]==D[route[-1]]: # Находим вершины для которых сходится минимальное значение + путь 
                    route.append(i)
    route = route[::-1] 
    return[route, D[end]]



for i in list(graph.keys()): # Выводим все вершины для удобного ввода
    print(i)
    
start = input('\nStart: ')
end = input('End: ')
print(dijkstra(graph, start, end))
