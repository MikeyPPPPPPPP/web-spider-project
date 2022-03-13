
class MainMenu:
    '''This is just the art'''
    def home(self, settings):
        print("""
        by Michael Provenzano

          _________      .__    .___            
         /   _____/_____ |__| __| _/___________ 
         \_____  \\____ \|  |/ __ |/ __ \_  __ \\
        /        \  |_> >  / /_/ \  ___/|  | \/
       /_______  /   __/|__\____ |\___  >__|   
                \/|__|           \/    \/       
        
        """)
        print('      Current Settings')
        print('     -----------------')
        print('      Url:         '+settings['url'])
        print('      User Agent:  '+settings['useragent'])
        print('      Depth:       '+str(settings['depth']))
        print('      Branch:      '+str(settings['branch']))
        print('\n\n')