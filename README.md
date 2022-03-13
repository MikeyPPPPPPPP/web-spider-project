TODO
finish the spider 

bonus:
add logging

import logging
logger = logging.getLogger()
handler = logging.FileHandler('spider.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


use inharentance