import os


def monthToNum(shortMonth):
    return {
        'January': 1,
        'February': 2,
        'March': 3,
        'April': 4,
        'May': 5,
        'June': 6,
        'July': 7,
        'August': 8,
        'September': 9,
        'October': 10,
        'November': 11,
        'December': 12
    }[shortMonth]


for file in os.listdir():
    # print(file)
    file_name, file_ext = os.path.splitext(file)
    # print(file_name)
    # print(file_ext)
    f_year, f_month = file_name.split('_')
    # print(file_name.split('_'))
    # print(monthToNum(f_month))
    r_month = str(monthToNum(f_month)).zfill(2)
    # # print(r_month)
    # print('{}{}{}'.format(f_year, r_month, file_ext))
    new_name = '{}{}{}'.format(f_year, r_month, file_ext)
    # # print(new_name)
    os.rename(file, str(new_name))
