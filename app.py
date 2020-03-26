from Company import Company
from Deal import Deal

##########################################
#sis radas, ka ievieto mainigaja ar visam kludainajam rindam
############################################
def remove_incorrect_line(deals_list):
    new_list = deals_list
    for string_line in new_list:
        if len(string_line.split(delimiter)) < 4:
            new_list.remove(string_line)
    return new_list


delimiter = "XXX"
deals = open("deals.csv", "r")
company_data = open("companyData.txt", "r")
company_name_list = []
deals_line_list = remove_incorrect_line(deals.readlines())
company_obj_dic = {} #saraksts ar Company objektiem, kur katram company name ir atbilstošs objekts
deals_obj_list = []

###############################
#sis nez kadel nedarbojas,
# jo pec tam lietotjot deals_line_list, tas ir ar kludainajam rindam
###############################
#for line in deals_line_list:
 #   if len(line.split(delimiter)) < 4:
  #      deals_line_list.remove(line)

#izveido dictionary ar company objektiem pret katru company nosaukumu
for line in company_data:
    company_name_list.append(line.split("-")[0].strip())
    company_obj_dic.update({line.split("-")[0].strip(): Company(line.split("-")[0].strip(), int(line.split("-")[1]))})

#saliek deal objektus listā
for line in deals_line_list:
    if len(line.split(delimiter)) < 4:
        continue
    line_split_list = line.split(delimiter)
    deals_obj_list.append(Deal(line_split_list[0], line_split_list[1], line_split_list[2], line_split_list[3]))

#sis veel jaapapeta vai ir logiski, jo printejot zemak rada vienu un to pašu objektu
#dazadam kompanijam
for deal in deals_obj_list:
    #company.buyer or company.seller
    company_obj_dic[deal.buyer].deals.append(deal)
    company_obj_dic[deal.seller].deals.append(deal)

#for name in company_name_list:
   # print(company_obj_dic[name].deals[0])


#deals.close()
#company_data.close()
