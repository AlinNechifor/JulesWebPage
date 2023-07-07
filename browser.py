from selenium import webdriver


class Browser:

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5) #asteapta dupa fiecare element asetapta maxim 5 sec pana il gasesste
    driver.set_page_load_timeout(5) #asteapta maxim 10 sec sa se incarce pagina indifevent de ce pagina accesez

    def close(self):
        self.driver.quit() # inchide driverul