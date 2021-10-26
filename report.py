import numpy
import numpy as np
import pandas as pd


def list_to_df(list):
    return pd.DataFrame(
        list,
        columns=['first_name', 'last_name', 'country', 'city', 'bdate', 'sex'],
    )


def full_refactor(data_df):
    data_df['country'] = np.vectorize(refactor_dict_location)(data_df['country'])
    data_df['city'] = np.vectorize(refactor_dict_location)(data_df['city'])
    data_df['bdate'] = np.vectorize(refactor_date)(data_df['bdate'])
    data_df['sex'] = np.vectorize(refactor_sex)(data_df['sex'])
    return data_df


def refactor_sex(sex):
    if isinstance(sex, (int, type(np.int64()))):
        if sex == 1:
            return 'Female'
        if sex == 2:
            return 'Male'

        return 'Unknown'
    else:
        raise ValueError('Invalid sex format, expected <int>')


def refactor_dict_location(dict_location):
    if isinstance(dict_location, dict):
        return dict_location.get('title', 'Unknown')
    elif isinstance(dict_location, type(np.nan)):
        return 'Unknown'
    raise ValueError('Invalid se format, expected <dict>')


def refactor_date(date):
    if isinstance(date, str):
        iso_date = date.split('.')

        if len(iso_date) < 2 or len(iso_date) > 3:
            raise ValueError('Invalid date format, expected "DD.MM.YYYY" or "DD.MM"')

        day = f'{"0" if len(iso_date[0]) == 1 else ""}{iso_date[0]}'
        month = f'{"0" if len(iso_date[1]) == 1 else ""}{iso_date[1]}'
        year = iso_date[2] if len(iso_date) == 3 else '0001'

        day_int = int(day)
        if day_int < 1 or day_int > 31:
            raise ValueError('The day should be in the range 1-31')

        month_int = int(month)
        if month_int < 1 or month_int > 12:
            raise ValueError('The month should be in the range 1-12')

        year_int = int(year)
        if year_int < 1:
            raise ValueError('The year should be greater than 0')
    elif isinstance(date, type(np.nan)):
        return '0001-01-01'
    else:
        raise ValueError('Invalid se format, expected <str>')

    return f'{year}-{month}-{day}'


def save_report(df_data, format):
    if format == 'JSON':
        df_data.to_json('./report.json', orient='table', indent=2, index=False)
    elif format == 'TSV':
        df_data.to_csv('./report.tsv', sep='\t', index=False)
    elif format == 'CSV':
        df_data.to_csv('./report.csv', sep=';', index=False)
    else:
        raise ValueError("Unknown report file format")
