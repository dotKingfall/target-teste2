## BRL
mydict = {"SP": 67836.43, "RJ": 36678.66, "MG": 29229.88, "ES": 27165.48, "OTHER": 19849.53}

def main():
    total = 180759.98 ## Total value this time
    
    for entry in mydict:
        val = (mydict[entry]/total) * 100
        print(entry, "had", format(val, ".2f"), "percent of shares")
    
main()