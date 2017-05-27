from reportlab.graphics.barcode import code39, code128, code93
#from reportlab.graphics.barcode import eanbc, qr, usps, ecc200datamatrix
from reportlab.graphics.barcode import eanbc, qr, ecc200datamatrix
from reportlab.graphics.shapes import Drawing
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import mm,inch
from reportlab.pdfgen import canvas
from reportlab.graphics import renderPDF
import reportlab.rl_settings
import os
#----------------------------------------------------------------------


#for reading filename
directory_settings = os.getcwd()+'\\'+'setprint.txt'

file_settings = open(directory_settings,'r')
list_set = []

for i,line_settings in enumerate(file_settings):
    
    if i == 0:
        list_set = line_settings.strip().split(',')
        directory_input = list_set[0]
        switch = list_set[1]
        filename = list_set[2]

directory = os.getcwd()+'\\'+'Output' 
    
if not os.path.exists(directory):
    os.makedirs(directory) 

#c = canvas.Canvas(directory+'\\'+'Syngenta_Packet_Print.pdf', pagesize=letter)
c = canvas.Canvas(directory+'\\'+filename, pagesize=letter)

c.setPageSize((400,200)) 


def _read_csv(fname,sw):

    file_csv = open(fname,'r')
    list_csv = []

    swt = sw

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

            #_create_barcodes(altd,plbr,plid,rrow,matd,abr1,trid,rsst,locc,trin,entn,swt,cont)
            #chang altid to mint
            _create_barcodes(altd,plbr,plid,rrow,matd,abr1,trid,rsst,locc,trin,entn,swt,cont,mint)           

def _create_barcodes(altid,plbar,ploid,rnrow,matid,abbrc1,triad,resst,locci,trian,entnn,swtc,cont,mint):
 
    bot = 15
    mid = 35
    rr_v = 165

    # draw a QR code #21 column mcn
    #delete double range row and plot id
    qr_altid = qr.QrCodeWidget(mint)
    bounds = qr_altid.getBounds()
    
    qr_plot = qr.QrCodeWidget(plbar)
    bounds = qr_plot.getBounds()
        
    width = bounds[2] - bounds[0]
    height = bounds[3] - bounds[1]
   
    #size of the drawing
    qaltid = Drawing(45, 45, transform=[80./width,0,0,80./height,0,0])
    qaltid.add(qr_altid)

    qplot = Drawing(45, 45, transform=[80./width,0,0,80./height,0,0])
    qplot.add(qr_plot)
 
    #qrcode for altid
    renderPDF.draw(qaltid, c, 40, 60)

    #qrcode for plotbar
    renderPDF.draw(qplot, c, 270, 110)
    
    #label altid
    c.setFont('Helvetica',12)
    c.drawString(30,55,altid)
    
    #label plot barcode
    c.setFont('Helvetica',12)
    c.drawString(270,106,plbar)
    
    if (len(ploid)) <= 4:
        #label for plotid 1
        c.setFont('Helvetica',20)
        c.drawString(35,135,ploid)

        #label for plotid 2
        c.setFont('Helvetica',20)
        c.drawString(230,85,ploid)

    else:
        c.setFont('Helvetica',20)
        c.drawString(35,135,ploid)

        #label for plotid 2
        c.setFont('Helvetica',20)
        c.drawString(230,85,ploid)        

    if len(rnrow) == 1:
        #label for range row 1
        c.setFont('Helvetica',20)
        c.drawString(30,rr_v,rnrow)

        #label for range row 2
        c.setFont('Helvetica',20)
        c.drawString(200,rr_v,rnrow)
    else:
        c.setFont('Helvetica',13)
        c.drawString(30,rr_v,rnrow)

        #label for range row 2
        c.setFont('Helvetica',13)
        c.drawString(165,rr_v,rnrow)

    #draw rectangle
    c.rect(210,50,180,30)

    #label for matid
    c.setFont('Helvetica',20)
    c.drawString(215,58,matid)

    if swtc == '1':
        #label for abbrc1

        if (len(abbrc1)) > 30:
            c.setFont('Helvetica',8)
            c.drawString(210,mid,abbrc1)
        else:
            c.setFont('Helvetica',10)
            c.drawString(210,mid,abbrc1)

    #label for trial id
    c.setFont('Helvetica',14)
    c.drawString(210,bot,triad)

    #label for research station
    c.setFont('Helvetica',14)
    c.drawString(30,mid,resst)

    #label for loc id
    c.setFont('Helvetica',14)
    c.drawString(30,bot,locci)

    #label for trial info
    c.setFont('Helvetica',14)
    c.drawString(80,mid,trian)

    #label for entry no 
    c.setFont('Helvetica',14)
    c.drawString(80,bot,'ENT.NO.')

    #label for entry no value
    c.setFont('Helvetica',14)
    c.drawString(140,bot,entnn)

    #label for cpu
    c.setFont('Helvetica',11)
    c.drawString(115,70,'CPU')

    #plaa = '10000'

    #if (len(plaa)) >= 6:
    c.setFont('Helvetica',11)
    c.drawString(140,70,cont)
    #if (len(plaa)) <= 3:
    #    c.setFont('Helvetica',11)
    #    c.drawString(190,98,plaa)

    #for new page
    c.showPage()

    c.save()

def read_settings():
    directory_settings = os.getcwd()+'\\'+'setprint.txt'

    file_settings = open(directory_settings,'r')
    list_set = []

    for i,line_settings in enumerate(file_settings):
        
        if i == 0:
            list_set = line_settings.strip().split(',')
            directory_input = list_set[0]
            switch = list_set[1]
    
    _read_csv(directory_input,switch)


if __name__ == "__main__":
    
    read_settings()
