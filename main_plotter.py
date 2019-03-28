import matplotlib.pyplot as plt
import numpy as np

from plotting_class import hr

def circlegenerator(r,limit):
	apers =[]
	R = np.sqrt(2)* r
	apers.append(r)
	apers.append(R)
	
	while R<limit:
		a = np.sqrt(R**2 + r**2)
		apers.append(a)
		R=a
	return apers

def plotit(data,label):
	
	avmag = data[0]
	aimag = data[1]
	acolour = data[2]
	arunc= data[6]
	acolunc=data[7]


	plt.scatter(acolour,avmag, s=4,label = str(label))
	a=-0.1
	xerr=np.array([0.05,0.02,0.01,0.004,0.003,0.002,0.001])
	yerr=np.array([0.08,0.03,0.015,0.008,0.005,0.003,0.002])
	xpos=np.array([a,a,a,a,a,a,a])
	ypos = np.array([7,6,5,4,3,2,1])
	
	plt.errorbar(xpos,ypos,xerr,yerr,fmt='none',color='red')
	#plt.errorbar(acolour,avmag,arunc,acolunc,fmt='none',colour='red')
	
	#for i in range(len(avmag)):
	
		
def plotrad(nstars,rads):
	
	plt.plot(nstars,rads,linewidth =0.5, label = 'Density in radial sections, HorI')
	plt.show()
	
def plotform(xlab,ylab,title):
	plt.ylabel(ylab)
	plt.xlabel(xlab)
	plt.title(title)
	plt.gca().invert_yaxis()
	#plt.legend()
	#horilims
	#plt.xlim((0,1.4))
	#plt.ylim((8,-1))
	
	
def regionplot(apertures):


	hori = hr()
	total_stars = []
	rads =[]
	
	for i in apertures:
		x = hori.read_cull('result',79000,2395,2943,i,'hori')
		plotit(x, 'Galactic Centre, rad =' + str(i))
		rads.append(i)
		total_stars.append(x[3])
	
	plt.rc('axes', labelsize = 20)
	
	stars=[]
	stars.append(total_stars[0])
	
	for j in range(1,len(total_stars)):
		stars.append(total_stars[j] - total_stars[j-1])
		
	plot_data = [rads,stars]
	
	f = open('rads.txt','w+')
	
	for i in range(len(rads)):
		f.write(str(rads[i])+'\n')
	f.close()
	
	f = open('stars.txt','w+')
	for i in range(len(stars)):
		f.write(str(stars[i])+ '\n')
	f.close()
	
	#return plot_data
		

	
	
	
	plotform('F606W$_0$-F814W$_0$','F606W$_0$', 'In Circular bands from centre')
	
def hori_isoplot():
	
	hori = hr()
	
	x = hori.read_cull('result',79000,'no','no','no','hori')
	plt.rc('axes', labelsize = 20)
	plotit(x, 'stars')
	hori.plotiso('0.0001-0.0005z_t13.5isochrone.dat',0.00020,0.00030,0.00040,0.00050, '13.5Gyr', 10)
	plotform('F606W$_0$-F814W$_0$','F606W$_0$', 'Hor I and Isochrones ')
	
def horii_isoplot():

	horii =hr()
	
	x = horii.read_cull('result_east',78000,'no','no','no','horii')
	y = horii.read_cull('result_west',78000,'no','no','no','horii')
	plt.rc('axes',labelsize = 20)
	plotit(x, 'stars')
	plotit(y, 'stars')
	horii.plotiso('0.0001-0.0005z_t13.5isochrone.dat',0.00020,0.00030,0.00040,0.00050, '13.5Gyr', 10)
	plotform('F606W$_0$-F814W$_0$','F606W$_0$', 'Hor II and Isochrones ')
	
def hori_alphaplot():
	
	hori = hr()
	
	x = hori.plotalphas(3199,748,1624,1796,-196,447)
	
	plotit(x, 'stars')
	hori.plotiso('0.0001-0.0005z_t13.5isochrone.dat',0.00020,0.00030,0.00040,0.00050, '13.5Gyr', 10)
	plotform('F606W$_0$-F814W$_0$','F606W$_0$', 'Alpha stars in HorI')
	

	
	#plt.show()

