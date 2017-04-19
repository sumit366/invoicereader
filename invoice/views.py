from django.shortcuts import render
import xlrd
from reportlab.pdfgen import canvas
from django.http import HttpResponse
import xlwt
from .models import Invoice
# import xlsxwriter
# from django.utils.encoding import smart_str
# import csv

def index(request):
    return render(request, 'home.html')


def excel_upload(request):

    if request.method == 'POST':
        file = request.FILES['invoice_file'].read()

        txt = upload_into_DB(file)
        # Create the HttpResponse object with the appropriate PDF headers.
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="Output.pdf"'

        # Create the PDF object, using the response object as its "file."
        p = canvas.Canvas(response)

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        p.drawString(0, 0, txt)

        # Close the PDF object cleanly, and we're done.
        p.showPage()
        p.save()

        return response

    return render(request, 'home.html')


def download_sample(request):
    # response = HttpResponse(content_type='text/csv')
    # response['Content-Disposition'] = 'attachment; filename=sample.csv'
    # writer = csv.writer(response, csv.excel)
    # response.write(u'\ufeff'.encode('utf8'))  # BOM (optional...Excel needs it to open UTF-8 file properly)
    # writer.writerow([
    #     smart_str(u"Product"),
    #     smart_str(u"Customer Type"),
    #     smart_str(u"Date"),
    #     smart_str(u"Actual Cost"),
    #     smart_str(u"Expected Cost"),
    #     smart_str(u"City "),
    #     smart_str(u"State"),
    #     smart_str(u"Zip"),
    #     smart_str(u"Region"),
    # ])

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="sample.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Sample')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Product', 'Customer Type', 'Date', 'Actual Cost', 'Expected Cost', 'City', 'State', 'Zip', 'Region' ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # # Sheet body, remaining rows
    # font_style = xlwt.XFStyle()
    #
    # rows = User.objects.all().values_list('username', 'first_name', 'last_name', 'email')
    # for row in rows:
    #     row_num += 1
    #     for col_num in range(len(row)):
    #         ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)

    return response


def upload_into_DB(file):
    book = xlrd.open_workbook(file_contents=file)
    sheet_names = book.sheet_names()
    sheet = book.sheet_by_name(sheet_names[0])
    txt = ''
    for r in range(1, sheet.nrows):
        product = sheet.cell(r, 0).value
        customer_type = sheet.cell(r, 1).value
        date = sheet.cell(r, 2).value
        actual = sheet.cell(r, 3).value
        expected = sheet.cell(r, 4).value
        city = sheet.cell(r, 5).value
        state = sheet.cell(r, 6).value
        zip_code = sheet.cell(r, 7).value
        region = sheet.cell(r, 8).value

        txt = txt + "Product : " + str(product) + " \n customer_type : " + str(customer_type) + \
              " \n actual : " + str(actual) + " \n expected : " + str(expected) + " \n"

        invoice = Invoice(product=product, customer_type=customer_type, date=date, actual=actual,
                          expected=expected, city=city, state=state, zip=zip_code, region=region)
        invoice.save()

    return txt

