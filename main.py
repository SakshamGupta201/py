with open("myfile.txt", 'r') as f:
    while (True):
        line = f.readline()
        if not line:
            break
        marks = line.split(',')
        m1 = marks[0]
        m2 = marks[1]
        m3 = marks[2].replace("\n",'')
        print(f"Marks of student1 in Math {m1}")
        print(f"Marks of student1 in Science {m2}")
        print(f"Marks of student1 in SST {m3}")
