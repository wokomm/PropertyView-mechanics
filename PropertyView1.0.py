# -*- coding: utf-8 -*-
#"""
#Created on Wed Jul 17 19:19:47 2019
#
#@author: gyzhu
#"""
#
#
### Note ###
# 2019.09.26
# Änderung gegenüber V1:
# Akzeptierung aller Amplitude-Satz von jeden Kennlinie-Files
# Man kann beliebige Amplituden Ein- bzw. Ausblenden durch Eingabe Amplitudegröße unter Shell-Abfrage
# Statt HYDRO_TEST_DATA sondern HYDRO_IDENTIFICATION_DATA als Standard-Kurven dargestellt
#
# 2020.01.29
# DynBushingView, StatBushingView.py, Bump.py, Damper.py, Rebound.py und Spring.py werden in PropertyView zusammengefasst.
#
# 2020.05.20
# Einbau GUI
#
#
#
##########################################################################################################################
############################################ Funktion Spring #################################################

import matplotlib.pyplot as plt
import matplotlib.style as mplstyle
import pylab
from matplotlib import pyplot as plt
from PyPDF2 import PdfFileReader, PdfFileWriter
import os

import re
import numpy as np

import glob


def spring_read(axi, dat):     
##    """ funktion """ 

    digits= []
    displ = []
    force = []
    S     = []   
    
    f=open(dat)
    line = f.readlines()
    rowsum=len(line)                                        # Gesamtanzahl der Lines vom readed File

#    print(rowsum)


    for i in range(0,rowsum):
        if (line[i].find('force'))>0:
            ia =i

    for i in range(ia+1,rowsum):            
        line_s = re.sub(r'\s', " ", line[i])                # matches [\t\n\r\f] and replaced with whitespace
        digits = line_s.split(" ")                          # splited einzelne Zahl oder Symbol

        p=0
        for j in range(0,len(digits)):                      # Filterung alle Elemente mit" "
            if not(digits[j] == '') :
                if p ==0:
                    displ.append(float(digits[j]))          # Sammelung des ersten Elementes mit Zahl
                    p = p+1
                            
                elif p ==1:
                    force.append(float(digits[j]))          # Sammelung des zweiten bzw. letzten Elementes mit Zahl
                    
                 
    if axi == 'displ':
        return displ

    if axi == 'force':
        return force
    
#--------------------------------------------------------------------------
def Spring_Plot(data, vtyp):
    for dat in data:    
        axi = 'displ'
        displ=spring_read(axi, dat)
        axi = 'force'
        force=spring_read(axi, dat)

        plt.plot(displ, force, label=str(dat))
        plt.legend(loc='lower left', bbox_to_anchor= (-1.0, 1.25), ncol=1, 
                   borderaxespad=0, frameon=False)

    plt.suptitle('Displacement - Force  von  Spring')    
    plt.xlabel('displ  [mm]')
    plt.ylabel('force  [N]') 
    plt.grid(True)
    if vtyp == 'show':
        plt.show()
    if vtyp == 'pdf' :
        plt.savefig('Spring.pdf', bbox_inches='tight')
        plt.close()
#        
############################################ Funktion Damper #################################################
def damper_read(axi, dat):     
##    """ funktion """ 
    
    digits= []
    veloc = []
    force = []
    
    f=open(dat)
    line = f.readlines()
    rowsum=len(line)                                        # Gesamtanzahl der Lines vom readed File

#    print(rowsum)


    for i in range(0,rowsum):
        if (line[i].find('force'))>0:
            ia =i

    for i in range(ia+1,rowsum):            
        line_s = re.sub(r'\s', " ", line[i])                # matches [\t\n\r\f] and replaced with whitespace
        digits = line_s.split(" ")                          # splited einzelne Zahl oder Symbol

        p=0
        for j in range(0,len(digits)):
            if not(digits[j] == '') :                       # Filterung alle Elemente mit" "
                if p ==0:
                    veloc.append(float(digits[j]))          # Sammelung des ersten Elementes mit Zahl
                    p = p+1
                            
                elif p ==1:
                    force.append(float(digits[j]))          # Sammelung des zweiten bzw. letzten Elementes mit Zahl
                    
                 
    if axi == 'veloc':
        return veloc

    if axi == 'force':
        return force
    
#------------------------------------------------------------------
def Damper_Plot(data, vtyp):
    for dat in data:   
        axi = 'veloc'
        veloc = damper_read(axi, dat)
        axi = 'force'
        force = damper_read(axi, dat)

        plt.plot(veloc, force, label=str(dat))
        plt.legend(loc='lower left', bbox_to_anchor= (-1.0, 1.25), ncol=1, borderaxespad=0, frameon=False)

    plt.suptitle('Velocity - Force  von  Dämpfer')    
    plt.xlabel('velocity  [mm/s]')
    plt.ylabel('force  [N]') 
    plt.grid(True) 
    if vtyp == 'show':
        plt.show()
    if vtyp == 'pdf' :
        plt.savefig('Damper.pdf', bbox_inches='tight')
        plt.close() 
       
#
############################################ Funktion Bump #################################################
def bump_read(axi, dat):     
##    """ funktion """ 
    
    digits= []
    displ = []
    force = []  
    
    f=open(dat)
    line = f.readlines()
    rowsum=len(line)                                        # Gesamtanzahl der Lines vom readed File

#    print(rowsum)


    for i in range(0,rowsum):
        if (line[i].find('force'))>0:
            ia =i

    for i in range(ia+1,rowsum):            
        line_s = re.sub(r'\s', " ", line[i])                # matches [\t\n\r\f] and replaced with whitespace
        digits = line_s.split(" ")                          # splited einzelne Zahl oder Symbol

        p=0
        for j in range(0,len(digits)):
            if not(digits[j] == '') :                       # Filterung alle Elemente mit" "
                if p ==0:
                    displ.append(float(digits[j]))          # Sammelung des ersten Elementes mit Zahl
                    p = p+1
                            
                elif p ==1:
                    force.append(float(digits[j]))          # Sammelung des zweiten bzw. letzten Elementes mit Zahl
                    
                 
    if axi == 'displ':
        return displ

    if axi == 'force':
        return force

#------------------------------------------------------------------------
def Bump_Plot(data, vtyp):
    for dat in data:
        axi = 'displ'
        displ=bump_read(axi, dat)
        axi = 'force'
        force=bump_read(axi, dat)

        plt.plot(displ, force, label=str(dat))
        plt.legend(loc='lower left', bbox_to_anchor= (-1.0, 1.25), ncol=1, 
                   borderaxespad=0, frameon=False)

    plt.suptitle('Displacement - Force  von  Bumpstop')    
    plt.xlabel('displ  [mm]')
    plt.ylabel('force  [N]') 
    plt.grid(True) 
    if vtyp == 'show':
        plt.show()
    if vtyp == 'pdf' :
        plt.savefig('Bump.pdf', bbox_inches='tight')
        plt.close()
#
############################################ Funktion Rebound #################################################
def rebound_read(axi, dat):     
##    """ funktion """ 
    
    digits= []
    displ = []
    force = []   
    
    f=open(dat)
    line = f.readlines()
    rowsum=len(line)                                        # Gesamtanzahl der Lines vom readed File

#    print(rowsum)


    for i in range(0,rowsum):
        if (line[i].find('force'))>0:
            ia =i

    for i in range(ia+1,rowsum):            
        line_s = re.sub(r'\s', " ", line[i])                # matches [\t\n\r\f] and replaced with whitespace
        digits = line_s.split(" ")                          # splited einzelne Zahl oder Symbol

        p=0
        for j in range(0,len(digits)):
            if not(digits[j] == '') :                       # Filterung alle Elemente mit" "
                if p ==0:
                    displ.append(float(digits[j]))          # Sammelung des ersten Elementes mit Zahl
                    p = p+1
                            
                elif p ==1:
                    force.append(float(digits[j]))          # Sammelung des zweiten bzw. letzten Elementes mit Zahl
                    
                 
    if axi == 'displ':
        return displ

    if axi == 'force':
        return force
    
#-----------------------------------------------------------------------
def Rebound_Plot(data, vtyp):
    for dat in data:   
        axi = 'displ'
        displ= rebound_read(axi, dat)
        axi = 'force'
        force= rebound_read(axi, dat)

        plt.plot(displ, force, label=str(dat))
        plt.legend(loc='lower left', bbox_to_anchor= (-1.0, 1.25), ncol=1, 
                       borderaxespad=0, frameon=False)

    plt.suptitle('Displacement - Force  von  Reboundstop')    
    plt.xlabel('displ  [mm]')
    plt.ylabel('force  [N]') 
    plt.grid(True) 
    if vtyp == 'show':
        plt.show()
    if vtyp == 'pdf' :
        plt.savefig('Rebound.pdf', bbox_inches='tight')
        plt.close()