def hori_dartiso(infile,age,alpha,feh):
	dart = hr()
	
	plt.rc('axes',labelsize = 20)
	
	dart.plotalphiso(age,alpha,feh,infile)
	
	

	
def hori_plot():
	hori = hr()
	
	plt.rc('axes',labelsize = 20)
	
	x = hori.read_cull('result',79000,'no','no','no','hori')
	#y = hori.read_cull('ghost_result',79000,'no','no','no','hori')
	plotit(x,'Long Exposure')
	#plotit(y,'Fitsky=3')

	plotform('F606W$_0$-F814W$_0$','F606W$_0$', 'HorI')

def horii_plot():
	horii = hr()
	
	plt.rc('axes',labelsize = 20)
	
	x = horii.read_cull('result_west',74000,'no','no','no','horii')
	y = horii.read_cull('result_east',74000,'no','no','no','horii')
	plotit(x,'HorII West')
	plotit(y,'HorII East')
	plotform('F606W$_0$-F814W$_0$','F606W$_0$', 'HorII')
	
	
def hori_short_plot():
	
	hori = hr()
	#plt.rc('axes',labelsize=20)
	
	x = hori.read_cull('sresult',79000,'no','no','no','hori')
	plotit(x,'Short Exposure')
	plotform('F606W$_0$-F814W$_0$','F606W$_0$', 'HorI')

def massseghori_plot(galaxy,filein,msrhigh,msrlow,mscolhigh,mscollow):
	read = hr()
	mass_data = read.isomasses(filein)
	
	isormag = mass_data[0]
	isocolour = mass_data[1]
	isomass = mass_data[2] 
	
	hst_data = read.read_cull('result',79000,'no','no','no','hori')
	hstrmag = hst_data[0]
	hstcolour = hst_data[2]
	hstxpix = hst_data[4]
	hstypix = hst_data[5]
	for i in range(len(hstrmag)):
		if hstrmag[i] < 3.5 or hstrmag[i] > 6.5:
			hstrmag[i] = np.nan
			hstcolour[i] = np.nan
			
		#elif hstcolour[i] < mscollow or hstcolour[i] > mscolhigh:
			#hstrmag[i] = np.nan
			#hstcolour[i] = np.nan
	final_mass = []
	
	
	
	for i in range(len(hstrmag)):
		disp_list = []
		for j in range(len(isormag)):
			
			xdist = hstcolour[i] - isocolour[j]
			ydist = hstrmag[i] - isormag[j]
			if ydist ==np.nan or xdist == np.nan:
				disp = 100000000
			else:
				disp = np.sqrt((xdist**2 + ydist**2))
			disp_list.append(disp)
		
		final_mass.append(isomass[np.argmin(disp_list)])


	findist_list = []
	centrex = 2153
	centrey = 2368
	for i in range(len(hstxpix)):
		xfdist = centrex - hstxpix[i]
		yfdist = centrey - hstypix[i]
		findist = np.sqrt(xfdist**2 + yfdist**2)
		findist_list.append(findist)
	for i in range(len(final_mass)):
		if final_mass[i] < 0.2:
			final_mass[i] = np.nan
			findist_list[i] = np.nan
	f = open('masses.txt','w+')
	for i in final_mass:
		f.write(str(i)+'\n')
	f.close()
	f = open('dists.txt','w+')
	for j in findist_list:
		f.write(str(i)+'\n')
	f.close()
	highmass = []
	lowmass = []
	for i in range(len(findist_list)):
		if 0.59<final_mass[i]<0.66:
			lowmass.append(findist_list[i])
		elif 0.69<final_mass[i]<0.76:
			highmass.append(findist_list[i])
	#plt.figure(1)
	plt.hist(lowmass,3000,cumulative = True,histtype='step',label = '0.6-0.65 solar masses')
	plt.hist(highmass,3000,cumulative = True,histtype='step',label = '0.7-0.75 solar masses')
	plt.ylabel('Number of stars in Mass Range')
	plt.xlabel('Distance from Galactic Center(pixels)')
	plt.title('HorI')
	plt.legend(loc=2)
	plt.show()
	#plt.figure(2)
	#plt.scatter(findist_list,final_mass)
	#plt.xlabel('Distance from Galatic centre(pixels)')
	#plt.ylabel('Mass, in Solar Masses')
	#plt.title('Hori')
	#plt.show()


