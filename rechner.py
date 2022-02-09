from typing import Counter
import matplotlib.pyplot as plt
import numpy as np
import statistics
import time


SEEDCAPITAL = 5000 # Startkapital
INVESTMENTHORIZON = 10 # Jahre des Anlegens
AVERAGEYIELD = 1.05 # Durchschnittliche Ertrag
MONTHLIYSAVINGRATE = 500 # Monatliche Sparrate
VOLARITY = 0.15 # Volarität
AVERAGEINFLATION = 0.02 # Durchschnittliche Inflation
ANNUALTAXONYIELD = 0.004 # Jährliche steuern
#LASS SIE SO WIE SIE SIND!:
NUMBEROFRECORDS = 1000
SELFPAID = SEEDCAPITAL + 0 # Tatsächlich eingezahltes Geld ohne Zinsen
A=0
B=0

print("Erfolg 1:", end='')

def yieldContinuedCalculator(InvestmentHorizon,AverageYield, Volarity, SeedCapital, MonthlySavingrate, AnnualTaxOnYield, NumberOfRecords):
    random_numbers = []
    result = []
    # calculating, depending on NumberOfRecords, many Lists of Lists with random values between low=(AverageYield-Volarity) and high=(AverageYield+Volarity)
    for i in range (0, NumberOfRecords):
        random_numbers.append(np.random.uniform(low=(AverageYield-Volarity), high=(AverageYield+Volarity), size=InvestmentHorizon).tolist())
    
    # calculating every result for each List in the random_numbers
    for x in range (0, NumberOfRecords):
        SeedCapital = SEEDCAPITAL
        result.append([(SeedCapital+12*MonthlySavingrate)*(random_numbers[x][0]-AnnualTaxOnYield)])
        
        # append the current result to resultlist
        for y in range (1, InvestmentHorizon): 
            result[x].append((result[x][y-1]+(12*MonthlySavingrate))*random_numbers[x][y])
    
    # returns the calculated resultlist
    return result

# calculate how much money you invested in total after all this years, without wins/losses
def moneyInvestedInTotal(SeedCapital, InvestmentHorizon, MonthlySavingRate):
    result = SeedCapital + (InvestmentHorizon*12*MonthlySavingRate)
    return result

def collectFinalResult():
    '''This method determines the final capital after a certain period of time under the desired conditions.'''
    data = yieldContinuedCalculator(INVESTMENTHORIZON, AVERAGEYIELD, VOLARITY, SEEDCAPITAL, MONTHLIYSAVINGRATE, ANNUALTAXONYIELD, NUMBEROFRECORDS)
    finalEndResults = []
    index = 0
    
    for sublist in data:
        finalEndResults.append(sublist[-1])
    
    finalEndResults.sort()
    average = statistics.fmean(finalEndResults)
    n = len(finalEndResults)
    fivePercOfN = int(n*0.05)
    twentyfivePercOfN = int(n*0.25)
    
    for x in range(0, len(finalEndResults)-1):
        if finalEndResults[x] <= average >= finalEndResults[x+1]:
            index = x
    
    sigma = int((n*0.6827)/2) #68,27%/2
    
    L = round(index - sigma, 0)
    if L < 0: L = 0
    
    R = round(index + sigma, 0)
    if R > len(finalEndResults): R = len(finalEndResults)-1
        
    mengL = finalEndResults[:L]
    mengR = finalEndResults[R:]
    mengAverage = finalEndResults[:index]
    
    bottom5 = finalEndResults[:fivePercOfN]
    top5 = finalEndResults[-fivePercOfN:]
    bottom25 = finalEndResults[:twentyfivePercOfN]
    top25 = finalEndResults[-twentyfivePercOfN:]
    
    avBottom5 = statistics.mean(bottom5)
    avTop5 = statistics.mean(top5)
    avBottom25 = statistics.mean(bottom25)
    avTop25 = statistics.mean(top25)
    
    
    #---------------------------------------------------------------------------------------------------------------------------
    
    print("")
    print(f'Insegesamt wurde eingezahlter Betrag: {moneyInvestedInTotal(SEEDCAPITAL, INVESTMENTHORIZON, MONTHLIYSAVINGRATE)}€')
    print("")
    print(f'Zeitraum:     {INVESTMENTHORIZON} Jahre')
    print(f'Startkapital: {SEEDCAPITAL}€')
    print(f'Zinsen:       {round((AVERAGEYIELD-1)*100, 2)}%')

    print("")
    
    print(f'Untere 5%:  {round(avBottom5, 2)}€')
    print(f'Obere  5%:  {round(avTop5, 2)}€')
    print(f'Untere 25%: {round(avBottom25, 2)}€')
    print(f'Obere  25%: {round(avTop25, 2)}€')
    print("----------------------")
    print(f'Durchschnitt : {round(average, 2)}€') 
    print("")
    print("")
    a=finalEndResults[L]
    b=finalEndResults[R]
    print(f'Mit einer Wahrscheinlichkeit von 68,72% liegt der zu erwartende Betrag zwischen {a}€ - {b}€')
    print("")
    print(f'Linke seite = {len(mengL)}\nRechte Seite= {len(mengR)}\nAvera Seite= {len(mengAverage)}')
    
    return average,a,b,finalEndResults


plt.style.use('seaborn')
average,A,B,data = collectFinalResult()
n, bins, patches=plt.hist(data,bins=200)
plt.xlabel("Vermögen in €")
plt.ylabel("Häufigkeit")
plt.title(f'Verteilung des Vermögens über {INVESTMENTHORIZON} Jahre bei {SEEDCAPITAL}€ Startkapital und ca. {round((AVERAGEYIELD-1)*100, 2)}% Gewinn p.A.')
plt.axvline(x=A, ymin=0.0, ymax=1, color="red")
plt.axvline(x=B, ymin=0.0, ymax=1, color="red")
plt.axvline(x=average, ymin=0, ymax=1, color="green")
plt.show()