#
################################################################## Function StatBushingView #####################################################################
    
import matplotlib.pyplot as plt
import matplotlib.style as mplstyle
import pylab
from matplotlib import pyplot as plt
from PyPDF2 import PdfFileReader, PdfFileWriter
import os

import re
import matplotlib.pyplot as plt
import matplotlib.style as mplstyle
import pylab
import numpy as np

import glob

########
def bushing0_read(axi, dat):     
#    """ funktion """ 
    x=[]
    fx=[]
    y=[]
    fy=[]
    z=[]
    fz=[]
    ax=[]
    tx=[]
    ay=[]
    ty=[]
    az=[]
    tz=[]
    ixm =  0
    iym =  0
    izm =  0
    iaxm = 0
    iaym = 0
    iazm = 0
  
      
    f=open(dat)
    line = f.readlines()
    rowsum=len(line)
#    print('rowsum', rowsum)
   
        
    for i in range(0,rowsum):
        #X=line[i]    
        #im =i
        
        if (line[i].find('fx'))>0:
            ixm = i
            #print('#ixm =',  ixm)
        if (line[i].find('fy'))>0:
            iym = i
            #print('#iym =',  iym) 
        if (line[i].find('fz'))>0:
            izm = i
            #print('#izm =',  izm) 
        if (line[i].find('tx'))>0:
            iaxm = i
            #print('#iaxm =',  iaxm) 
        if (line[i].find('ty'))>0:
            iaym = i
            #print('#iaym =',  iaym)                  
        if (line[i].find('tz'))>0:
            iazm = i
            #print('#iazm =',  iazm)   
                  
## Sammlung x und fx:                   
    for i in range(ixm+1,iym-2):                                # Split jede Reihe durch Tab- oder Leerzeichen 
        if (line[i].find('\t'))>0:
            X=line[i].split('\t')
        else:
            X=line[i].split(' ')
#        print(X)
              
        p=0
        for j in range(0,len(X)):                               # Split jede Reihe durch Tab- oder Leerzeichen 
            if not((X[j] == '') or (X[j] == '\t')) :
                if p ==0:
                    x.append(float(X[j]))                       # Sammelung des ersten Elementes mit Zahl
            
                    p = p+1
                            
                elif p ==1:
                    fx.append(float(X[j]))                      # Sammelung des zweiten bzw. letzten Elementes mit Zahl


## Sammlung y und fy:                
    for i in range(iym+1,izm-2):
        if (line[i].find('\t'))>0:
            Y=line[i].split('\t')
        else:
            Y=line[i].split(' ')
        #print(Y)
              
        p=0
        for j in range(0,len(Y)):
            
            if not((Y[j] == '') or (Y[j] == '\t')) :
                if p ==0:
                    y.append(float(Y[j]))
                    p = p+1
                            
                elif p ==1:
                    fy.append(float(Y[j]))
                    

## Sammlung z und fz:             
    for i in range(izm+1,iaxm-2):
        if (line[i].find('\t'))>0:
            Z=line[i].split('\t')
        else:
            Z=line[i].split(' ')
        #print(Z)
              
        p=0
        for j in range(0,len(Z)):
            
            if not((Z[j] == '') or (Z[j] == '\t')) :
                if p ==0:
                    z.append(float(Z[j]))
                    p = p+1
                            
                elif p ==1:
                    fz.append(float(Z[j]))


## Sammlung ax und tx: 
    for i in range(iaxm+1,iaym-2):
        if (line[i].find('\t'))>0:
            AX=line[i].split('\t')
        else:
            AX=line[i].split(' ')
       #print(AX)

        p=0
        for j in range(0,len(AX)):
            if not((AX[j] == '') or (AX[j] == '\t')) :
                if p ==0:
                    ax.append(float(AX[j]))
                    p = p+1
                            
                elif p ==1:
                    tx.append(float(AX[j]))


## Sammlung ay und ty:              
    for i in range(iaym+1,iazm-2):
        if (line[i].find('\t'))>0:
            AY=line[i].split('\t')
        else:
            AY=line[i].split(' ')
        #print(AY)
              
        p=0
        for j in range(0,len(AY)):
            
            if not((AY[j] == '') or (AY[j] == '\t')) :
                if p ==0:
                    ay.append(float(AY[j]))
                    p = p+1
                            
                elif p ==1:
                    ty.append(float(AY[j]))
                    
            
## Sammlung az und tz:         
    for i in range(iazm+1,rowsum):
#        print('line[i].find', line[i].find('\t') )
        if (line[i].find('  '))>0:
            AZ=line[i].split('  ')
        elif (line[i].find('\t'))>0:
            AZ=line[i].split('\t')
        elif (line[i].find('  '))>0:
            AZ=line[i].split('  ')
        else :
            AZ=line[i].split(' ')
            #print(AZ)
              
        p=0
        for j in range(0,len(AZ)):
            
            if not((AZ[j] == '') or (AZ[j] == '\t') or (AZ[j] == '\n')):
                if p ==0:
                    az.append(float(AZ[j]))
                    p = p+1
                            
                elif p ==1:
                    tz.append(float(AZ[j]))
                    
#    print('# az =', az)
#    print('# tz =', tz)                
  
    f.close
    
    
    if axi == 'x':
     return x
    if axi == 'fx':
     return fx
    if axi == 'y':
     return y
    if axi == 'fy':
     return fy   
    if axi == 'z':
     return z
    if axi == 'fz':
     return fz 
    if axi == 'ax':
     return ax
    if axi == 'tx':
     return tx
    if axi == 'ay':
     return ay
    if axi == 'ty':
     return ty 
    if axi == 'az':
     return az
    if axi == 'tz':
     return tz


########
def bushing_plot(axi_x, axi_y, data, vtyp):   
    
    import matplotlib.pyplot as plt
    import matplotlib.style as mplstyle
    import pylab


    for dat in data:   
        axi = axi_x
        axiX = bushing0_read(axi, dat)
        axi = axi_y
        axiY = bushing0_read(axi, dat)

        plt.plot(axiX, axiY, label=dat)
#       plt.legend()
        plt.legend(loc='lower left', bbox_to_anchor= (-1.0, 1.25), ncol=1, borderaxespad=0, frameon=False)

    if (axi_x=='x' or axi_x=='y' or axi_x=='z'):
        plt.suptitle('Displacement - Force  in  '+ axi_x + ' - Richtung')
        plt.xlabel(axi_x + '  [mm]')
        plt.ylabel(axi_y + '  [N]')
    if (axi_x=='ax' or axi_x=='ay' or axi_x=='az'):
        plt.suptitle('Angle - Moment  um  '+ axi_x + ' - Richtung')        
        plt.xlabel(axi_x + '  [°]')
        plt.ylabel(axi_y + '  [Nmm]')   
    plt.grid(True)
    if vtyp == 'show':
        plt.show()
    if vtyp == 'pdf' :
        plt.savefig('staBushing_' + axi_y + '.pdf', bbox_inches='tight')
        plt.close()



################## StatbushingView #######################  
#    
def StatbushingPlot(data, komp, vtyp):
    if komp == 'x':
        bushing_plot('x', 'fx', data, vtyp)
    if komp == 'y':       
        bushing_plot('y', 'fy', data, vtyp)
    if komp == 'z':   
        bushing_plot('z', 'fz', data, vtyp)
    if komp == 'ax':
        bushing_plot('ax', 'tx', data, vtyp)
    if komp == 'ay':        
        bushing_plot('ay', 'ty', data, vtyp)
    if komp == 'az':    
        bushing_plot('az', 'tz', data, vtyp)    
        
        
        
