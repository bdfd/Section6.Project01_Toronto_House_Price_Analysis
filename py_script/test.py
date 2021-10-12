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
    year, month = file_name.split('_')
    # print(monthToNum(month))
    print('{}{}{}{}'.format(year, monthToNum(month), file_name, file_ext))

    # Need to remove whitespace
    # f_title = f_title.strip()
    # f_course = f_course.strip()
    # f_number = f_number.strip()

    # Want to remove the number sign?
    # f_number = f_number.strip()[1:]

    # One thing I noticed about this output is that if it was sorted by filename
    # then the 1 and 10 would be next to each other. How do we fix this? One way we can fix this is to pad
    # the numbers. So instead of 1, we'll make it 01. If we had hundreds of files then this would maybe need to be 001.
    # We can do this in Python with zfill
    # f_number = f_number.strip()[1:].zfill(2)

    # print('{}-{}-{}{}'.format(f_number, f_course, f_title, file_ext))

    # You have the power to reformat in any way you see fit
    # print('{}-{}{}'.format(f_number, f_title.strip(), file_ext.strip()))

    # new_name = '{}-{}{}'.format(file_num, file_title, file_ext)

    # os.rename(fn, new_name)
