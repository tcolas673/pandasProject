import pandas as pd
from contactType import contactList
from matplotlib import pyplot as plt 
import xml.etree.ElementTree as etree
import os


tree = etree.parse('results.xml')
root = tree.getroot()
columns = ['company_name', 'login', 'approved_scope', 'address', 'city', 'state', 'country', 'zip_code', 'contact_name', 'phone_number', 'email']

rows = []

for node in root.findall('Row'):
    
    company_name = node.find("tcb_name").text

    login = node.find("tcb_login").text

    approved_scope = node.find("approved_scope").text

    address = node.find("address").text

    city = node.find("city").text

    state = node.find("state").text

    country = node.find("country").text
    
    zip_code = node.find("zip_code").text

    contact_information = node.find("contact_information").text
    contact_name, email, phone_number = contactList(contact_information)
    rows.append({'company_name': company_name, 'login': login,'approved_scope':approved_scope, 'address':address,'city': city, 'state': state, 'country': country,'zip_code':zip_code, 'contact_name': contact_name, 'email':email, 'phone_number': phone_number })

    dataframe = pd.DataFrame(rows, columns = columns)
    
print(dataframe.groupby('company_name')['approved_scope'].apply(' '.join).head())
