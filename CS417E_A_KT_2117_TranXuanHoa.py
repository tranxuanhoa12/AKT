G = []
P = []
H = []
const = 10

def create_queue(Open):
    for i in range(const):
        Open.append([0, 0, 0])  # Thêm giá trị thứ ba cho heuristic

def is_empty_queue(Open):
    return len(Open) - Open.count(Open[0]) == 0

def add_queue(Open, n, value, index, heuristic):
    n += 1
    Open[n][0] = value
    Open[n][1] = index
    Open[n][2] = heuristic
    i = n
    while i > 1:
        j = i // 2
        if (Open[i][0] + Open[i][2]) < (Open[j][0] + Open[j][2]):
            Open[i], Open[j] = Open[j], Open[i]
        i = j
    return n

def remove_queue(Open):
    value = Open[1][0]
    index = Open[1][1]
    heuristic = Open[1][2]
    n = len(Open) - Open.count(Open[0])
    Open[1][0] = Open[n][0]
    Open[1][1] = Open[n][1]
    Open[1][2] = Open[n][2]
    Open[n][0] = 0
    Open[n][1] = 0
    Open[n][2] = 0
    n -= 1
    i = 1
    while i <= n // 2:
        j = i * 2
        if j < n:
            if (Open[j][0] + Open[j][2]) > (Open[j + 1][0] + Open[j + 1][2]):
                j += 1
            if (Open[i][0] + Open[i][2]) > (Open[j][0] + Open[j][2]):
                Open[i], Open[j] = Open[j], Open[i]
        else:
            if (Open[i][0] + Open[i][2]) > (Open[j][0] + Open[j][2]):
                Open[i], Open[j] = Open[j], Open[i]
        i += 1
    return value, index, heuristic, n

def split_string(string):
    parts = string.split()
    return int(parts[0]), int(parts[1]), int(parts[2])

def init_graph(path, G):
    with open(path) as f:
        n, a, z = split_string(f.readline().replace('\t', ' '))
        for i in range(n + 1):
            G.append([0] * (n + 1))
        while True:
            string = f.readline()
            if not string:
                break
            i, j, x = split_string(string.replace('\t', ' '))
            G[i][j] = G[j][i] = int(x)
    return n, a, z

def read_heuristics(path, H):
    with open(path) as f:
        while True:
            string = f.readline()
            if not string:
                break
            H.append(int(string.strip()))

def view_matrix(G, n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print("%d" % G[i][j], end=' ')
        print()

def algorithm_for_tree(G, P, H, n, s, g):
    result = 0
    Close = [0] * (n + 1)
    O = [0] * (n + 1)
    Open = []
    create_queue(Open)
    m = 0
    m = add_queue(Open, 0, result, s, H[s])
    O[s] = 1
    P[s] = s
    while not is_empty_queue(Open):
        value, u, heuristic, m = remove_queue(Open)
        if u == g:
            result = value
            break
        for v in range(1, n + 1):
            if G[u][v] != 0 and O[v] == 0 and Close[v] == 0:
                x = value + G[u][v]
                m = add_queue(Open, m, x, v, H[v])
                O[v] = 1
                P[v] = u
        Close[u] = 1
        O[u] = 0
    return result

def print_path(P, n, s, g):
    Path = [0] * (n + 1)
    print("\n Đường đi ngắn nhất từ %d" % s, "đến %d" % g, "là\nPath:", end=' ')
    Path[0] = g
    i = P[g]
    k = 1
    while i != s:
        Path[k] = i
        k += 1
        i = P[i]
    Path[k] = s
    for j in range(k + 1):
        i = k - j
        if i > 0:
            print("%d=> " % Path[i], end=' ')
        else:
            print("%d" % Path[i], end=' ')

def main():
    n, s, g = init_graph("Graph.inp", G)
    read_heuristics("Heuristic.inp", H)
    print("n: %d" % n, end='\n')
    view_matrix(G, n)
    for i in range(0, n + 1):
        P.append(0)
    result = algorithm_for_tree(G, P, H, n, s, g)
    print_path(P, n, s, g)
    print("\n result: %d " % result, end='\n')

if __name__ == "__main__":
    main()


#Graph.inp
# 6 1 6
# 1 2 1
# 1 3 3
# 2 4 6
# 2 5 2
# 3 5 1
# 4 6 4
# 5 6 2

# Heuristic.inp
# 0
# 1
# 3
# 6
# 2
# 1
# 4
# 2