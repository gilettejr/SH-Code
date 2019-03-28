

import matplotlib.pyplot as plt
import numpy as np

#libraries imported



class hr:
	
#class to hold reading, culling and isochrone plotting functions

	
	def plotiso(self,inputfile,z1,z2,z3,z4,age,dist):
		
#plots Padova isochrones over four metallicities at a chosen distance. dist = 10 gives absolute magnitudes

		
		def apparent(M,dguess):
			m = M + 5*np.log10(dguess/10)
			return m

#converts absolute magitude into apparent magnitude if dist other than 10 is chosen


		def floatynumpy(stringy):
			out = np.array([float(i) for i in stringy])
			return out
			
#function to convert a list of strings into an array of floats


		def fzc(z,zarray):
			for i in range(len(zarray)):
				if zarray[i] == z:
					out = i
					break
			return out
			
#function to seperate different metallicities in isochrone tables

		def trim(iso,lab):
			for i in range(len(iso)):
				if lab[i] > 3:
					iso[i] = np.nan

			return iso
			
#function to trim isochrones to main sequence and red giant branch
	#1 Z

	#29 606

	#34
		init = []
		rmag = []
		imag = []
		tag=[]
#empty lists created to be filled with data
		f=open(inputfile, 'r')
		lines = f.readlines()

		for x in lines:
			rmag.append(x.split()[28])
			imag.append(x.split()[33])
			init.append(x.split()[0])
			tag.append(x.split()[7])
#input file opened for reading, data for rmag, imag, initalZ and trimming tag read in

	#print(rmag)
		zinit = floatynumpy(init)
		armag = floatynumpy(rmag)
		atag = floatynumpy(tag)

		aimag = floatynumpy(imag)
		
		armag = trim(armag,atag)
		aimag = trim(aimag,atag)
		
#lists of strings changed to arrays of floats, isochrones trimmed
		
		acolour = armag - aimag
		
#array for r-i colour defined

		for i in range(len(rmag)):
			armag[i] = apparent(armag[i],dist)
			aimag[i] = apparent(aimag[i],dist)

		zone = fzc(z1,zinit)
		ztwo = fzc(z2,zinit)
		zthree = fzc(z3,zinit)
		zfour = fzc(z4,zinit)

#magnitudes changed to represent distance if chosen, different initial z values assigned to variables

		plt.plot(acolour[:zone],armag[:zone], linewidth =0.5, label = age + ', Z= '+ '0.0001' + ', ' + str(dist) + ' pc')
		plt.plot(acolour[zone:ztwo],armag[zone:ztwo], linewidth = 0.5, label = age + ', Z= '+ '0.0002'+ ', ' + str(dist) + ' pc')
		plt.plot(acolour[ztwo:zthree],armag[ztwo:zthree], linewidth =0.5, label = age + ', Z= '+ '0.0003  '+', ' + str(dist) + ' pc')
		plt.plot(acolour[zthree:zfour],armag[zthree:zfour],linewidth = 0.5, label = age + ', Z= '+'0.0004'+ ', ' + str(dist) + ' pc')
		plt.plot(acolour[zfour:],armag[zfour:],linewidth = 0.5, c = 'k',label = age + ', Z= '+ '0.0005'+ ', ' + str(dist) + ' pc')

#isochrones for different z plotted and labelled accordingly
		
		#plotiso('0.01-0.03z_t12.7isochrone.dat',0.01500,0.02000,0.02500,0.03000,'13.5')
		#plotiso('0.01-0.03z_t4.7isochrone.dat',0.01500,0.02000,0.02500,0.03000)
		#plotiso('0.01-0.05z_t1isochrone.dat',0.02000,0.03000,0.04000,0.05000)
		#plotiso('0.0001-0.0301z_t2.7isochrone.dat',0.00510,0.01010,0.01510,0.02010)
		
		
		#plt.show()
		
	def plotalphiso(self,age,alpha,feh,infile):
		
