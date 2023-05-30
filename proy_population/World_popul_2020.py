
import matplotlib.pyplot as plt
from utils import population_by_country
from read_csv import read_csv
'''
este programa analiza el cambio de poblacion del pais elegido con
respecto al año pasado, asi como también mostrará la grafica de tarta
de la población mundial, comparando el pais elegido con paises similares
en poblacion
codigo hecho por: josé juan martínez lópez 
'''

Data = read_csv('./archivos/world-population-by-country-2020.csv')


def graph_pie(Data,values,country):
    i = int(country['\ufeffno'])-1
    
    fig, ax = plt.subplots()
    ax.set_title('poblacion del mundo')
    val = values[i-5:i+5]
    dat = Data[i-5:i+5]
    if i < 5:
        val = values[0:9]
        dat = Data[0:9]
    elif i>229: 
        val = values[224:234]
        dat = Data[224:234]

    ax.pie(val, labels = dat)
    ax.axis("equal")
    ax.legend(val)

    plt.tight_layout()
    plt.show()

def differentation(Data,country):
    popul = [float(i['Population 2020'].replace(',','')) for i in Data[:]]
    change = [i['Yearly Change'].replace('%','') for i in Data[:]]
    net = [int(i['Net Change'].replace(',','')) for i in Data[:]]
    
    change = [float(i)/100 for i in change]
    
    Change_stimated = []
    diff = []
    countries = []
    for i in range(0,len(popul)):
        Change_stimated.append(int(popul[i]*change[i]))
        diff.append(net[i]-Change_stimated[i])
        countries.append(Data[i]['Country (or dependency)']) 
        neto = int(country['Net Change'].replace(',',''))
        
        if net[i] == neto and diff[i] < 0 :
            print(Data[i]['Country (or dependency)'],'DEBAJO DE LA ESPECTATIVA DE POBLACION: incremento neto'
                  ,net[i],'incremento estimado',Change_stimated[i],'diferencia',diff[i])
        elif net[i] == neto and diff[i] >= 0 :
            print(Data[i]['Country (or dependency)'],'ARRIBA DE LA ESPECTATIVA DE POBLACION: incremento neto'
                  ,net[i],'incremento estimado',Change_stimated[i],'diferencia',diff[i])
    return diff,Change_stimated,countries,popul


def main():
    pais = input('escribe algun pais: ')
    pais = pais.capitalize()
    country = population_by_country(Data,pais)


    values,changes,countries,popul = differentation(Data,country[0])
    graph_pie(countries,popul,country[0])
    #graph_pie(countries,changes)
   

if __name__=='__main__':
    main()