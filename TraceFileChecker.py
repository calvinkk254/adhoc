#aodv,olsr
import os
import matplotlib.pyplot as plt

def checkThroughput(traceFileName:str,packSize:int):
	flieOpenObject = open('./mixed-wireless.tr','rt')
	throughput:int =0
	fail:int=0
	while True :
		singleLine=[]
		line = flieOpenObject.readline()
		if not line:
			break
		line=line.replace("\n","")
		tempList=line.split(" ")
		if(tempList[0]=="d"):fail+=1
		elif(tempList[0]=="r"):throughput+=1
	print("Throughput:",throughput-fail,"\n")
	return (throughput-fail)*packSize

if __name__ == '__main__':
	traceFileName="mixed-wireless.tr"
	packSize=100
	print(checkThroughput(traceFileName,packSize),"kb")
