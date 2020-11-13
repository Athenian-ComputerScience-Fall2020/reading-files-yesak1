# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#


# Read temps.txt and print it without the blank line at the end

with open ('temps.txt') as file_object:
    contents = file_object.read()
print(contents.rstrip())

# Read temps.txt line by line and print with no whitespace
with open ('temps.txt') as file_object:
    for line in file_object:
        print(line.rstrip())


# Make a list of lines from the file
with open ('temps.txt') as file_object:
    line_list = file_object.readlines()
print(line_list)


# Edit the elements to eliminate whitespace in the list
with open ('temps.txt') as file_object:
    line_list = file_object.readlines()

list_length = len(line_list)
for i in range(list_length):
    line_list[i] = line_list[i].rstrip()
print(line_list)


def avg_temp():
    with open('temps.txt') as file_object:
        line_list = file_object.readlines()
        list_length = len(line_list)
        sum_list = 0
    for i in range(1, list_length):
        line_list[i] = line_list[i].rstrip()
        sum_list = int(line_list[i])+sum_list
    print(sum_list)
    average_list = sum_list/(list_length-1)
    average_list = round(average_list, 2)

    return average_list


if __name__ == '__main__':
    print(avg_temp())

