f = open('database.txt')
answer = {}
for line in f:
    k, v = line.strip().split('=')
    answer[k.strip()] = v.strip()

f.close()
