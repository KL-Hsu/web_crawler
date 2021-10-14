import requests 
from bs4 import BeautifulSoup
import pandas as pd 
import time 
'''
Author: Allen Hsu 
Date: 2021/10/13
Purpose: Download table of protein cleavage sites by given Uniprot ID(s) from TopFind database
Input: A list file of Uniprot IDs 
Output: Downloaded .csv file (cleavage site info) per each ID
        Three log files contains info of running time, protein without cleavage, Error 
Target database: TopFind(https://topfind.clip.msl.ubc.ca/home/index)
'''

def save_list(a_list, filename):
    string = '' 
    with open(filename, 'w') as f:
        for i in a_list:
            string += str(i) + '\n'
        f.write(string)

ID_ls = []
with open('Dependency/uniprot_IDs_reviewed_human_proteins.list', 'r') as f:
    IDs = f.readlines() 
    for ID in IDs:
        ID_ls.append(ID.strip())

time_ls = []
error_ls = []
no_cleavage_ls = []

for ID in ID_ls:

    try:
        start = time.time()
        response = requests.get('https://topfind.clip.msl.ubc.ca/proteins/show/' + ID)
        soup = BeautifulSoup(response.text, 'html.parser')
        end = time.time()
        run_time = end - start
        time_ls.append(run_time)
        print('Sucess! ', run_time)

        cleavage_num = int(soup.find_all("div", class_="card")[2].find('h2').getText().strip())

        if cleavage_num != 0:
            tables = soup.find_all('table')
            df = pd.read_html(str(tables))[3]

            gene_name = pd.read_html(str(tables))[0][1][1]
            uniprot_ID = pd.read_html(str(tables))[0][1][6]
            
            Gene_name_ls = [gene_name for i in range(len(df["Position"]))]
            uniprot_ID_ls = [uniprot_ID for i in range(len(df["Position"]))]
            
            df.insert(loc=0, column="Uniprot ID", value=uniprot_ID_ls)
            df.insert(loc=0, column="Gene name", value=Gene_name_ls)
            
            filename = 'Download/'+ID+'.csv'
            df.to_csv(filename, index=False)
        else:
            no_cleavage_ls.append(ID)

    except:
        error_ls.append(ID)
        print("Error! ", ID)

save_list(time_ls, 'Log/time.txt')
save_list(error_ls, 'Log/error.txt')
save_list(no_cleavage_ls, 'Log/no_cleavage.txt')