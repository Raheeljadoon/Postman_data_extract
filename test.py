import json
from fpdf import FPDF



with open('token url.postman_test_run.json')as f:
    data = json.load(f)


# print(data)
url=''
name=''
time=''
response_code=''
response_name=''
number =  1
# my_data = data[]
with open('postman.txt', 'w') as f:
    for result_data in data['results']:
    # print(result_data)
    

        url  = result_data['url']+'\n'
        name = result_data['name']+'\n'
        time = str(result_data['time'])+'\n'
        response_code = str(result_data['responseCode']['code'])+'\n'
        response_name = result_data['responseCode']['name']+'\n'

        f.write('================API NO :'+str(number)+'\n')   
        f.write('\n') 
        f.write('url is :'+url)
        f.write('name is :'+name)
        f.write('time is :'+str(time))
        f.write('response code is :'+str(response_code))
        f.write('response name is :'+response_name)
        f.write('\n')

        number +=1
      

pdf = FPDF()


pdf.add_page()


pdf.set_font("Arial", size = 15)

g = open("postman.txt", "r")
for x in g:
    pdf.cell(200, 10, txt = x, ln = 1, align = 'C')

# save the pdf with name .pdf
pdf.output("POStman_api.pdf")  



