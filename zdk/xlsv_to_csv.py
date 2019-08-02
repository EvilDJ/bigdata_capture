import pandas as pd


def xlsx_to_csv_pd():
    data_xls = pd.read_excel('./data/0.xlsx', index_col=0)
    data_xls.to_csv('./data/0.csv', encoding='utf-8')


if __name__ == '__main__':
    xlsx_to_csv_pd()
