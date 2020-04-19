import os
#makes the list of files in the directory, appends new lines to the file

#list of the files in the folder
arr = os.listdir()
fh = open("descriptions.txt","r+")
file_arr = list()

for line in fh:
    # if line.startswith('#'): continue
    file_arr.append(line.rstrip())
# print(file_arr)
# print(arr)
for entry in arr:
    if entry.startswith('.'): continue
    if entry not in file_arr:
        fh.write(f"{entry} \n")
        # print(entry)


# for name in arr:
#     #doesn't list hidden files
#     if name[0] != '.': fh.write(f"{name} \n")
fh.close()