################################################################## Function DynBushingView #####################################################################
#
############################### Lesen Identifikation-File #######################################  
def bushing_read(axi, dat):     
#    """ funktion """ 
    
    freq=[]
    ampl=[]
    cdyn=[]
    phas=[]
    km=[]           
    am=[] 
      
    f=open(dat)
    line = f.readlines()
    rowsum=len(line)                                            # Gesamtanzahl der Lines vom readed File
  
        
    for i in range(0,rowsum):
            
        if (line[i].find('HYDRO_IDENTIFICATION_DATA'))>0:
            ia = i
        
        if (line[i].find('HYDRO_TEST_DATA'))>0:
            ie = i
  
     
    for i in range(ia+2, ie-1):
        line_s = re.sub(r'\s', " ", line[i])                    # matches [\t\n\r\f] and replaced with whitespace

        digits = line_s.split(' ')                              # splited einzelne Zahl oder Symbol
       
        
        p=0
        for j in range(0,len(digits)):
            
            if not((digits[j] == ' ') or (digits[j] == '')):    # Filterung alle Elemente mit Tab- oder Leerzeichen
                if p ==0:
                    ampl.append(float(digits[j]))               # Sammlung amplitude-werte
                    p = p+1
                elif p ==1:
                    freq.append(float(digits[j]))               # Sammlung frequenz-werte
                    p = p+1
                elif p ==2:
                    cdyn.append(float(digits[j]))               # Sammlung cdyn-werte
                    p = p+1
                elif p ==3:
                    phas.append(float(digits[j]))               # Sammlung phas-werte
                    

                    
    le =  len(ampl)              
    for k in range(0,le):        
        if (ampl[k]!=ampl[k-1]):
            km.append(k)                                        # Reihen-Nr., wo Amplitude beginnt, beendet oder geaendert
            am.append(ampl[k])                                  # Auflisten aller Amplitudengröße pro File bzw. Kennlinie
            
    if(ampl[le-1]==ampl[0]):
            km.append(0)
            
    km.append(le)                                               # Addieren die letzte Reihen-Nr.          
    am.append(ampl[le-1])                                       # Addieren die zweite letzte Amplitude (nötig?)
              
  
    f.close

    if axi == 'am':
     return am    
    if axi == 'km':
     return km
    if axi == 'ampl':
     return ampl
    if axi == 'freq':
     return freq
    if axi == 'cdyn':
     return cdyn
    if axi == 'phas':
     return phas   
#
#
############################### Lesen Testing-File ####################################### 
#
def bushing_read_testdata(axi, dat):     
#    """ funktion """ 
    
    freq=[]
    ampl=[]
    cdyn=[]
    phas=[]
    km=[]                                                       # km-1: Amplitude-Anzahl
    am=[]
    ie1=8e9
    ie2=9e9
  
      
    f=open(dat)
    line = f.readlines()
    rowsum=len(line)                                            # Gesamtanzahl der Lines vom readed File
   
        
    for i in range(0,rowsum):
            
        if (line[i].find('HYDRO_TEST_DATA'))>0:
            ia = i
        
        if (line[i].find('$OBJECTIVE_FUNCTION'))==0:
            ie1 = i
                
        if (line[i].find('***'))>0:
            ie2 = i
 
    ie = min(ie1, ie2)                                          # Nehmen vorne Reihe als Ende-Reihe

             
     
    for i in range(ia+2,ie):
        line_s = re.sub(r'\s', " ", line[i])                    # matches [\t\n\r\f] and replaced with whitespace

        digits = line_s.split(' ')                              # splited einzelne Zahl oder Symbol
        
        
        p=0
        for j in range(0,len(digits)):
            
            if not((digits[j] == ' ') or (digits[j] == '')):    # Filterung alle Elemente mit Tab- oder Leerzeichen
                if p ==0:
                    ampl.append(float(digits[j]))               # Sammlung amplitude-werte
                    p = p+1
                elif p ==1:
                    freq.append(float(digits[j]))               # Sammlung frequenz-werte
                    p = p+1
                elif p ==2:
                    cdyn.append(float(digits[j]))               # Sammlung cdyn-werte
                    p = p+1
                elif p ==3:
                    phas.append(float(digits[j]))               # Sammlung phas-werte
                    

                    
    le =  len(ampl)           
    for k in range(0,le):               
        if (ampl[k]!=ampl[k-1]):
            km.append(k)                                        # Reihen-Nr., wo Amplitude beginnt, beendet oder geaendert
            am.append(ampl[k])                                  # Auflisten aller Amplitudengröße pro File bzw. Kennlinie
            
    if(ampl[le-1]==ampl[0]):
            km.append(0)
            
    km.append(le)                                               # Addieren die letzte Reihen-Nr.   
    am.append(ampl[le-1])                                       # Addieren die zweite letzte Amplitude (nötig?)
              
  
    f.close

    if axi == 'am':
     return am    
    if axi == 'km':
     return km
    if axi == 'ampl':
     return ampl
    if axi == 'freq':
     return freq
    if axi == 'cdyn':
     return cdyn
    if axi == 'phas':
     return phas   
#  
################################ Vorbereitung #####################################
#
# km:       Reihen-Nr., wo Amplitude beginnt, beendet oder geaendert
# am:       Auflisten aller Amplitudengröße pro File bzw. Kennlinie
# aq:       Auflisten aller Amplitudengröße aller File bzw. Kennlinie
# rq:       Auflisten aller aq-Anzahl
# r:        Zähler der Amplitudengröße-Wechsel
# q:        Zähler der File bzw. Kennlinie
# qm:       Zahl der File bzw. Kennlinie mit gleichem Amplitudengröße-Satz  
#
def Vorbereitung(data):
#
### Entnehmen von IDENTIFICATION_DATA ###
#    
    aq = []                                                 
    rq = []
    r = 0       
    q = 0

    for dat in data:

        axi = 'km'
        km=bushing_read(axi, dat)                                                   # km: Reihen-Nr., wo Amplitude beginnt, beendet oder geaendert
    
        rq.append(len(km))                                                          # rq: Sammelung Anzahl km aller Files bzw. Auflisten aller aq-Anzahl
    
        axi = 'am'
        am=bushing_read(axi, dat)                                                   # am: Auflisten aller Amplitudengröße pro File bzw. Kennlinie

        aq.append(am)                                                               # aq: Auflisten aller Amplitudengröße aller File bzw. Kennlinie
        
        q = q+1 
   
    qm = q                                                                          # qm: Anahl der File bzw. Kennlinien

#
#
### Entnehmen von TEST_DATA ###
#
    aq2 = []                                                 
    rq2 = []
    r2 = 0       
    q2 = 0

    for dat in data:
        dat=data[q2]

        axi = 'km'
        km2=bushing_read_testdata(axi, dat)
    
        rq2.append(len(km2))
    
        axi = 'am'
        am2=bushing_read_testdata(axi, dat)

        aq2.append(am2)
    
    
        q2 = q2+1 
   
    qm2 = q2
    
#    
    return qm, aq, rq, qm2, aq2, rq2  
      
    
#####################################  Cdynamic - Frequenz  #####################################
###
#
# km:       Reihen-Nr., wo Amplitude beginnt, beendet oder geaendert
# am:       Auflisten aller Amplitudengröße pro File bzw. Kennlinie
# aq:       Auflisten aller Amplitudengröße aller File bzw. Kennlinie
# rq:       Auflisten aller aq-Anzahl
# r:        Zähler der Amplitudengröße-Wechsel
# q:        Zähler der File bzw. Kennlinie
# qm:       Zahl der File bzw. Kennlinie  
#
def DynBushing_Cdyn(data, qm, aq, rq, qm2, aq2, rq2, ftyp):
    Cdyn={}
#    PHI={}
    Cdyn2={}
#    PHI2={}
    #Amp=[]      
    DatAmp=[]
    DatAmp2=[]
#  
#
### Entnehmen von IDENTIFICATION_DATA ###
# 
    for q in range(0, qm):                                                          # Loop für Files bzw. Kennlinien
        for r in range(1, rq[q]):                                                   # Loop für Amplituden
        
            dat=data[q]
        
            axi = 'km'
            km=bushing_read(axi, dat)
        
            axi = 'ampl'
            ampl=bushing_read(axi, dat)
        
            axi = 'freq'
            freq=bushing_read(axi, dat)

    
            axi = 'cdyn'
            cdyn=bushing_read(axi, dat)    
     
            Freqenz=[]
            Cdynamic=[]

            for n in range(km[r-1], km[r]):                                         # Loop aller Frequenz-Zelle innerhalb einer Amplitudegröße
                Freqenz.append(freq[n])
                Cdynamic.append(cdyn[n])
       
            D_cdyn = {(str(ampl[km[r]-1]), dat): [Freqenz, Cdynamic, dat]}          # Erstellen Dictionary {(Ampl, File): [Freq, Cdyn, File]}
            Cdyn.update(D_cdyn)                                                     # Update bzw. Fertigstellung D_cdyn für aller Ampl. unter aller Files

            dat_amp = [dat, str(ampl[km[r]-1])]                                     # Erstellen List [ File, Ampl]
            DatAmp.append(dat_amp)                                                  # Sammlung o.g. List für aller Ampl. unter aller Files

