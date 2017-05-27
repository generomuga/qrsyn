import sys.frozen
from reportlab.graphics.barcode import code39, code128, code93
from reportlab.graphics.barcode import eanbc, qr, usps, ecc200datamatrix
from reportlab.graphics.shapes import Drawing
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import mm,inch
from reportlab.pdfgen import canvas
from reportlab.graphics import renderPDF

#----------------------------------------------------------------------
c = canvas.Canvas("E:\\Sample pics\\barcodes.pdf", pagesize=letter)
c.setPageSize((400,200)) 

def read_csv(fname):

    file_csv = open(fname,'r')
    list_csv = []

    for i,line_csv in enumerate(file_csv):
        
        if i > 0:

            list_csv = line_csv.strip().split(',')

            trid = list_csv[0]
            rrow = list_csv[1]
            plid = list_csv[2]
            locc = list_csv[3]
            cont = list_csv[4]
            plaa = list_csv[5]
            rsst = list_csv[6]
            trin = list_csv[7]
            entn = list_csv[8]
            abr1 = list_csv[9]
            abr2 = list_csv[10]
            abr3 = list_csv[11]
            matd = list_csv[12]
            admc = list_csv[13]
            ress = list_csv[14]
            cgen = list_csv[15]
            malt = list_csv[16]
            plbr = list_csv[17]
            depl = list_csv[18]
            mast = list_csv[19]
            mint = list_csv[20]
            altd = list_csv[21]


            #print (matid)
            create_barcodes(altd,plbr,plid,rrow,matd,abr1,trid,rsst,locc,trin,entn)           

def create_barcodes(altid,plbar,ploid,rnrow,matid,abbrc1,triad,resst,locci,trian,entnn):
 
    #c = canvas.Canvas("E:\\Sample pics\\barcodes"+matid+".pdf", pagesize=letter)
    #c = canvas.Canvas("E:\\Sample pics\\barcodes.pdf", pagesize=letter)
    
    #c.setPageSize((400,400)) 

    # draw a QR code
    qr_altid = qr.QrCodeWidget(altid)
    bounds = qr_altid.getBounds()
    
    qr_plot = qr.QrCodeWidget(plbar)
    bounds = qr_plot.getBounds()
    
    #qr_plot = ecc200datamatrix.ECC200DataMatrix(matid)
    #bounds# = qr_plot.getBounds()
    
    width = bounds[2] - bounds[0]
    height = bounds[3] - bounds[1]
    
    #bounds
    #width = bounds[2] - bounds[0]
    #height = bounds[3] - bounds[1]

    #d = Drawing(45, 45, transform=[45./width,0,0,45./height,0,0])
    
    #size of the drawing
    qaltid = Drawing(45, 45, transform=[80./width,0,0,80./height,0,0])
    qaltid.add(qr_altid)

    qplot = Drawing(45, 45, transform=[80./width,0,0,80./height,0,0])
    qplot.add(qr_plot)

    #qp = Drawing(45, 45)
    #qp.add(qr_plot)
    
    #renderPDF.draw(d, c, 15, 405)
    
    #qrcode for altid
    renderPDF.draw(qaltid, c, 40, 90)

    #qrcode for plotbar
    renderPDF.draw(qplot, c, 270, 115)
    
    #label altid
    c.setFont('Helvetica',12)
    c.drawString(30,85,altid)
    
    #label plot barcode
    c.setFont('Helvetica',12)
    c.drawString(270,110,plbar)
    
    #label for plotid 1
    c.setFont('Helvetica',20)
    c.drawString(80,165,ploid)

    #label for plotid 2
    c.setFont('Helvetica',20)
    c.drawString(210,140,ploid)

    #label for range row 1
    c.setFont('Helvetica',20)
    c.drawString(50,165,rnrow)

    #label for range row 2
    c.setFont('Helvetica',20)
    c.drawString(230,165,rnrow)

    #draw rectangle
    #c.rect(0.2*inch,0.2*inch,1*inch,1.5*inch)
    c.rect(210,70,180,30)

    #label for matid
    c.setFont('Helvetica',20)
    c.drawString(215,78,matid)

    #label for abbrc1
    c.setFont('Helvetica',10)
    c.drawString(210,50,abbrc1)

    #label for trial id
    c.setFont('Helvetica',14)
    c.drawString(210,30,triad)

    #label for research station
    c.setFont('Helvetica',14)
    c.drawString(30,50,resst)

    #label for loc id
    c.setFont('Helvetica',14)
    c.drawString(30,30,locci)

    #label for trial info
    c.setFont('Helvetica',14)
    c.drawString(80,50,trian)

    #label for entry no 
    c.setFont('Helvetica',14)
    c.drawString(80,30,'ENT.NO.')

    #label for entry no value
    c.setFont('Helvetica',14)
    c.drawString(140,30,entnn)

    #for new page
    c.showPage()

    c.save()

 
if __name__ == "__main__":
    
    #create_barcodes()
    read_csv('E:\Sample pics\\Input - Copy.csv')    
    


