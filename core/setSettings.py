import json
import os

class setup:
    '''this will create a file if there i'snt one already'''
    def __init__(self, name='spiderLog.json'):
        self.filename = name
        if os.path.exists(self.filename) == False:
            with open(self.filename,'w') as file:
                file.write(self.makeNew())
            
    '''This will make a fresh json file with default values'''
    def makeNew(self):
        self.data = {
            'url':'',
            'useragent':'spider',
            'depth':'max',
            'branch':False
        }
        return json.dumps(self.data, indent=3)

    '''this funchion changes a setting in the settings file'''
    def changeSetting(self, setting, value):
        jFile = open(self.filename, "r")
        ojFile = json.load(jFile)
        jFile.close()
        ojFile[setting] = value
        jFile = open(self.filename, "w")
        json.dump(ojFile, jFile, indent=3)
        jFile.close()

    '''Prints the contents of the settings file kinda neat'''
    def showSettings(self):
        jFile = open(self.filename, "r")
        ojFile = json.load(jFile)
        jFile.close()
        print('\nSettings\n--------\n')
        for x in ojFile:
            print(f'{x}:{ojFile[x]}')
        print('\n')

    '''returns the contents of the settings file in a json formate'''
    def returnSettings(self):
        jFile = open(self.filename, "r")
        ojFile = json.load(jFile)
        jFile.close()
        return ojFile