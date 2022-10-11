import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)  # or 1000
pd.set_option('display.max_rows', None)  # or 1000
pd.set_option('display.max_colwidth', None)


xls = pd.ExcelFile('sales_data.xlsx')


dfSales = pd.read_excel(
    xls, 0, usecols=['_SalesTeamID', "Unit Price"])


dfTeam = pd.read_excel(
    xls, 5, usecols=['_SalesTeamID', 'Sales Team'])


totalSalesPerPerson = {}
amountOfSalesPersons = 28

for teamIndex, teamRow in dfTeam.head(amountOfSalesPersons).iterrows():

    for salesIndex, salesRow in dfSales.head(200).iterrows():
        if teamRow["_SalesTeamID"] == salesRow['_SalesTeamID']:

            if teamRow["_SalesTeamID"] in totalSalesPerPerson:
                totalSalesPerPerson[teamRow["_SalesTeamID"]
                                    ] += salesRow['Unit Price']
            else:
                totalSalesPerPerson[teamRow["_SalesTeamID"]
                                    ] = salesRow['Unit Price']


# alles afronden
for key in totalSalesPerPerson:
    totalSalesPerPerson[key] = round(totalSalesPerPerson[key], 1)


xAxis = totalSalesPerPerson.keys()
yAxis = totalSalesPerPerson.values()

plt.figure(figsize=(11, 6))
plt.bar(xAxis, yAxis)
plt.title('Aantal sales per persoon')
plt.xlabel('Personen')
plt.xticks(list(xAxis))
plt.ylabel('Totaal aantal sales in dollars')

plt.show()
