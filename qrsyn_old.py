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
    
    if i == 1:
        list_set = line_settings.strip().split(',')
        directory_input = list_set[0]
        #switch = list_set[1]
        filename = list_set[1]

directory = os.getcwd()+'\\'+'Output' 
    
if not os.path.exists(directory):
    os.makedirs(directory) 

#c = canvas.Canvas(directory+'\\'+'Syngenta_Packet_Print.pdf', pagesize=letter)
c = canvas.Canvas(directory+'\\'+filename, pagesize=letter)

c.setPageSize((400,200)) 

def _read_csv(fname):

    file_csv = open(fname,'r')
    list_csv = []

    for i,line_csv in enumerate(file_csv):
        
        if i > 0:

            list_csv = line_csv.strip().split(',')

            crpcd = list_csv[0]
            matid = list_csv[1]
            hname = list_csv[2]
            abbrc = list_csv[3]
            cgene = list_csv[4]
            admnc = list_csv[5]
            polid = list_csv[6]
            lotid = list_csv[7]
            gencd = list_csv[8]
            fptid = list_csv[9]
            mcnbd = list_csv[10]
            mvrmk = list_csv[11]
            mltst = list_csv[12]
            mstsl = list_csv[13]
            label = list_csv[14]


            #print (crpcd+' '+matid+' '+hname+' '+abbrc+' '+cgene+' '+admnc+' '+polid+' '+lotid+' '+gencd+' '+fptid+' '+mcnbd+' '+mvrmk+' '+mltst+' '+mstsl+' '+label)
            _create_barcodes(matid,lotid,admnc,hname,fptid,cgene,mcnbd,crpcd,gencd)           
            
def _create_barcodes(matid,lotid,admnc,hname,fptid,cgene,mcnbd,crpcd,gencd):
    
    # draw a QR code
    qr_lotid = qr.QrCodeWidget(lotid)
    bounds = qr_lotid.getBounds()
    

    qr_mcnbd = qr.QrCodeWidget(mcnbd)
    bounds = qr_mcnbd.getBounds()
        
    width = bounds[2] - bounds[0]
    height = bounds[3] - bounds[1]
   
    
    #size of the drawing
    qlotid = Drawing(10, 10, transform=[80./width,0,0,80./height,0,0])
    #qlotid = Drawing(45, 45, transform=[80./width,0,0,80./height,0,0])
    qlotid.add(qr_lotid)

    
    qmcnbd = Drawing(45, 45, transform=[80./width,0,0,80./height,0,0])
    qmcnbd.add(qr_mcnbd)
 
    #qrcode for lotid
    renderPDF.draw(qlotid, c, 10, 110)

    #qrcode for mcnbid
    renderPDF.draw(qmcnbd, c, 310,110)
    
    #label matid
    c.setFont('Helvetica',20)
    c.drawString(90,165,matid)
    
    #label lotid
    c.setFont('Helvetica',12)
    c.drawString(20,100,lotid)
    
    #label for admnc 1
    c.setFont('Helvetica',16)
    c.drawString(20,80,admnc)

    #label for highname
    c.setFont('Helvetica',12)
    c.drawString(20,60,hname)

    #label for fptid
    c.setFont('Helvetica',12)
    c.drawString(18,40,fptid)

    #label for cgenes
    c.setFont('Helvetica',12)
    c.drawString(20,25,cgene)

    #label for mcnbd
    c.setFont('Helvetica',12)
    c.drawString(280,100,mcnbd)

    #label for crpcd
    c.setFont('Helvetica',12)
    c.drawString(290,70,crpcd)

    #label for gencd
    c.setFont('Helvetica',12)
    c.drawString(290,30,gencd)

    #label for loc id
    #c.setFont('Helvetica',14)
    #c.drawString(30,30,locci)

    #label for trial info
    #c.setFont('Helvetica',14)
    #c.drawString(80,50,trian)

    #label for entry no 
    #c.setFont('Helvetica',14)
    #c.drawString(80,30,'ENT.NO.')

    #label for entry no value
    #c.setFont('Helvetica',14)
    #c.drawString(140,30,entnn)

    #for new page
    c.showPage()

    c.save()
    #'''
    #pass
  
def read_settings():
    directory_settings = os.getcwd()+'\\'+'setprint.txt'

    file_settings = open(directory_settings,'r')
    list_set = []

    for i,line_settings in enumerate(file_settings):
        
        if i == 1:
            list_set = line_settings.strip().split(',')
            directory_input = list_set[0]
            #switch = list_set[1]
    
    #_read_csv(directory_input,switch)
    _read_csv(directory_input)


if __name__ == "__main__":
    
    read_settings()
