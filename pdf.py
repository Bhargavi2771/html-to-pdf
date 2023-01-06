#https://wkhtmltopdf.org/

import pdfkit

#Define path to wkhtmltopdf.exe
path_to_wkhtmltopdf = r'C:Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe'

#Define url
url = 'https://wkhtmltopdf.org'

#Point pdfkit configuration to wkhtmltopdf.exe
config = pdfkit.configuration(wkhtmltopdf = path_to_wkhtmltopdf)

#Convert Webpage to pdf
pdfkit.from_url(url, output_path = 'webpage.pdf', configuration = config)