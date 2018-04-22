def create_list(filename):
    out_list = []
    with open(filename, "r") as infile:
        n, m = [int(w) for w in infile.readline().split()]
        for line in infile:
            i, j = [int(w) for w in line.split()]
            out_list.append((i, j))
    return out_list, n, m

def create_dict(filename):
    connections_list, n, m = create_list(filename)
    city_connections = {}
    for connection in connections_list:
        conn1, conn2 = connection
        if conn1 in city_connections:
            city_connections[conn1].add(conn2)
        if conn1 not in city_connections:
            city_connections[conn1] = set([conn2])
        if conn2 in city_connections:
            city_connections[conn2].add(conn1)
        if conn2 not in city_connections:
            city_connections[conn2] = set([conn1])
    return city_connections, n, m

connections, n, m = create_dict("input")

def component(i):
    cities_in_component = set([i])
    if i in connections:
        candidates = connections[i].copy()
    else:
        candidates = set([])
    while len(candidates) > 0:
        city = candidates.pop()
        connected_to_city = connections[city].copy()
        candidates |= (connected_to_city - cities_in_component)
        cities_in_component.add(city)
    return cities_in_component

num_components = 0

cities = set(range(n))
while len(cities) > 0:
    city = cities.pop()
    num_components += 1
    cities -= component(city)

print num_components - 1
