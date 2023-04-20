import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt

image_data = nib.load('FLAIR (1).nii.gz')
image = image_data.get_fdata()

tol = 1
tau = 150
k1 = np.amin(image)
k2 = np.mean(image)
k3 = np.amax(image)
print(k1, k2, k3)

for i in range(0,3):
  d1 = np.abs(k1 - image)
  d2 = np.abs(k2 - image)
  d3 = np.abs(k3 - image)

  segmentationCluster = np.zeros_like(image)
  segmentationCluster[np.multiply(d1 < d2, d1 < d3)] = 0
  segmentationCluster[np.multiply(d2 < d1, d2 < d3)] = 1
  segmentationCluster[np.multiply(d3 < d1, d3 < d2)] = 2

  k1 = image[segmentationCluster == 0].mean()
  k2 = image[segmentationCluster == 1].mean()
  k3 = image[segmentationCluster == 2].mean()

  print(k1,k2,k3)

# plt.imshow(segmentationCluster[:, :, 24])