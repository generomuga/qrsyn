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

list_input = []

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

c.setPageSize((200,400)) 

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

            #print (uuid)
            #print (crpcd+' '+matid+' '+hname+' '+abbrc+' '+cgene+' '+admnc+' '+polid+' '+lotid+' '+gencd+' '+fptid+' '+mcnbd+' '+mvrmk+' '+mltst+' '+mstsl+' '+label)
            #_create_barcodes(matid,lotid,admnc,hname,fptid,cgene,mcnbd,crpcd,gencd)           
            #_create_barcodes(crpcd,matid,hname,abbrc,cgene,admnc,lotid,gencd,fptid,uuid,altid,mltst,treat,discl,label,highAbbrc)           
            list_input.append(crpcd+','+matid+','+hname+','+abbrc+','+cgene+','+admnc+','+lotid+','+gencd+','+fptid+','+uuid+','+altid+','+mltst+','+treat+','+discl+','+label+','+highAbbrc)

    #loop = len(list_input)/4.0
    rowCount = len(list_input)/4.0
    #rowCount = 32/4.0
    rem = len(list_input) % 4

    if rem == 1:
        rowCount = round(rowCount) + 1
        for i in range(3):
            list_input.append(crpcd+','+matid+','+hname+','+abbrc+','+cgene+','+admnc+','+lotid+','+gencd+','+fptid+','+uuid+','+altid+','+mltst+','+treat+','+discl+','+label+','+highAbbrc)
    if rem == 2:
        rowCount = round(rowCount) + 1
        for i in range(2):
            list_input.append(crpcd+','+matid+','+hname+','+abbrc+','+cgene+','+admnc+','+lotid+','+gencd+','+fptid+','+uuid+','+altid+','+mltst+','+treat+','+discl+','+label+','+highAbbrc)
    if rem == 3:
        rowCount = round(rowCount) + 1
        for i in range(1):
            list_input.append(crpcd+','+matid+','+hname+','+abbrc+','+cgene+','+admnc+','+lotid+','+gencd+','+fptid+','+uuid+','+altid+','+mltst+','+treat+','+discl+','+label+','+highAbbrc)
    if rem == 0:
        rowCount = round(rowCount) + 1

    #print (str(rem)+' '+str(rowCount))
    in1,in2,in3,in4 = 0,1,2,3
    inc = 4
    for idx in range(int(rowCount)):
        print (str(in1)+' '+str(in2)+' '+str(in3)+' '+str(in4))
        _createBarcode(in1,in2,in3,in4)
        in1 = in1 + inc
        in2 = in2 + inc
        in3 = in3 + inc
        in4 = in4 + inc
    
def _create_barcodes(crpcd,matid,hname,abbrc,cgene,admnc,lotid,gencd,fptid,uuid,altid,mltst,treat,discl,label,highAbbrc):
 
    # draw a QR code
    #qr_matid = qr.QrCodeWidget(matid)
    #bounds = qr_matid.getBounds()
    
    qr_uuid = qr.QrCodeWidget(uuid)
    bounds = qr_uuid.getBounds()
        
    width = bounds[2] - bounds[0]
    height = bounds[3] - bounds[1]
   
    #size of the drawing
    #qmatid = Drawing(10, 10, transform=[80./width,0,0,80./height,0,0])
    #qlotid = Drawing(45, 45, transform=[80./width,0,0,80./height,0,0])
    #qmatid.add(qr_matid)

    quuid = Drawing(45, 45, transform=[80./width,0,0,80./height,0,0])
    quuid.add(qr_uuid)
 
    #qrcode for matid
    #renderPDF.draw(qmatid, c, 110, 10)

    #qrcode for uuid
    renderPDF.draw(quuid, c, 5,300)
    
    '''
    
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


def _createBarcode(in1,in2,in3,in4):
 
    # draw a QR code
    #qr_matid = qr.QrCodeWidget(matid)
    #bounds = qr_matid.getBounds()

    buffQrVer = 8
    buffQrHor = 0

    if in1 >= 0:

        crpcd,matid,hname,abbrc,cgene,admnc,lotid,gencd,fptid,uuid,altid,mltst,treat,discl,label,highAbbrc = list_input[in1].split(',')

        qr_uuid = qr.QrCodeWidget(uuid)
        bounds = qr_uuid.getBounds()
            
        width = bounds[2] - bounds[0]
        height = bounds[3] - bounds[1]
       
        #size of the drawing
        #qmatid = Drawing(10, 10, transform=[80./width,0,0,80./height,0,0])
        #qlotid = Drawing(45, 45, transform=[80./width,0,0,80./height,0,0])
        #qmatid.add(qr_matid)

        quuid = Drawing(45, 45, transform=[80./width,0,0,80./height,0,0])
        quuid.add(qr_uuid)
     
        #qrcode for matid
        #renderPDF.draw(qmatid, c, 110, 10)

        #qrcode for uuid
        renderPDF.draw(quuid, c, 5,300+buffQrVer)
        
        #label number
        c.setFont('Helvetica',12)
        c.drawString(15,375+buffQrVer,str(in1+1))

        #label matid
        c.setFont('Helvetica',15)
        c.drawString(70,375+buffQrVer,matid)
        
        #label for admnc
        c.setFont('Helvetica',12)
        c.drawString(90,335+buffQrVer,admnc)


        '''
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
            #print (highAbbrc)

    #_read_csv(directory_input,switch)
    _read_csv(directory_input,highAbbrc)


if __name__ == "__main__":
    
    read_settings()
