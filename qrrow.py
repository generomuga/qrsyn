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
list_input = []

for i,line_settings in enumerate(file_settings):
    
    if i == 0:
        list_set = line_settings.strip().split(',')
        directory_input = list_set[0]
        switch = list_set[1]
        filename = list_set[3]

directory = os.getcwd()+'\\'+'Output' 
    
if not os.path.exists(directory):
    os.makedirs(directory) 

#c = canvas.Canvas(directory+'\\'+'Syngenta_Packet_Print.pdf', pagesize=letter)
c = canvas.Canvas(directory+'\\'+filename, pagesize=letter)

c.setPageSize((1100,400)) 

def _read_csv(fname,sw):

    file_csv = open(fname,'r')
    list_csv = []

    swt = sw

    #row_count = sum(1 for row in file_csv)
    #print (row_count)
    #saving to list

    for i,line_csv in enumerate(file_csv):
        
        if i > 0:

            list_csv = line_csv.strip().split(',')

            if list_csv[0] != '':
                trid = list_csv[0]
            else:
                trid = 'null'

            if list_csv[1] != '':
                rrow = list_csv[1]
            else:
                rrow = 'null'

            if list_csv[2] != '':    
                plid = list_csv[2]
            else:
                plid = 'null'

            if list_csv[3] != '':
                locc = list_csv[3]
            else:
                locc = 'null'

            if list_csv[4] != '':      
                cont = list_csv[4]
            else:
                cont = 'null'

            if list_csv[5] != '':
                plaa = list_csv[5]
            else:
                plaa = 'null'

            if list_csv[6] != '':
                rsst = list_csv[6]
            else:
                rsst = 'null'

            if list_csv[7] != '':
                trin = list_csv[7]
            else:
                trin = 'null'

            if list_csv[8] != '':
                entn = list_csv[8]
            else:
                entn = 'null'

            if list_csv[9] != '': 
                abr1 = list_csv[9]
            else:
                abr1 = 'null'

            if list_csv[10] != '':    
                abr2 = list_csv[10]
            else:
                abr2 = 'null'

            if list_csv[11] != '':    
                abr3 = list_csv[11]
            else:
                abr3 = 'null'

            if list_csv[12] != '':    
                matd = list_csv[12]
            else:
                matd = 'null'

            if list_csv[13] != '':    
                admc = list_csv[13]
            else:
                admc = 'null'

            if list_csv[14] != '':     
                ress = list_csv[14]
            else:
                ress = 'null'

            if list_csv[15] != '':
                cgen = list_csv[15]
            else:
                cgen = 'null'

            if list_csv[16] != '':   
                malt = list_csv[16]
            else: 
                malt = 'null'

            if list_csv[17] != '':
                plbr = list_csv[17]
            else:
                plbr = 'null'

            if list_csv[18] != '':
                depl = list_csv[18]
            else:
                depl = 'null'

            if list_csv[19] != '':    
                mast = list_csv[19]
            else:
                mast = 'null'

            if list_csv[21] != '':    
                mint = list_csv[20]
            else:   
                mint = 'null'

            if list_csv[21] != '':    
                altd = list_csv[21]
            else:
                altd = 'null'

            list_input.append(trid+','+rrow+','+plid+','+locc+','+cont+','+plaa+','+rsst+','+trin+','+entn+','+abr1+','+abr2+','+abr3+','+matd+','+admc+','+ress+','+cgen+','+malt+','+plbr+','+depl+','+mast+','+mint+','+altd)

            #_create_barcodes(matd,altd,plid,plbr,trid)           

    row_count = int(len(list_input)/4)
    rem = len(list_input) % 4

    if rem == 1:    
        row_count = round(row_count) + 1
        for i in range(3):
            list_input.append(trid+','+rrow+','+plid+','+locc+','+cont+','+plaa+','+rsst+','+trin+','+entn+','+abr1+','+abr2+','+abr3+','+matd+','+admc+','+ress+','+cgen+','+malt+','+plbr+','+depl+','+mast+','+mint+','+altd)            
        
    if rem == 2:
        row_count = round(row_count) + 1
        for i in range(2):
            list_input.append(trid+','+rrow+','+plid+','+locc+','+cont+','+plaa+','+rsst+','+trin+','+entn+','+abr1+','+abr2+','+abr3+','+matd+','+admc+','+ress+','+cgen+','+malt+','+plbr+','+depl+','+mast+','+mint+','+altd)            
    if rem == 3:
        row_count = round(row_count) + 1
        for i in range(1):
            list_input.append(trid+','+rrow+','+plid+','+locc+','+cont+','+plaa+','+rsst+','+trin+','+entn+','+abr1+','+abr2+','+abr3+','+matd+','+admc+','+ress+','+cgen+','+malt+','+plbr+','+depl+','+mast+','+mint+','+altd)               
    if rem == 0:
        row_count = row_count 

    in1,in2,in3,in4 = 0,1,2,3
    inc = 4

    for idx_input in range(int(round(row_count))):        
        #print (idx_input)
        _create_qrcode(in1,in2,in3,in4)1
        in1 = in1 + inc
        in2 = in2 + inc
        in3 = in3 + inc
        in4 = in4 + inc
        
