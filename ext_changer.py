import os,sys
folder = 'E:/'
for filename in os.listdir(folder):
    file = os.path.join(folder,filename)
    new = file.replace('.mp4','.m4a')
    output = os.rename(file,new)
