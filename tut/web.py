# import pandas as pd # library for data analysis
# import requests # library to handle requests
# from bs4 import BeautifulSoup # library to parse HTML documents
# # get the response in the form of html
# wikiurl="https://en.wikipedia.org/wiki/United_States"
# table_class="infobox ib-country vcard"
# response=requests.get(wikiurl)
# print(response.status_code)


# # parse data from the html into a beautifulsoup object
# soup = BeautifulSoup(response.text, 'html.parser')

# # print('Classes of each table:')
# # for table in soup.find_all('table'):
# #     print(table.get('class'))


# # Creating list with all tables
# tables = soup.find_all('table')

# #  Looking for the table with the classes 'wikitable' and 'sortable'
# table = soup.find('table', class_='infobox')

# # Defining of the dataframe
# df = pd.DataFrame(columns=['Neighborhood', 'Zone', 'Area', 'Population', 'Density', 'Homes_count'])

# # Collecting Ddata
# for row in table.tbody.find_all('tr'):    
#     # Find all data for each column
#     columns = row.find_all('td')
    
#     if(columns != []):
#         neighborhood = columns[0].text.strip()
#         zone = columns[1].text.strip()
#         area = columns[2].span.contents[0].strip('&0.')
#         population = columns[3].span.contents[0].strip('&0.')
#         density = columns[4].span.contents[0].strip('&0.')
#         homes_count = columns[5].span.contents[0].strip('&0.')

#         df = df.append({'Neighborhood': neighborhood,  'Zone': zone, 'Area': area, 'Population': population, 'Density': density, 'Homes_count': homes_count}, ignore_index=True)
#         df.head()














# # indiatable=soup.find('table',{'class':"infobox ib-country vcard"})

# # for i in indiatable:
# #     print(i)
# #     print(" ")


from bs4 import BeautifulSoup
import requests 

soup = BeautifulSoup(requests.get("https://en.wikipedia.org/wiki/United_States").text)
# first we should find our table object:
table = soup.find('table', class_="infobox")
# then we can iterate through each row and extract either header or row values:
header = []
rows = []
for i, row in enumerate(table.find_all('tr')):
    if i == 0:
        header = [el.text.strip() for el in row.find_all('th')]
    else:
        rows.append([el.text.strip() for el in row.find_all('td')])

print(header)
for row in rows:
    print(row)
