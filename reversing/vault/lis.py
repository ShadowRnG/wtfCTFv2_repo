l=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

w = 'aaa'

file = open('wl.txt','a')

for a in range(len(l)):
    wl = list(w)
    wl[0] = l[a]
    w = "".join(wl)
    for b in range(len(l)):
        wl = list(w)
        wl[1] = l[b]
        w = "".join(wl)
        for c in range(len(l)):
            wl = list(w)
            wl[2] = l[c]
            w = "".join(wl)
            file.write(w + "\n")

file.close()