#
###  Entnehmen von TEST_DATA ###      
#
    for q2 in range(0, qm2):                                                        # Loop für Files bzw. Kennlinien
        for r in range(1, rq2[q2]):                                                 # Loop für Amplituden
        
            dat=data[q2]
        
            axi = 'km'
            km2=bushing_read_testdata(axi, dat)
        
            axi = 'ampl'
            ampl2=bushing_read_testdata(axi, dat)
        
            axi = 'freq'
            freq2=bushing_read_testdata(axi, dat) 
    
            axi = 'cdyn'
            cdyn2=bushing_read_testdata(axi, dat)        

            Freqenz2=[]
            Cdynamic2=[]
                   
            for n in range(km2[r-1], km2[r]):                                       # Loop aller Frequenz-Zelle innerhalb einer Amplitudegröße   
                Freqenz2.append(freq2[n])
                Cdynamic2.append(cdyn2[n]) 

            D_cdyn2 = {(str(ampl2[km2[r]-1]), dat): [Freqenz2, Cdynamic2, dat]}     # Erstellen Dictionary {(Ampl, File): [Freq, Cdyn, File]}
            Cdyn2.update(D_cdyn2)                                                   # Sammlung D_cdyn für aller Ampl. unter aller Files
            

            dat_amp2 = [dat, str(ampl2[km2[r]-1])]                                  # Erstellen List [ File, Ampl]
            DatAmp2.append(dat_amp2)                                                # Sammlung o.g. List für aller Ampl. unter aller Files
     
#
    return DatAmp, DatAmp2, Cdyn, Cdyn2           


##################################  DynBushingPlot_Cdyn ####################################
#
def DynBushingPlot_Cdyn(data, Cdyn, Cdyn2, ftyp, vtyp, EingabeAmp, EingabeAmp2):
#    
    print('\n---------------------- Kennlinie-Kurve-Darstellung:  Steifigkeit - Frequenz  -----------------------')  
#
#### Erzeugung Frequenz-Steifigkeit-Kurven: ####  
    if ftyp == 'Idenfile':                                                                                  # DATA-Wahl = 1 für Zeigen nur IDENTIFICATION_DATA 
        for a in EingabeAmp:                                                                                # Loop Amplitudegröße
            for dat in data:                                                                                # Loop Files
                key = (a, dat)                                                                              # Erzeugung key (Amplitudegröße, File)
                if key in Cdyn:                                                                             # If key innerhalb Dictionary Cdyn:
                    plt.plot(Cdyn[key][0], Cdyn[key][1], label='Amplitude '+ a + 'mm:  '+Cdyn[key][2])      # Plot Frequenz-Cdyn mit Label aus Ampl. und File mit Verzeichnis
                    plt.legend(loc='lower left', bbox_to_anchor= (-1.0, 1.25), ncol=1,                      # Label positionieren
                                   borderaxespad=0, frameon=False)

        plt.suptitle('Frequenz - dynamische Steifigkeit')
        plt.xlabel('frequenz  [Hz]')
        plt.ylabel('Cdyn  [N/mm]')   
        plt.grid(True) 
        if vtyp == 'show':
            plt.show()
        if vtyp == 'pdf' :
            plt.savefig('dynBushing_Cdyn.pdf', bbox_inches='tight')
            plt.close() 

      
    if ftyp == 'Testfile':                                                                                            # DATA-Wahl = 2 für Zeigen nur TEST_DATA 
#        for a in EingabeAmp2:# 2020.02.11
        for a in EingabeAmp2:    
            for dat in data:
                key = (a, dat)
                if key in Cdyn2:
                    plt.plot(Cdyn2[key][0], Cdyn2[key][1], '--', label='Amplitude '+ a + 'mm:  '+Cdyn2[key][2]+'   - aus TEST_DATA')
                    plt.legend(loc='lower left', bbox_to_anchor= (-1.0, 1.25), ncol=1, 
                                   borderaxespad=0, frameon=False)                  

        plt.suptitle('Frequenz - dynamische Steifigkeit')
        plt.xlabel('frequenz  [Hz]')
        plt.ylabel('Cdyn aus Test  [N/mm]')   
        plt.grid(True) 
        if vtyp == 'show':
            plt.show()
        if vtyp == 'pdf' :
            plt.savefig('dynBushing_Cdyn.pdf', bbox_inches='tight')
            plt.close() 
    


    if ftyp == 'Allfile':                                                                                             # DATA-Wahl = 0 für Zeigen IDENTIFICATION_DATA und TEST_DATA
#        for a in EingabeAmp2:# 2020.02.11
        for a in EingabeAmp:     
            for dat in data:
                key = (a, dat)
#            if key in Cdyn2:
                if (key in Cdyn) and (key in Cdyn2):
                    plt.plot(Cdyn[key][0], Cdyn[key][1], label='Amplitude '+ a + 'mm:  '+Cdyn[key][2])
                    plt.plot(Cdyn2[key][0], Cdyn2[key][1], '--', label='Amplitude '+ a + 'mm:  '+Cdyn2[key][2]+'   - aus TEST_DATA')             
#                plt.plot(Cdyn2[key][0], Cdyn2[key][1], '--', label='Amplitude und File wie oben, aber aus TEST_DATA')                
                    plt.legend(loc='lower left', bbox_to_anchor= (-1.0, 1.25), ncol=1, 
                               borderaxespad=0, frameon=False)

        plt.suptitle('Frequenz - dynamische Steifigkeit')
        plt.xlabel('frequenz  [Hz]')
        plt.ylabel('Cdyn  [N/mm]')   
        plt.grid(True) 
        if vtyp == 'show':
            plt.show()
        if vtyp == 'pdf' :
            plt.savefig('dynBushing_Cdyn.pdf', bbox_inches='tight')
            plt.close() 

    
#######################################  Phase - Frequenz  ##################################
###
#
# km:       Reihen-Nr., wo Amplitude beginnt, beendet oder geaendert
# am:       Auflisten aller Amplitudengröße pro File bzw. Kennlinie
# aq:       Auflisten aller Amplitudengröße aller File bzw. Kennlinie
# rq:       Auflisten aller aq-Anzahl
# r:        Zähler der Amplitudengröße-Wechsel
# q:        Zähler der File bzw. Kennlinie
# qm:       Zahl der File bzw. Kennlinie (mit gleichem Amplitudengröße-Satz) 
# 
#
def DynBushing_PHI(data, qm, aq, rq, qm2, aq2, rq2, ftyp):
# 
    PHI={}
    PHI2={}  
    DatAmp=[]
    DatAmp2=[]
    for q in range(0, qm):
        for r in range(1, rq[q]):
        
            dat=data[q]
        
            axi = 'km'
            km=bushing_read(axi, dat)
        
            axi = 'ampl'
            ampl=bushing_read(axi, dat)
        
            axi = 'freq'
            freq=bushing_read(axi, dat)

    
            axi = 'phas'
            phas=bushing_read(axi, dat)    
     
            Freqenz=[]
            Phase=[]

            for n in range(km[r-1], km[r]):
                Freqenz.append(freq[n])
                Phase.append(phas[n])
       
            D_phase = {(str(ampl[km[r]-1]), dat): [Freqenz, Phase, dat]}
            PHI.update(D_phase)
        
#
            dat_amp = [dat, str(ampl[km[r]-1])]                                     # Erstellen List [ File, Ampl]
            DatAmp.append(dat_amp)                                                  # Sammlung o.g. List für aller Ampl. unter aller Files

#
    for q2 in range(0, qm2):
        for r in range(1, rq2[q2]):
        
            dat=data[q2]
        
            axi = 'km'
            km2=bushing_read_testdata(axi, dat)
        
            axi = 'ampl'
            ampl2=bushing_read_testdata(axi, dat)
        
            axi = 'freq'
            freq2=bushing_read_testdata(axi, dat) 
    
            axi = 'phas'
            phas2=bushing_read_testdata(axi, dat)        

            Freqenz2=[]
            Phase2=[]
                   
            for n in range(km2[r-1], km2[r]):            
                Freqenz2.append(freq2[n])
                Phase2.append(phas2[n]) 

                Freqenz2.append(freq2[n])
                Phase2.append(phas2[n]) 
                      
            D_phase2 = {(str(ampl2[km2[r]-1]), dat): [Freqenz2, Phase2, dat]}
            PHI2.update(D_phase2)     

