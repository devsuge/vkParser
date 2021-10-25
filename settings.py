import pyinputplus as pyip


def get_settings():
    #token = ''
    token = input('Enter your vk_token: ')

    #u_id =
    u_id = input('Enter the id of the person for the report: ')

    formats = ['CSV', 'TSV', 'JSON']
    format = pyip.inputMenu(formats, 'Choose one of type report:\n')
    #format = 'CSV'

    return {'token': token, 'id': u_id, 'format': format}
