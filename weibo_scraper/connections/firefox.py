import logging
from selenium.webdriver import Firefox
#from constants import local_paths

def start():
    logging.info('\nstarting the driver')
    #driver = webdriver.PhantomJS(executable_path=local_paths.phantomjs_path)
    driver = Firefox(executable_path='/Users/jhonyortiz/weibo-scraper-master/geckodriver')
    ## necessary for elements to be located
    driver.set_window_size(1124, 850)
    return driver
