# import os
# import tabula

# pdf_dir = 'data/test'
# csv_dir = 'data/Toront_House_History_Price_CSV'

# convert PDF into CSV file
# tabula.convert_into("test.pdf", "output.csv", output_format="csv", pages='all')
# for file in os.listdir(pdf_dir):
#     file_name = file.split('.')[0]
#     print('Converted pdf to csv ...\n')
#     try:
#         tabula.convert_into(f'{pdf_dir}/{file}',
#                             f"{csv_dir}/{file_name}.csv",
#                             output_format="csv", pages="all")
#     except:
#         print(file, 'not converted\n')

# import tabula

# # Read pdf into list of DataFrame
# df = tabula.read_pdf("test.pdf", pages='all')
