if __name__=='__main__':
    d = set()
    with open("CONTACT.in", "r") as f:
        for line in f:
            line = line.strip()
            if line:
                d.add(line.lower())
    for x in sorted(d):
        print(x)