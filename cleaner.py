import re
from predicate import *

F = open("cited clean.txt", encoding="utf-8", mode="w");

with open("author information of cited publications.txt", encoding="utf-8") as file:
	data = file.readlines();
	for line in data[1:]:
		parts = line.split("\t");
		parts = list(map(lambda x:x.strip(),parts));

		if not test1(parts[2]):
			nameInitialsTitle = test2(parts[2],parts[3]);
			if nameInitialsTitle:
				if len(nameInitialsTitle) == 2:
					nameInitials = test7(nameInitialsTitle[0].strip());
					if nameInitials:
						F.write(parts[0]);
						F.write(",");
						F.write(nameInitials[0].lower().strip());
						F.write(",");
						F.write(nameInitials[1].lower().strip());
						F.write(",");
						F.write(nameInitialsTitle[1].lower().strip());
						F.write("\n");
					else:
						F.write(parts[0]);
						F.write(",");
						F.write(nameInitialsTitle[0].lower().strip());
						F.write(",");
						F.write(",");
						F.write(nameInitialsTitle[1].lower().strip());
						F.write("\n");
				else:
					initials = test3(nameInitialsTitle[0],nameInitialsTitle[1]);
					if initials:
						F.write(parts[0]);
						F.write(",");
						F.write(nameInitialsTitle[0].lower().strip());
						F.write(",");
						F.write(initials.lower().strip());
						F.write(",");
						F.write(nameInitialsTitle[2].lower().strip());
						F.write("\n");
					else:
						nameInitials = test7(nameInitialsTitle[0]);
						F.write(parts[0]);
						F.write(",");
						F.write(nameInitials[0].lower().strip());
						F.write(",");
						F.write(nameInitials[1].lower().strip());
						F.write(",");
						F.write(nameInitialsTitle[2].lower().strip());
						F.write("\n");
			else:
				initials = test3(parts[2],parts[3]);
				if initials:
					F.write(parts[0]);
					F.write(",");
					F.write(parts[2].lower().strip());
					F.write(",");
					F.write(initials.lower().strip());
					F.write(",");
					F.write("\n");
				else:
					initials = test4(parts[2],parts[3]);
					if initials:
						F.write(parts[0]);
						F.write(",");
						F.write(parts[2].lower().strip());
						F.write(",");
						F.write(initials.lower().strip());
						F.write(",");
						F.write("\n");
					else:
						name = test5(parts[2],parts[3]);
						if name:
							F.write(parts[0]);
							F.write(",");
							F.write(name.lower().strip());
							F.write(",");
							F.write(",");
							F.write("\n");
						else:
							nameInitials = test6(parts[2], parts[3]);
							if nameInitials:
								F.write(parts[0]);
								F.write(",");
								F.write(nameInitials[0].lower().strip());
								F.write(",");
								F.write(nameInitials[1].lower().strip());
								F.write(",");
								F.write("\n");
							else:
								nameInitials = test7(parts[2]);
								if nameInitials:
									F.write(parts[0]);
									F.write(",");
									F.write(nameInitials[0].lower().strip());
									F.write(",");
									F.write(nameInitials[1].lower().strip());
									F.write(",");
									F.write("\n");
								elif test8(parts[2]):
									name = parts[2].replace("-", "").replace("'", "").strip();
									initials = test3(name, parts[3]);
									F.write(parts[0]);
									F.write(",");
									F.write(name.lower().strip());
									F.write(",");
									F.write(initials.lower().strip());
									F.write(",");
									F.write("\n");
								else:
									pass;

F.close();