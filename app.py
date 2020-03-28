from Company import Company
from Deal import Deal


def get_company_with_biggest_purchase():
    biggest_sum = 0
    company_with_biggest_purchase = ""
    for deal in deals_obj_list:
        if int(deal.sum_with_curr[0:-3]) > biggest_sum:
            biggest_sum = int(deal.sum_with_curr[0:-3])
            company_with_biggest_purchase = deal.buyer
    print("Company who made the biggest purchase: " +
          company_with_biggest_purchase + " (" + str(biggest_sum) + "EUR)")


def get_company_with_biggest_purchase_count():
    purchase_count = 0
    company_with_biggest_purchase_count = ""
    for name in company_name_list:
        if company_obj_dic[name].get_total_purchases_count() > purchase_count:
            purchase_count = company_obj_dic[name].get_total_purchases_count()
            company_with_biggest_purchase_count = name
    print("Company with biggest purchase count: " + company_with_biggest_purchase_count +
          ". With: " +str(purchase_count)+" purchases.")


def get_medium_deal_sum():
    sum_counter = 0
    for deal in deals_obj_list:
        sum_counter += int(deal.sum_with_curr[0:-3])
    return round(sum_counter/len(deals_obj_list))


def get_error_type(line):
    all_error_list.append(line)
    if unique_error_type_list.count(line) < 1:
        unique_error_type_list.append(line)


def get_error_type_count():
    for err in unique_error_type_list:
        if err == "\n":
            print("Empty line type errors are " + str(all_error_list.count(err)) + " times in deals doc.")
            continue
        print(err.strip()+" type errors are "+str(all_error_list.count(err))+" times in deals doc.")


delimiter = "XXX"
deals = open("deals.csv", "r")
company_data = open("companyData.txt", "r")
company_name_list = []
deals_line_list = deals.readlines()
company_obj_dic = {} #saraksts ar Company objektiem, kur katram company name ir atbilstošs objekts
deals_obj_list = []
#error_counter = 0
unique_error_type_list = []
all_error_list = []

#izveido dictionary ar company objektiem pret katru company nosaukumu
for line in company_data:
    company_name = line.split("-")[0].strip()
    company_name_list.append(company_name)
    company_obj_dic.update({company_name: Company(company_name, int(line.split("-")[1]))})

#saliek deal objektus listā
for line in deals_line_list:
    if len(line.split(delimiter)) < 4:
        get_error_type(line)
        #error_counter += 1
        continue
    line_split_list = line.split(delimiter)
    deals_obj_list.append(Deal(line_split_list[0].strip(), line_split_list[1].strip(), line_split_list[2].strip(), line_split_list[3]))

get_error_type_count()

#for com_name in company_name_list:
#    for deal in deals_obj_list:
#        if deal.buyer == com_name or deal.seller == com_name:
#            company_obj_dic[com_name].deals.append(deal)

for deal in deals_obj_list:
    company_obj_dic[deal.buyer].deals.append(deal)
    company_obj_dic[deal.seller].deals.append(deal)

#company_obj_dic["Frodo"].get_sales_total()
#company_obj_dic["Frodo"].get_purchases_total()
#company_obj_dic["Frodo"].get_final_balance()
#company_obj_dic["Frodo"].get_purchase_stats()
#get_company_with_biggest_purchase()
#get_company_with_biggest_purchase_count()
#print(str(error_counter) + " errors occurred.")
#print(get_medium_deal_sum())

# izprinte uzņēmumus kuriem gala bilance būtu negatīva
# pat, ja veiktu aizņēmumu sākuma kapitāla vērtībā
for name in company_name_list:
    if company_obj_dic[name].get_final_balance()+company_obj_dic[name].starting_cap < 0:
        print("Negative final balance has: "+company_obj_dic[name].name)


deals.close()
company_data.close()