#function to plot Dartmouth isochrones. Age, alpha and [Fe/H] for graph labels only
		
		def floatynumpy(stringy):
			out = np.array([float(i) for i in stringy])
			return out
#floatynumpy defined again
		rmag = []
		imag = []
#empty lists defined
		f=open(infile, 'r')
		lines = f.readlines()[9:]
#dartmouth data file read in
		for x in lines:
			rmag.append(x.split()[10])
			imag.append(x.split()[15])
#lists filled with isochrones magnitudes
		
		rmag = floatynumpy(rmag)
		imag = floatynumpy(imag)
		colour = rmag - imag
		
#lists turned into arrays
		
		plt.plot(colour,rmag,linewidth = 1,color='black')
		
#isochrones plotted

	def isomasses(self,infile):
		#function to plot Dartmouth isochrones. Age, alpha and [Fe/H] for graph labels only
		
		def floatynumpy(stringy):
			out = np.array([float(i) for i in stringy])
			return out
#floatynumpy defined again
		rmag = []
		imag = []
		m=[]
#empty lists defined
		f=open(infile, 'r')
		lines = f.readlines()[9:]
#dartmouth data file read in
		for x in lines:
			rmag.append(x.split()[10])
			imag.append(x.split()[15])
			m.append(x.split()[1])
#lists filled with isochrones magnitudes
		
		rmag = floatynumpy(rmag)
		imag = floatynumpy(imag)
		m = floatynumpy(m)
		colour = rmag - imag
		mass_data = np.array([rmag,colour,m])
		return mass_data
		
	def read_cull(self,infile,distance,a,b,rad,ufd):
		
#function to cull and plot data after photometry from dolphot
		
		def absolute(m,d):
			M = m-5*np.log10(d/10)
			return M
#function to produce an absolute magnitude from apparent magnitude and distance
		def floatynumpy(stringy):
			out = np.array([float(i) for i in stringy])
			return out
#used for same as before
		def param_cull(object_type,rerror_flag, ierror_flag):
#culling function based on dolphot recommendations
			if object_type > 1:
				
				return True
				
			elif rerror_flag>3 or ierror_flag>3:
				
				return True	
				
			else:
				return False

#returns true if data needs to be culled


		def crater_cull(red_signal_noise, infra_signal_noise, red_sharp, infra_sharp, red_crowd, infra_crowd):
			
#culling function based on recommendations from crater team
			
			if red_signal_noise < 5 or infra_signal_noise < 5:
				
				return True
			elif (red_sharp + infra_sharp)**2 > 0.1:
				#mag > 0.3
				return True
			elif red_crowd + infra_crowd > 1.0:
				
				return True
			else:
				return False
				
		def ghost_cull(red_signal_noise, infra_signal_noise, red_sharp, infra_sharp, red_crowd, infra_crowd):
			
#culling function based on recommendations from ghost 1 team
			
			if red_signal_noise < 5 or infra_signal_noise < 5:
				
				return True
			elif red_sharp + infra_sharp < -0.06 or red_sharp + infra_sharp > 1.30:
				
				return True
			elif red_crowd + infra_crowd > 0.16:
				return True
			else:
				return False
				
		def rad_cull(pointx, pointy, centrex, centrey, radius):
			
#culling function for only detecting stars in a circular radius from a defined position
			
			if (((pointx-centrex)**2 + (pointy-centrey)**2)**(0.5) ) > radius:
				return True
			else:
				return False
			
	
		print('Reading in data')

		f = open(infile,"r")
		lines = f.readlines()
		obnum = []
		sharp = []

		vmag = []
		imag = []

	#crater culls
		rsnr = []
		isnr = []
		rsharp = []
		isharp = []
		rcrowd = []
		icrowd = []
		rerr = []
		ierr = []
		xcord =[]
		ycord = []
		runc = []
		iunc = []
#lists made for dolphot columns

		deleted = []
		celeted = []
		geleted = []
		
