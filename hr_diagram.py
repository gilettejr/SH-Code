import numpy as np
import matplotlib.pyplot as plt
from isochrones import plotiso

#606 - R Band
#814 - I Band
#I want I - V

#things to look at:sharpness,error flag

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



def crater_cull(red_signal_noise, infra_signal_noise, red_sharp, infra_sharp, red_crowd, infra_crowd):
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
	if red_signal_noise < 5 or infra_signal_noise < 5:
		
		return True
	elif red_sharp + infra_sharp < -0.06 or red_sharp + infra_sharp > 1.30:
		
		return True
	elif red_crowd + infra_crowd > 0.16:
		return True
	else:
		return False

def read_cull(infile,distance):
	
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



#aerr = np.array(ferr)
	acolour = avmag - aimag

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

	#vextinction = 1.789
	#iextinction = 1.105
	#horI
	#vextinction = 0.036
	#iextinction = 0.022
	
	#horII
	
	vextinction = 0.05
	iextinction = 0.031
	
	for j in range(len(avmag)):
	
		avmag[j] = avmag[j] - vextinction
		aimag[j] = aimag[j] - iextinction	
	
	
		if param_cull(aonum[j], arerr[j],aierr[j]) == True:
		
			avmag[j] = np.nan
			aimag[j] = np.nan
			acolour[j] = np.nan
			deleted.append(0)
		#elif crater_cull(arsnr[j],aisnr[j],arsharp[j],aisharp[j],arcrowd[j],aicrowd[j]) == True:
			#avmag[j] = np.nan
			#aimag[j] = np.nan
			#acolour[j] = np.nan
			#celeted.append(0)	
	
		elif ghost_cull(arsnr[j],aisnr[j],arsharp[j],aisharp[j],arcrowd[j],aicrowd[j]) == True:
			avmag[j] = np.nan
			aimag[j] = np.nan
			acolour[j] = np.nan
			geleted.append(0)

		
	print(len(deleted))
	print('Objects deleted from basic scrubbing')

	print(len(celeted))
	print('Objects deleted from crater recommendations')

	print(len(geleted))
	print('Objects deleted from GHOST recommendations')
	
	data = [avmag,aimag,acolour]
	
	return data

	for k in range(len(cgpavmagdl)):
		if cgpavmagdl[k] > 99 or cgpavmagdl[k]-cgpaimagdl[k] < -50:
			cgpavmagdl[k] = np.nan
			cgpaimagdl[k] = np.nan
		
	mk = 'markersize = 0.1'
		
	fig, (ax1, ax2,ax3) = plt.subplots(1,3,)
	ax1.plot(avmag - aimag, avmag, 'o', mk)
	ax1.invert_yaxis()


	ax1.set_title('Colour Magnitude diagram for HorI after culling')

	ax1.set(xlabel='F606-F814', ylabel='F606 Mag')

	ax1.set_xlim([-0.26, 3.70])
	ax1.set_ylim([29.0, 19.0])


	ax2.plot(cgpavmagdl-cgpaimagdl, cgpavmagdl, 'ko',mk,label = 'c,g,p')
	ax2.plot(cpavmagdl-cpaimagdl, cpavmagdl, 'go',mk,label = 'c,p')
	ax2.plot(cgavmagdl-cgaimagdl, cgavmagdl, 'ro',mk,label = 'c,g')
	ax2.plot(gpavmagdl-gpaimagdl, gpavmagdl, 'co',mk,label = 'g,p')
	ax2.plot(cavmagdl - caimagdl, cavmagdl, 'mo',mk,label = 'c')
	ax2.plot(gavmagdl- gaimagdl, gavmagdl, 'yo',mk,label = 'g')
	ax2.plot(pavmagdl-paimagdl, pavmagdl, 'bo',mk,label = 'p')

	ax2.invert_yaxis()

	ax2.set(xlabel='F606-F814', ylabel='F814 Mag')
	ax2.set_title('Colour Magnitude diagram for culled HorI stars')
	ax2.set_xlim([-0.26, 3.70])
	ax2.set_ylim([29.0, 19.0])

	legend = ax2.legend(loc = 'lower right')
	for legend_handle in legend.legendHandles:
		legend_handle._legmarker.set_markersize(20)

	ax3.plot(cgpavmagdl-cgpaimagdl, cgpavmagdl, 'ko',mk,label = 'c,g,p')
	ax3.plot(cpavmagdl-cpaimagdl, cpavmagdl, 'go',mk,label = 'c,p')
	ax3.plot(cgavmagdl-cgaimagdl, cgavmagdl, 'ro',mk,label = 'c,g')
	ax3.plot(gpavmagdl-gpaimagdl, gpavmagdl, 'co',mk,label = 'g,p')
	ax3.plot(cavmagdl - caimagdl, cavmagdl, 'mo',mk,label = 'c')
	ax3.plot(gavmagdl- gaimagdl, gavmagdl, 'yo',mk,label = 'g')
	ax3.plot(pavmagdl-paimagdl, pavmagdl, 'bo',mk,label = 'p')
	ax3.plot(avmag - aimag, avmag, 'o',mk,label = 'nf')
	ax3.set(xlabel='F606-F814', ylabel='F606 Mag')
	ax3.set_title('Colour Magnitude diagram for culled HorI stars')
	ax3.legend(loc = 'lower right')
	ax3.invert_yaxis()
	ax3.set_xlim([-0.26, 3.70])
	ax3.set_ylim([29.0, 19.0])
	plt.show()
	


