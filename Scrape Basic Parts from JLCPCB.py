#!python3
import http.client
import json
import csv

conn= http.client.HTTPSConnection("jlcpcb.com")
headers = {'Content-type': 'application/x-www-form-urlencoded'}
with open('Basic Parts.csv', 'w', newline='') as csv_file:
    component_writer = csv.writer(csv_file, delimiter=';')
    component_writer.writerow(['Manufacturer','LCSC Part #','Description','Package','Stock','Type','MFR.Part #',
                                      'Datasheet','Price (USD)'])
    for n in range(1,8):
        data=f"currentPage={n}&pageSize=100&keyword=&secondeSortName=&componentSpecification="
        conn.request("POST", "/shoppingCart/smtGood/selectSmtComponentList", data , headers)
        r1 = conn.getresponse()
        body = r1.read()
        print(r1.status)        
        for component in json.loads(body)['data']['list']:
            if component['componentLibraryType']=='base':
                component_writer.writerow([component['componentBrandEn'],component['componentCode'],component[ 'describe'],component['componentSpecificationEn']+"\t",
                                            component['stockCount'],component['componentTypeEn'],component['componentModelEn'],component['dataManualUrl'],
                                            str(component['componentPrices'][0]['productPrice']).replace('.',',')])      
conn.close()

