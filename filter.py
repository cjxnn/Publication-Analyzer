import re

country = [(re.compile("Bahrain",re.IGNORECASE),"bh"),(re.compile("Bolivia",re.IGNORECASE),"bo"),(re.compile("Bahamas",re.IGNORECASE),"bs"),
(re.compile("Kyrgyzstan",re.IGNORECASE),"kg"),(re.compile("Lao\t$",re.IGNORECASE),"la"),(re.compile("Nauru",re.IGNORECASE),"nr"),
(re.compile("Senegal",re.IGNORECASE),"sn"),(re.compile("Bangladesh",re.IGNORECASE),"bd"),(re.compile("barbados",re.IGNORECASE),"bb"),
(re.compile("Belgium",re.IGNORECASE),"be"),(re.compile("Bosnia",re.IGNORECASE),"ba"),(re.compile("Botswana",re.IGNORECASE),"bw"),
(re.compile("Brazil\t$",re.IGNORECASE),"br"),(re.compile("Cameroon",re.IGNORECASE),"cm"),(re.compile("Canada\t$",re.IGNORECASE),"ca"),
(re.compile("(?<!\w)Chile(?!\w)",re.IGNORECASE),"cl"),(re.compile("(?<!\w)China(?!\w)",re.IGNORECASE),"cn"),(re.compile("Colombia",re.IGNORECASE),"co"),
(re.compile("Congo\t$",re.IGNORECASE),"cg"),(re.compile("Côte",re.IGNORECASE),"ci"),(re.compile("Cuba\t$",re.IGNORECASE),"cu"),
(re.compile("Denmark",re.IGNORECASE),"dk"),(re.compile("Egypt",re.IGNORECASE),"eg"),(re.compile("Ethiopia",re.IGNORECASE),"et"),
(re.compile("Finland",re.IGNORECASE),"fi"),(re.compile("(?<!\w)France(?!\w)",re.IGNORECASE),"fr"),(re.compile("Gambia",re.IGNORECASE),"gm"),
(re.compile("Germany",re.IGNORECASE),"de"),(re.compile("Ghana\t",re.IGNORECASE),"gh"),(re.compile("Greece",re.IGNORECASE),"gr"),
(re.compile("Guinea-Bissau",re.IGNORECASE),"gw"),(re.compile("Haiti",re.IGNORECASE),"ht"),(re.compile("Hong Kong",re.IGNORECASE),"hk"),
(re.compile("(?<!\w)India(?!\w)",re.IGNORECASE),"in"),(re.compile("Indonesia",re.IGNORECASE),"id"),(re.compile("(?<!\w)Iran(?!\w)",re.IGNORECASE),"ir"),
(re.compile("Ireland\t$",re.IGNORECASE),"ie"),(re.compile("Israel\t$",re.IGNORECASE),"il"),(re.compile("Italy",re.IGNORECASE),"it"),
(re.compile("Japan",re.IGNORECASE),"jp"),(re.compile("Kenya",re.IGNORECASE),"ke"),(re.compile("Korea",re.IGNORECASE),"kr"),(re.compile("Austria\t$",re.IGNORECASE),"at"),
(re.compile("Lebanon",re.IGNORECASE),"lb"),(re.compile("Malawi\t$",re.IGNORECASE),"mw"),(re.compile("Malaysia",re.IGNORECASE),"my"),
(re.compile("Mali\t$",re.IGNORECASE),"ml"),(re.compile("(?<!-)Australia",re.IGNORECASE),"au"),(re.compile("Marshall Islands",re.IGNORECASE),"mh"),
(re.compile("Mexico",re.IGNORECASE),"mx"),(re.compile("Morocco",re.IGNORECASE),"ma"),(re.compile("Namibia",re.IGNORECASE),"na"),(re.compile("Argentina",re.IGNORECASE),"ar"),
(re.compile("Netherlands",re.IGNORECASE),"nl"),(re.compile("Caledonia",re.IGNORECASE),"nc"),(re.compile("Nigeria\t$",re.IGNORECASE),"ng"),(re.compile("Norway",re.IGNORECASE),"no"),
(re.compile("Panama",re.IGNORECASE),"pa"),(re.compile("Peruana",re.IGNORECASE),"pe"),(re.compile("Peruvian",re.IGNORECASE),"pe"),(re.compile("Poland\t$",re.IGNORECASE),"pl"),
(re.compile("porto portugal|portuguese|Portugal\t$",re.IGNORECASE),"pt"),(re.compile("Puerto Rico",re.IGNORECASE),"pr"),(re.compile("Romania",re.IGNORECASE),"ro"),
(re.compile("Russian Federation",re.IGNORECASE),"ru"),(re.compile("Saudi",re.IGNORECASE),"sa"),(re.compile("Serbia(?!\w)|serbian",re.IGNORECASE),"rs"),
(re.compile("Seychelles",re.IGNORECASE),"sc"),(re.compile("Singapore",re.IGNORECASE),"sg"),(re.compile("Slovakia",re.IGNORECASE),"sk"),(re.compile("South Africa",re.IGNORECASE),"za"),
(re.compile("Spain(\t($|a)| )",re.IGNORECASE),"es"),(re.compile("Sweden",re.IGNORECASE),"se"),(re.compile("Switzerland",re.IGNORECASE),"ch"),(re.compile("Taiwan",re.IGNORECASE),"tw"),
(re.compile("Tanzania",re.IGNORECASE),"tz"),(re.compile("Thailand",re.IGNORECASE),"th"),(re.compile("Turkey",re.IGNORECASE),"tr"),(re.compile("Uganda",re.IGNORECASE),"ug"),
(re.compile("United Kingdom",re.IGNORECASE),"gb"),(re.compile("United States",re.IGNORECASE),"us"),(re.compile("uruguay",re.IGNORECASE),"uy"),(re.compile("Venezuela",re.IGNORECASE),"ve"),
(re.compile("Viet Nam",re.IGNORECASE),"vn"),(re.compile("Zambia(?!\w)",re.IGNORECASE),"zm"),(re.compile("(?<!\w)usa(?!\w)",re.IGNORECASE),"us"),
(re.compile("Rotterdam",re.IGNORECASE),"nl"),(re.compile("Rozzano",re.IGNORECASE),"it"),
];

