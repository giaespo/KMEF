#!/usr/bin/python3
from ... import settings
import mfp
import mfp.job
import mfp.device

TONERTYPE={
           1:"YELLOW",
           2:"MAGENTA",
           3:"CYAN",
           4:"BLACK"
       }
       
TONERSTATUS={
            1:"EXIST",
            2:"NEAR_EMPTY",
            3:"EMPTY"
            }
 
TRAYTYPE={
          1:"AUTO",
          2:"MANUAL",
          3:"TRAY_1",
          4:"TRAY_2",
          5:"TRAY_3",
          6:"TRAY_4",
          7:"TRAI_5"
          }

TRAYSTATUS={
            1:"NOT_EXIST",
            2:"OPEN",
            3:"DOWN",
            4:"RAISING",
            5:"READY"
            }  
            
PAPERSTATUS={
            0:"EMPTY",
            50:"NEAR_EMPTY",
            100:"ENOUGH"
            } 
            
class HDD(object):
    def getUnivocalName(self):
        import datetime
        now = datetime.datetime.now()
        name=now.strftime("%Y-%m-%d-%H-%M-%S-") + str(now.microsecond) 
        return name
    
    def listFolder(self,fold):
        import os
        try:
            return os.listdir(settings.appFolder + settings.tmpFolder + fold)
        except:
            return []			

    def createFolder(self,name):
        import os
        os.makedirs(settings.appFolder + settings.tmpFolder + name)
    
    def deleteFile(self,name):
        import os
        try:
            os.remove(settings.appFolder + name)
            return True
        except Exception as e:
            return False
    
    def checkFileExistence(self,name):
        import os
        try:
            myfile = open(settings.appFolder + name, "r+")
            return True 
        except:
            return False
        
    def deleteFolder(self,name):
        import os
        os.removedirs(settings.appFolder + settings.tmpFolder + name)

    def read3k(self):
        return self.fileobj.read(3072)

    def encodeFileb64(self,filename):
        import base64
        filenameb64=filename.split('.')[0] + '.txt'
        try:
            self.fileobj=open(settings.appFolder + filename,"rb")
            
            fout = open(settings.appFolder + filenameb64,"a")
            for piece in iter(self.read3k,b""):
                val=base64.b64encode(piece)
                fout.write(str(val))
            fout.close()
                
            self.fileobj.close()			
            #val=base64.b64encode(bf)
# save base64 string to given text file
            #filenameb64=filename.split('.')[0] + '.txt'
            #fout = open(settings.appFolder + filenameb64,"w")
            #fout.write(str(val))
            #fout.close()
        except Exception as e:
            val=e
        return filenameb64
        
    
        
    def decodeFileb64(self,b64File,filename):
        import base64
        try:
            f=open(settings.appFolder + settings.tmpFolder + filename , "wb")
            f.write(base64.decodestring(b64File))
            f.close()
            return true
        except:
            return False       

class Device(object):
    def checkStatus(self,jobid):
        result=0
        try:
            search = mfp.job.SearchByJobID(mfp.JobStatus.ACTIVE, int(jobid))
            d_lst= mfp.job.get_jobinfo_list(search, 1, mfp.JOBINFO_LIST_NUM_MAX)
        #d_lst = mfp.job.get_jobinfo_list(mfp.job.SearchByJobID(mfp.JobStatus.DONE, jobid), 1, 1)
            if len(d_lst) > 0:
                result  = len(d_lst)
            return result
        except Exception as e:
            result=str(e)
        
        
class Printer(Device):
    def checkPaperStatus(self):
        res={}
        for el in TRAYTYPE:
            pape = mfp.device.get_input_tray_info(el)
            if pape.status==5:
                res[TRAYTYPE[el]]=PAPERSTATUS[pape.paper_remain]
        return res
        
    def checkTonerStatus(self):
        res={}
        for el in TONERTYPE:
            ton = mfp.device.get_toner_info(el)
            res[TONERTYPE[el]]=TONERSTATUS[ent.status]
        return res

        

    def print(self,info):
        result='OK'
        try:
            pjl_command=''
            #num of copies
            if 'num' not in info:
                info['num']="1"
                pjl_command = pjl_command + '@PJL SET COPIES = ' + info["num"] + '\r\n'
            #input Tray
            if 'tray' not in info:
                info['tray']="AUTO"
            pjl_command = pjl_command + '@PJL SET MEDIASOURCE = ' + info["tray"] + '\r\n'
            #set color
            if 'color' not in info:
                info['color']=""
            pjl_command = pjl_command + '@PJL SET PLANESINUSE = ' + info["color"] + '\r\n'
            #set side
            if 'duplex' not in info:
                info['duplex']=""
            pjl_command = pjl_command + '@PJL SET DUPLEX = ' + info["duplex"] + '\r\n'
            #create file
            #hd=HDD()
            # Open the print stream
            pstream = mfp.job.open_print_stream()
            # Add number of sets in PJL
            pstream.write_data(pjl_command)
            # Add print data
            pstream.write_file(settings.appFolder + settings.tmpFolder + info['filename'])
            # The print job gets started by closing the print stream
            pstream.close()
            # If error does not occur, display 'completion' message
            result = "Job Executed"
        except mfp.MFPValidationErr:
            # Error when the a prohibited combination is set in job settings
            result = "MFPValidationErr"
        except mfp.MFPNotSupportedErr:
            # Error when trying to set invalid job setting or invalid parameter
            result = "MFPNotSupportedErr"
        except mfp.MFPInvalidStateErr:
            # Error when MFP is in a state where Job cannot be executed, e.g. During admin mode
            result = "MFPInvalidStateErr"
        except Exception as e:
            result=str(e)
        return result
        





class Scanner(Device):
    def checkPlaten(self):
        is_doc_present = mfp.device.is_document_on(mfp.Device.PLATEN)
        return is_doc_present 
        
    def checkADF(self):
        is_doc_present = mfp.device.is_document_on(mfp.Device.ADF)
        return is_doc_present
        
    def scan(self,info):
        result='OK'
        try:
            hdd = mfp.job.TxHDD(settings.appFolder + '/' + info['path'])
            scan = mfp.job.Scan()
            scan.set_tx_list([hdd])
            #scan.set_original_type(mfp.OriginalType.TEXT)
            scan.set_scan_side(mfp.ScanSide.SIMPLEX)
            scan.set_resolution(mfp.Resolution.DPI_200_200)
            scan.set_density(0)
            scan.set_color(mfp.ColorMode.AUTO)#SINGLE_COLOR)
            scan.set_paper_size(mfp.OriginalSizeType.STANDARD, mfp.PaperSize.SEF_A4)
            scan.set_back_density(mfp.BackgroundRemovalLevel.AUTO)
            scan.set_file_type(mfp.job.FileTypePDF())
            #scan.set_page_setting(mfp.PageSetting.EACH)
            #scan.set_original_direction(mfp.OriginalDirection.TOP)
            scan.set_file_name(info['filename'])
            JobID = mfp.job.start(scan)

        except mfp.MFPValidationErr:
           # Error when the a prohibited combination is set in job settings
            result = "MFPValidationErr"
        except mfp.MFPNotSupportedErr:
        # Error when trying to set invalid job setting or invalid parameter  
            result = "MFPNotSupportedErr"
        except mfp.MFPInvalidStateErr:
        # Error when MFP is in a state where Job cannot be executed, e.g. During admin mode
            result = "MFPInvalidStateErr"
        except Exception as l:
            result=l
        return JobID,result