#lists made to determine number of culled stars
		
		for x in lines:
			vmag.append(x.split()[15])
			imag.append(x.split()[28])
			obnum.append(x.split()[10])
			sharp.append(x.split()[6])
			rsnr.append(x.split()[19])
			isnr.append(x.split()[32])
			rsharp.append(x.split()[20])
			isharp.append(x.split()[33])
			rcrowd.append(x.split()[22])
			icrowd.append(x.split()[35])
			rerr.append(x.split()[23])
			ierr.append(x.split()[36])
			xcord.append(x.split()[2])
			ycord.append(x.split()[3])
			runc.append(x.split()[17])
			iunc.append(x.split()[30])

			print(len(vmag))
#lists filled with appropriate columns of data

		#err.append(x.split()[23])
		f.close()

		
		


		avmag = floatynumpy(vmag)
		aimag = floatynumpy(imag)
		aonum = floatynumpy(obnum)
		asharp = floatynumpy(sharp)
		arsnr = floatynumpy(rsnr)
		aisnr = floatynumpy(isnr)
		arsharp = floatynumpy(rsharp)
		aisharp= floatynumpy(isharp)
		arcrowd= floatynumpy(rcrowd)
		aicrowd= floatynumpy(icrowd)
		arerr = floatynumpy(rerr)
		aierr = floatynumpy(ierr)
		axcord = floatynumpy(xcord)
		aycord = floatynumpy(ycord)
		arunc = floatynumpy(runc)
		aiunc = floatynumpy(iunc)
		#print(axcord[7])
#lists of strings converted to arrays of floats
	#ferr = [float(i) for i in err]

		celeted = []

	#pavmagdl = np.array([])
	#gavmagdl = np.array([])
	#cavmagdl = np.array([])
	#gpavmagdl = np.array([])
	#cgavmagdl = np.array([])
	#cpavmagdl = np.array([])
	#cgpavmagdl = np.array([])
	#paimagdl = np.array([])
	#gaimagdl = np.array([])
	#caimagdl = np.array([])
	#gpaimagdl = np.array([])
	#cgaimagdl = np.array([])
	#cpaimagdl = np.array([])
	#cgpaimagdl = np.array([])
	
		
			


		for i in range(len(avmag)):
			avmag[i] = absolute(avmag[i],distance)
			aimag[i] = absolute(aimag[i],distance)		

#apparent magnitudes ci=onverted into absolute magnitudes

	#aerr = np.array(ferr)
		acolour = avmag - aimag
		
#v-r colour defined

		print('Mapping bad stars')

		#for j in range(len(avmag)):	
			#if ghost_cull(arsnr[j],aisnr[j],arsharp[j],aisharp[j],arcrowd[j],aicrowd[j]) ==True and crater_cull(arsnr[j],aisnr[j],arsharp[j],aisharp[j],arcrowd[j],aicrowd[j]) == True and param_cull(aonum[j], avmag[j],acolour[j],asharp[j]) == True:
				#cgpavmagdl = np.append(cgpavmagdl,avmag[j])
				#cgpaimagdl = np.append(cgpaimagdl,aimag[j])
			
			#elif param_cull(aonum[j], avmag[j],acolour[j],asharp[j]) == True and crater_cull(arsnr[j],aisnr[j],arsharp[j],aisharp[j],arcrowd[j],aicrowd[j]) == True:
				#cpavmagdl = np.append(cpavmagdl, avmag[j])
				#cpaimagdl = np.append(cpaimagdl, aimag[j])
			
			#elif param_cull(aonum[j], avmag[j],acolour[j],asharp[j]) == True and ghost_cull(arsnr[j],aisnr[j],arsharp[j],aisharp[j],arcrowd[j],aicrowd[j]) == True:
				#gpavmagdl = np.append(gpavmagdl, avmag[j])
				#gpaimagdl = np.append(gpaimagdl, aimag[j])
			
			#elif crater_cull(arsnr[j],aisnr[j],arsharp[j],aisharp[j],arcrowd[j],aicrowd[j]) == True and ghost_cull(arsnr[j],aisnr[j],arsharp[j],aisharp[j],arcrowd[j],aicrowd[j]) == True:
				#cgavmagdl = np.append(cgavmagdl, avmag[j])
				#cgaimagdl = np.append(cgaimagdl, aimag[j])
			
			#elif param_cull(aonum[j], avmag[j],acolour[j],asharp[j]) == True:
				#pavmagdl = np.append(pavmagdl, avmag[j])
				#paimagdl = np.append(paimagdl, aimag[j])
			
			#elif crater_cull(arsnr[j],aisnr[j],arsharp[j],aisharp[j],arcrowd[j],aicrowd[j]) == True:
				#cavmagdl = np.append(cavmagdl, avmag[j])
				#caimagdl = np.append(caimagdl, aimag[j])
			
			#elif ghost_cull(arsnr[j],aisnr[j],arsharp[j],aisharp[j],arcrowd[j],aicrowd[j]) == True:
				#gavmagdl = np.append(gavmagdl, avmag[j])
				#gaimagdl = np.append(gaimagdl, aimag[j])

		print('Deleting bad stars')

		if ufd == 'hori':
		#horI
			vextinction = 0.036
			iextinction = 0.022
			#vextinction = 5475439583749587
			#iextinction = 345677
		
		elif ufd == 'horii':
		#horII
		
			vextinction = 0.05
			iextinction = 0.031
			
		else:
			
			vextinction = 0
			iextinction = 0
			
			print('No extinction correction applied')
