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

def _read_csv(fname,highAbbrc):

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
            lotid = list_csv[6]
            gencd = list_csv[7]
            fptid = list_csv[8]
            uuid = list_csv[9]
            altid = list_csv[10]
            mltst = list_csv[11]
            treat = list_csv[12]
            discl = list_csv[13]
            label = list_csv[14]

            #print (crpcd+' '+matid+' '+hname+' '+abbrc+' '+cgene+' '+admnc+' '+polid+' '+lotid+' '+gencd+' '+fptid+' '+mcnbd+' '+mvrmk+' '+mltst+' '+mstsl+' '+label)
            #_create_barcodes(matid,lotid,admnc,hname,fptid,cgene,mcnbd,crpcd,gencd)           
            _create_barcodes(crpcd,matid,hname,abbrc,cgene,admnc,lotid,gencd,fptid,uuid,altid,mltst,treat,discl,label,highAbbrc)           
                        
def _create_barcodes(crpcd,matid,hname,abbrc,cgene,admnc,lotid,gencd,fptid,uuid,altid,mltst,treat,discl,label,highAbbrc):
 
    # draw a QR code
    qr_matid = qr.QrCodeWidget(matid)
    bounds = qr_matid.getBounds()
    
    qr_uuid = qr.QrCodeWidget(uuid)
    bounds = qr_uuid.getBounds()
        
    width = bounds[2] - bounds[0]
    height = bounds[3] - bounds[1]
   
    #size of the drawing
    qmatid = Drawing(10, 10, transform=[80./width,0,0,80./height,0,0])
    #qlotid = Drawing(45, 45, transform=[80./width,0,0,80./height,0,0])
    qmatid.add(qr_matid)

    quuid = Drawing(45, 45, transform=[80./width,0,0,80./height,0,0])
    quuid.add(qr_uuid)
 
    #qrcode for matid
    renderPDF.draw(qmatid, c, 10, 110)

    #qrcode for uuid
    renderPDF.draw(quuid, c, 310,110)
    
    #label matid
    c.setFont('Helvetica',20)
    c.drawString(90,165,matid)
    
    #label lotid
    c.setFont('Helvetica',12)
    c.drawString(20,100,lotid)
    
    #label for highname
    if highAbbrc == '0':
        c.setFont('Helvetica',12)
        c.drawString(20,80,abbrc)
    else:
        c.setFont('Helvetica',12)
        c.drawString(20,80,hname)

    #label for fptid
    c.setFont('Helvetica',12)
    c.drawString(20,60,fptid)

    #label for admnc 
    c.setFont('Helvetica',16)
    c.drawString(20,40,admnc)
    
    #label for treatment
    c.setFont('Helvetica',12)
    c.drawString(20,20,treat)
 
    #label for altid
    c.setFont('Helvetica',12)
    c.drawString(200,120,altid)
    
    #label for cgenes
    c.setFont('Helvetica',12)
    c.drawString(200,100,cgene)
    
    #label for crpcd
    c.setFont('Helvetica',12)
    c.drawString(270,165,crpcd)

    #label for gencd
    c.setFont('Helvetica',12)
    c.drawString(200,60,gencd)

    #label for disclaimer
    c.setFont('Helvetica',10)
    c.drawString(200,40,discl)
    
    '''
    #label for trial info
    #c.setFont('Helvetica',14)
    #c.drawString(80,50,trian)

    #label for entry no 
    #c.setFont('Helvetica',14)
    #c.drawString(80,30,'ENT.NO.')

    #label for entry no value
    #c.setFont('Helvetica',14)
    #c.drawString(140,30,entnn)
    '''
    #for new page
    c.showPage()

    c.save()

def read_settings():
    directory_settings = os.getcwd()+'\\'+'setprint.txt'

    file_settings = open(directory_settings,'r')
    list_set = []

    for i,line_settings in enumerate(file_settings):
        
        if i == 1:
            list_set = line_settings.strip().split(',')
            directory_input = list_set[0]
            highAbbrc = list_set[2]
            #switch = list_set[1]

    #_read_csv(directory_input,switch)
    _read_csv(directory_input,highAbbrc)


if __name__ == "__main__":
    
    read_settings()
