import numpy as np
import matplotlib.pyplot as plt
from astropy import wcs

def apparent_stars(star_catalog_name):
    
    star_catalog = np.genfromtxt('%s.csv' %star_catalog_name, delimiter=',')    
    
    stars_id = star_catalog[:,0][1::]
    stars_ra = star_catalog[:,1][1::]
    stars_dec = star_catalog[:,2][1::]
    stars_mag = star_catalog[:,3][1::]
    return stars_id, stars_ra, stars_dec, stars_mag



stars_id, stars_ra, stars_dec, stars_mag = apparent_stars('HIP_mag6')



width = 200
height = 200


wcs2 = wcs.WCS(naxis=2)
wcs2.wcs.crpix = [width/2.0, height/2.0]
wcs2.wcs.crval = [0, 89.99]
#wcs2.wcs.cdelt =init_wcs.wcs.cdelt
wcs2.wcs.cdelt = [-1.0, 1.0]
wcs2.wcs.ctype = ["RA---ARC", "DEC--ARC"]




stars_temp_x, stars_temp_y = wcs2.all_world2pix(stars_ra, stars_dec, 0, 
    maxiter=20, tolerance=1.0e-4, adaptive=True, detect_divergence=False, quiet=True)



stars_ixym = [(id01, i2, j2, m2) for (id01, i2, j2, m2) in zip(stars_id, stars_temp_x, stars_temp_y, stars_mag)
	if i2>0 and i2<width
	and j2>0 and j2<height]
stars_ids, stars_x, stars_y, stars_mags = zip(*stars_ixym)



# Work on Size of Alpha values of the Stars with their magnitude 
#print(list(stars_mags))
#stars_mags_new = [np.max(stars_mags)-(np.min(stars_mags)+x)-1 for x in list(stars_mags)]
stars_mags_new = []
for i3 in list(stars_mags):
    if i3 <= 0:
        stars_mags_new.append(7)
    elif i3<=1:
        stars_mags_new.append(6)
    elif i3<=2:
        stars_mags_new.append(5)
    elif i3<=3:
        stars_mags_new.append(4)
    elif i3<=4:
        stars_mags_new.append(3)
    elif i3<=5:
        stars_mags_new.append(2)
    else:
        stars_mags_new.append(1)


fig = plt.figure()
ax = fig.add_subplot()
#plt.subplot()#projection=wcs2)
ax.scatter(stars_x, stars_y, s=stars_mags_new, alpha=1.0, color=(0.8, 0.8, 0.8), edgecolors='none')

#ax = plt.gca()
ax.set_facecolor((0.0, 0.0, 0.2))
#plt.grid()#color='white', ls='solid')
ax.set_aspect('equal', adjustable='box')
#ax.axis('equal')
#ax.set_xlim(xmin=0.0, xmax=100)
ax.set_xlim(0, 200)
ax.set_ylim(0, 200)
ax.get_xaxis().set_ticks([])
ax.get_yaxis().set_ticks([])
#ax.aspect('equal', 'datalim')
#ax.margins(0.1)
plt.savefig('test.png', pad_inches=0.0, bbox_inches='tight', dpi=2000)
plt.show()