#
            dat_amp2 = [dat, str(ampl2[km2[r]-1])]                                  # Erstellen List [ File, Ampl]
            DatAmp2.append(dat_amp2)                                                # Sammlung o.g. List für aller Ampl. unter aller Files
#            
#
    return DatAmp, DatAmp2, PHI, PHI2
#
################################# DynBushingPlot_PHI ####################################
def DynBushingPlot_PHI(data, PHI, PHI2, ftyp, vtyp, EingabeAmp, EingabeAmp2):
#    
    print('\n---------------------- Kennlinie-Kurve-Darstellung: Verlustwinkel - Frequenz -----------------------')  
#           
#### Erzeugung Frequenz-Verlustwinkel-Kurven: ####
    if ftyp == 'Idenfile':        
        for a in EingabeAmp:  
            for dat in data:
                key = (a, dat)
                if key in PHI:
                    plt.plot(PHI[key][0], PHI[key][1], label='Amplitude '+ a + 'mm:  '+PHI[key][2])
                    plt.legend(loc='lower left', bbox_to_anchor= (-1.0, 1.25), ncol=1, 
                                   borderaxespad=0, frameon=False)

        plt.suptitle('Frequenz - Verlustwinkel')
        plt.xlabel('frequenz  [Hz]')
        plt.ylabel('Phase  [deg]')   
        plt.grid(True) 
        if vtyp == 'show':
            plt.show()
        if vtyp == 'pdf' :
            plt.savefig('dynBushing_PHI.pdf', bbox_inches='tight')
            plt.close() 

    if ftyp == 'Testfile':  
#    print('EingabeAmp2', EingabeAmp2)  
#    print('EingabeAmp', EingabeAmp)  
        for a in EingabeAmp:  
            for dat in data:
                key = (a, dat)
                if key in PHI2:
                    plt.plot(PHI2[key][0], PHI2[key][1], '--', label='Amplitude '+ a + 'mm:  '+PHI2[key][2] +'   - aus TEST_DATA')
                    plt.legend(loc='lower left', bbox_to_anchor= (-1.0, 1.25), ncol=1, 
                                   borderaxespad=0, frameon=False)
                
#                print('a: ', a)               
                

        plt.suptitle('Frequenz - Verlustwinkel')
        plt.xlabel('frequenz  [Hz]')
        plt.ylabel('Phase aus Test [deg]')   
        plt.grid(True) 
        if vtyp == 'show':
            plt.show()
        if vtyp == 'pdf' :
            plt.savefig('dynBushing_PHI.pdf', bbox_inches='tight')
            plt.close() 

    if ftyp == 'Allfile': 
#    print('PHI: ', PHI) 
#    print('PHI2: ', PHI2)        
        for a in EingabeAmp2:  
#        for a in EingabeAmp: 
            for dat in data:
                key = (a, dat)
#            if key in PHI2:
                if (key in PHI) and (key in PHI2):
                    plt.plot(PHI[key][0], PHI[key][1], label='Amplitude '+ a + 'mm:  '+PHI[key][2])
                    plt.plot(PHI2[key][0], PHI2[key][1], '--', label='Amplitude '+ a + 'mm:  '+PHI2[key][2] +'   - aus TEST_DATA')
                    plt.legend(loc='lower left', bbox_to_anchor= (-1.0, 1.25), ncol=1, 
                                   borderaxespad=0, frameon=False) 


        plt.suptitle('Frequenz - Verlustwinkel')
        plt.xlabel('frequenz  [Hz]')
        plt.ylabel('Phase [deg]')   
        plt.grid(True) 
        if vtyp == 'show':
            plt.show()
        if vtyp == 'pdf' :
            plt.savefig('dynBushing_PHI.pdf', bbox_inches='tight')
            plt.close() 


#---------------------------------------------------------------------------------------
### MergePDF ###########################################################################
#---------------------------------------------------------------------------------------
#    
def merge_pdfs(paths, output):
    pdf_writer = PdfFileWriter()

    for path in paths:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            # Add each page to the writer object
            pdf_writer.addPage(pdf_reader.getPage(page))

    # Write out the merged PDF
    with open(output, 'wb') as out:
        pdf_writer.write(out)
     # print('merge_pdfs vorlaeufig auskommantiert')
#   
#----------------------------------------------------------------------------------------------------
### Steurungsfile ###################################################################################
#----------------------------------------------------------------------------------------------------
def PropView(typ, data, komp, ftyp, vtyp, amp):

    
#---- typ -------------------------------------------------------------------------------       
# typ: 1 (Spring),  2 (Damper),  3 (Bump),  4 (Rebound), 5 (sta.Bushing), 6 (dyn.Bushing) 
#       
#------------------------------------------- 1
#
    if typ == 'Spring':
        Spring_Plot(data, vtyp)
#        
#------------------------------------------ 2 
#
    if typ == 'Damper':
        Damper_Plot(data, vtyp)
#        
#------------------------------------------ 3 
#
    if typ == 'Bump':
        Bump_Plot(data, vtyp)
# 
#------------------------------------------ 4 
#
    if typ == 'Rebound':
        Rebound_Plot(data, vtyp)
#            
#------------------------------------------ 5         
#          
    if typ == 'sta.Bushing':
        StatbushingPlot(data, komp, vtyp)
#
#------------------------------------------ 6   

    if typ == 'dyn.Bushing' and komp=='Cdyn&PHI':
        qm, aq, rq, qm2, aq2, rq2 = Vorbereitung(data)
        DatAmp, DatAmp2, PHI, PHI2 = DynBushing_PHI(data, qm, aq, rq, qm2, aq2, rq2, ftyp)
        DatAmp, DatAmp2, Cdyn, Cdyn2 = DynBushing_Cdyn(data, qm, aq, rq, qm2, aq2, rq2, ftyp)
            
        # ------ Eingabe aus GUI --------           
        EingabeAmp = amp        
        EingabeAmp2 = EingabeAmp         
            
        DynBushingPlot_Cdyn(data, Cdyn, Cdyn2, ftyp, vtyp, EingabeAmp, EingabeAmp2)
        DynBushingPlot_PHI(data, PHI, PHI2, ftyp, vtyp, EingabeAmp, EingabeAmp2)  

  
     
#####################################################################################################################################################        
###========================================================================= GUI ====================================================================    

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication
import sys

from PyQt5.QtCore import Qt
import os

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from time import sleep

komp_x  =   '0'


