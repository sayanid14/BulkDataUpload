import json
import pandas as pd
from simple_salesforce import Salesforce, SalesforceLogin,  SFType

username = 'shine@gmail.com'
password = 'Hogwarts14$'
security_token = 'fbkJaHZ2a01483BuI98LhXk1'
domain = 'login'

#sf = Salesforce(username=username, password=password, security_token=security_token, domain=domain)
#print(sf)
session_id, instance= SalesforceLogin(username=username, password=password, security_token=security_token, domain=domain)
sf = Salesforce(instance=instance, session_id=session_id)

#meta_org=sf.describe()
#df_sobjects= pd.DataFrame(meta_org['sobjects'])
#df_sobjects.to_csv('org metadata info.csv', index=False)

load_data=pd.read_csv('Bulk_Test.csv')
bulk_data=[]
for row in load_data.itertuples() :
    d =row._asdict()
    del d['Index']
    bulk_data.append(d)

sf.bulk.Bulk_Test__c.insert(bulk_data)


