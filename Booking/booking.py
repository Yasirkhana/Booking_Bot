from ast import Str
from datetime import date, datetime
from select import select
from selenium import webdriver

import Booking.constant as const     
import os

class booking(webdriver.Chrome):
    def __init__(self, driver_path=r'C:\seleniumDriver\chromedriver_win32', teardown=False):
         self.driver_path = driver_path
         self.teardown = teardown
         os.environ['PATH'] += self.driver_path
         super(booking, self).__init__()
         self.implicitly_wait(15)
         self.maximize_window()

    def __exit__(self,exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()


    def land_first_page(self):
        self.get(const.URL)
        
    # def change_currency(self, currency=None):
    #     currency_element = self.find_element_by_css_selector(
    #         'button[data-tooltip-text="Choose your currency"]'
    #         )
    #     currency_element.click()
    #     select_currency = self.find_element_by_css_selector(
    #         f'a[data-modal-header-async-url-param*="selected_currency={currency}"]'
    #     )
    #     select_currency.click()

    def select_location(self,location=None):
        enter_location = self.find_element_by_id('ss')
        enter_location.clear()
        enter_location.send_keys(location)

        first_result = self.find_element_by_css_selector(
            'li[data-i="0"]'
        )
        first_result.click()

      
    def select_date(self,check_in_date,check_out_date):

        checkin = self.find_element_by_css_selector(
            f'td[data-date="{check_in_date}"]'
        )
        checkin.click()

        checkout = self.find_element_by_css_selector(
            f'td[data-date="{check_out_date}"]'
        )
        checkout.click()


    def select_guests(self, guest_number=None):

        guest_element = self.find_element_by_id('xp__guests__toggle')

        guest_element.click()

        # # increase_btn = self.find_element_by_css_selector(
        # #     'button[aria-label="Increase number of Adults"]'
        # #     )
        guest_count = self.find_element_by_css_selector(
            'span[data-bui-ref="input-stepper-value"]'
        )
        print("NUmber OF GUEST =" + guest_count.text)
        # # while(guest_number != guest_count){

        # # }    
    while True:
        decrease_button = self.find_element_by_css_selector(
            'button[data-bui-ref="input-stepper-subtract-button"]'
        )
        decrease_button.click()

        increase_btn = self.find_element_by_css_selector(
            'button[data-bui-ref="input-stepper-add-button"]'   
        )
        
        adult_value_element = self.find_element_by_id('group_adults')
        adult_value = adult_value_element.get_attribute('value')

        if int(adult_value) == 1:
            break
