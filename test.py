from rectpack import newPacker,PackingMode

rectangles = [(100, 30), (40, 60), (30, 30),(70, 70), (100, 50), (30, 30)]
bins = [(300, 450), (80, 40), (200, 150)]

packer = newPacker(mode=PackingMode.Offline)

# Add the rectangles to packing queue
for r in rectangles:
	packer.add_rect(*r)

# Add the bins where the rectangles will be placed
for b in bins:
	packer.add_bin(*b)

# Start packing
packer.pack()
# Obtain number of bins used for packing
nbins = len(packer)

# Index first bin
abin = packer[0]

# Bin dimmensions (bins can be reordered during packing)
width, height = abin.width, abin.height

# Number of rectangles packed into first bin
nrect = len(packer[0])

# Second bin first rectangle
rect = packer[0][0]

# rect is a Rectangle object
x = rect.x # rectangle bottom-left x coordinate
y = rect.y # rectangle bottom-left y coordinate
w = rect.width
h = rect.height
for abin in packer:
  print(abin.bid) # Bin id if it has one
  for rect in abin:
    print(rect)

# import numpy as np
# A=np.array([[1,5],[3,7]])
# B=np.array([[2,-1],[4,2]])
# print(np.einsum('ij, ji ->', A,B))