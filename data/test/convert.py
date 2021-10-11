# Import the required Module
import tabula
# Read a PDF File
df = tabula.read_pdf("test.pdf", pages='all')[0]
# convert PDF into CSV
tabula.convert_into("test.pdf", "iplmatch.csv",
                    output_format="csv", pages='all')
print(df)