countrys = [(re.compile("Afghan",re.IGNORECASE),"af"),(re.compile("British Columbia",re.IGNORECASE),"ca"),(re.compile("British",re.IGNORECASE),"gb"),
(re.compile("Chinese",re.IGNORECASE),"cn"),(re.compile("Danish ",re.IGNORECASE),"dk"),(re.compile(" Paris|paris\t$",re.IGNORECASE),"fr"),
(re.compile("Hellenic",re.IGNORECASE),"gr"),(re.compile("tübingen",re.IGNORECASE),"de"),(re.compile("Pujol(\t$|”)",re.IGNORECASE),"es"),
(re.compile("Italian",re.IGNORECASE),"it"),(re.compile("Kyrgyz",re.IGNORECASE),"kg"),(re.compile("Polish",re.IGNORECASE),"pl"),
(re.compile("Arabian",re.IGNORECASE),"bh"),(re.compile("Swiss ",re.IGNORECASE),"ch"),(re.compile("\tAmerican",re.IGNORECASE),"us"),
];

state = re.compile(
"Washington|California|Connecticut|atlanta|Illinois|Indiana|Iowa|Kansas|Louisiana|Maryland|baltimore|"
"Massachusetts|Jersey|New York|Dakota|Oklahoma|Oregon|Pennsylvania|Tennessee|Texas|Virginia Institute"
,re.IGNORECASE);

countryss = [(re.compile("(?<!\w)(ag)(?!( |-)?\w|\.)",re.IGNORECASE),"ag"),(re.compile("(?<!\w)(sl)(?!( |-)?\w|\.)",re.IGNORECASE),"es")];

statess = re.compile(f"(?<!\w)(MO|MN|ME|TN|MA|IL|PA|ks|WA|ND|OR|TX)(?!( |-)?\w|\.|\u0327)");

def test1(line):
	for c in country:
		if c[0].search(line):
			return c[1];

def test2(line):
	for c in countrys:
		if c[0].search(line):
			return c[1];

def test3(line):
	return state.search(line);

def test4(line):
	for c in countryss:
		if c[0].search(line):
			return c[1];

def test5(line):
	return statess.search(line);