#appropriate extinction corrections defined, depending on galaxy
		for j in range(len(avmag)):
		
			avmag[j] = avmag[j] - vextinction
			aimag[j] = aimag[j] - iextinction
			
#extinction corrections applied to absolute magnitudes
		
			if param_cull(aonum[j], arerr[j],aierr[j]) == True:
			
				avmag[j] = np.nan
				aimag[j] = np.nan
				acolour[j] = np.nan
				axcord[j] = np.nan
				aycord[j] = np.nan
				aiunc[j]=np.nan
				arunc[j]=np.nan
				deleted.append(0)
			#elif crater_cull(arsnr[j],aisnr[j],arsharp[j],aisharp[j],arcrowd[j],aicrowd[j]) == True:
				#avmag[j] = np.nan
				#aimag[j] = np.nan
				#acolour[j] = np.nan
				#celeted.append(0)	
		
			elif ghost_cull(arsnr[j],aisnr[j],arsharp[j],aisharp[j],arcrowd[j],aicrowd[j]) == True:
				avmag[j] = np.nan
				aimag[j] = np.nan
				axcord[j] = np.nan
				aycord[j] = np.nan
				acolour[j] = np.nan
				aiunc[j]=np.nan
				arunc[j]=np.nan
				geleted.append(0)
				
		acolour = avmag - aimag
		acolunc = np.sqrt(aiunc**2+arunc**2)
		for k in range(len(avmag)):
		
			if a =='no' or b=='no' or rad =='no':
				break
			
			elif axcord[k] == np.nan:
				continue
			
			elif rad_cull(axcord[k],aycord[k],a,b,rad) == True:
				avmag[k] = np.nan
				aimag[k] = np.nan
				#print('yeeet')
				celeted.append(0)
			else:
				continue
			
		
		
		print(len(deleted))
		print('Objects deleted from basic scrubbing')

		print(len(celeted))
		print('Objects deleted from crater recommendations')

		print(len(geleted))
		print('Objects deleted from GHOST recommendations')
		
		area = (len(avmag) - (len(celeted) + len(geleted) + len(deleted)))
		
		data = [avmag,aimag,acolour,area,axcord,aycord,arunc,acolunc]
 
		return data
		
	def plotalphas(self, x1, y1, x2, y2, x3, y3):
		
		def absolute(m,d):
			M = m-5*np.log10(d/10)
			return M
		
		def floatynumpy(stringy):
			out = np.array([float(i) for i in stringy])
			return out
			
		def param_cull(object_type,rerror_flag, ierror_flag):
			if object_type > 1:
				
				return True
				
			elif rerror_flag>3 or ierror_flag>3:
				
				return True	
				
			else:
				return False
				
		def ghost_cull(red_signal_noise, infra_signal_noise, red_sharp, infra_sharp, red_crowd, infra_crowd):
			if red_signal_noise < 5 or infra_signal_noise < 5:
				
				return True
			elif red_sharp + infra_sharp < -0.06 or red_sharp + infra_sharp > 1.30:
				
				return True
			elif red_crowd + infra_crowd > 0.16:
				return True
			else:
				return False
		
		
		f = open('sresult',"r")
		lines = f.readlines()
		obnum = []
		sharp = []

		vmag = []
		imag = []

	#crater culls
		rsnr = []
		isnr = []
		rsharp = []
		isharp = []
		rcrowd = []
		icrowd = []
		rerr = []
		ierr = []
		xcord =[]
		ycord = []

		deleted = []
		celeted = []
		geleted = []
		for x in lines:
			vmag.append(x.split()[15])
			imag.append(x.split()[28])
			obnum.append(x.split()[10])
			sharp.append(x.split()[6])
			rsnr.append(x.split()[19])
			isnr.append(x.split()[32])
			rsharp.append(x.split()[20])
			isharp.append(x.split()[33])
			rcrowd.append(x.split()[22])
			icrowd.append(x.split()[35])
			rerr.append(x.split()[23])
			ierr.append(x.split()[36])
			xcord.append(x.split()[2])
			ycord.append(x.split()[3])

			print(len(vmag))
		
		#err.append(x.split()[23])
		f.close()

		
		


		avmag = floatynumpy(vmag)
		aimag = floatynumpy(imag)
		aonum = floatynumpy(obnum)
		asharp = floatynumpy(sharp)
		arsnr = floatynumpy(rsnr)
		aisnr = floatynumpy(isnr)
		arsharp = floatynumpy(rsharp)
		aisharp= floatynumpy(isharp)
		arcrowd= floatynumpy(rcrowd)
		aicrowd= floatynumpy(icrowd)
		arerr = floatynumpy(rerr)
		aierr = floatynumpy(ierr)
		axcord = floatynumpy(xcord)
		aycord = floatynumpy(ycord)
		
		vextinction = 0.036
		iextinction = 0.022
		
		for j in range(len(avmag)):
		
			avmag[j] = avmag[j] - vextinction
			aimag[j] = aimag[j] - iextinction	
		
		
			#if param_cull(aonum[j], arerr[j],aierr[j]) == True:
			
				#avmag[j] = np.nan
				#aimag[j] = np.nan
				
				#axcord[j] = np.nan
				#aycord[j] = np.nan
				#deleted.append(0)
				#continue
			#elif crater_cull(arsnr[j],aisnr[j],arsharp[j],aisharp[j],arcrowd[j],aicrowd[j]) == True:
				#avmag[j] = np.nan
				#aimag[j] = np.nan
				#acolour[j] = np.nan
				#celeted.append(0)	
		
			##elif ghost_cull(arsnr[j],aisnr[j],arsharp[j],aisharp[j],arcrowd[j],aicrowd[j]) == True:
				#avmag[j] = np.nan
				#aimag[j] = np.nan
				#axcord[j] = np.nan
				#aycord[j] = np.nan
				
				#geleted.append(0)
				
		err = 50
			
		for i in range(len(avmag)):
			
			if (axcord[i] > x1-err and axcord[i] < x1+err) and (aycord[i] > y1-err and aycord[i] < y1+err):
				continue
			elif (axcord[i] > x2-err and axcord[i] <x2+err) and (aycord[i] > y2-err and aycord[i] < y2+err):
				continue
			elif axcord[i] == x3 and aycord[i] == y3:
				continue
			else:
				
				avmag[i] = np.nan
				aimag[i] = np.nan
				
		
		
		
		
		for i in range(len(avmag)):
			avmag[i] = absolute(avmag[i],79000)
			aimag[i] = absolute(aimag[i],79000)
		
		
		
		acolour = avmag - aimag
		
		data = [avmag,aimag,acolour,'some']
		
		return data

