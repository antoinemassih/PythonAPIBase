import camelot

# PDF file to extract tables from
file = "data/eStatement.pdf"

tables = camelot.read_pdf(file)

print("Total tables extracted:", tables.n)