# Inflation_bot   
Telegram bot which let you get full information about inflation rate, price change, purchasing power of money
in such countries and unions as **Belarus🇧🇾, Brazil🇧🇷, Canada🇨🇦, European Union🇪🇺, Eurozone, France🇫🇷, Germany🇩🇪, Greece🇬🇷, India🇮🇳, 
Japan🇯🇵, Kazakhstan🇰🇿, Mexico🇲🇽, Russia🇷🇺, Spain🇪🇸, Turkey🇹🇷, Ukraine🇺🇦, United Kingdom🇬🇧, United States🇺🇸.** 
Inflation_bot uses [Statbureau Api](https://www.statbureau.org/en/inflation-api)





###Commands
[Inflation_bot](https://telegram.me/Inflation_bot) supports the following commands:  

`Inflation <country> <startdate>-<enddate>`  
The command allows **calculating inflation rate** (percentage) between the start of the first month and end of the second for a given country.
* _country_ - the name of country or Emoji flag (e. g. European Union, EU or 🇪🇺)
* _startdate_ - the first year or month, inclusive (e. g. 1993, 1993/05 or 1993/5)
* _enddate_ - the last year or month, inclusive  
returns inflation rate, decimal, percentage

`Price change <country> <startdate>-<enddate> <decimal amount>`  
The command allows **calculating the price change** due to inflation between the start of the first month and end of the second for a given country.  
* _country_ - the name of country or Emoji flag
* _startdate_ - the first year or month, inclusive
* _enddate_ - the last year or month, inclusive
* _amount_ - the price in the beginning of the first month  
returns the price in the end of the second period, adjusted to the inflation, decimal  


`Value change <country> <startdate>-<enddate> <decimal amount>`  
The command allows **to determine the change of the money purchasing power** due to inflation between the start of the first month and end of the second for a given country.  
* _country_ - the name of country or Emoji flag
* _startdate_ - the first year or month, inclusive
* _enddate_ - the last year or month, inclusive
* _amount_ - the price in the beginning of the first month  
returns the amount in the end of the second period, adjusted to the inflation, decimal


`Get denominations <country>`  
* _country_ - the name of country or Emoji flag  
returns a list of denominations that happened in the given country.

`Get inflation <country> <startdate>-<enddate> <m*>`(_*optional. Set annual by default_)
* _country_ - the name of country or Emoji flag
* _startdate_ - the first year or month, inclusive
* _enddate_ - the last year or month, inclusive
* _m_ - get monthly inflation rates  
returns the full dataset of annual or monthly inflation rates from _startdate_ to _enddate_.







###### For more data visit [www.statbureau.org](https://www.statbureau.org) 
