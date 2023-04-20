import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt

image_data = nib.load('FLAIR (1).nii.gz')
image = image_data.get_fdata()

x = 1
y = 1
z = 1

tol = 3
valor_medio_cluster = image[x, y, z]
segmentationRegion = np.zeros_like(image)

for dx in [-1, 0, 1] :
  for dy in [-1, 0, 1] :
    for dz in [-1, 0, 1] :
      if np.abs(valor_medio_cluster - image[x+dx, y+dy, z+dz]) < tol :
        segmentationRegion[x+dx, y+dy, z+dz] = 1
      else :
        segmentationRegion[x+dx, y+dy, z+dz] = 0
  
valor_medio_cluster = image[segmentationRegion == 1].mean()

# x = 1
# y = 1
# z = 1

# tol = 3
# valor_medio_cluster = image[x, y, z]
# segmentationRegion = np.zeros_like(image)

# def within_boundaries(coord, shape):
#   return all(0 <= c < s for c, s in zip(coord, shape))

# def add_neighbors(coord):
#   for dx in [-1, 0, 1]:
#     for dy in [-1, 0, 1]:
#       for dz in [-1, 0, 1]:
#         neighbor = (coord[0] + dx, coord[1] + dy, coord[2] + dz)
#       if within_boundaries(neighbor, image.shape) and not segmentationRegion[neighbor]:
#         if np.abs(valor_medio_cluster - image[neighbor]) < tol:
#           segmentationRegion[neighbor] = 1
#           add_neighbors(neighbor)

# valor_medio_cluster = image[segmentationRegion == 1].mean()
# print("Mean value of the cluster:", valor_medio_cluster)