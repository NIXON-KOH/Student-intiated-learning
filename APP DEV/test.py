import os
 
os.chdir("/Users/Nixon Koh/Desktop/DEV_1/Assets")
print(os.getcwd())
 
for count,f in enumerate(os.listdir()):
    f_name, f_ext = os.path.splitext(f)
    f_name = f[:-6]
 
    new_name = f'{f_name}{f_ext}'
    os.rename(f, new_name)