class Ui_MainWindow(object): 
    
    file = []
    # data = []  
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1125, 675)
        self.Show = QtWidgets.QRadioButton(MainWindow)
        self.Show.setGeometry(QtCore.QRect(960, 20, 70, 17))
        self.Show.setObjectName("Show")
        self.PDF = QtWidgets.QRadioButton(MainWindow)
        self.PDF.setGeometry(QtCore.QRect(1050, 20, 70, 17))
        self.PDF.setObjectName("PDF")
        self.Type_comboBox = QtWidgets.QComboBox(MainWindow)
        self.Type_comboBox.setGeometry(QtCore.QRect(80, 20, 711, 22))
        self.Type_comboBox.setObjectName("Type_comboBox")
        self.Type = QtWidgets.QLabel(MainWindow)
        self.Type.setGeometry(QtCore.QRect(40, 20, 41, 21))
        self.Type.setObjectName("Type")
        self.File_lineEdit = QtWidgets.QLineEdit(MainWindow)
        self.File_lineEdit.setGeometry(QtCore.QRect(80, 70, 921, 21))
        self.File_lineEdit.setObjectName("File_lineEdit")
        self.Seek = QtWidgets.QPushButton(MainWindow)
        self.Seek.setGeometry(QtCore.QRect(1020, 70, 71, 21))
        self.Seek.setObjectName("Seek")
        self.File = QtWidgets.QLabel(MainWindow)
        self.File.setGeometry(QtCore.QRect(40, 70, 31, 20))
        self.File.setObjectName("File")
        self.FileList_ListWgt = QtWidgets.QListWidget(MainWindow)
        self.FileList_ListWgt.setGeometry(QtCore.QRect(40, 130, 1001, 121))
        self.FileList_ListWgt.setObjectName("FileList_ListWgt")
        self.FileSelected_ListWgt = QtWidgets.QListWidget(MainWindow)
        self.FileSelected_ListWgt.setGeometry(QtCore.QRect(40, 280, 1001, 121))
        self.FileSelected_ListWgt.setObjectName("FileSelected_ListWgt")
        self.FileList = QtWidgets.QLabel(MainWindow)
        self.FileList.setGeometry(QtCore.QRect(520, 110, 47, 13))
        self.FileList.setObjectName("FileList")
        self.FileSelected = QtWidgets.QLabel(MainWindow)
        self.FileSelected.setGeometry(QtCore.QRect(510, 260, 71, 16))
        self.FileSelected.setObjectName("FileSelected")
        self.down = QtWidgets.QPushButton(MainWindow)
        self.down.setGeometry(QtCore.QRect(1050, 130, 41, 121))
        self.down.setObjectName("down")
        self.up = QtWidgets.QPushButton(MainWindow)
        self.up.setGeometry(QtCore.QRect(1050, 280, 41, 121))
        self.up.setObjectName("up")
        self.Component = QtWidgets.QLabel(MainWindow)
        self.Component.setGeometry(QtCore.QRect(40, 420, 61, 16))
        self.Component.setObjectName("Component")
        self.x = QtWidgets.QCheckBox(MainWindow)
        self.x.setGeometry(QtCore.QRect(40, 440, 31, 17))
        self.x.setObjectName("x")
        self.y = QtWidgets.QCheckBox(MainWindow)
        self.y.setGeometry(QtCore.QRect(90, 440, 31, 17))
        self.y.setObjectName("y")
        self.z = QtWidgets.QCheckBox(MainWindow)
        self.z.setGeometry(QtCore.QRect(140, 440, 31, 17))
        self.z.setObjectName("z")
        self.ax = QtWidgets.QCheckBox(MainWindow)
        self.ax.setGeometry(QtCore.QRect(40, 470, 70, 17))
        self.ax.setObjectName("ax")
        self.ay = QtWidgets.QCheckBox(MainWindow)
        self.ay.setGeometry(QtCore.QRect(90, 470, 70, 17))
        self.ay.setObjectName("ay")        
        self.az = QtWidgets.QCheckBox(MainWindow)
        self.az.setGeometry(QtCore.QRect(140, 470, 41, 17))
        self.az.setObjectName("az")
        self.Filetype = QtWidgets.QLabel(MainWindow)
        self.Filetype.setGeometry(QtCore.QRect(730, 420, 47, 13))
        self.Filetype.setObjectName("Filetype")
        self.iden = QtWidgets.QCheckBox(MainWindow)
        self.iden.setGeometry(QtCore.QRect(730, 440, 70, 17))
        self.iden.setObjectName("iden")
        self.test = QtWidgets.QCheckBox(MainWindow)
        self.test.setGeometry(QtCore.QRect(870, 440, 70, 17))
        self.test.setObjectName("test")
        self.Amplitude = QtWidgets.QLabel(MainWindow)
        self.Amplitude.setGeometry(QtCore.QRect(730, 470, 50, 16))             
        self.Amplitude.setObjectName("Amplitude")
        self.Amplitude_lineEdit = QtWidgets.QLineEdit(MainWindow)
        self.Amplitude_lineEdit.setGeometry(QtCore.QRect(730, 490, 361, 23))    # (730, 490, 300, 23) (730, 490, 361, 20)
        self.Amplitude_lineEdit.setObjectName("Amplitude_lineEdit")
        self.Run = QtWidgets.QPushButton(MainWindow)
        self.Run.setGeometry(QtCore.QRect(430, 500, 75, 23))
        self.Run.setObjectName("Run")
        self.Close = QtWidgets.QPushButton(MainWindow)
        self.Close.setGeometry(QtCore.QRect(570, 500, 75, 23))
        self.Close.setObjectName("Close")
        self.info = QtWidgets.QPushButton(MainWindow)
        self.info.setGeometry(QtCore.QRect(1046, 467, 46, 23))                  # (1040, 467, 52, 23) (1040, 490, 50, 23) (1040, 480, 50, 23)
        self.info.setObjectName("info") 
        self.Clear = QtWidgets.QPushButton(MainWindow)
        self.Clear.setGeometry(QtCore.QRect(1040, 527, 52, 23))                 # (1040, 525, 50, 23) (1040, 505, 50, 23)
        self.Clear.setObjectName("Clear")        
        self.textEdit = QtWidgets.QTextEdit(MainWindow)
        self.textEdit.setGeometry(QtCore.QRect(40, 550, 1051, 101))
        self.textEdit.setObjectName("textEdit")
        self.Massage = QtWidgets.QLabel(MainWindow)
        self.Massage.setGeometry(QtCore.QRect(40, 530, 47, 13))
        self.Massage.setObjectName("Massage")
        #
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PropertyView 1.0"))
        self.Show.setText(_translate("MainWindow", "Show"))
        self.PDF.setText(_translate("MainWindow", "PDF"))
        self.Type.setText(_translate("MainWindow", "Type"))
        self.Seek.setText(_translate("MainWindow", "Seek"))
        self.File.setText(_translate("MainWindow", "File"))
        self.FileList.setText(_translate("MainWindow", "File List"))
        self.FileSelected.setText(_translate("MainWindow", "File Selected"))
        # self.down.setText(_translate("MainWindow", "↓"))
        # self.up.setText(_translate("MainWindow", "↑"))
        self.down.setText(_translate("MainWindow", "down"))
        self.up.setText(_translate("MainWindow", "up"))              
        self.Component.setText(_translate("MainWindow", "Component"))
        self.x.setText(_translate("MainWindow", "x"))
        self.y.setText(_translate("MainWindow", "y"))
        self.z.setText(_translate("MainWindow", "z"))
        self.ax.setText(_translate("MainWindow", "ax"))
        self.ay.setText(_translate("MainWindow", "ay"))
        self.az.setText(_translate("MainWindow", "az"))
        self.Filetype.setText(_translate("MainWindow", "Filetype"))
        self.iden.setText(_translate("MainWindow", "iden"))
        self.test.setText(_translate("MainWindow", "test"))
        self.Amplitude.setText(_translate("MainWindow", "Amplitude"))
        self.Run.setText(_translate("MainWindow", "Run"))
        self.Close.setText(_translate("MainWindow", "Close"))
        self.info.setText(_translate("MainWindow", "info"))
        self.Clear.setText(_translate("MainWindow", "Clear"))
        self.Massage.setText(_translate("MainWindow", "Massage"))

        ##
        ## nachdefiniert - also nicht aus ui automatisch generiert 
        ##
        #
        # Type_comboBox-Funktion: Type
        # 
        self.Type_comboBox.addItem('Spring')
        self.Type_comboBox.addItem('Damper')
        self.Type_comboBox.addItem('Bump') 
        self.Type_comboBox.addItem('Rebound')
        self.Type_comboBox.addItem('sta.Bushing')
        self.Type_comboBox.addItem('dyn.Bushing')  
        # self.Type_comboBox.activated[str].connect(self.onChanged) 
        
        #
        # PushButton-Funktion: Run
        #         
        # self.Run.setText(_translate("MainWindow", "Run"))
        self.Run.setToolTip("This is an Run-button für Kurven-Zeigen und -Vergleich")     # Maus Stop --> Info wird an Button gezeigt 
        self.Run.clicked.connect(self.RunBtn)                                             # PushButton-Funktion --> Verbindung Button und Ereignis

        #
        # PushButton-Funktion: Close
        #  
        # self.Close.setText(_translate("MainWindow", "Close")) 
        # self.Close.clicked.connect(QCoreApplication.instance().quit)                    # Close-Funktion schon in QCoreApplication
        self.Close.setToolTip("um Programm zu schliessen, Bitte 2 mal <Close> druecken")  # Maus Stop --> Info wird an Button gezeigt 
        self.Close.clicked.connect(self.CloseBtn)                                         # def Close am Ende liegt, damit man Programm schließen kann
        
        #
        # PushButton-Funktion: Seek, down, up
        # 
        self.Seek.clicked.connect(self.SeekBtn)
        self.down.clicked.connect(self.downBtn)
        self.up.clicked.connect(self.upBtn)
        self.info.clicked.connect(self.infoBtn)         
        self.Clear.clicked.connect(self.ClearBtn) 
       
        # 
        # set Checked  -und dann-  connect QCheckBox-Funktion (self.x, .y, .z, .ax, .ay, .az, .iden, .test) :
        # 
        self.x.setChecked(False)
        self.x.stateChanged.connect(self.changeX)
        self.y.setChecked(False)
        self.y.stateChanged.connect(self.changeY)
        self.z.setChecked(False)
        self.z.stateChanged.connect(self.changeZ)  
        self.ax.setChecked(False)
        self.ax.stateChanged.connect(self.changeAX)
        self.ay.setChecked(False)
        self.ay.stateChanged.connect(self.changeAY)
        self.az.setChecked(False)
        self.az.stateChanged.connect(self.changeAZ)
        #
        self.iden.setChecked(False)
        self.iden.stateChanged.connect(self.changeAY)
        self.test.setChecked(False)
        self.test.stateChanged.connect(self.changeAZ)        
        
        #
        # RadioButton Show/PDF
        #
        self.Show.setChecked(True)
        self.Show.toggled.connect(self.onClicked)  
        self.PDF.toggled.connect(self.onClicked) 
        
        #
        # Amplitude_lineEdit 
        #
        # self.nameLabel.setText('Name:')

        

    ###
    ### Definition Ereignis in Verbindung mit *Funktion
    ###
    
    #
    # definition RadioButton-Funktion: self.Show/PDF -> Show oder PDF-File
    # 	
    def onClicked(self):
        if self.Show.isChecked():
            vtyp =  'show' 
        if self.PDF.isChecked():
            vtyp =  'pdf' 
            
        # print("vtyp is %s" % (vtyp))        
        return vtyp
                    

    #
    # definition SeekBtn
    #  
    def SeekBtn(self):                                                          # general function to open directories
        print("Datei - Auswahldialog geklickt")
        typ = self.Type_comboBox.currentText()
        # print("typ is: ", typ)
        
        if typ == 'Spring' :
            self.get_File(self.File_lineEdit, "Property File select", "Files (*.spr)")
        if typ == 'Damper' :
            self.get_File(self.File_lineEdit, "Property File select", "Files (*.dpr)")            
        if typ == 'Bump' :
            self.get_File(self.File_lineEdit, "Property File select", "Files (*.bum)")     
        if typ == 'Rebound' :
            self.get_File(self.File_lineEdit, "Property File select", "Files (*.reb)")
        if typ == 'sta.Bushing' :
            self.get_File(self.File_lineEdit, "sta.Bushing File select", "Files (*.bus)")                 
        if typ == 'dyn.Bushing' :
            self.get_File(self.File_lineEdit, "Property File select", "Files (*.hbu)")     
            
        
    def get_File(self, lineEditName, caption, fileFilter): 
        
        openPath = lineEditName.text()  
        self.dlg = QtWidgets.QFileDialog.getOpenFileName(None, caption, openPath, fileFilter)
        if self.dlg:           
            lineEditName.setText(self.dlg[0]) 
            self.FileList_ListWgt.insertItem(0, self.dlg[0])
               
    #
    # definition downBtn (down)
    #
    def downBtn(self):
        row = self.FileList_ListWgt.currentRow()
        item_2 = self.FileList_ListWgt.takeItem(row).text()                     # Click (down) item_2 in FileList_ListWgt genommen
        self.FileSelected_ListWgt.insertItem(99, item_2)                        # insertItem item_2 in FileSelected_ListWgt und immer nach unten (am 99-te Reihe) stehen        
        
        # ! Feststellung file bzw. data fuer aller Property-Files:
        self.file.append(item_2)                                               
        
        del item_2          
        

    #
    # definition upBtn (up)
    #
    def upBtn(self):
        row = self.FileSelected_ListWgt.currentRow()
        item_1 = self.FileSelected_ListWgt.takeItem(row).text()                 # Click (up) item_1 in SelectedList_ListWgt genommen
        self.FileList_ListWgt.insertItem(99, item_1)                            # insertItem item_1 zurück in FileList_ListWgt und immer nach unten (am 99-te Reihe) stehen
        
        self.file.remove(item_1)
       
        del item_1  
        
               
    ## Fuer stat.Bushing  
    #
    # definition QCheckBox-Funktion (self.x, .y, .z, .ax, .ay, .az, Show, PDF)
    #        
    def changeX(self):

        if self.x.isChecked() == True:
            komp_x =  'x' 
            # print(komp_x)
        else:
            komp_x =  'no'
            # print('no x') 
		
        return komp_x
    

    def changeY(self):

        if self.y.isChecked() == True:
            komp_y =  'y' 
            # print(komp_y)
        else:
            komp_y =  'no'
            # print('no y') 
		
        return komp_y


    def changeZ(self):

        if self.z.isChecked() == True:
            komp_z =  'z' 
            # print(komp_z)
        else:
            komp_z =  'no'
            # print('no z') 
		
        return komp_z


    def changeAX(self):

        if self.ax.isChecked() == True:
            komp_ax =  'ax' 
            # print(komp_ax)
        else:
            komp_ax =  'no'
            # print('no ax') 
		
        return komp_ax 


    def changeAY(self):

        if self.ay.isChecked() == True:
            komp_ay =  'ay' 
            # print(komp_ay)
        else:
            komp_ay =  'no'
            # print('no ay') 
		
        return komp_ay


    def changeAZ(self):

        if self.az.isChecked() == True:
            komp_az =  'az' 
            # print(komp_az)
        else:
            komp_az =  'no'
            # print('no az') 
		
        return komp_az
    
    
    ## Fuer dyn.Bushing 
    #
    # Info bzw. Überblick ueber Amplitude per einzelnes Bushing-File
    #
    def infoBtn(self):
 
        typ = 'dyn.Bushing'
        # data = self.file
        data = self.fileCtrl(typ)                                               # Hier data ist lokal list
            
        ftyp =  'default'   
        
        qm, aq, rq, qm2, aq2, rq2 = Vorbereitung(data)
        DatAmp, DatAmp2, default, default = DynBushing_PHI(data, qm, aq, rq, qm2, aq2, rq2, ftyp)
        DatAmp, DatAmp2, default, default = DynBushing_Cdyn(data, qm, aq, rq, qm2, aq2, rq2, ftyp) 
        
        print('\n--- Ueberblick Kennlinie-Files und ihre Amplituden fuer IDENTIFICATION_DATA ---\n')
        self.textEdit.insertPlainText('--- Ueberblick Kennlinie-Files und ihre Amplituden fuer IDENTIFICATION_DATA ---') 
                                                    
        for p in range(0, len(DatAmp)):
            if (p==0):                                                          # Beim ersten File-Ampl-Paar:
                print(DatAmp[p][0], ': ')                                       # print File-Name mit Verzeichnis
                self.textEdit.insertPlainText('\n' + DatAmp[p][0] + ':\n ')
                self.textEdit.insertPlainText('Amplitude [mm]:   ')
                 
                print('Amplitude [mm]: ', DatAmp[p][1])                         # print Amplitudegröße
                self.textEdit.insertPlainText(DatAmp[p][1] + '   ')
            
        
            elif DatAmp[p][0] == DatAmp[p-1][0] :                               # Beim p-te File-Ampl-Paar, wenn File gleich wie Vorgänger:                     
                print('Amplitude [mm]: ', DatAmp[p][1])                         # print NUR Amplitudegröße     
                self.textEdit.insertPlainText(DatAmp[p][1] + '   ')
        
            elif (DatAmp[p][0] != DatAmp[p-1][0]):                              # Beim p-te File-Ampl-Paar, wenn File anders als Vorgänger:
                print(DatAmp[p][0], ': ')                                       # print File-Name mit Verzeichnis
                self.textEdit.insertPlainText('\n' + DatAmp[p][0] + ':\n ')
                self.textEdit.insertPlainText('Amplitude [mm]:   ')
                
                print('Amplitude [mm]: ', DatAmp[p][1])                         # print Amplitudegröße
                self.textEdit.insertPlainText(DatAmp[p][1] + '   ') 

        print('\n-------- Ueberblick Kennlinie-Files und ihre Amplituden fuer TEST_DATA ---------\n')
        self.textEdit.insertPlainText('\n\n-------- Ueberblick Kennlinie-Files und ihre Amplituden fuer TEST_DATA ---------')
        
        for p2 in range(0, len(DatAmp2)):
            if (p2==0):
                print(DatAmp2[p2][0], ': ')
                self.textEdit.insertPlainText('\n' + DatAmp2[p2][0] + ':\n ') 
                self.textEdit.insertPlainText('Amplitude [mm]:   ')
                
                print('Amplitude [mm]: ', DatAmp2[p2][1]) 
                self.textEdit.insertPlainText(DatAmp2[p2][1] + '   ')

            elif (DatAmp2[p2][0] == DatAmp2[p2-1][0]):
                print('Amplitude [mm]: ', DatAmp2[p2][1])
                self.textEdit.insertPlainText(DatAmp2[p2][1] + '   ')
        
            elif DatAmp2[p2][0] != DatAmp2[p2-1][0] :
                print(DatAmp2[p2][0], ': ')
                self.textEdit.insertPlainText('\n' + DatAmp2[p2][0] + ':\n ')
                self.textEdit.insertPlainText('Amplitude [mm]:   ')               
                
                print('Amplitude [mm]: ', DatAmp2[p2][1])
                self.textEdit.insertPlainText(DatAmp2[p2][1] + '   ') 
                

        print('\n--------------------------------------------------------------------------------------------------------------------')
        self.textEdit.insertPlainText('\n\n---------------------------------------------------------------------------------------------------------------------')
        print('\n Enter a list of amplitude separated by space (z.B.: 0.5 0.4 2.0): \n')
        self.textEdit.insertPlainText('\n Enter a list of amplitude separated by space (z.B.: 1.0 0.4 2.0) under Amplitude in the Interface!')
        self.textEdit.insertPlainText('\n---------------------------------------------------------------------------------------------------------------------\n\n')



    def ClearBtn(self):        
        # sleep(12)
        print('\n---------Clear------------')
        self.textEdit.setText("")

    #
    # amplitude-List festsellung
    #
    def AmpInp(self):
        ampli = self.Amplitude_lineEdit.text()
        ampl = re.sub(r'\s', " ", ampli)                                        # matches [\t\n\r\f] and replaced with whitespace
        amp = ampl.split(" ")                                                   # splited einzelne Zahl oder Symbol       
        print('amp: ',  amp)
        return amp
       
    
    #
    # fileCtrl  - File bzw. Fileindex Kontrolle
    #    
    def fileCtrl(self, typ):
        data =[]                                                                # data ist hier local list    
        if typ == 'Spring' :
            idx = 'spr'
        elif typ == 'Damper':
            idx = 'dpr'        
        elif typ == 'Bump':
            idx = 'bum'
        elif typ == 'Rebound':
            idx = 'reb'            
        elif typ == 'sta.Bushing':
            idx = 'bus'            
        elif typ == 'dyn.Bushing':
            idx = 'hbu'
           
        for f in self.file:
            fi = re.compile(idx).findall(f)
            if fi:
                data.append(f)                  
            else:
                print('Warnung: KEIN richtige File fuer', typ, ' -->', f + '\n\n')
                self.textEdit.insertPlainText('Warnung: KEIN richtige File fuer ' + typ + ' -->' + f + '\n\n')
            
        # print('!Das ist data ', data)
        return data
        
    
    ##############################################
    ## Run  - Final Aufruf jedes Property jeweils!
    ##############################################    
    def RunBtn(self):     

        typ = self.Type_comboBox.currentText() 

        #       
        # --- 1. Spring, 2.Damper, 3.Bump, 4.Rebound (typ & data) -Aufruf:
        #
     
        if typ == 'Spring' or 'Damper' or 'Bump' or 'Rebound':
            print("# typ is %s" % (typ))
   
            data = self.fileCtrl(typ)
            
            komp = 'default'                                                    # bliebige string
            
            ftyp = 'default'                                                    # bliebige string
            
            vtyp = self.onClicked()
            # print("#vtyp is %s" % (vtyp)) 
            
            amp   = ['default']                                                 # bliebige list           
                    
            PropView(typ, data, komp, ftyp, vtyp, amp)

            
            if (vtyp == 'pdf') and (typ != 'sta.Bushing') and (typ != 'dyn.Bushing'):
                self.textEdit.insertPlainText('\n<<' + typ + '.pdf>>' + ' schon erzeugt! \n\n')    
            
            
            
        #
        #--- 5. statisches Bushing (typ & data & komp & vtyp) -Aufruf:         
        #         
        
        if typ == 'sta.Bushing' :
            # print("#typ is %s" % (typ))
            
            vtyp = self.onClicked()
            # print("#vtyp is %s" % (vtyp)) 
 
            ftyp = 'default'

            # data = self.file 
            data = self.fileCtrl(typ)

            amp   = ['default']                                                 # bliebige list    

            paths = []            

            komp_x =  self.changeX()
            komp = komp_x
            # print("#komp_x=", komp)
            PropView(typ, data, komp, ftyp, vtyp, amp)
            if vtyp == 'pdf' and komp == 'x' :
                paths.append('staBushing_fx.pdf')


            komp_y =  self.changeY()
            komp = komp_y
            # print("#komp_y=", komp)
            PropView(typ, data, komp, ftyp, vtyp, amp)
            if vtyp == 'pdf' and komp == 'y' :
                paths.append('staBushing_fy.pdf')       

        
            komp_z =  self.changeZ()
            komp = komp_z
            # print("#komp_z=", komp)
            PropView(typ, data, komp, ftyp, vtyp, amp)
            if vtyp == 'pdf' and komp == 'z' :
                paths.append('staBushing_fz.pdf')

              
            komp_ax =  self.changeAX()
            komp = komp_ax
            # print("#komp_ax=", komp)
            PropView(typ, data, komp, ftyp, vtyp, amp)
            if vtyp == 'pdf' and komp == 'ax' :
                paths.append('staBushing_tx.pdf')

             
            komp_ay =  self.changeAY()
            komp = komp_ay
            # print("#komp_ay=", komp)
            PropView(typ, data, komp, ftyp, vtyp, amp)
            if vtyp == 'pdf' and komp == 'ay' :
                paths.append('staBushing_ty.pdf')

        
            komp_az =  self.changeAZ()
            komp = komp_az
            # print("#komp_az=", komp)
            PropView(typ, data, komp, ftyp, vtyp, amp)
            if vtyp == 'pdf' and komp == 'az' :
                paths.append('staBushing_tz.pdf')


            if vtyp == 'pdf' :
                sleep(1)
                merge_pdfs(paths, output='staBushingView.pdf') 
        
                # print('alle PDF: ', paths) 
                for path in paths:
                    os.remove(path)
                    
                #os.remove(paths)                   # remove nur string

                self.textEdit.insertPlainText('\n<<' + typ + 'View.pdf>>' + ' schon zusammenfassend erzeugt! \n\n')   
                
                

        #
        #--- 6. dynamisches Bushing (typ & data & ftyp & vtyp) -Aufruf:        
        #         
        
        if typ == 'dyn.Bushing' :
            # print("#typ is %s" % (typ))          

            # data = self.file
            data = self.fileCtrl(typ)
               
            komp = 'Cdyn&PHI'
            
            if self.iden.isChecked():
                ftyp =  'Idenfile'        
            if self.test.isChecked():
                ftyp =  'Testfile'   
                if self.iden.isChecked() and self.test.isChecked():            
                    ftyp = 'Allfile'
            print("#ftyp is %s" % (ftyp))  
            
            vtyp = self.onClicked()

            
            # # ------ Eingabe aus GUI --------           
            # # EingabeAmp  = Ui_MainWindow.AmpInp
            amp = self.AmpInp()
            
            PropView(typ, data, komp, ftyp, vtyp, amp)
            
            if vtyp == 'pdf' :
                # Gesamt-PDF  
                paths = ['dynBushing_Cdyn.pdf', 'dynBushing_PHI.pdf']
                merge_pdfs(paths, output='dynBushingView.pdf')
                os.remove('dynBushing_Cdyn.pdf')
                os.remove('dynBushing_PHI.pdf') 
                
                self.textEdit.insertPlainText('\n<<' + typ + 'View.pdf>>' + ' schon zusammenfassend erzeugt! \n\n')   
                
     
           

    ###
    # definition Close
    ###  
    def CloseBtn(self):                                                         # def Close muss am Ende liegen, um Programm abzuschließen
        # from PyQt5.QtCore import QCoreApplication
        # QCoreApplication.instance().quit                                      # Close-Funktion schon in QCoreApplication
        self.Close.clicked.connect(QCoreApplication.instance().quit)
        print("Noch einmal das <Close> Druecken, wird das Programm abgeschlossen werden")
        # sys.exit(1)
        # sys.exit(app.exec_())
        # sys.exit('listofitems not long enough')
        #QtCore.QCoreApplication.instance().quit 
        
                                      
        
#----------------------------------------- Main UI -------------------------------------------------------------------------------------------------
#import MainView
from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
