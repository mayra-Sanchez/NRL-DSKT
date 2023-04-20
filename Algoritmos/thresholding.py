import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt

image_data = nib.load('FLAIR (1).nii.gz')
image = image_data.get_fdata()

tol = 1
tau = 150
while True:
  print(tau)

  segmentationThresholding = image >= tau
  mBG = image[np.multiply(image > 10, segmentationThresholding == 0)].mean()
  mFG = image[np.multiply(image > 10, segmentationThresholding == 1)].mean()

  tau_post = 0.5 * (mBG + mFG)

  if np.abs(tau - tau_post) < tol:
    break
  else:
    tau = tau_post

# plt.imshow(segmentationThresholding[:, :, 24])