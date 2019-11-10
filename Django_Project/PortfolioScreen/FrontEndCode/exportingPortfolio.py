import json
from django.http import HttpResponse, FileResponse
import os
import csv
import sys
import json
from fpdf import FPDF
from .PDFWriter import PDFWriter

x = '{ "name":"John", "age":30, "city":"New York"}'

def error_exit(message):
    sys.stderr.write(message)
    sys.exit(1)


def exportCSV(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="output.csv"'

    y = json.loads(x)
    writer = csv.writer(response)
    for (k, v) in y.items():
        writer.writerow([str(k),str(v)])
    return response

def exportPDFAlt(request):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial")
    pdf.cell(200, 10, txt="Welcome to Python!", ln=1, align="C")
    pdf.output("simple_demo.pdf")
    f = open("simple_demo.pdf",'rb')
    response = FileResponse(f,as_attachment=True)
    #HttpResponse(pdf.output("simple_demo.pdf"),content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="output.pdf"'
    #os.remove("simple_demo.pdf")
    return response


def exportPDF(request):


    y = json.loads(x)
    lis = []
    for (k, v) in y.items():
        lis.append(k+","+str(v))

    data = { \
        'pdf_filename': 'output.pdf', \
        'font_name': 'Courier', \
        'font_size': 12, \
        'header': 'Your_Portfolio', \
        'lines': lis \
        }

    try:
        pdf_filename = data['pdf_filename']
        font_name = data['font_name']
        font_size = data['font_size']
        header = data['header']
        lines = data['lines']
    except Exception as e:
        error_exit("Invalid JSON data: {}".format(e))
    # Generate the PDF using the data values.
    try:
        with PDFWriter(pdf_filename) as pw:
            pw.setFont(font_name, font_size)
            pw.setHeader(header)
            for line in lines:
                pw.writeLine(line)
            pw.close()
            f = open("output.pdf", 'rb')
            response = FileResponse(f, as_attachment=True)
            # HttpResponse(pdf.output("simple_demo.pdf"),content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="output.pdf"'
    except IOError as ioe:
        error_exit("IOError while generating PDF file: {}".format(ioe))
    except Exception as e:
        error_exit("Error while generating PDF file: {}".format(e))


    return response