import numpy as np
import matplotlib.pyplot as plt
#from main_plotter import hori_plot
#source ids are: 4741083594827008640
#4740787585680726528

class gaia_data:
	
	def read_table(self,infile,d):
		
		def floatynumpy(stringy):
			out = np.array([float(i) for i in stringy])
			return out
			
		def absolute(m,dist):
			M = m-5*np.log10(dist/10)
			return M
			
		f = open(infile,'r')
		lines = f.readlines()[1:]
		fill_list = []
		columns = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
		columnames = [sid,ra,raerr,dec,decerr,parr,parrerr,pmra,pmraerr,pmdec,pmdecerr,exnoise,gmag,bmag,rmag,b_r]=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
		for x in lines:
			for j in (columns):
				columnames[j].append(x.split(',')[j])
				
		#print(ra)
		#print(dec)
		#getridofspacesprint(parr)
		#[source_id,ra] = [[],[]]
		#print(fill_list)
		#print(source_id)
		#print(pmdec)
		
		
		
		for j in columnames:
			for i in range(len(ra)):
				if j[i] == '':
					j[i] = np.nan
		
		sid = floatynumpy(sid)
		ra = floatynumpy(ra)
		raerr = floatynumpy(raerr)
		dec = floatynumpy(dec)
		decerr = floatynumpy(decerr)
		parr = floatynumpy(parr)
		parrerr = floatynumpy(parrerr)
		pmra = floatynumpy(pmra)
		pmraerr = floatynumpy(pmraerr)
		pmdec = floatynumpy(pmdec)
		pmdecerr = floatynumpy(pmdecerr)
		exnoise = floatynumpy(exnoise)
		gmag = floatynumpy(gmag)
		bmag = floatynumpy(bmag)
		rmag = floatynumpy(rmag)
		b_r = floatynumpy(b_r)
		
		for i in range(len(bmag)):
			bmag[i] = bmag[i]-5*np.log10(d/10)
		
		return np.array([sid,ra,raerr,dec,decerr,parr,parrerr,pmra,pmraerr,pmdec,pmdecerr,exnoise,bmag,rmag,b_r])
		
	def culling(self, col):
		def gaia_cull(parr,pmra,pmraerr,pmdec,pmdecerr,exnoise):
			horpmra = 0.926
			horpmraerr = 0.070
			horpmdec = -0.569
			horpmdecerr = 0.065
			if parr > 0.5:
				return True
				
			#elif ((pmra + pmraerr < horpmra-horpmraerr) and (pmra - pmraerr > horpmra+horpmraerr)) or ((pmdec + pmdecerr < horpmdec-horpmdecerr) and (pmdec - pmdecerr > horpmdec + horpmdecerr)):
				#return True
			
			elif exnoise > 1:
				
				return True
		
		for i in range(len(col[0])):
			if gaia_cull(col[5][i],col[7][i],col[8][i],col[9][i],col[10][i],col[11][i]) == True:
				for j in col:
					j[i] = np.nan
			else:
				continue
				
		return col
	
	def plotalphiso(self,age,alpha,feh,infile):
		
#function to plot Dartmouth isochrones. Age, alpha and [Fe/H] for graph labels only
		
		def floatynumpy(stringy):
			out = np.array([float(i) for i in stringy])
			return out
#floatynumpy defined again
		bmag = []
		rmag = []
#empty lists defined
		f=open(infile, 'r')
		lines = f.readlines()[9:]
#dartmouth data file read in
		for x in lines:
			bmag.append(x.split()[6])
			rmag.append(x.split()[7])
#lists filled with isochrones magnitudes
		
		bmag = floatynumpy(bmag)
		rmag = floatynumpy(rmag)
		colour = bmag - rmag
		
#lists turned into arrays
		
		#plt.plot(colour,bmag,linewidth = 1,label = ('Age=' + str(age) + 'Gyrs, alpha='+str(alpha) +', [Fe/H] = ' + str(feh) ),color = 'black')
		
		
			
		
		
		#pmdec = floatynumpy(pmdec)
yeet = gaia_data()
#data = yeet.read_table('hori_gaia_data.csv')
data = yeet.read_table('hori.csv',79000)
data = yeet.culling(data)

#x = data[0]
#y = data[1]
#print(x)
#print(np.array([7,5,3,2]))
#hori_plot()
plt.xlabel('BP-RP')
plt.ylabel('BP Mean Magnitude')
plt.title('HorI')
plt.scatter(data[14],data[12],s=2)
#yeet.plotalphiso(13,0.4,-2.0,'dmgaia_13.0_0.4_-2z.txt')
plt.gca().invert_yaxis()
plt.show()