def massseghorii_plot(galaxy,filein,msrhigh,msrlow,mscolhigh,mscollow):
	read = hr()
	mass_data = read.isomasses(filein)
	
	isormag = mass_data[0]
	isocolour = mass_data[1]
	isomass = mass_data[2] 
	
	whst_data = read.read_cull('result_west',78000,'no','no','no','horii')
	ehst_data = read.read_cull('result_east',78000,'no','no','no','horii')
	whstrmag = whst_data[0]
	whstcolour = whst_data[2]
	whstxpix = whst_data[4]
	whstypix = whst_data[5]
	ehstrmag = ehst_data[0]
	ehstcolour = ehst_data[2]
	ehstxpix = ehst_data[4]
	ehstypix = ehst_data[5]
	for i in range(len(whstrmag)):
		if whstrmag[i] < 3.5 or whstrmag[i] > 6.5:
			whstrmag[i] = np.nan
			whstcolour[i] = np.nan
	
	for i in range(len(ehstrmag)):
		if ehstrmag[i] < 3.5 or ehstrmag[i] > 6.5:
			ehstrmag[i] = np.nan
			ehstcolour[i] = np.nan
			
		#elif hstcolour[i] < mscollow or hstcolour[i] > mscolhigh:
			#hstrmag[i] = np.nan
			#hstcolour[i] = np.nan
	wfinal_mass = []
	efinal_mass = []
	
	
	
	for i in range(len(whstrmag)):
		wdisp_list = []
		for j in range(len(isormag)):
			
			wxdist = whstcolour[i] - isocolour[j]
			wydist = whstrmag[i] - isormag[j]
			if wydist ==np.nan or wxdist == np.nan:
				wdisp = 100000000
			else:
				wdisp = np.sqrt((wxdist**2 + wydist**2))
			wdisp_list.append(wdisp)
		
		wfinal_mass.append(isomass[np.argmin(wdisp_list)])
	
	for i in range(len(ehstrmag)):
		edisp_list = []
		for j in range(len(isormag)):
			
			exdist = ehstcolour[i] - isocolour[j]
			eydist = ehstrmag[i] - isormag[j]
			if eydist ==np.nan or exdist == np.nan:
				edisp = 100000000
			else:
				edisp = np.sqrt((exdist**2 + eydist**2))
			edisp_list.append(edisp)
		
		efinal_mass.append(isomass[np.argmin(edisp_list)])


	wfindist_list = []
	efindist_list = []
	wcentrex = 2174
	wcentrey = 4129
	ecentrex = 2173
	ecentrey = 4130
	for i in range(len(whstxpix)):
		wxfdist = wcentrex - whstxpix[i]
		wyfdist = wcentrey - whstypix[i]
		wfindist = np.sqrt(wxfdist**2 + wyfdist**2)
		wfindist_list.append(wfindist)
		
	for i in range(len(ehstxpix)):
		exfdist = ecentrex - ehstxpix[i]
		eyfdist = ecentrey - ehstypix[i]
		efindist = np.sqrt(exfdist**2 + eyfdist**2)
		efindist_list.append(efindist)
		
	wfindist_list = np.array(wfindist_list)
	efindist_list = np.array(efindist_list)
	wfinal_mass = np.array(wfinal_mass)
	efinal_mass = np.array(efinal_mass)
	
	findist_list = np.concatenate((wfindist_list,efindist_list),axis = 0)
	final_mass = np.concatenate((wfinal_mass,efinal_mass),axis = 0)
		
	for i in range(len(final_mass)):
		if final_mass[i] < 0.2:
			final_mass[i] = np.nan
			findist_list[i] = np.nan
	highmass = []
	lowmass = []
	for i in range(len(findist_list)):
		if 0.59<final_mass[i]<0.66:
			lowmass.append(findist_list[i])
		elif 0.69<final_mass[i]<0.76:
			highmass.append(findist_list[i])
	#plt.figure(1)
	plt.hist(lowmass,3000,cumulative = True,histtype='step',label = '0.6-0.65 solar masses')
	plt.hist(highmass,3000,cumulative = True,histtype='step',label = '0.7-0.75 solar masses')
	plt.ylabel('Number of stars in Mass Range')
	plt.xlabel('Distance from Galactic Center(pixels)')
	plt.title('HorII')
	plt.legend(loc=2)
	plt.show()
	#plt.figure(2)
	#plt.scatter(findist_list,final_mass)
	#plt.xlabel('Distance from Galatic centre(pixels)')
	#plt.ylabel('Mass, in Solar Masses')
	#plt.title('Hori')
	#plt.show()
	

