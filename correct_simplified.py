import sys


correct_registers = {
    'MT': 'MT',
    'NA': 'NA',
    'LY': 'LY',
    'SP': 'SP',
    'ID': 'ID',
    'IT': 'IT',
    'ID': 'ID',
    'NE': 'ne',
    'SR': 'sr',
    'RE': 're',
    'HI': 'HI',
    'EN': 'en',
    'RA': 'ra',
    'FI': 'fi',
    'LT': 'lt',
    'IN': 'IN',
    'RV': 'rv',
    'OB': 'ob',
    'RS': 'rs',
    'AV': 'av',
    'OP': 'OP',
    'DS': 'ds',
    'ED': 'ed',
    'IP': 'IP', #until here we have the ones that remain the same
    'HT': '',
    'RP': '',
    'IB': '',
    'CM': '',
    'OI': '',
    'OH': '',
    'JD': 'dtp',
    'PO': '',
    'OO': '',
    'TR':'',
    'OI': '',
    'AD': '',
    'LE': '',
    'MA': '',
    'ON': '',
    'OE': '',
    'OF': '',
    'FH': 'fi', #FAQ abt how to combined with FAQ informational
    'FA': 'fi', # FAQ for some languages
    'EB': 'ed', # news blogs / editorials under IP 
    'TS': '',
    'OL': '',
    'SL': '',
    'PR': '',
    'OS': '',
    'TA': '',
    'TV': '',
    'FS': '',
    'TA': '',
    'RR': '',
    'QA': '',
    'DF': '',
    'TB': 'nb',
    'PB': 'nb',
    'CB': 'nb',
    'OA': '',
    'SS': '',
    'FC': '',
    'DT': 'dtp',
    'DP': 'dtp',
    'PA': '',
    'HA': '',
    'SO': '',
    'IG': ''
}

def correct(tags): #can include several
    finals = []
    tags=tags.strip().upper()
    if "IG" in tags:
        if "DS" in tags:
            tags=tags.replace("IG", "IP")
        else:
            tags=tags.replace("IG", "")
    for label in tags.strip().split(" "):
        if len(label) <1:
            continue
        finals.append(correct_registers.get(label))
    return " ".join(finals)


for line in sys.stdin:
    print(correct(line))
