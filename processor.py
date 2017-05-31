from filter import test1
from filter import test2
from filter import test3
from filter import test4
from filter import test5

F = open("cited country.txt", encoding="utf-8", mode="w");
with open("author information of cited publications.txt", encoding="utf-8") as file:
    data = file.readlines();
    for line in data[1:]:
        parts = line.strip().split("\t");
    
        if len(parts) == 5 and len(parts[4]) > 0:
            F.write(parts[0]);
            F.write(",");
            F.write(parts[4].strip().lower());
            F.write("\n");
        else:
            country = test1(line);
            if country:
                F.write(parts[0]);
                F.write(",");
                F.write(country.strip().lower());
                F.write("\n");
            else:
                country = test2(line);
                if country:
                    F.write(parts[0]);
                    F.write(",");
                    F.write(country.strip().lower());
                    F.write("\n");
                elif test3(line):
                    F.write(parts[0]);
                    F.write(",");
                    F.write("us");
                    F.write("\n");
                else:
                    country = test4(line);
                    if country:
                        F.write(parts[0]);
                        F.write(",");
                        F.write(country.strip().lower());
                        F.write("\n");
                    elif test5(line):
                        F.write(parts[0]);
                        F.write(",");
                        F.write("us");
                        F.write("\n");
F.close();

F = open("citing country.txt", encoding="utf-8", mode="w");
with open("author information of citing publications.txt", encoding="utf-8") as file:
    data = file.readlines();
    for line in data[1:]:
        parts = line.strip().split("\t");
    
        if len(parts) == 5 and len(parts[4]) > 0:
            F.write(parts[0]);
            F.write(",");
            F.write(parts[4].strip().lower());
            F.write("\n");
        else:
            country = test1(line);
            if country:
                F.write(parts[0]);
                F.write(",");
                F.write(country.strip().lower());
                F.write("\n");
            else:
                country = test2(line);
                if country:
                    F.write(parts[0]);
                    F.write(",");
                    F.write(country.strip().lower());
                    F.write("\n");
                elif test3(line):
                    F.write(parts[0]);
                    F.write(",");
                    F.write("us");
                    F.write("\n");
                else:
                    country = test4(line);
                    if country:
                        F.write(parts[0]);
                        F.write(",");
                        F.write(country.strip().lower());
                        F.write("\n");
                    elif test5(line):
                        F.write(parts[0]);
                        F.write(",");
                        F.write("us");
                        F.write("\n");
F.close();