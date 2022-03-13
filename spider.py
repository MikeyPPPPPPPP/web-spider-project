#!/usr/local/bin/python3
from getargs.getArgs import getArguments
from core import menu, setSettings, spider

def main(args):
    s = setSettings.setup()

    if args.url != '':
        s.changeSetting('url', args.url)
    if args.useragent != None:
        s.changeSetting('useragent', args.useragent)
    if args.depth != None:
        s.changeSetting('depth', args.depth)
    if args.branch != None:
        s.changeSetting('depth', args.depth)

    m = menu.MainMenu()
    m.home(s.returnSettings())

    ms = spider.mainSpider(s.returnSettings())
    ms.getInitalUrls()
    ms.weNeedToGoDeeper()
            

if __name__ == '__main__':
    arg = getArguments()
    sett = arg.Gargs()
    if sett.url:
        main(sett)
    




