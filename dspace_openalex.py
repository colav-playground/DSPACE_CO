#!/usr/bin/env python
# coding: utf-8
import helium as hel
import pandas as pd
import time

df = pd.read_csv('https://github.com/colav-playground/DSPACE_CO/raw/refs/heads/main/dspace_openalex.csv')
df['repository_name'] = df['repository_name'].str.replace('\t',' ')

hel.start_chrome()
hel.go_to('https://docs.google.com/forms/d/e/1FAIpQLSf86ozWOlLPmlP9wsSyL7LBdjn867ydLsbcEEAb_4wE1Ug2NQ/viewform')

for i in list(range(31,df.shape[0])):
    hel.write('restrepo@udea.edu.co',into="Correo electrónico")
    hel.write(df.iloc[i]['base_url'],into="Your repository's OAI-PMH endpoint")
    hel.write(df.iloc[i]['repository_name'],into="Your repository's name")
    hel.press(hel.TAB)
    hel.write(df.iloc[i]['home_page'])
    hel.write(df.iloc[i]['inst_name'],into="Institution that hosts your repository")
    hel.click("Enviar")
    time.sleep(1)
    hel.wait_until(hel.Text("Enviar otra respuesta").exists)

    hel.click('Enviar otra respuesta')
    hel.wait_until(hel.Text("Correo electrónico").exists)
    #break
