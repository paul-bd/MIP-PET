# MIP-PET (maximum intensity projection for positon emission tomography)
create Maximum Intensity Projection from nii


#Usage : 
import gif_mip

gif_mip.create_mipGIF_from_3D(img,nb_image=40,duration=0.1,is_mask=False,borne_max=None)

#Notes : 
 -image in nibabel format
 -nb_image= the number of image ~angle of rotation (360/nb_image)
 -duration=0.1 
 -is_mask=False
 -borne_max= define the vmax (for PET activity ~15000)
