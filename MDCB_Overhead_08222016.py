# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 11:22:27 2016


"""

#!/usr/bin/env python
# coding=UTF-8

import pymysql
import re
import os
import sys
import csv

# Open the relevant files.


def main():

         #Query
         db = pymysql.connect("localhost","root","admin","newoverheaddb")
         c=db.cursor()
         ##The naming conventions for this code follows the title of the overhead Total followed by the name of the funding agencies
         
         #Declaration of arrays. These arrays will later be used to compute the final values.
         #Arracys definition for USDOL
         MDCBOTUSDOL=[]
         MDCBOTONCAMPUSUSDOL=[]
         MDCBOTOffCampusOnCampusIOsDOL=[]
         MDCBOTONAllOffCAMPUSUSDOL=[]
         
         #Arracys definition for USDOD
         MDCBOTUSDOD=[]
         MDCBOTONCAMPUSUSDOD=[]
         MDCBOTOffCampusOnCampusIOsDOD=[]
         MDCBOTONAllOffCAMPUSUSDOD=[]        
         
         #Arrays for definition of USAID
         MDCBOTUSAID=[]
         MDCBOTONCAMPUSUSAID=[]
         MDCBOTOffCampusOnCampusIOsUSAID=[]
         MDCBOTONAllOffCAMPUSUSAID=[]  
         
         #Arary definitions for SouthAndCentralAsia
         MDCBOTSouthCentralAsia=[]
         MDCBOTONCAMPUSSouthCentralAsia=[]
         MDCBOTOffCampusOnCampusIOsSouthCentralAsia=[]
         MDCBOTONAllOffCAMPUSSouthCentralAsia=[]  
         
         #Array definition for State
         MDCBOTState=[]
         MDCBOTONCAMPUSState=[]
         MDCBOTOffCampusOnCampusIOsState=[]
         MDCBOTONAllOffCAMPUSState=[]
         
         #Array definitions for SAMHSA
         MDCBOTSAMSHA=[]
         MDCBOTONCAMPUSSAMSHA=[]
         MDCBOTOffCampusOnCampusIOsSAMSHA=[]
         MDCBOTONAllOffCAMPUSSAMSHA=[]
         
         #Array definitions for Redacted
         MDCBOTRedacted=[]
         MDCBOTONCAMPUSRedacted=[]
         MDCBOTOffCampusOnCampusIOsRedacted=[]
         MDCBOTONAllOffCAMPUSRedacted=[]
         
         #Array Definitions for State/PRM
         MDCBOTStatePRM=[]
         MDCBOTONCAMPUSStatePRM=[]
         MDCBOTOffCampusOnCampusIOsStatePRM=[]
         MDCBOTONAllOffCAMPUSStatePRM=[]
         
         #Array Definitions for PeaceCorps
         MDCBOTPeaceCorps=[]
         MDCBOTONCAMPUSPeaceCorps=[]
         MDCBOTOffCampusOnCampusIOsPeaceCorps=[]
         MDCBOTONAllOffCAMPUSPeaceCorps=[]
         
         #Array definitions for OGHA
         MDCBOTOGHA=[]
         MDCBOTONCAMPUSOGHA=[]
         MDCBOTOffCampusOnCampusIOsOGHA=[]
         MDCBOTONAllOffCAMPUSOGHA=[]

         #Array Definitions for OGAC
         MDCBOTOGAC=[]
         MDCBOTONCAMPUSOGAC=[]
         MDCBOTOffCampusOnCampusIOsOGAC=[]
         MDCBOTONAllOffCAMPUSOGAC=[]
         
         #Array definition fpr Office of Secretary
         MDCBOTOfficeSecretary=[]
         MDCBOTONCAMPUSOfficeSecretary=[]
         MDCBOTOffCampusOnCampusIOsOfficeSecretary=[]
         MDCBOTONAllOffCAMPUSOfficeSecretary=[]
         
         #Array definition for NIH
         MDCBOTNIH=[]
         MDCBOTONCAMPUSNIH=[]
         MDCBOTOffCampusOnCampusIOsNIH=[]
         MDCBOTONAllOffCAMPUSNIH=[]
         
         
         #Codes to pull the data for Overhead Total Cost of USDOL begins################################################################
         #Extract sum of MDCB_Overhead value from db. This is names as "Total MDCB Cost" in Excel
         c.execute("""Select year, sum(MDCB_Overhead) as MDCB_OverheadTotal from overhead_USDOL_MDCB_Overhead group by year""")
                           
         #Fetch the data from overhead_USDOL_MDCB_Overhead and store them to an array
         for row in c.fetchall():
             data=[]
             data.append(row[0])
             data.append(float(row[1]))
             MDCBOTUSDOL.append(data)
         
         for idx in range(len(MDCBOTUSDOL)):
             print (MDCBOTUSDOL[idx])  
             
         #Extract Modified OverheadTotal cost from db by year.   
         c.execute("""Select year, sum(InternationalScenario) as MDCB_OverheadTotal from overhead_USDOL_CurrentOnCampusScenario group by year""")
         for row in c.fetchall():
             data=[]
             data.append(row[0])
             data.append(float(row[1]))
             MDCBOTONCAMPUSUSDOL.append(data)
        
         for idx in range(len(MDCBOTONCAMPUSUSDOL)):
             print (MDCBOTONCAMPUSUSDOL[idx])
             
        #Query to pull the USDOL_OffCampusOnCampusIOs group by year 
         c.execute("""Select year, sum(OffCampus_OnCampusIOs) as MDCB_OverheadTotal from overhead_USDOL_OffCampusOnCampusIOs group by year""")
         for row in c.fetchall():
             data=[]
             data.append(row[0])
             data.append(float(row[1]))
             MDCBOTOffCampusOnCampusIOsDOL.append(data)
     
         for idx in range(len(MDCBOTOffCampusOnCampusIOsDOL)):
             print (MDCBOTOffCampusOnCampusIOsDOL[idx])
           
          # #Query to pull the USDOL_All_OffCampusOnCampusIOs group by year 
         c.execute("""Select year, sum(InternationalScenario) as MDCB_OverheadTotal from overhead_USDOL_AllOffCampus group by year""")
         for row in c.fetchall():
             data=[]
             data.append(row[0])
             data.append(float(row[1]))
             MDCBOTONAllOffCAMPUSUSDOL.append(data)
        
         for idx in range(len(MDCBOTONAllOffCAMPUSUSDOL)):
             print (MDCBOTONAllOffCAMPUSUSDOL[idx])   
          
         #Codes to pull the data for Overhead Total Cost of USDOL ends################################################################
         #####################################################################################################################################################
         ####################################################################################################################################################3
        
        ##################USDOD Codes to extract USDOD begins from here####################################################################################### 
        #Extract sum of MDCB_Overhead value from db. This is names as "Total MDCB Cost" in Excel
        
         c.execute("""Select year, sum(MDCB_Overhead) as MDCB_OverheadTotal from overhead_USDOD_MDCB_Overhead group by year""")
         for row in c.fetchall():
             data=[]
             data.append(row[0])
             data.append(float(row[1]))
             MDCBOTUSDOD.append(data)
     

         for idx in range(len(MDCBOTUSDOD)):
             print (MDCBOTUSDOD[idx])  
             
         #Extract Modified OverheadTotal cost from db by year.   
         c.execute("""Select year, sum(InternationalScenario) as MDCB_OverheadTotal from overhead_USDOD_CurrentOnCampusScenario group by year""")
         for row in c.fetchall():
             data=[]
             data.append(row[0])
             data.append(float(row[1]))
             MDCBOTONCAMPUSUSDOD.append(data)
                          
         for idx in range(len( MDCBOTONCAMPUSUSDOD)):
             print ( MDCBOTONCAMPUSUSDOD[idx])    
        
        #Query to pull the USDOD_OffCampusOnCampusIOs group by year 
         c.execute("""Select year, sum(OffCampus_OnCampusIOs) as MDCB_OverheadTotal from overhead_USDOD_OffCampusOnCampusIO group by year""")
         for row in c.fetchall():
             data=[]
             data.append(row[0])
             data.append(float(row[1]))
             MDCBOTOffCampusOnCampusIOsDOD.append(data)
                          
         for idx in range(len(MDCBOTOffCampusOnCampusIOsDOD)):
             print (MDCBOTOffCampusOnCampusIOsDOD[idx])
        
        #Query to pull the USDOL_All_OffCampusOnCampusIOs group by year 
         c.execute("""Select year, sum(InternationalScenario) as MDCB_OverheadTotal from overhead_USDOD_AllOffCampus group by year""")
         for row in c.fetchall():
             data=[]
             data.append(row[0])
             data.append(float(row[1]))
             MDCBOTONAllOffCAMPUSUSDOD.append(data)
                         
         for idx in range(len(MDCBOTONAllOffCAMPUSUSDOD)):
             print (MDCBOTONAllOffCAMPUSUSDOD[idx])
                   
      #Codes to pull the data for Overhead Total Cost of USDOD ends################################################################
     #####################################################################################################################################################
     ####################################################################################################################################################3
      
     ##################USAID Codes to extract USDOD begins from here#######################################################################################      
     #Extract sum of MDCB_Overhead value from db. This is names as "Total MDCB Cost" in Excel 
         c.execute("""Select year, sum(MDCB_Overhead) as MDCB_OverheadTotal from overhead_USAID_MDCB_Overhead group by year""")
     
     #Fetch the data from overhead_USAID_MDCB_Overhead and store them to an array
         for row in c.fetchall():
             data=[]
             data.append(row[0])
             data.append(float(row[1]))
             MDCBOTUSAID.append(data)
                   
         for idx in range(len(MDCBOTUSAID)):
             print (MDCBOTUSAID[idx])  

#Extract Modified OverheadTotal cost from db by year.   
         c.execute("""Select year, sum(InternationalScenario) as MDCB_OverheadTotal from overhead_USAID_CurrentOnCampusScenario group by year""")
         for row in c.fetchall():
             data=[]
             data.append(row[0])
             data.append(float(row[1]))
             MDCBOTONCAMPUSUSAID.append(data)

         for idx in range(len(MDCBOTONCAMPUSUSAID)):
             print (MDCBOTONCAMPUSUSAID[idx])
             
               #Query to pull the USDOL_OffCampusOnCampusIOs group by year 
         c.execute("""Select year, sum(OffCampus_OnCampusIOs) as MDCB_OverheadTotal from overhead_USAID_OffCampusOnCampusIOs group by year""")
         for row in c.fetchall():
           data=[]
           data.append(row[0])
           data.append(float(row[1]))
           MDCBOTOffCampusOnCampusIOsUSAID.append(data)
   
         for idx in range(len(MDCBOTOffCampusOnCampusIOsUSAID)):
           print (MDCBOTOffCampusOnCampusIOsUSAID[idx])
           
         ##Query to pull the USDOL_All_OffCampusOnCampusIOs group by year 
         c.execute("""Select year, sum(InternationalScenario) as MDCB_OverheadTotal from overhead_USAID_AllOffCampus group by year""")
         for row in c.fetchall():
          data=[]
          data.append(row[0])
          data.append(float(row[1]))
          MDCBOTONAllOffCAMPUSUSAID.append(data)
         
         for idx in range(len(MDCBOTONAllOffCAMPUSUSAID)):
             print (MDCBOTONAllOffCAMPUSUSAID[idx])   

        #Codes to pull the data for Overhead Total Cost of USAID ends################################################################
        #####################################################################################################################################################

         ###Codes to pull the data for Overhead Total Cost of South and Central Asia begins################################################################
         #Extract sum of MDCB_Overhead value from db. This is names as "Total MDCB Cost" in Excel
         c.execute("""Select year, sum(MDCB_Overhead) as MDCB_OverheadTotal from overhead_SouthCentralAsia_MDCB_Overhead group by year""")
        
         #Fetch the data from overhead_SouthCentralAsia_MDCB_Overhead and store them to an array
         for row in c.fetchall():
             data=[]
             data.append(row[0])
             data.append(float(row[1]))
             MDCBOTSouthCentralAsia.append(data)
         
         for idx in range(len(MDCBOTSouthCentralAsia)):
             print (MDCBOTSouthCentralAsia[idx])  
             
                #Extract Modified OverheadTotal cost from db by year.   
         c.execute("""Select year, sum(InternationalScenario) as MDCB_OverheadTotal from overhead_SouthCentralAsia_CurrentOnCampusScenario group by year""")
         for row in c.fetchall():
             data=[]
             data.append(row[0])
             data.append(float(row[1]))
             MDCBOTONCAMPUSSouthCentralAsia.append(data)
             
         for idx in range(len(MDCBOTONCAMPUSSouthCentralAsia)):
             print (MDCBOTONCAMPUSSouthCentralAsia[idx])
             
         #Query to pull the US_SouthCentralAsia_OffCampusOnCampusIOs group by year 
         c.execute("""Select year, sum(OffCampus_OnCampusIOs) as MDCB_OverheadTotal from overhead_SouthCentralAsia_OffCampusOnCampusIOs group by year""")
         for row in c.fetchall():
             data=[]
             data.append(row[0])
             data.append(float(row[1]))
             MDCBOTOffCampusOnCampusIOsSouthCentralAsia.append(data)
     
         for idx in range(len(MDCBOTOffCampusOnCampusIOsSouthCentralAsia)):
             print (MDCBOTOffCampusOnCampusIOsSouthCentralAsia[idx])

        # #Query to pull the SouthCentralAsia_All_OffCampus group by year 
         c.execute("""Select year, sum(InternationalScenario) as MDCB_OverheadTotal from overhead_SouthCentralAsia_AllOffCampus group by year""")
         for row in c.fetchall():
             data=[]
             data.append(row[0])
             data.append(float(row[1]))
             MDCBOTONAllOffCAMPUSSouthCentralAsia.append(data)
                         
         for idx in range(len(MDCBOTONAllOffCAMPUSSouthCentralAsia)):
             print (MDCBOTONAllOffCAMPUSSouthCentralAsia[idx])   
         #Codes to pull SouthCentralAsia data ends
      #########################################################################################################################################
             
        #Codes to pull [State] Overhead Data starts
        #Extract sum of MDCB_Overhead value from db. This is names as "Total MDCB Cost" in Excel
         c.execute("""Select year, sum(MDCB_Overhead) as MDCB_OverheadTotal from overhead_State_MDCB_Overhead group by year""")
       #Fetch the data from overhead_USDOL_MDCB_Overhead and store them to an array
         for row in c.fetchall():
             data=[]
             data.append(row[0])
             data.append(float(row[1]))
             MDCBOTState.append(data)

         for idx in range(len(MDCBOTState)):
             print (MDCBOTState[idx])  
  
    #Extract Modified OverheadTotal cost from db by year.   
         c.execute("""Select year, sum(InternationalScenario) as MDCB_OverheadTotal from overhead_State_CurrentOnCampusScenario group by year""")
         for row in c.fetchall():
             data=[]
             data.append(row[0])
             data.append(float(row[1]))
             MDCBOTONCAMPUSState.append(data)

         for idx in range(len(MDCBOTONCAMPUSState)):
             print (MDCBOTONCAMPUSState[idx])
    
    #Query to pull the State_OffCampusOnCampusIOs group by year 
         c.execute("""Select year, sum(OffCampus_OnCampusIOs) as MDCB_OverheadTotal from overhead_State_OffCampusOnCampusIOs group by year""")
         for row in c.fetchall():
             data=[]
             data.append(row[0])
             data.append(float(row[1]))
             MDCBOTOffCampusOnCampusIOsState.append(data)

         for idx in range(len(MDCBOTOffCampusOnCampusIOsState)):
             print (MDCBOTOffCampusOnCampusIOsState[idx])

 # #Query to pull the State_All_OffCampusOnCampusIOs group by year 
         c.execute("""Select year, sum(InternationalScenario) as MDCB_OverheadTotal from overhead_State_AllOffCampus group by year""")
         for row in c.fetchall():
             data=[]
             data.append(row[0])
             data.append(float(row[1]))
             MDCBOTONAllOffCAMPUSState.append(data)
                         
         for idx in range(len(MDCBOTONAllOffCAMPUSState)):
             print (MDCBOTONAllOffCAMPUSState[idx]) 
         #Codes to pull SouthCentralAsia data ends
      #########################################################################################################################################
      #Codes to pull [SAMHSA] Overhead Data starts
      #Extract sum of MDCB_Overhead value from db. This is names as "Total MDCB Cost" in Excel     
         c.execute("""Select year, sum(MDCB_Overhead) as MDCB_OverheadTotal from  overhead_SAMHSA_MDCB_Overhead group by year""")
       #Fetch the data from overhead_USDOL_MDCB_Overhead and store them to an array
         for row in c.fetchall():
             data=[]
             data.append(row[0])
             data.append(float(row[1]))
             MDCBOTSAMSHA.append(data)

         for idx in range(len( MDCBOTSAMSHA)):
             print ( MDCBOTSAMSHA[idx])  

         #Extract Modified OverheadTotal cost from db by year.   
         c.execute("""Select year, sum(InternationalScenario) as MDCB_OverheadTotal from overhead_SAMHSA_CurrentOnCampusScenario group by year""")
         for row in c.fetchall():
             data=[]
             data.append(row[0])
             data.append(float(row[1]))
             MDCBOTONCAMPUSSAMSHA.append(data)

         for idx in range(len(MDCBOTONCAMPUSSAMSHA)):
             print (MDCBOTONCAMPUSSAMSHA[idx])

       #Query to pull the SAMHSA_OffCampusOnCampusIOs group by year 
         c.execute("""Select year, sum(OffCampus_OnCampusIOs) as MDCB_OverheadTotal from overhead_SAMHSA_OffCampusOnCampusIOs group by year""")
         for row in c.fetchall():
             data=[]
             data.append(row[0])
             data.append(float(row[1]))
             MDCBOTOffCampusOnCampusIOsSAMSHA.append(data)
             
         for idx in range(len(MDCBOTOffCampusOnCampusIOsSAMSHA)):
             print (MDCBOTOffCampusOnCampusIOsSAMSHA[idx])

 # #Query to pull the SAMHSA_All_OffCampusOnCampusIOs group by year 
         c.execute("""Select year, sum(InternationalScenario) as MDCB_OverheadTotal from overhead_SAMHSA_AllOffCampus group by year""")
         for row in c.fetchall():
             data=[]
             data.append(row[0])
             data.append(float(row[1]))
             MDCBOTONAllOffCAMPUSSAMSHA.append(data)
                          
         for idx in range(len(MDCBOTONAllOffCAMPUSSAMSHA)):
             print (MDCBOTONAllOffCAMPUSSAMSHA[idx])   
 #Codes to pull SAMHSA data ends
      #########################################################################################################################################
             
      #Codes to pull [Redacted] Overhead Data starts
     #Extract sum of MDCB_Overhead value from db. This is names as "Total MDCB Cost" in Excel
         c.execute("""Select year, sum(MDCB_Overhead) as MDCB_OverheadTotal from overhead_Redacted_MDCB_Overhead group by year""")
     #Fetch the data from overhead_USDOL_MDCB_Overhead and store them to an array
         for row in c.fetchall():
             data=[]
             data.append(row[0])
             data.append(float(row[1]))
             MDCBOTRedacted.append(data)
             
         for idx in range(len(MDCBOTRedacted)):
             print (MDCBOTRedacted[idx])  
       
        #Extract Modified OverheadTotal cost from db by year.   
         c.execute("""Select year, sum(InternationalScenario) as MDCB_OverheadTotal from overhead_Redacted_CurrentOnCampusScenario group by year""")
         for row in c.fetchall():
             data=[]
             data.append(row[0])
             data.append(float(row[1]))
             MDCBOTONCAMPUSRedacted.append(data)
       
         for idx in range(len(MDCBOTONCAMPUSRedacted)):
             print (MDCBOTONCAMPUSRedacted[idx])

   #Query to pull the Redacted_OffCampusOnCampusIOs group by year 
         c.execute("""Select year, sum(OffCampus_OnCampusIOs) as MDCB_OverheadTotal from overhead_Redacted_OffCampusOnCampusIOs group by year""")
         for row in c.fetchall():
             data=[]
             data.append(row[0])
             data.append(float(row[1]))
             MDCBOTOffCampusOnCampusIOsRedacted.append(data)
     
         for idx in range(len(MDCBOTOffCampusOnCampusIOsRedacted)):
             print (MDCBOTOffCampusOnCampusIOsRedacted[idx])
             
           # #Query to pull the Redacted_All_OffCampusOnCampusIOs group by year 
         c.execute("""Select year, sum(InternationalScenario) as MDCB_OverheadTotal from overhead_Redacted_AllOffCampus group by year""")
         for row in c.fetchall():
             data=[]
             data.append(row[0])
             data.append(float(row[1]))
             MDCBOTONAllOffCAMPUSRedacted.append(data)
              
         for idx in range(len(MDCBOTONAllOffCAMPUSRedacted)):
             print (MDCBOTONAllOffCAMPUSRedacted[idx]) 
      #Codes to pull SAMHSA data ends
      #########################################################################################################################################
              
      #Codes to pull [State/PRM] Overhead Data starts
     #Extract sum of MDCB_Overhead value from db. This is names as "Total MDCB Cost" in Excel
         c.execute("""Select year, sum(MDCB_Overhead) as MDCB_OverheadTotal from overhead_StatePRM_MDCB_Overhead group by year""")
    #Fetch the data from overhead_StatePRM_MDCB_Overhead and store them to an array
         for row in c.fetchall():
             data=[]
             data.append(row[0])
             data.append(float(row[1]))
             MDCBOTStatePRM.append(data)
        
         for idx in range(len(MDCBOTStatePRM)):
            print (MDCBOTStatePRM[idx]) 
            
     #Extract Modified OverheadTotal cost from db by year.   
         c.execute("""Select year, sum(InternationalScenario) as MDCB_OverheadTotal from overhead_StatePRM_CurrentOnCampusScenario group by year""")
         for row in c.fetchall():
             data=[]
             data.append(row[0])
             data.append(float(row[1]))
             MDCBOTONCAMPUSStatePRM.append(data)
        
         for idx in range(len(MDCBOTONCAMPUSStatePRM)):
             print (MDCBOTONCAMPUSStatePRM[idx])
             
         #Query to pull the StatePRM_OffCampusOnCampusIOs group by year 
         c.execute("""Select year, sum(OffCampus_OnCampusIOs) as MDCB_OverheadTotal from overhead_StatePRM_OffCampusOnCampusIOs group by year""")
         for row in c.fetchall():
             data=[]
             data.append(row[0])
             data.append(float(row[1]))
             MDCBOTOffCampusOnCampusIOsStatePRM.append(data)
             
         for idx in range(len(MDCBOTOffCampusOnCampusIOsStatePRM)):
             print (MDCBOTOffCampusOnCampusIOsStatePRM[idx])
   
     # #Query to pull the USDOL_All_OffCampusOnCampusIOs group by year 
         c.execute("""Select year, sum(InternationalScenario) as MDCB_OverheadTotal from overhead_StatePRM_AllOffCampus group by year""")
         for row in c.fetchall():
             data=[]
             data.append(row[0])
             data.append(float(row[1]))
             MDCBOTONAllOffCAMPUSStatePRM.append(data)
                          
         for idx in range(len(MDCBOTONAllOffCAMPUSStatePRM)):
             print (MDCBOTONAllOffCAMPUSStatePRM[idx])   
         ######################State/PRM Ends#######################################################
         
         ############Codes to pull  Peace Corps begins##################
         #Extract sum of MDCB_Overhead value from db. This is names as "Total MDCB Cost" in Excel
         c.execute("""Select year, sum(MDCB_Overhead) as MDCB_OverheadTotal from overhead_PeaceCorps_MDCB_Overhead group by year""")
        #Fetch the data from overhead_USDOL_MDCB_Overhead and store them to an array
         for row in c.fetchall():
             data=[]
             data.append(row[0])
             data.append(float(row[1]))
             MDCBOTPeaceCorps.append(data)

         for idx in range(len(MDCBOTPeaceCorps)):
             print (MDCBOTPeaceCorps[idx])  
             
              #Extract Modified OverheadTotal cost from db by year.   
         c.execute("""Select year, sum(InternationalScenario) as MDCB_OverheadTotal from overhead_PeaceCorps_CurrentOnCampusScenario group by year""")
         for row in c.fetchall():
             data=[]
             data.append(row[0])
             data.append(float(row[1]))
             MDCBOTONCAMPUSPeaceCorps.append(data)

         for idx in range(len(MDCBOTONCAMPUSPeaceCorps)):
             print (MDCBOTONCAMPUSPeaceCorps[idx])
             
             #Query to pull the PeaceCorps_OffCampusOnCampusIOs group by year 
         c.execute("""Select year, sum(OffCampus_OnCampusIOs) as MDCB_OverheadTotal from overhead_PeaceCorps_OffCampusOnCampusIOs group by year""")
         for row in c.fetchall():
             data=[]
             data.append(row[0])
             data.append(float(row[1]))
             MDCBOTOffCampusOnCampusIOsPeaceCorps.append(data)
             
         for idx in range(len(MDCBOTOffCampusOnCampusIOsPeaceCorps)):
             print (MDCBOTOffCampusOnCampusIOsPeaceCorps[idx])

          # #Query to pull the PeaceCorps_All_OffCampusOnCampusIOs group by year 
         c.execute("""Select year, sum(InternationalScenario) as MDCB_OverheadTotal from overhead_PeaceCorps_AllOffCampus group by year""")
         for row in c.fetchall():
             data=[]
             data.append(row[0])
             data.append(float(row[1]))
             MDCBOTONAllOffCAMPUSPeaceCorps.append(data)
                     
         for idx in range(len(MDCBOTONAllOffCAMPUSPeaceCorps)):
             print (MDCBOTONAllOffCAMPUSPeaceCorps[idx])   
#################################Query to pull PeaceCorps ends#######################################

###############################Query to pull OGHA starts#######################################
 #Extract sum of MDCB_Overhead value from db. This is names as "Total MDCB Cost" in Excel
         c.execute("""Select year, sum(MDCB_Overhead) as MDCB_OverheadTotal from overhead_HHSOGHA_MDCB_Overhead group by year""")
          #Fetch the data from overhead_OGHA_MDCB_Overhead and store them to an array
         for row in c.fetchall():
             data=[]
             data.append(row[0])
             data.append(float(row[1]))
             MDCBOTOGHA.append(data)
             
         for idx in range(len(MDCBOTOGHA)):
             print (MDCBOTOGHA[idx])  
         #Extract Modified OverheadTotal cost from db by year.   
         c.execute("""Select year, sum(InternationalScenario) as MDCB_OverheadTotal from overhead_OGHA_CurrentOnCampusScenario group by year""")
         for row in c.fetchall():
             data=[]
             data.append(row[0])
             data.append(float(row[1]))
             MDCBOTONCAMPUSOGHA.append(data)
         for idx in range(len(MDCBOTONCAMPUSOGHA)):
             print (MDCBOTONCAMPUSOGHA[idx])

#Query to pull the OGHA_OffCampusOnCampusIOs group by year 
         c.execute("""Select year, sum(OffCampus_OnCampusIOs) as MDCB_OverheadTotal from overhead_OGHA_OffCampusOnCampusIOs group by year""")
         for row in c.fetchall():
             data=[]
             data.append(row[0])
             data.append(float(row[1]))
             MDCBOTOffCampusOnCampusIOsOGHA.append(data)
         for idx in range(len(MDCBOTOffCampusOnCampusIOsOGHA)):
             print (MDCBOTOffCampusOnCampusIOsOGHA[idx])
# #Query to pull the OGHA_All_OffCampusOnCampusIOs group by year 
         c.execute("""Select year, sum(InternationalScenario) as MDCB_OverheadTotal from overhead_OGHA_AllOffCampus group by year""")
         for row in c.fetchall():
             data=[]
             data.append(row[0])
             data.append(float(row[1]))
             MDCBOTONAllOffCAMPUSOGHA.append(data)
         for idx in range(len(MDCBOTONAllOffCAMPUSOGHA)):
             print (MDCBOTONAllOffCAMPUSOGHA[idx])   
#################################Query to pull OGHA ends#######################################

###############################Query to pull OGAC starts#######################################
#Extract sum of MDCB_Overhead value from db. This is names as "Total MDCB Cost" in Excel
         c.execute("""Select year, sum(MDCB_Overhead) as MDCB_OverheadTotal from overhead_StateOGAC_MDCB_Overhead group by year""")
         #Fetch the data from overhead_OGAC_MDCB_Overhead and store them to an array
         for row in c.fetchall():
             data=[]
             data.append(row[0])
             data.append(float(row[1]))
             MDCBOTOGAC.append(data)
         for idx in range(len(MDCBOTOGAC)):
             print (MDCBOTOGAC[idx])  
#Extract Modified OverheadTotal cost from db by year.   
         c.execute("""Select year, sum(InternationalScenario) as MDCB_OverheadTotal from overhead_OGAC_CurrentOnCampusScenario group by year""")
         for row in c.fetchall():
             data=[]
             data.append(row[0])
             data.append(float(row[1]))
             MDCBOTONCAMPUSOGAC.append(data)
         for idx in range(len(MDCBOTONCAMPUSOGAC)):
             print (MDCBOTONCAMPUSOGAC[idx])
      #Query to pull the USDOL_OffCampusOnCampusIOs group by year 
         c.execute("""Select year, sum(OffCampus_OnCampusIOs) as MDCB_OverheadTotal from overhead_OGAC_OffCampusOnCampusIOs group by year""")
         for row in c.fetchall():
             data=[]
             data.append(row[0])
             data.append(float(row[1]))
             MDCBOTOffCampusOnCampusIOsOGAC.append(data)
         for idx in range(len(MDCBOTOffCampusOnCampusIOsOGAC)):
             print (MDCBOTOffCampusOnCampusIOsOGAC[idx])
 # #Query to pull the OGAC_All_OffCampusOnCampusIOs group by year 
         c.execute("""Select year, sum(InternationalScenario) as MDCB_OverheadTotal from overhead_OGAC_AllOffCampus group by year""")
         for row in c.fetchall():
             data=[]
             data.append(row[0])
             data.append(float(row[1]))
             MDCBOTONAllOffCAMPUSOGAC.append(data)
             c.close()
             return('Complete!')
         for idx in range(len(MDCBOTONAllOffCAMPUSOGAC)):
             print (MDCBOTONAllOffCAMPUSOGAC[idx])   
#################################Query to pull OGAC ends#######################################

###############################Query to pull OfficeSecretary starts#######################################
#Extract sum of MDCB_Overhead value from db. This is names as "Total MDCB Cost" in Excel
         c.execute("""Select year, sum(MDCB_Overhead) as MDCB_OverheadTotal from overhead_HHSOfficeSecretary_MDCB_Overhead group by year""")  
          #Fetch the data from overhead_OfficeSecretary_MDCB_Overhead and store them to an array
         for row in c.fetchall():
             data=[]
             data.append(row[0])
             data.append(float(row[1]))
             MDCBOTOfficeSecretary.append(data)
         for idx in range(len(MDCBOTOfficeSecretary)):
             print (MDCBOTOfficeSecretary[idx])  
        #Extract Modified OverheadTotal cost from db by year.   
         c.execute("""Select year, sum(InternationalScenario) as MDCB_OverheadTotal from overhead_OfficeSecretary_CurrentOnCampusScenario group by year""")
         for row in c.fetchall():
             data=[]
             data.append(row[0])
             data.append(float(row[1]))
             MDCBOTONCAMPUSOfficeSecretary.append(data)
         for idx in range(len(MDCBOTONCAMPUSOfficeSecretary)):
             print (MDCBOTONCAMPUSOfficeSecretary[idx])
              #Query to pull the OfficeSecretary_OffCampusOnCampusIOs group by year 
         c.execute("""Select year, sum(OffCampus_OnCampusIOs) as MDCB_OverheadTotal from overhead_OfficeSecretary_OffCampusOnCampusIOs group by year""")
         for row in c.fetchall():
             data=[]
             data.append(row[0])
             data.append(float(row[1]))
             MDCBOTOffCampusOnCampusIOsOfficeSecretary.append(data)

         for idx in range(len(MDCBOTOffCampusOnCampusIOsOfficeSecretary)):
             print (MDCBOTOffCampusOnCampusIOsOfficeSecretary[idx])
             
              # #Query to pull the OfficeSecretary_All_OffCampusOnCampusIOs group by year 
         c.execute("""Select year, sum(InternationalScenario) as MDCB_OverheadTotal from overhead_OfficeSecretary_AllOffCampus group by year""")
         for row in c.fetchall():
             data=[]
             data.append(row[0])
             data.append(float(row[1]))
             MDCBOTONAllOffCAMPUSOfficeSecretary.append(data)
             c.close()
             return('Complete')
         for idx in range(len(MDCBOTONAllOffCAMPUSOfficeSecretary)):
             print (MDCBOTONAllOffCAMPUSOfficeSecretary[idx])  
#################################Query to pull HHSOfficeSecretary ends#######################################

###############################Query to pull NIH starts#######################################
#Extract sum of MDCB_Overhead value from db. This is names as "Total MDCB Cost" in Excel
         c.execute("""Select year, sum(MDCB_Overhead) as MDCB_OverheadTotal from overhead_HHSNIH_MDCB_Overhead group by year""")
#Fetch the data from overhead_NIH_MDCB_Overhead and store them to an array
         for row in c.fetchall():
             data=[]
             data.append(row[0])
             data.append(float(row[1]))
             MDCBOTNIH.append(data)
         for idx in range(len(MDCBOTNIH)):
             print (MDCBOTNIH[idx])  
          #Extract Modified OverheadTotal cost from db by year.   
         c.execute("""Select year, sum(InternationalScenario) as MDCB_OverheadTotal from overhead_NIH_CurrentOnCampusScenario group by year""")
         for row in c.fetchall():
             data=[]
             data.append(row[0])
             data.append(float(row[1]))
             MDCBOTONCAMPUSNIH.append(data)
         for idx in range(len(MDCBOTONCAMPUSNIH)):
             print (MDCBOTONCAMPUSNIH[idx])
    #Query to pull the NIH_OffCampusOnCampusIOs group by year 
         c.execute("""Select year, sum(OffCampus_OnCampusIOs) as MDCB_OverheadTotal from overhead_NIH_OffCampusOnCampusIOs group by year""")
         for row in c.fetchall():
             data=[]
             data.append(row[0])
             data.append(float(row[1]))
             MDCBOTOffCampusOnCampusIOsNIH.append(data)

         for idx in range(len(MDCBOTOffCampusOnCampusIOsNIH)):
             print (MDCBOTOffCampusOnCampusIOsNIH[idx])
              # #Query to pull the NIH_All_OffCampusOnCampusIOs group by year 
         c.execute("""Select year, sum(InternationalScenario) as MDCB_OverheadTotal from overhead_NIH_AllOffCampus group by year""")
         for row in c.fetchall():
             data=[]
             data.append(row[0])
             data.append(float(row[1]))
             MDCBOTONAllOffCAMPUSNIH.append(data)
        
         for idx in range(len(MDCBOTONAllOffCAMPUSNIH)):
             print (MDCBOTONAllOffCAMPUSNIH[idx])   



        

if __name__ == '__main__':
	status = main()
	sys.exit(status)
