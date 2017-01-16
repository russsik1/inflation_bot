inflationBot_token = '01234XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX56789'
                      
warningMessage = 'Error. Please check your command'

start_text = '*Calculate inflation rate for period:*\n' \
             '_Inflation country yyyy/mm-yyyy/mm*_ (_mm_ - optional)\n' \
             '*Calculate inflation rate for year:*\n' \
             '_country yyyy_\n' \
             '*Calculate the price change:* \n' \
             '_Price change country yyyy/mm-yyyy/mm amount_ \n' \
             '*Determine the change of the money purchasing power:* \n' \
             '_Value change country yyyy/mm-yyyy/mm amount_ \n' \
             '*Get list of denominations* (soon)\n' \
             '_Get denominations country_ \n' \
             '*Get full dataset of annual or monthly inflation rates* (soon)\n' \
             '_Get inflation country_ \n' \
             'List of countries: /countries\n' \
             'Examples: /examples'

help_text = 'For more details see this page'

example_text = 'Type _Inflation Russia 2016/1-2016/12_ and see what get'

not_ready_text = 'The command are still under development (will be ready soon)'

countries = {0: ['united-states',
                 'United States',
                 'united states',
                 'united states of america',
                 'us',
                 'usa',
                 'сша',
                 'соединенные штаты',
                 'соединенные штаты америки',
                 'usd',
                 '$',
                 '🇺🇸'],
             1: ['russia', 'Russia', 'россия',  'rur', '₽', '🇷🇺'],
             2: ['european-union',
                 'European Union',
                 'european union',
                 'eu',
                 'ес',
                 'евросоюз',
                 'европейский союз',
                 'eur',
                 '€',
                 '🇪🇺'],
             3: ['eurozone', 'Eurozone', 'ez', 'еврозона', 'EZ '],
             4: ['japan', 'Japan', 'япония',  'jpy', '¥', '🇯🇵'],
             5: ['germany', 'Germany', 'германия', '🇩🇪'],
             6: ['united-kingdom',
                 'United Kingdom',
                 'united kingdom',
                 'uk',
                 'великобритания',
                 'gbp',
                 '£',
                 '🇬🇧'],
             7: ['canada', 'Canada', 'канада', 'cad', '🇨🇦'],
             8: ['ukraine', 'Ukraine', 'украина',  'uah', '₴', '🇺🇦'],
             9: ['france', 'France', 'франция', '🇫🇷'],
             10: ['india', 'India', 'индия', 'inr', '₹', '🇮🇳'],
             11: ['belarus', 'Belarus', 'беларусь', 'белоруссия', 'byr', 'p.', '🇧🇾'],
             12: ['mexico', 'Mexico', 'мексика',  'mxn', '🇲🇽'],
             13: ['kazakhstan', 'Kazakhstan', 'казахстан', 'kzt', 'лв', '🇰🇿'],
             14: ['spain', 'Spain', 'испания', '🇪🇸'],
             15: ['greece', 'Greece', 'греция', '🇬🇷'],
             16: ['brazil', 'Brazil', 'бразилия', 'brl', 'R$', '🇧🇷'],
             17: ['turkey', 'Turkey', 'турция', 'trl', '₤', '🇹🇷']}

countries_list = ''.join([s[1][-1] + s[1][1] + '\n' for s in countries.items()])
