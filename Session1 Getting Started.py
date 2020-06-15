"""   Day1            Profits             SBI
OnePlus    150 Units       200 per phone       3000 per phone
          Day2             Profits             SBI
Oneplus   250 units        200                 3000 per phome
          Day3             Profits             SBI
Oneplus   100 units        200                 3000 per phone

          Day1             Profits             SBI
HomeAppl  120 units        50 per appl         100 per appl
          Day2             Profits             SBI
HomeAppl  220 units        50 per appl         100 per appl
          Day3             Profits             SBI
HomeAppl  180 units        50 per appl         100 per appl

"""
#model
#onePlusDaySales = 150 #A generic programming variable name declaration
one_plus_day_1_sales = 150
one_plus_day_2_sales = 250
one_plus_day_3_sales = 100

profit_to_amazon_from_oneplus = 200.27

discounts_from_sbi_to_oneplus = 3000.12

home_appl_day1_sales = 120
home_appl_day2_sales = 220
home_appl_day3_sales = 180

profit_to_amazon_from_homeappl = 50
discounts_from_sbi_to_homeappl = 3000.12

# Controller: Computation
total_oneplus_sales = one_plus_day_1_sales + one_plus_day_2_sales + one_plus_day_3_sales
total_homeappl_sales = home_appl_day1_sales + home_appl_day2_sales + home_appl_day3_sales
print("total_oneplus_sales",(total_oneplus_sales))
print("total_homeappl_sales",(total_homeappl_sales))

#view: User interface to display the data
net_oneplus_profits = total_oneplus_sales * profit_to_amazon_from_oneplus
net_homeappl_profits = total_homeappl_sales * profit_to_amazon_from_homeappl
print("oneplus sales profits made by amazon",(net_oneplus_profits))
print("homeappl sales profits made by amazon",(net_homeappl_profits))


# computation : where do amazon made more profits

if net_oneplus_profits>net_homeappl_profits:
    print("Amazon made more profits on oneplus by", (net_oneplus_profits - net_homeappl_profits))
else:
    print("Amazon made more profits on Home Appliances by", (net_homeappl_profits - net_oneplus_profits))




