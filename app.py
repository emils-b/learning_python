from Company import Company

deals = open("deals.csv", "r")
company_data = open("companyData.txt", "r")
deals_line_list = deals.readlines()
company_obj_list = []

for line in company_data:
    company_obj_list.append(Company(line.split("-")[0].strip(), int(line.split("-")[1])))

for company in company_obj_list:
    print(company.name + " " + str(company.starting_cap))

for line in deals_line_list:
    if len(line.split("XXX")) < 4:
        deals_line_list.remove(line)


deals.close()
company_data.close()