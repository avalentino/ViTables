"This creates an HDF5 file with a potentially large number of objects"

import sys
import numpy
import tables

filename = 'large_number_of_objects.h5'

# Open a new empty HDF5 file
fileh = tables.openFile(filename, mode = "w")

# nlevels -- Number of levels in hierarchy
# ngroups -- Number of groups on each level
# ndatasets -- Number of arrays on each group
# LR: Low ratio groups/datasets
#nlevels, ngroups, ndatasets = (3, 1, 1000)
# MR: Medium ratio groups/datasets
nlevels, ngroups, ndatasets = (3, 10, 100)
# HR: High ratio groups/datasets
#nlevels, ngroups, ndatasets = (30, 10, 10)

# Create an Array to save on disk
a = numpy.array([-1, 2, 4], dtype=numpy.int16)

group = fileh.root
group2 = fileh.root
for k in range(nlevels):
    for j in range(ngroups):
        for i in range(ndatasets):
            # Save the array on the HDF5 file
            fileh.createArray(group2, 'array'+str(i), a, "Signed short array")
        # Create a new group
        group2 = fileh.createGroup(group, 'group'+str(j))
    # Create a new group
    group3 = fileh.createGroup(group, 'ngroup'+str(k))
    # Iterate over this new group (group3)
    group = group3
    group2 = group3

fileh.close()