def plotit(data):
	
	avmag = data[0]
	aimag = data[1]
	acolour = data[2]

	plt.scatter(acolour,avmag,s=0.5, label = 'HorII Data')
	#plotiso('0.01-0.03z_t12.7isochrone.dat',0.01500,0.02000,0.02500,0.03000)
	#plotiso('0.01-0.03z_t4.7isochrone.dat',0.01500,0.02000,0.02500,0.03000)
	#plotiso('0.01-0.05z_t1isochrone.dat',0.02000,0.03000,0.04000,0.05000)
	#plotiso('0.01-0.05z_t2.7isochrone.dat',0.02000,0.03000,0.04000,0.05000)
	#plotiso('0.0001-0.02010_t2.7isochrone.dat',0.00510,0.01010,0.01510,0.02010)
	#plotiso('0.0001-0.0201z_t4.7isochrone.dat',0.00510,0.01010,0.01510,0.02010)
	#plotiso('0.0001-0.00014z_t12.7isochrone.dat',0.00011,0.00012,0.00013,0.00014)	#looks best right now
	#plotiso('0.0001-0.0004z_t8.7isochrone.dat',0.00011,0.00012,0.00013,0.00014)
	#plotiso('0.0001-0.0005z_t12.7isochrones.dat',0.00020,0.00030,0.00040,0.00050)	#nope, this one
	#plotiso('0.0001-0.0005z_t13isocr.dat',0.00020,0.00030,0.00040,0.00050, '13Gyr',10)
	#plotiso('0.0001-0.0005z_t13.5isochrone.dat',0.00020,0.00030,0.00040,0.00050, '13.5Gyr', 10)
	plt.ylabel('F606W (ACS)')
	plt.xlabel('F606W-F814W (ACS)')
	plt.title('HorI Data with Isochrones')
	#plt.xlim((0.3,1.5))
	#plt.ylim((-2,10))
	
	plt.legend()
	#plt.savefig('06_02_ghost.png')
	
def main():
	read_cull('result',10)
	#plotting_data =  read_cull('result_west',78000)
	#plotting_data = read_cull('result_east',78000)
	#plotit(plotting_data)
	#plotiso('0.0001-0.0005z_t13.5isochrone.dat',0.00020,0.00030,0.00040,0.00050, '13.5Gyr', 10)
	#plt.gca().invert_yaxis()
	#plt.show()

main()
