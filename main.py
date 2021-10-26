import requests.exceptions

import settings
import report
import vk_api_only

if __name__ == '__main__':

    print('***SETTINGS***')
    report_settings = settings.get_settings()
    print('***SETTINGS***\n')

    print('GET_FRIENDS_REPORT')
    try:
        raw_data = vk_api_only.get_friends(report_settings['token'], report_settings['id'])
    except ValueError as value_error:
        print(f'The report cannot be received for the following reason: {value_error}')
    except requests.exceptions.ConnectionError:
        print('Failed to connect to VK API, check your connection and try again')
    except requests.exceptions.Timeout:
        print('Request timeout to VK API, try again')
    print('DONE\n')

    raw_data = report.list_to_df(raw_data)

    print('REFACTOR_REPORT')
    try:
        data = report.full_refactor(raw_data)
    except ValueError as value_error:
        print(f'The report cannot be received for the following reason: {value_error}')
    print('DONE\n')

    print('SAVE_REPORT')
    try:
        report.save_report(data, report_settings['format'])
    except ValueError as value_error:
        print(f'The report cannot be received for the following reason: {value_error}')
    print('DONE\n')