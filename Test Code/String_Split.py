my_file = open("test.txt", "r")

content = my_file.read()

print(content)

content_list = content.split(" ")

my_file.close()

print(content_list)