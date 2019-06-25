# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


email = 'tester@gmail.com'
login = 'TesterWSB'
haslo_email = '123456789Yko'
valid_telephone = '723245685'
valid_kraj = 'Polska'
firma = 5 # Rodzaje firmy:
# jednoosobowa działalność gospodarcza = 3
# spółka akcyjna = 4
# spółka z o.o. = 5
# spółka komandytowo-akcyjna = 6
# spółka komandytowa = 7
# spółka partnerska = 8
# spółka jawna = 9
# fundacja = 10
# stowarzyszenie rejestrowe = 11
# spółka cywilna = 12
# inny = 2
KRS = '0000978'
name = 'Kostiantyn' #
surname = 'Yakushenko' #
nazwa_firmy = 'WSBtest'
nip_firmy = '1545500645'
adres_firmy = 'ul. 9 Maja'
kod_pocztowy = '51-671'
miasto = 'Wroclaw'
wojew = 'DS' # Województwo:
# dolnośląskie = DS
# kujawsko-pomorskie = KP
# lubelskie = LB
# lubuskie = LS
# łódzkie = LD
# małopolskie = MP
# mazowieckie = MZ
# opolskie = OP
# podkarpackie = PK
# podlaskie = PL
# pomorskie = PM
# śląskie = SL
# świętokrzyskie = SK
# warmińsko-mazurskie = WM
# wielkopolskie = WP
# zachodniopomorskie = ZP


class AllegroRegistration(unittest.TestCase):
    """
    Scenariusz Rejestracja
    """
# Warunki wstępne:
    # Wejdz na https://allegro.pl#/
    def setUp(self):
        self.driver = webdriver.Chrome() #Firefox()
        self.driver.get("https://allegro.pl")
        # Maksymalizuj okno przeglądarki
        self.driver.maximize_window()

    def tearDown(self):
        pass


    def test_case1(self):
        driver = self.driver
        time.sleep(1)

        Rejestracja_data_analytics = driver.find_element_by_xpath('//button[@data-role="reject-consent"]')
        Rejestracja_data_analytics.click()

        # 1. Kliknij w prawym górnym rogu "Moje ALLEGRO"
        MojeAllegro_btn = driver.find_element_by_xpath('//span[@data-description="header account name"]')
        MojeAllegro_btn.click()
        # 2. Kliknij "ZALOZ KONTO"
        Rejestracja_btn = driver.find_element_by_xpath('//a[@data-description="header register button"]')
        Rejestracja_btn.click()
        # 3. Kliknij "firma"
        firma_btn = driver.find_element_by_xpath('//label[@class="m-label"] [@for="radio2"]')
        firma_btn.click()
        time.sleep(3)
        # 4. Wprowadź adres email
        email_field = driver.find_element_by_xpath('//*[@formcontrolname="email"] [@id="email"]')
        email_field.send_keys(email)

        #5. Wprowadź Login
        Login_field = driver.find_element_by_xpath('//*[@formcontrolname="login"] [@id="login"]')
        Login_field.send_keys(login)

        #6. Wprowadź Haslo
        haslo_field = driver.find_element_by_xpath('//input[@autocomplete="new-password"] [@id="password"]')
        haslo_field.send_keys(haslo_email)

        #7. Wprowadź Telefon
        telefon_field = driver.find_element_by_xpath('//input[@formcontrolname="phone"] [@id="phone"]')
        telefon_field.send_keys(valid_telephone)

        #8. Wprowadź kraj
        kraj_field = driver.find_element_by_xpath('//*[@formcontrolname="countryCode"]')
        kraj_field.click()
        # pozostałe kraje ...
        kraj2_field = driver.find_element_by_xpath('//option[@value="-1"]')
        kraj2_field.click()
        # Wpisujemy potrzebnej kraj
        kraj3_field = driver.find_element_by_xpath('//input[@placeholder="Wpisz nazwę kraju"] [@id="countryName"]')
        kraj3_field.send_keys(valid_kraj)
        kraj4_field = driver.find_element_by_xpath('//*[@class="m-type m-type--paragraph m-color-gray"]')
        kraj4_field.click()

        #9.  Wprowadź Rodzaj firmy
        rodzaj_field = driver.find_element_by_xpath('//*[@formcontrolname="legalForm"]')
        rodzaj_field.click()

        odzaj_field = driver.find_element_by_xpath('//option[@value="%s"]'%(firma))
        odzaj_field.click()

        #10. Wprowadź KRS
        if ( 4 <= firma <= 11 ):
            krs_field = driver.find_element_by_xpath('//*[@formcontrolname="companyRegister"]')
            krs_field.send_keys(KRS)
        elif ( firma == 3 ):
            #11. Wprowadź Imię
            name_field = driver.find_element_by_xpath('//*[@formcontrolname="firstName"]')
            name_field.send_keys(name)
            #12. Wprowadź Nazwisko
            surname_field = driver.find_element_by_xpath('//*[@formcontrolname="lastName"]')
            surname_field.send_keys(surname)

        #13. Wprowadź Nazwa firmy
        nazwa_field = driver.find_element_by_xpath('//*[@formcontrolname="name"]')
        nazwa_field.send_keys(nazwa_firmy)
        #14. Wprowadź nip
        nip_field = driver.find_element_by_xpath('//*[@formcontrolname="taxId"]')
        nip_field.send_keys(nip_firmy)
        #15. Wprowadź Adres firmy
        adres_field = driver.find_element_by_xpath('//*[@formcontrolname="addressLine"]')
        adres_field.send_keys(adres_firmy)
        #16. Wprowadź Kod pocztowy
        kod_pocz_field = driver.find_element_by_xpath('//*[@formcontrolname="zipCode"]')
        kod_pocz_field.send_keys(kod_pocztowy)
        #17. Wprowadź Miasto
        miasto_field = driver.find_element_by_xpath('//*[@formcontrolname="city"]')
        miasto_field.send_keys(miasto)

        #18. Wprowadź wojewodztwo wojew.
        wojew_field = driver.find_element_by_xpath('//*[@formcontrolname="state"]')
        wojew_field.click()

        wojew_field = driver.find_element_by_xpath('//option[@value="%s"]'%(wojew))
        wojew_field.click()

        #19. Kliknij "Akceptuje postanowienia Regulaminu Allegro"
        regulamin_btn = driver.find_element_by_xpath('//label[@class="m-label"] [@for="agreementTerms"]')
        regulamin_btn.click()


        #20. Kliknij "ZAKLADAM KONTO"
        rejest_btn = driver.find_element_by_xpath('//button[@id="submitFrom"]')
        rejest_btn.click()



        driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        time.sleep(7)
        driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
