import re

def sub(line):
	line = re.sub("[^\w\s'\.\+\\\\-]", "", line);
	line = re.sub("[ďðđ]", "d", line);
	line = re.sub("[ÿỳý]", "y", line);
	line = re.sub("[ṕρ]", "p", line);
	line = re.sub("[тẗțʇţť]", "t", line);
	line = re.sub("[źẑżž]", "z", line);
	line = re.sub("[ğǵĝģǧ]", "g", line);
	line = re.sub("[ĉćčç]", "c", line);
	line = re.sub("æ", "ae", line);
	line = re.sub("[ŕř]", "r", line);
	line = re.sub("ḿ", "m", line);
	line = re.sub("[ḧɥ]", "h", line);
	line = re.sub("[àāăåąãáǎäâ]", "a", line);
	line = re.sub("[šşŝś]", "s", line);
	line = re.sub("[ǩķкḱ]", "k", line);
	line = re.sub("[ūυũůüûùǔú]", "u", line);
	line = re.sub("œ", "oe", line);
	line = re.sub("[ñǹņňń]", "n", line);
	line = re.sub("[ĺłľ]", "l", line);
	line = re.sub("[ìíίîïǐĩĭī]", "i", line);
	line = re.sub("[βßв]", "b", line);
	line = re.sub("[əéěęèėẽȩêëễѐ]", "e", line);
	line = re.sub("[őӧôοốöøόōõǒóò∅]", "o", line);
	return line;

F = open("output.txt", encoding="utf-8", mode="w");

citedA = {};
citingA = {};

citedC = {};
citingC = {};

with open("cited clean.txt", encoding="utf-8") as file:
    data = file.readlines();
    for line in data:
        parts = line.strip().split(",");

        if parts[0] not in citedA:
            citedA[parts[0]] = [];

        regex = sub(parts[1]).replace("-", " ").replace(" ", "[\s-]+");

        if parts[2]:
            initials = sub("\W+".join(parts[2]));
            regex = f"{regex}\W+{initials}(?!\w)";

        if parts[3]:
            regex = f"{regex},(?<!\w){parts[3]}(?!\w)";
        else:
            regex = f"{regex},";

        citedA[parts[0]].append((regex,",".join(parts[1:])));

with open("author information of citing publications.txt", encoding="utf-8") as file:
    data = file.readlines();
    for line in data[1:]:
        parts = line.split("\t");

        if parts[0] not in citingA:
            citingA[parts[0]] = [];

        line = f"{parts[2]} {parts[3]}".lower();
        citingA[parts[0]].append((sub(line), line));

with open("cited country.txt", encoding="utf-8") as file:
    data = file.readlines();
    for line in data:
        parts = line.strip().split(",");

        if parts[0] not in citedC:
            citedC[parts[0]] = {};

        if parts[1] not in citedC[parts[0]]:
            citedC[parts[0]][parts[1]] = 1;
        else:
            citedC[parts[0]][parts[1]] += 1;
        

with open("citing country.txt", encoding="utf-8") as file:
    data = file.readlines();
    for line in data:
        parts = line.strip().split(",");

        if parts[0] not in citingC:
            citingC[parts[0]] = {};

        if parts[1] not in citingC[parts[0]]:
            citingC[parts[0]][parts[1]] = 1;
        else:
            citingC[parts[0]][parts[1]] += 1;

with open("citing-cited-link.txt", encoding="utf-8") as file:
    data = file.readlines();
    for line in data[1:]:
        parts = line.strip().split("\t");

        countA,countC,counts = 0,0,0;
        if parts[0] in citedA and parts[1] in citingA:
            for ct in citingA[parts[1]]:
                for cd in citedA[parts[0]]:
                    rs = cd[0].split(",");
                    m = re.match(rs[0], ct[0]);
                    if m:
                        if rs[1]:
                            m = re.search(rs[1], ct[0]);
                            if m:
                                countA += 1;
                                #F.write(cd[1]);
                                #F.write("\n");
                                #F.write(ct[1]);
                                #F.write("\n");
                        else:
                            countA += 1;
                            #F.write(cd[1]);
                            #F.write("\n");
                            #F.write(ct[1]);
                            #F.write("\n");

        if parts[0] in citedC and parts[1] in citingC:
            for ct in citingC[parts[1]].keys():
                for cd in citedC[parts[0]].keys():
                    if ct == cd:
                        countC += 1;
                        counts += min(citedC[parts[0]][cd],citingC[parts[1]][ct]);

        F.write(parts[0]);
        F.write("\t");
        F.write(parts[1]);
        F.write("\t");
        F.write(str(countA));
        F.write("\t");
        F.write(str(countC));
        F.write("\t");
        F.write(str(counts));
        F.write("\n");
                                
F.close();
