# -*- coding: utf-8 -*-
"""
Created on Wed Jul 30 13:09:05 2014

@author: B48861
"""

import matplotlib.pyplot  as plt
import math


class log():
    def is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            pass
    
        return False
    
    def readLogFile(self, fileName):
        
        startLog=0
        logFile = open(fileName, "r")
        
        
        data = []
        legend = []
        
        lineStart = 0 
        
        i=0
        for line in logFile :
             if (line.find("BEGIN_LOG") >= 0) :
                print "Begin_Log found"
                lineStart = i
                print lineStart    
             i=i+1
            
        print "done"
        print lineStart        
        i=0    
        logFile.seek(0,0)
        if(lineStart > 0) :
            for line in logFile :
                print line
                if (i == lineStart-1) :
                    break
                i=i+1
        
        
        i=-1
        for line in logFile :
            #Discard empty line 
            if (not line.strip() ) :
                continue
            
            if (line.find("BEGIN_LOG") >= 0) :
                print "Begin_Log found"
                startLog=1
                continue
                
            if  (line.find("END_LOG") >= 0) :   
                print "END_LOG found"
                break
            
            if(startLog) :
                if (not self.is_number(line)) :
                    print "New cat found" 
                    print line
                    data.append([])   
                    legend.append([str(line[:-4])])                
                    i = i+1                            
                else : 
                    data[i].append(float(line))
                
                
       
        return data, legend
    
    def display(self, data, legend):
        fig = plt.figure()
      
        i=0
        print len(data)
        for d in data :
            ax = fig.add_subplot(2,3,i)
            i=i+1
            
            ax.plot(d, label=legend[i-1])
            ax.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=4, mode="expand", borderaxespad=0.)
    
        plt.show()

if __name__=="__main__":
    data, legend = readLogFile("logPython.txt")

    display(data, legend)




