import sys


correct_registers = {
    'MT': 'MT',
    'NA': 'NA',
    'LY': 'LY',
    'SP': 'SP',
    'ID': 'ID',
    'IT': 'IT',
    'ID': 'ID',
    'NE': 'NE',
    'SR': 'SR',
    'RE': 'NE',
    'HI': 'HI',
    'EN': 'EN',
    'RA': 'RA',
    'FI': 'FI',
    'LT': 'LT',
    'IN': 'IN',
    'RV': 'RV',
    'OB': 'OB',
    'RS': 'RS',
    'AV': 'AV',
    'OP': 'OP',
    'DS': 'DS',
    'ED': 'ED',
    'IP': 'IP', #until here we have the ones that remain the same
    'HT': '',
    'RP': '',
    'IB': '',
    'CM': '',
    'OI': '',
    'OH': '',
    'JD': 'DTP',
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
    'FH': 'FI', #FAQ abt how to combined with FAQ informational
    'FA': 'FI', # FAQ for some languages
    'EB': 'ED', # news blogs / editorials under IP 
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
    'TB': 'NB',
    'PB': 'NB',
    'CB': 'NB',
    'OA': '',
    'SS': '',
    'FC': '',
    'DT': 'DTP',
    'DP': 'DTP',
    'PA': '',
    'HA': '',
    'SO': '',
    'IG': ''
}

def correct(tags): #can include several
    finals = []
    tags=tags.strip()
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
