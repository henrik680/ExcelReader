import pandas as pd
import openpyxl as excel
import requests


def openExelUrl(url):
    print(url)
    s = requests.get(url).content
    xl = pd.read_excel(s, engine='openpyxl')
    print("done")
    return xl


fileUrl = "http://epi6.energimyndigheten.se/SharePoint/Eugen/Godkända anläggningar.xlsx"
df = openExelUrl(fileUrl)

print(df.head(n=10))