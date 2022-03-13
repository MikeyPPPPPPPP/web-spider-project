import requests
from bs4 import BeautifulSoup

class mainSpider:
    '''This is the main function ie the spider that it is actualy made for'''
    def __init__(self, settings):
        self.mainUrl = settings['url']
        self.urls = {}
        self.doneUrls = []
        self.domains = []
        self.depthCounter = 0
        self.settingDepthCounter = settings['depth']

    '''this will validate a url to make sure it starts with the mainurl'''
    def validetUrl(self, url) -> str:
        if url.startswith(self.mainUrl):
            return url
        else:
            if url.startswith('http') == False:
                if url.startswith('/'):
                    return self.mainUrl+url
                else:
                    return self.mainUrl+'/'+url
            else:
                return url

    '''this will turn https://shopping.google.com/?nord= into https://shopping.google.com/'''    
    def getMainUrl(self, url):
        firsttwo = url.split('/')
        return f'{firsttwo[0]}//{firsttwo[2]}/'
    
    '''This will get all tha a[hrefs] on the first page and the other domains'''
    def getInitalUrls(self):
        self.depthCounter += 1
        self.urls['depth-'+str(self.depthCounter)]=[]
        r = requests.get(self.validetUrl(self.mainUrl)).text
        soup = BeautifulSoup(r, 'lxml')
        for url in soup.find_all('a', href=True):
            if self.validetUrl(url['href']) not in self.urls['depth-'+str(self.depthCounter)]:
                print(self.validetUrl(url['href']))
                if self.validetUrl(url['href']).startswith(self.mainUrl):
                    self.urls['depth-'+str(self.depthCounter)].append(self.validetUrl(url['href']))
                elif self.validetUrl(url['href']).startswith(self.mainUrl) == False:
                    try:
                        if self.mainUrl not in url['href'].split('//')[0] + '//' + url['href'].split('//')[1].split('/')[0]:
                            if url['href'].split('//')[0] + '//' + url['href'].split('//')[1].split('/')[0] not in self.domains:
                                try:
                                    self.domains.append( url['href'].split('//')[0] + '//' + url['href'].split('//')[1].split('/')[0])
                                except:
                                    pass
                    except:
                        pass
        self.doneUrls.append(self.mainUrl)

    
    '''This will recurcivly spider until the depth is reached'''
    def weNeedToGoDeeper(self):
        if self.depthCounter <= int(self.settingDepthCounter):
            self.depthCounter += 1
            self.urls['depth-'+str(self.depthCounter)]=[]
            for urls in self.urls['depth-'+str(self.depthCounter - 1)]:
                r = requests.get(urls).text#self.validetUrl(self.mainUrl)
                soup = BeautifulSoup(r, 'lxml')
                for url in soup.find_all('a', href=True):
                    if self.validetUrl(url['href']) not in [y for x in self.urls for y in self.urls[x]]:
                        if self.validetUrl(url['href']).startswith(self.getMainUrl(urls)):
                            self.urls['depth-'+str(self.depthCounter)].append(self.validetUrl(url['href']))
                            print(self.validetUrl(url['href']))
                        elif self.validetUrl(url['href']).startswith(urls) == False:
                            try:
                                if urls not in url['href'].split('//')[0] + '//' + url['href'].split('//')[1].split('/')[0]:
                                    if url['href'].split('//')[0] + '//' + url['href'].split('//')[1].split('/')[0] not in self.domains:
                                        try:
                                            self.domains.append( url['href'].split('//')[0] + '//' + url['href'].split('//')[1].split('/')[0])
                                        except:
                                            pass
                            except:
                                pass
                self.doneUrls.append(urls)
            self.weNeedToGoDeeper()


        else:
            pass
            

        
    