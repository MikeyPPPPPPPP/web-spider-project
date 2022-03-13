import argparse

class getArguments:
    '''this will handle getting the arguments befor the program is ran'''
    def Gargs(self):
        self.start = argparse.ArgumentParser()
        self.start.add_argument('--url', help="This is the base url", required=True)
        self.start.add_argument('--depth', help="The depth you want to go (default max)", required=False)
        self.start.add_argument('--branch', help='Go to other domains', required=False)
        self.start.add_argument('--useragent', help='Add a useragent', required=False)
        return self.start.parse_args()