import csv
import pandas as pd
class Actions:
    def __init__(self):
        self.sortContact()
    def add_contact(self,nametoadd,numbertoadd):
        with open('Contact.csv','a',newline='\n') as file:
            writer = csv.writer(file)
            writer.writerow([nametoadd,numbertoadd])
            file.close()
        self.sortContact()
    def delete_contact(self,nametodelete):
        df = pd.read_csv('Contact.csv')
        if nametodelete not in df.Name.values.tolist():
            raise Exception("Not present")
        else:
            df =df.drop(df.loc[df['Name']==nametodelete].index)
            df.to_csv('Contact.csv',index=False)
        self.sortContact()
    def displayall(self):
        df = pd.read_csv('Contact.csv')
        if len(df)==0:
            return 'Contact is Empty'
        return df.to_string(index=False)
    def sortContact(self):
        df = pd.read_csv('Contact.csv')
        df = df.sort_values(by=['Name'],kind='heapsort')
        df.to_csv('Contact.csv',index=False)
    def updateContact(self,nametoupdate,new_number):
        df = pd.read_csv('Contact.csv')
        nameslist = df.Name.values.tolist()
        if nametoupdate not in df.Name.values.tolist():
            raise Exception("Not present")
        else:
            self.delete_contact(nametoupdate)
            self.add_contact(nametoupdate,new_number)
    def searchContact(self,nametosearch):
        df = pd.read_csv('Contact.csv')
        if nametosearch not in df.Name.values.tolist():
            raise Exception("Not present")
        else:
            df = df.loc[df['Name']==nametosearch]
            return df.to_string(index=False)
a = Actions()