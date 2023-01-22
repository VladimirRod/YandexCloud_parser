import gspread
import datetime
import json

service_account = gspread.service_account(filename='credentials.json')  # Google Sheet Api token
sheet_id = service_account.open_by_key('********************************************')  # Sheet_id
worksheet = sheet_id.sheet1

with open('vm_info') as vm_info:
    text = vm_info.readlines()[3:]

worksheet.clear()
worksheet.append_row(['Последнее обновление:' + json.dumps(datetime.datetime.now(), default=str)])
worksheet.append_row(['ID', 'Название', 'Зона доступности', 'Статус', 'Внешний IP', 'Внутренний IP'])
for i in text:
    beautify = i.split('|')
    id = beautify[1]
    name = beautify[2]
    zone_id = beautify[3]
    status = beautify[4]
    external_ip = beautify[5]
    internal_id = beautify[6]
    worksheet.append_row([id, name, zone_id, status, external_ip, internal_id])
