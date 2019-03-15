Python = []
Web = []


count1 = raw_input("\nEnter number of Students in Python\t-")
studentPython = int(count1)

print("Enter the Student names in Pyhton Class-")
for i in range(studentPython):
    name = raw_input("\n")
    Python.append(name)

count2 = raw_input("\nEnter number of Students in Web\t-")
studentWeb = int(count2)

print("Enter the Student names in Web Class-")
for i in range(studentWeb):
    name = raw_input("\n")
    Web.append(name)

#print(myList)

set1 = set(Python)
set2 = set(Web)
common = set1.intersection(set2)
union = set1.union(set2)

notCommon = union - common

print("Common students- {0}".format(common))
print("Students who attend only one class - {0}".format(notCommon))