import re

# APPLY IN ORDER: 1<-2<-3<-4<-5<-6<-7<-8<-9<-10<-11<-12<-13<-14<-15<-16<-17<-18<-19<-20<-21<-22<-23<-24<-25<-26<-27<-28

# a valid character
cedilla = u"\u0327";
diaeresis = u"\u0308";
al = f"(?:[^\W\d_]|{cedilla}|{diaeresis})";

namex = ("^institut|^depart|^dept|^clinic|^faculty|^university|^cancer|"
"^and\s|^national\s|^skin\s|^center\s|^the\s|^tom\s|"
"umc\s|johns\s|mayo\s|ncic\s|erasmus\s|barba\s|imperial\s|ludwig\s|marciniak\s|"
"wolfgang|matrix|postgraduate|eortc|royal|implementation|epigenetic|outreach|qol|calgary|"
"civile|physiology|multi|purnomo|hopital|federal|washington|management|nutrition|tours|"
"necker|calgary|boston|chinese"
"");

initialx = ("dept|med|hosp|cent|sec|department|unit|university|cellular|research|disease|"
"istituto|division|malaysia|section|gastroenterology|aereo|service|respiratory|chemistry"
"");


title = "(jr|jnr|sr|st|md|dr|ii|iii|iv)";

aff1 = "prog|depts|glaxo";
aff2 = "national|section";
aff3 = "(?:national|section|jordi|au)"

'''
	name:
		must not contain namex
'''
def test1(name):
	return re.search(f"{namex}",name.lower());

'''
	name:
		must contain title

	initials:
		must contain title

	return namme, initials and title
'''
def test2(name, initials):
	m = re.match(f"{title}(\.|-|\s)-?\s?(.*)", name.lower());
	if m:
		return (m.group(3), initials, m.group(1));
	else:
		m = re.match(f"(.+)\s{title}\.?(\s.*|$)", name.lower());
		if m:
			m = list(m.groups());
			t = m.pop(1);
			return ("".join(m), initials, t);
		else:
			m = re.match(f"{title}\.?$", initials.lower());
			if m:
				return (name, m.group(1));

'''
	name:
		must contain letters
		optionally contain space between letters
		optionally contain apostrophe between letters
		optionally contain hyphen between letters

	initials:
		- optional and will be removed
		must be single characters followed by more than one dots except at the end or followed by space
		can be followed by words

	return: initials without dots
'''
def test3(name, initials):
	if re.match(f"{al}+((-|')?{al}+)*(\s{al}+((-|')?{al}+)*)*$",name):
		m = re.match(f"({al}\.+)+(({al}(?=\s|$))|(?=\s|$|({al}+\s)))",initials.replace("-",""));
		if m:
			return m.group(0).replace(".","");

'''
	name:
		must contain letters
		optionally contain space between letters
		optionally contain apostrophe between letters
		optionally contain hyphen between letters

	initials:
		must be single characters followed by a dot and aff1

	return: initials without dots
'''
def test4(name, initials):
	if re.match(f"{al}+((-|')?{al}+)*(\s{al}+((-|')?{al}+)*)*$",name):
		m = re.match(f"({al}\.)+(?={aff1})",initials.lower());
		if m:
			return m.group(0).replace(".","");

'''
	name:
		must contain letters
		optionally contain space between letters
		optionally contain apostrophe between letters
		optionally contain hyphen between letters

	initials:
		must not contain initialx

	return: name with aff2 removed
'''
def test5(name, initials):
	if re.match(f"{al}+((-|')?{al}+)*(\s{al}+((-|')?{al}+)*)*$",name):
		m = re.match(f".*(?=\s{aff2})", name.lower());
		if m:
			return m.group(0);
		elif re.search(f"{initialx}",initials.lower()):
			return name;

'''
	name:
		must contain letters
		optionally contain space between letters
		optionally contain apostrophe between letters
		optionally contain hyphen between letters
		must be followed by space and single letters before dots
		optionally followed by hyphens

	initials:
		must be single letters before dots
		optionally followedy by space and aff3
		when hyphens are removed

	return names from part of name and initial from concatenation of name and initial parts with hyphens, dots removed
'''
def test6(name, initials):
	m = re.match(f"({al}+(?:(?:-|')?{al}+)*(?:\s{al}+(?:(?:-|')?{al}+)*)*)\s((?:{al}\.-?)+)",name);
	if m:
		n = re.match(f"((?:{al}\.)+)($|\s{aff3})", initials.lower().replace("-",""));
		if n:
			return (m.group(1), (m.group(2)+n.group(1)).replace("-", "").replace(".", ""));

'''
	name:
		must contain letters
		optionally contain space between letters
		optionally contain apostrophe between letters
		optionally contain hyphen between letters
		must be followed by space and single letters before dots except at the end or before space
		optionally preceded by hyphens
		optionally followed by words but must not end in dots

	initials:
		anything

	return name and initials without dots or hyphens
'''
def test7(name):
	m = re.match(f"({al}+(?:(?:-|')?{al}+)*(?:\s{al}+(?:(?:-|')?{al}+)*)*)\s+((?:-?{al}\.)+(?:{al}?(?:$|\s)|(?!{al}+\.)))",name);
	if m:
		return (m.group(1), m.group(2).replace("-", "").replace(".", ""));

'''
	name:
		must contain apostrophe at the end
		or contain a hyphen preceded by letter and followed by space
		or contain a hyphen preceded by space

	return name
'''
def test8(name):
	return re.search(f"\s-|{al}-\s|'$", name);