
sheep = True
while sheep:
    a = int(input("first num "))
    b = int(input("second num "))
    bun = "Do you want to continue? yes/no "
    slay = "nah bestie, it is not giving, retry"
    bob = (str(input("What do you want to do? + - * / ")))
    if bob == "+":
        print(a + b)
        bam1 = (str(input( bun )))    #3
        if bam1 == "yes":
            continue
        elif bam1 == "no":
            sheep = False
    elif bob == "-":
        print(a - b)
        bam2 = (str(input( bun )))
        if bam2 == "yes":
            continue
        elif bam2 == "no":
            sheep = False
    elif bob == "/":
        if a == 0:
            print(slay)
            continue
        elif b == 0:
            print(slay)
            continue
        else:
            print(a/b)
            bam2 = (str(input( bun )))
            if bam2 == "yes":
                continue
            elif bam2 == "no":
                sheep = False
    elif bob == "*" :
        print(a * b)
        bam1 = (str(input( bun )))   
        if bam1 == "yes":
            continue
        elif bam1 == "no":
            sheep = False
            