def main():
	
	#hori_isoplot()
	#horii_isoplot()
	#plt.show()
	#circles = circlegenerator(300,1000)
	#regionplot(circles)
	#x = data[0]
	#y = data[1]
	hori_plot()
	#horii_plot()
	#hori_short_plot()
	#hori_dartiso('dm_13.5_0_-2.4.txt',13.5,0,-2.4)
	#hori_dartiso('dm_13.5_0.2_-2.4.txt',13.5,0.2,-2.4)
	#hori_dartiso('dm_13.5_0.4_-2.4.txt',13.5,0.4,-2.4)
	#hori_dartiso('dm_13.5_0.6_-2.4.txt',13.5,0.6,-2.4)
	#hori_dartiso('dm_13.5_0_-2.0.txt',13.5,0,-2.0)
	#hori_dartiso('dm_13.5_0.2_-2.0.txt',13.5,0.2,-2.0)
	hori_dartiso('dm_13.5_0.4_-2.0.txt',13.5,0.4,-2.0)
	#the one above is the best one for both ufds!!!
	#hori_dartiso('dm_13.5_0.6_-2.0.txt',13.5,0.6,-2.0)
	#hori_dartiso('dm_13.0_0_-2.4.txt',13.0,0,-2.4)
	#hori_dartiso('dm_13.0_0.2_-2.4.txt',13.0,0.2,-2.4)
	#hori_dartiso('dm_13.0_0.4_-2.4.txt',13.0,0.4,-2.4)
	#hori_dartiso('dm_13.0_0.6_-2.4.txt',13.0,0.6,-2.4)
	#hori_dartiso('dm_13.0_0_-2.0.txt',13.0,0,-2.0)
	#hori_dartiso('dm_13.0_0.2_-2.0.txt',13.0,0.2,-2.0)
	#hori_dartiso('dm_13.0_0.4_-2.0.txt',13.0,0.4,-2.0)
	#hori_dartiso('dm_13_0.6_-2.0.txt',13.0,0.6,-2.0)
	#hori_dartiso('dm_13.5_0_-2.2.txt',13.5,0,-2.2)
	#hori_dartiso('dm_13.5_0_-2.0.txt',13.5,0,-2.0)
	#hori_dartiso('dm_13.7_0.2_-2.4.txt',13.7,0.2,-2.4)
	#hori_dartiso('dm_14_0.4_-2.0.txt',14,0.4,-2.0)
	#hori_dartiso('dm_13.5_0_-1.5.txt',13,0,-1.5)
	#hori_alphaplot()
	#plt.gca().invert_yaxis()
	#plt.legend()
	plt.xlim(-0.3,1.16)
	plt.ylim(7.5,-0.6)
	plt.show()
	
	#plt.rc('axes',labelsize = 20)
	#massseghori_plot('hori','dm_13.5_0.4_-2.0.txt',7.1,-0.2,0.86,0.36)
	#massseghorii_plot('horii','dm_13.5_0.4_-2.0.txt',7.1,-0.2,0.86,0.36)
	#plotrad(x,y)
	
	 

main()

#read in isochrones and hubble data
#also need x and y cordinates
#then assign masses based on nearest isochrone stars in colour space
#plot masses against distance from galactic center
#mass segregation, yay or nay?
