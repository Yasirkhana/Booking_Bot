from ctypes.wintypes import PINT
from locale import currency
from Booking.booking import booking

with booking() as bot:
    bot.land_first_page()
    
    bot.change_currency(currency='USD')
    bot.select_location(location='Karachi, Pakistan')
    bot.select_date(
        check_in_date='2022-01-25',
        check_out_date='2022-01-28')

    bot.select_guests(guest_number=10)

    ## 1:28:52 ##