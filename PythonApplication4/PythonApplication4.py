import openpyxl
import numpy
import pandas as pd
import os
##############################################
############ Excel Scraper ###################
##############################################



os.chdir('C:\\Users\\Daniel\\Desktop')
df = pd.read_excel("airport Data.xlsx")
df.columns = ['AIRPORT', 'YEAR', 'MONTH', 'DOMESTIC INBOUND', 'DOMESTIC OUTBOUND', 'DOMESTIC TOTAL', 
                                    'INTERNATIONAL INBOUND', 'INTERNATIONAL OUTBOUND', 'INTERNATIONAL TOTAL', 'TOTAL INBOUND', 
                                    'TOTAL OUTBOUND', 'TOTAL FLIGHTS']

#  print ("row['AIRPORT'], row['TOTAL OUTBOUND'], row['TOTAL INBOUND'], row['YEAR']")

ListNSW = [0,0,0,0,0]
ListTAS = [0,0,0,0,0]
ListACT = [0,0,0,0,0]
ListQSLD = [0,0,0,0,0]
ListWA = [0,0,0,0,0]
ListNT = [0,0,0,0, 0]
ListSA = [0,0,0,0,0]
ListVIC = [0,0,0,0,0]

Airport = ''
TotalFlights = 0
DomesticInbound = 0
DomesticOutbound = 0
InternationalInbound = 0
InternationalOutbound = 0
Year = 2016
#print(df)
#file = open('Requests.txt', 'w')

for index, row in df.iterrows():
        # print(row['AIRPORT'], row['DOMESTIC INBOUND'], row['DOMESTIC OUTBOUND'], 
         #      row['INTERNATIONAL INBOUND'], row['INTERNATIONAL OUTBOUND'], row['YEAR'])
         if (row['YEAR'] == 2016):
             if (row['AIRPORT'] == 'MELBOURNE'):
                ListVIC[1] = ListVIC[1] + row['DOMESTIC INBOUND']
                ListVIC[2] = ListVIC[2] + row['DOMESTIC OUTBOUND']
                ListVIC[3] = ListVIC[3] + row['INTERNATIONAL INBOUND']
                ListVIC[4] = ListVIC[4] + row['INTERNATIONAL OUTBOUND']
                ListVIC[0] = ListVIC[0] + row['TOTAL FLIGHTS']
             if (row['AIRPORT'] == 'WILLIAMTOWN' or row['AIRPORT'] == 'SYDNEY' or row['AIRPORT'] == 'BULLINA'):
                    ListNSW[1] = ListNSW[1] + row['DOMESTIC INBOUND']
                    ListNSW[2] = ListNSW[2] + row['DOMESTIC OUTBOUND']
                    ListNSW[3] = ListNSW[3] + row['INTERNATIONAL INBOUND']
                    ListNSW[4] = ListNSW[4] + row['INTERNATIONAL OUTBOUND']
                    ListNSW[0] = ListNSW[0] + + row['TOTAL FLIGHTS']
             if (row['AIRPORT'] == 'LAUNCESTON' or row['AIRPORT'] == 'HOBART'):
                 ListTAS[1] = ListTAS[1] + row['DOMESTIC INBOUND']
                 ListTAS[2] = ListTAS[2] + row['DOMESTIC OUTBOUND']
                 ListTAS[3] = ListTAS[3] + row['INTERNATIONAL INBOUND']
                 ListTAS[4] = ListTAS[4] + row['INTERNATIONAL OUTBOUND']
                 ListTAS[0] = ListTAS[0] + row['TOTAL FLIGHTS']
                 # ListTAS[0] = ListTAS[0] + row['INTERNATIONAL OUTBOUND'] + row['INTERNATIONAL INBOUND'] + row['DOMESTIC OUTBOUND'] + row['DOMESTIC INBOUND']
             if (row['AIRPORT'] == 'DARWIN' or row['AIRPORT'] == 'ALICE SPRINGS'):
                 ListNT[1] = ListNT[1] + row['DOMESTIC INBOUND']
                 ListNT[2] = ListNT[2] + row['DOMESTIC OUTBOUND']
                 ListNT[3] = ListNT[3] + row['INTERNATIONAL INBOUND']
                 ListNT[4] = ListNT[4] + row['INTERNATIONAL OUTBOUND']
                 ListNT[0] = ListNT[0] + + row['TOTAL FLIGHTS']
             if (row['AIRPORT'] == 'TOWNSVILLE' or row['AIRPORT'] == 'SUNSHINE COAST' or row['AIRPORT'] == 'ROCKHAMPTON'
               or row['AIRPORT'] == 'MACKAY' or row['AIRPORT'] == 'HAMILTON ISLAND' or row['AIRPORT'] == 'GOLD COAST' 
               or row['AIRPORT'] == 'CAIRINS' or row['AIRPORT'] == 'BRISBANE'):
                 ListQSLD[1] = ListQSLD[1] + row['DOMESTIC INBOUND']
                 ListQSLD[2] = ListQSLD[2] + row['DOMESTIC OUTBOUND']
                 ListQSLD[3] = ListQSLD[3] + row['INTERNATIONAL INBOUND']
                 ListQSLD[4] = ListQSLD[4] + row['INTERNATIONAL OUTBOUND']
                 ListQSLD[0] = ListQSLD[0] + row['TOTAL FLIGHTS']
             if (row['AIRPORT'] == 'KARRATHA' or row['AIRPORT'] == 'PERTH'):
                 ListWA[1] = ListWA[1] + row['DOMESTIC INBOUND']
                 ListWA[2] = ListWA[2] + row['DOMESTIC OUTBOUND']
                 ListWA[3] = ListWA[3] + row['INTERNATIONAL INBOUND']
                 ListWA[4] = ListWA[4] + row['INTERNATIONAL OUTBOUND']
                 ListWA[0] = ListWA[0] + row['TOTAL FLIGHTS']
             if (row['AIRPORT'] == 'ADELAIDE'):
                 ListSA[1] = ListSA[1] + row['DOMESTIC INBOUND']
                 ListSA[2] = ListSA[2] + row['DOMESTIC OUTBOUND']
                 ListSA[3] = ListSA[3] + row['INTERNATIONAL INBOUND']
                 ListSA[4] = ListSA[4] + row['INTERNATIONAL OUTBOUND']
                 ListSA[0] = ListSA[0] + row['TOTAL FLIGHTS']
             if (row['AIRPORT'] == 'CANBERRA'): 
                 ListACT[1] = ListACT[1] + row['DOMESTIC INBOUND']
                 ListACT[2] = ListACT[2] + row['DOMESTIC OUTBOUND']
                 ListACT[3] = ListACT[3] + row['INTERNATIONAL INBOUND']
                 ListACT[4] = ListACT[4] + row['INTERNATIONAL OUTBOUND']
                 ListACT[0] = ListACT[0] + row['TOTAL FLIGHTS']

print('Working...')
print('')

def lsp(list):
    t = list
    print('Total Flights: ' + str(t[0]))
    print('Domestic Inbound: ' + str(t[1]))
    print('Domestic Outbound: ' + str(t[2]))
    print('International Inbound: ' + str(t[3]))
    print('International Outbound: ' + str(t[4]))
    print('')

print('NSW')
lsp(ListNSW)

print('TAS')
lsp(ListTAS)

print('ACT')
lsp(ListACT)

print('QLSD')
lsp(ListQSLD)

print('WA')
lsp(ListWA)

print('NT')
lsp(ListNT)

print('SA')
lsp(ListSA)

print('VIC')
lsp(ListVIC) 
