### A COPIER POUR IMPORTER LES FONCTIONS
#import sys
#sys.path
#sys.path.append('/Users/Paul/Documents/soft/Python/my_func/')
#import my_functions_python
#
#
#

import os
import nibabel as nib
import numpy as np
import SimpleITK as sitk
import nilearn
import shutil
import glob
import matplotlib.pylab as plt
import imageio
import datetime
import numpy as np
import scipy
from scipy import ndimage



#### Create MIP GIF
def create_gif(filenames, duration):
    images = []
    for filename in filenames:
        images.append(imageio.imread(filename))
    output_file = 'Gif-%s.gif' % datetime.datetime.now().strftime('%Y-%M-%d-%H-%M-%S')
    imageio.mimsave(output_file, images, duration=duration)


def create_mipGIF_from_3D(img,nb_image=40,duration=0.1,is_mask=False,borne_max=None):
    ls_mip=[]
    while len(img.shape)>3:
        img=nib.squeeze_image(img)
    img_data=img.get_data()
    img_data+=1e-5
    
    for angle in np.linspace(0,360,nb_image):
        ls_slice=[]
        for i in range(img_data.shape[-1]):
            ls_slice.append(scipy.ndimage.interpolation.rotate(img_data[:,:,i],angle))
        vol_angle=np.stack(ls_slice,axis=-1)
        MIP=np.amax(vol_angle,axis=1)
        MIP[MIP<2*1e-5]=0
        MIP=np.flipud(MIP.T)
        ls_mip.append(MIP)
    try:
        shutil.rmtree('test_gif/')
    except:
        pass
    os.mkdir('test_gif/')

ls_image=[]
for mip,i in zip(ls_mip,range(len(ls_mip))):
    fig,ax=plt.subplots()
    ax.set_axis_off()
    if borne_max is None:
        if is_mask==True:
            borne_max=1
            else:
                borne_max=15000
    plt.imshow(mip,cmap='Greys',vmax=borne_max)
        fig.savefig('test_gif/MIP'+'%04d' % (i)+'.png')
        plt.close(fig)

filenames=glob.glob('test_gif/*.png')

create_gif(filenames, duration)
try:
    shutil.rmtree('test_gif/')
    except:
        pass

