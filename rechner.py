import matplotlib.pyplot as plt
import numpy as np
import statistics


SEEDCAPITAL = 5000 # Startkapital
INVESTMENTHORIZON = 50 # Jahre des Anlegens
AVERAGEYIELD = 1.05 # Durchschnittliche Ertrag
MONTHLIYSAVINGRATE = 500 # Monatliche Sparrate
VOLARITY = 0.15 # Volarität
AVERAGEINFLATION = 0.02 # Durchschnittliche Inflation
ANNUALTAXONYIELD = 0.004 # Jährliche steuern
SELFPAID = SEEDCAPITAL + 0 # Tatsächlich eingezahltes Geld ohne Zinsen
NUMBEROFRECORDS = 10000






def yieldContinuedCalculator(InvestmentHorizon,AverageYield, Volarity, SeedCapital, MonthlySavingrate, AnnualTaxOnYield, NumberOfRecords):
    
    random_numbers = []
    result = []
    
    for i in range (0, NumberOfRecords):
        random_numbers.append(np.random.uniform(low=(AverageYield-Volarity), high=(AverageYield+Volarity), size=InvestmentHorizon).tolist())
    
    for x in range (0, NumberOfRecords):
        SeedCapital = SEEDCAPITAL
        result.append([(SeedCapital+12*MonthlySavingrate)*(random_numbers[x][0]-AnnualTaxOnYield)])
        
        for y in range (1, InvestmentHorizon): 
            result[x].append((result[x][y-1]+(12*MonthlySavingrate))*random_numbers[x][y])
    
    return result

def moneyInvestedInTotal(SeedCapital, InvestmentHorizon, MonthlySavingRate):
    result = SeedCapital + (InvestmentHorizon*12*MonthlySavingRate)
    return result

def collectFinalResult():
    '''This method determines the final capital after a certain period of time under the desired conditions.'''
    data = yieldContinuedCalculator(INVESTMENTHORIZON, AVERAGEYIELD, VOLARITY, SEEDCAPITAL, MONTHLIYSAVINGRATE, ANNUALTAXONYIELD, NUMBEROFRECORDS)
    finalEndResults = []
    
    for sublist in data:
        finalEndResults.append(sublist[-1])
    
    finalEndResults.sort()
    average = statistics.mean(finalEndResults)
    n = len(finalEndResults)
    fivePercOfN = int(n*0.05)
    twentyfivePercOfN = int(n*0.25)
    
    
    
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
    
    return finalEndResults


plt.style.use('seaborn')
data = collectFinalResult()
n, bins, patches=plt.hist(data,bins=200)
plt.xlabel("Vermögen in €")
plt.ylabel("Häufigkeit")
plt.title(f'Verteilung des Vermögens über {INVESTMENTHORIZON} Jahre bei {SEEDCAPITAL}€ Startkapital und ca. {round((AVERAGEYIELD-1)*100, 2)}% Gewinn p.A.')
plt.show()