def _create_qrcode(in1,in2,in3,in4):
    
    buff1 = 300
    buff2 = 200
    buff3 = 100
    buff4 = 0

    if in1 >= 0:

        trid,rrow,plid,locc,cont,plaa,rsst,trin,entn,abr1,abr2,abr3,matd,admc,ress,cgen,malt,plbr,depl,mast,mint,altd = list_input[in1].split(',')
        #print (trid+' '+rrow+' '+plid)

        # draw a QR code for matid
        #qr_matd = qr.QrCodeWidget(matd)
        #bounds = qr_matd.getBounds()
        
        # draw a QR code for container id
        qr_altd = qr.QrCodeWidget(altd)
        bounds = qr_altd.getBounds()

        # draw a QR code for plot barcode
        qr_plbr = qr.QrCodeWidget(plbr)
        bounds = qr_plbr.getBounds()
        
        width = bounds[2] - bounds[0]
        height = bounds[3] - bounds[1]
       
        #size of the drawing
        #qmatd = Drawing(45, 45, transform=[80./width,0,0,80./height,0,0])
        #qmatd.add(qr_matd)

        qaltd = Drawing(45, 45, transform=[80./width,0,0,80./height,0,0])
        qaltd.add(qr_altd)
     
        qplbr = Drawing(45, 45, transform=[80./width,0,0,80./height,0,0])
        qplbr.add(qr_plbr)
     
        #qrcode for altid
        ###renderPDF.draw(qmatd, c, 300, 15+buff1)
        renderPDF.draw(qplbr, c, 300, 15+buff1)

        #qrcode for plotbar
        renderPDF.draw(qaltd, c, 600, 15+buff1)

        #qrcode for plotbar
        renderPDF.draw(qplbr, c, 850, 17+buff1)

        #qrcode for plotbar
        renderPDF.draw(qplbr, c, 1000, 17+buff1)

        #label matid
        #c.setFont('Helvetica',12)
        #c.drawString(305,10+buff1,matd)

        #plot bar 1
        c.setFont('Helvetica',12)   
        c.drawString(305,10+buff1,plbr)
        
        #label container id
        c.setFont('Helvetica',12)
        c.drawString(590,10+buff1,altd)

        #label matid
        c.setFont('Helvetica',12)
        c.drawString(450,25+buff1,matd)

        #label for range row
        c.setFont('Helvetica',10)   
        c.drawString(445,12+buff1,rrow)

        #label plot id
        if len(plid) == 4:
            c.setFont('Helvetica',18)
            c.drawString(463,60+buff1,plid)
        else:
            c.setFont('Helvetica',18)   
            c.drawString(435,60+buff1,plid)
        
        #plot bar 1
        c.setFont('Helvetica',10)   
        c.drawString(857,17+buff1,plbr)
        
        #plot bar 2
        c.setFont('Helvetica',10)   
        c.drawString(1007,17+buff1,plbr)
        
        #plot id small 1
        if len(plid) == 4:
            c.setFont('Helvetica',12)   
            c.drawString(878,7+buff1,plid)

            c.setFont('Helvetica',12)   
            c.drawString(1028,7+buff1,plid)
        else:
            c.setFont('Helvetica',12)   
            c.drawString(855,7+buff1,plid)

            c.setFont('Helvetica',12)   
            c.drawString(1005,7+buff1,plid)

        #trial id
        c.setFont('Helvetica',15)   
        c.drawString(410,40+buff1,trid)

        
    if in2 >= 0:

        trid,rrow,plid,locc,cont,plaa,rsst,trin,entn,abr1,abr2,abr3,matd,admc,ress,cgen,malt,plbr,depl,mast,mint,altd = list_input[in2].split(',')
        #print (trid+' '+rrow+' '+plid)

        # draw a QR code for matid
        #qr_matd = qr.QrCodeWidget(matd)
        #bounds = qr_matd.getBounds()
        
        # draw a QR code for container id
        qr_altd = qr.QrCodeWidget(altd)
        bounds = qr_altd.getBounds()

        # draw a QR code for plot barcode
        qr_plbr = qr.QrCodeWidget(plbr)
        bounds = qr_plbr.getBounds()
        
        width = bounds[2] - bounds[0]
        height = bounds[3] - bounds[1]
       
        #size of the drawing
        #qmatd = Drawing(45, 45, transform=[80./width,0,0,80./height,0,0])
        #qmatd.add(qr_matd)

        qaltd = Drawing(45, 45, transform=[80./width,0,0,80./height,0,0])
        qaltd.add(qr_altd)
     
        qplbr = Drawing(45, 45, transform=[80./width,0,0,80./height,0,0])
        qplbr.add(qr_plbr)
     
        #qrcode for altid
        #renderPDF.draw(qmatd, c, 300, 15+buff2)
        renderPDF.draw(qplbr, c, 300, 15+buff2)

        #qrcode for plotbar
        renderPDF.draw(qaltd, c, 600, 15+buff2)

        #qrcode for plotbar
        renderPDF.draw(qplbr, c, 850, 17+buff2)

        #qrcode for plotbar
        renderPDF.draw(qplbr, c, 1000, 17+buff2)

        #label matid
        #c.setFont('Helvetica',12)
        #c.drawString(305,10+buff2,matd)
        #label plot id
        c.setFont('Helvetica',12)   
        c.drawString(305,10+buff2,plbr)


        #label container id
        c.setFont('Helvetica',12)
        c.drawString(590,10+buff2,altd)


        #label plot id
        if len(plid) == 4:
            c.setFont('Helvetica',18)
            c.drawString(463,60+buff2,plid)
        else:
            c.setFont('Helvetica',18)   
            c.drawString(435,60+buff2,plid)
        
        #plot bar 1
        c.setFont('Helvetica',10)   
        c.drawString(857,17+buff2,plbr)
        
        #plot bar 2
        c.setFont('Helvetica',10)   
        c.drawString(1007,17+buff2,plbr)


        #label matid
        c.setFont('Helvetica',12)
        c.drawString(450,25+buff2,matd)

        #label for range row
        c.setFont('Helvetica',10)   
        c.drawString(445,12+buff2,rrow)
        
        #plot id small 1
        if len(plid) == 4:
            c.setFont('Helvetica',12)   
            c.drawString(878,7+buff2,plid)

            c.setFont('Helvetica',12)   
            c.drawString(1028,7+buff2,plid)
        else:
            c.setFont('Helvetica',12)   
            c.drawString(855,7+buff2,plid)

            c.setFont('Helvetica',12)   
            c.drawString(1005,7+buff2,plid)

        #trial id
        c.setFont('Helvetica',15)   
        c.drawString(410,40+buff2,trid)
        
        
    if in3 >= 0:

        trid,rrow,plid,locc,cont,plaa,rsst,trin,entn,abr1,abr2,abr3,matd,admc,ress,cgen,malt,plbr,depl,mast,mint,altd = list_input[in3].split(',')
        #print (trid+' '+rrow+' '+plid)

        # draw a QR code for matid
        qr_matd = qr.QrCodeWidget(matd)
        bounds = qr_matd.getBounds()
        
        # draw a QR code for container id
        qr_altd = qr.QrCodeWidget(altd)
        bounds = qr_altd.getBounds()

        # draw a QR code for plot barcode
        qr_plbr = qr.QrCodeWidget(plbr)
        bounds = qr_plbr.getBounds()
        
        width = bounds[2] - bounds[0]
        height = bounds[3] - bounds[1]
       
        #size of the drawing
        qmatd = Drawing(45, 45, transform=[80./width,0,0,80./height,0,0])
        qmatd.add(qr_matd)

        qaltd = Drawing(45, 45, transform=[80./width,0,0,80./height,0,0])
        qaltd.add(qr_altd)
     
        qplbr = Drawing(45, 45, transform=[80./width,0,0,80./height,0,0])
        qplbr.add(qr_plbr)
     
        #qrcode for altid
        #renderPDF.draw(qmatd, c, 300, 15+buff3)
        #qrcode for plot id
        renderPDF.draw(qplbr, c, 300, 15+buff3)

        #qrcode for plotbar
        renderPDF.draw(qaltd, c, 600, 15+buff3)

        #qrcode for plotbar
        renderPDF.draw(qplbr, c, 850, 17+buff3)

        #qrcode for plotbar
        renderPDF.draw(qplbr, c, 1000, 17+buff3)

        #label matid
        #c.setFont('Helvetica',12)
        #c.drawString(305,10+buff3,matd)
        #label plot id
        c.setFont('Helvetica',12)   
        c.drawString(305,10+buff3,plbr)
        
        #label container id
        c.setFont('Helvetica',12)
        c.drawString(590,10+buff3,altd)
        
        #label plot id
        if len(plid) == 4:
            c.setFont('Helvetica',18)
            c.drawString(463,60+buff3,plid)
        else:
            c.setFont('Helvetica',18)   
            c.drawString(435,60+buff3,plid)
        
        #plot bar 1
        c.setFont('Helvetica',10)   
        c.drawString(857,17+buff3,plbr)
        
        #plot bar 2
        c.setFont('Helvetica',10)   
        c.drawString(1007,17+buff3,plbr)

        #label matid
        c.setFont('Helvetica',12)
        c.drawString(450,25+buff3,matd)

        #label for range row
        c.setFont('Helvetica',10)   
        c.drawString(445,12+buff3,rrow)
        
        #plot id small 1
        if len(plid) == 4:
            c.setFont('Helvetica',12)   
            c.drawString(878,7+buff3,plid)

            c.setFont('Helvetica',12)   
            c.drawString(1028,7+buff3,plid)
        else:
            c.setFont('Helvetica',12)   
            c.drawString(855,7+buff3,plid)

            c.setFont('Helvetica',12)   
            c.drawString(1005,7+buff3,plid)

        #trial id
        c.setFont('Helvetica',15)   
        c.drawString(410,40+buff3,trid)
    
    if in4 >= 0:

        trid,rrow,plid,locc,cont,plaa,rsst,trin,entn,abr1,abr2,abr3,matd,admc,ress,cgen,malt,plbr,depl,mast,mint,altd = list_input[in4].split(',')
        #print (trid+' '+rrow+' '+plid)

        # draw a QR code for matid
        qr_matd = qr.QrCodeWidget(matd)
        bounds = qr_matd.getBounds()
        
        # draw a QR code for container id
        qr_altd = qr.QrCodeWidget(altd)
        bounds = qr_altd.getBounds()

        # draw a QR code for plot barcode
        qr_plbr = qr.QrCodeWidget(plbr)
        bounds = qr_plbr.getBounds()
        
        width = bounds[2] - bounds[0]
        height = bounds[3] - bounds[1]
       
        #size of the drawing
        qmatd = Drawing(45, 45, transform=[80./width,0,0,80./height,0,0])
        qmatd.add(qr_matd)

        qaltd = Drawing(45, 45, transform=[80./width,0,0,80./height,0,0])
        qaltd.add(qr_altd)
     
        qplbr = Drawing(45, 45, transform=[80./width,0,0,80./height,0,0])
        qplbr.add(qr_plbr)
     
        #qrcode for altid
        #renderPDF.draw(qmatd, c, 300, 15+buff4)
        #qrcode for plot id
        renderPDF.draw(qplbr, c, 300, 15+buff4)

        #qrcode for plotbar
        renderPDF.draw(qaltd, c, 600, 15+buff4)

        #qrcode for plotbar
        renderPDF.draw(qplbr, c, 850, 17+buff4)

        #qrcode for plotbar
        renderPDF.draw(qplbr, c, 1000, 17+buff4)

        #label matid
        #c.setFont('Helvetica',12)
        #c.drawString(305,10+buff4,matd)
        #label plot id
        c.setFont('Helvetica',12)   
        c.drawString(305,10+buff4,plbr)
        
        #label container id
        c.setFont('Helvetica',12)
        c.drawString(590,10+buff4,altd)
        
        #label plot id
        if len(plid) == 4:
            c.setFont('Helvetica',18)
            c.drawString(463,60+buff4,plid)
        else:
            c.setFont('Helvetica',18)   
            c.drawString(435,60+buff4,plid)
        
        #plot bar 1
        c.setFont('Helvetica',10)   
        c.drawString(857,17+buff4,plbr)
        
        #plot bar 2
        c.setFont('Helvetica',10)   
        c.drawString(1007,17+buff4,plbr)

        #label matid
        c.setFont('Helvetica',12)
        c.drawString(450,25+buff4,matd)

        #label for range row
        c.setFont('Helvetica',10)   
        c.drawString(445,12+buff4,rrow)
        
        #plot id small 1
        if len(plid) == 4:
            c.setFont('Helvetica',12)   
            c.drawString(878,7+buff4,plid)

            c.setFont('Helvetica',12)   
            c.drawString(1028,7+buff4,plid)
        else:
            c.setFont('Helvetica',12)   
            c.drawString(855,7+buff4,plid)

            c.setFont('Helvetica',12)   
            c.drawString(1005,7+buff4,plid)

        #trial id
        c.setFont('Helvetica',15)   
        c.drawString(410,40+buff4,trid)
    
    #for new page
    c.showPage()
    c.save()

