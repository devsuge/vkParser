import requests.exceptions

import settings
import report
import vk_api_only

if __name__ == '__main__':

    report_settings = settings.get_settings()

    try:
        raw_data = vk_api_only.get_friends(report_settings['token'], report_settings['id'])
    except ValueError as value_error:
        print(f'The report cannot be received for the following reason: {value_error}')
    except requests.exceptions.ConnectionError:
        print('Failed to connect to VK API, check your connection and try again')
    except requests.exceptions.Timeout:
        print('Request timeout to VK API, try again')

    raw_data = report.list_to_df(raw_data)

    try:
        data = report.full_refactor(raw_data)
    except ValueError as value_error:
        print(f'The report cannot be received for the following reason: {value_error}')

    try:
        report.save_report(data, report_settings['format'])
    except ValueError as value_error:
        print(f'The report cannot be received for the following reason: {value_error}')
