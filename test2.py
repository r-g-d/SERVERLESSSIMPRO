from optpack import containerMappedPM
cnt = 0
for i in range(6):
   for j in range(119):
      cnt+=containerMappedPM[i][j]
print(cnt)