def _create_barcodes(matid,altd,plid,plbr,trid):
 
    # draw a QR code for matid
    qr_matid = qr.QrCodeWidget(matid)
    bounds = qr_matid.getBounds()
    
    # draw a QR code for container id
    qr_altd = qr.QrCodeWidget(altd)
    bounds = qr_altd.getBounds()

    # draw a QR code for plot barcode
    qr_plbr = qr.QrCodeWidget(plbr)
    bounds = qr_plbr.getBounds()
    
    width = bounds[2] - bounds[0]
    height = bounds[3] - bounds[1]
   
    #size of the drawing
    qmatid = Drawing(45, 45, transform=[80./width,0,0,80./height,0,0])
    qmatid.add(qr_matid)

    qaltd = Drawing(45, 45, transform=[80./width,0,0,80./height,0,0])
    qaltd.add(qr_altd)
 
    qplbr = Drawing(45, 45, transform=[80./width,0,0,80./height,0,0])
    qplbr.add(qr_plbr)
 
    #qrcode for altid
    renderPDF.draw(qmatid, c, 300, 15)

    #qrcode for plotbar
    renderPDF.draw(qaltd, c, 600, 15)

    #qrcode for plotbar
    renderPDF.draw(qplbr, c, 850, 17)

    #qrcode for plotbar
    renderPDF.draw(qplbr, c, 1000, 17)

    #label matid
    c.setFont('Helvetica',12)
    c.drawString(305,10,matid)
    
    #label container id
    c.setFont('Helvetica',12)
    c.drawString(590,10,altd)
    
    #label plot id
    if len(plid) == 4:
        c.setFont('Helvetica',18)
        c.drawString(463,60,plid)
    else:
        c.setFont('Helvetica',18)   
        c.drawString(435,60,plid)
    
    #plot bar 1
    c.setFont('Helvetica',10)   
    c.drawString(857,17,plbr)
    
    #plot bar 2
    c.setFont('Helvetica',10)   
    c.drawString(1007,17,plbr)
    
    #plot id small 1
    if len(plid) == 4:
        c.setFont('Helvetica',12)   
        c.drawString(878,7,plid)

        c.setFont('Helvetica',12)   
        c.drawString(1028,7,plid)
    else:
        c.setFont('Helvetica',12)   
        c.drawString(855,7,plid)

        c.setFont('Helvetica',12)   
        c.drawString(1005,7,plid)

    #trial id
    c.setFont('Helvetica',15)   
    c.drawString(410,40,trid)
   
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
