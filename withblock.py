with open("this.txt")as f:
    t = f.read()
    print(t)
    if 'twinkle' in t:
        print("it is present")
    else:
        print("absent")
