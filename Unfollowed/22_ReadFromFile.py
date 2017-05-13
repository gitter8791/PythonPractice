'''
Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file, and print out
the results to the screen. I have a .txt file for you, if you want to use it!
'''
names_list = []

with open('nameslist.txt', 'r') as open_file:
    for single_line in open_file.readlines():
        if single_line.strip() not in names_list:
            names_list.append(single_line.strip())

print(len(names_list))
