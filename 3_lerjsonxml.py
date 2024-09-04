import json

def readJSON():
    with open("./dados.json") as jsondir:
        res = json.load(jsondir)
    return res

def main():
    data = readJSON()
    total, mediaMensal, diasFaturados = 0, 0, 0
    minVal, maxVal = float("inf"), 0
    diasMedia = 0
    
    for el in data:
        val = el["valor"]
        if val > 0:
            diasFaturados += 1
            total += val
            
            if val < minVal:
                minVal = val
            
            if maxVal < val:
                maxVal = val
    
    mediaMensal = total/diasFaturados
    
    for el in data:
        val = el["valor"]
        if val >= mediaMensal:
            diasMedia += 1
    
    print("Faturamento total:", format(total, ".2f"))
    print("Média mensal:", format(mediaMensal, ".2f"))
    print("Dia de menor faturamento:", format(minVal, ".2f"))
    print("Dia de maior faturamento:", format(maxVal, ".2f"))
    print("Dias com faturamento acima da média:", diasMedia)
    return True


main()