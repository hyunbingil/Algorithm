a = input()
for i in range(0, len(a)):
    start = a[i]
    end = a[i+1:]
    start = start + (str(0)*len(end))
    print("["+start+"]")