import matplotlib.pyplot as plt
import numpy as np

def apparent(M,dguess):
	m = M + 5*np.log10(dguess/10)
	return m
	

def floatynumpy(stringy):
	out = np.array([float(i) for i in stringy])
	return out

def fzc(z,zarray):
	for i in range(len(zarray)):
		if zarray[i] == z:
			out = i
			break
	return out
	
def trim(iso,lab):
	for i in range(len(iso)):
		if lab[i] > 3:
			iso[i] = np.nan
			
	return iso
	
def plotiso(inputfile,z1,z2,z3,z4,age,dist):
#1 Z

#29 606

#34
	init = []
	rmag = []
	imag = []
	tag=[]

	f=open(inputfile, 'r')
	lines = f.readlines()

	for x in lines:
		rmag.append(x.split()[28])
		imag.append(x.split()[33])
		init.append(x.split()[0])
		tag.append(x.split()[7])


#print(rmag)
	zinit = floatynumpy(init)
	armag = floatynumpy(rmag)
	atag = floatynumpy(tag)

	aimag = floatynumpy(imag)
	
	armag = trim(armag,atag)
	aimag = trim(aimag,atag)
	
	acolour = armag - aimag

	for i in range(len(rmag)):
		armag[i] = apparent(armag[i],dist)
		aimag[i] = apparent(aimag[i],dist)

	zone = fzc(z1,zinit)
	ztwo = fzc(z2,zinit)
	zthree = fzc(z3,zinit)
	zfour = fzc(z4,zinit)


	plt.plot(acolour[:zone],armag[:zone], linewidth =0.5, label = age + ', Z= '+ str(z1-(z2-z1)) + str(dist))
	plt.plot(acolour[zone:ztwo],armag[zone:ztwo], linewidth = 0.5, label = age + ', Z= '+ str(z2-(z2-z1))+ str(dist))
	plt.plot(acolour[ztwo:zthree],armag[ztwo:zthree], linewidth =0.5, label = age + ', Z= '+ str(z3-(z2-z1))+ str(dist))
	plt.plot(acolour[zthree:zfour],armag[zthree:zfour],linewidth = 0.5, label = age + ', Z= '+ str(z4-(z2-z1))+ str(dist))
	plt.plot(acolour[zfour:],armag[zfour:],linewidth = 0.5, c = 'k',label = age + ', Z= '+ str(z4)+ str(dist))

def main():
	
	plotiso('0.01-0.03z_t12.7isochrone.dat',0.01500,0.02000,0.02500,0.03000,'13.5')
	#plotiso('0.01-0.03z_t4.7isochrone.dat',0.01500,0.02000,0.02500,0.03000)
	#plotiso('0.01-0.05z_t1isochrone.dat',0.02000,0.03000,0.04000,0.05000)
	#plotiso('0.0001-0.0301z_t2.7isochrone.dat',0.00510,0.01010,0.01510,0.02010)
	
	plt.ylabel('F606W')
	plt.xlabel('F606W - F814W')
	plt.gca().invert_yaxis()
	plt.legend()
	plt.show()

#main()

