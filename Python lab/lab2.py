def Convert(tup, di):
    for a, b in tup:
        di.setdefault(a, []).append(b)
    return di

# count = input("\nEnter number of tuples to be enterted\t-")
# noTup = int(count)


# for i in range(noTup):
#     name = input("\nEnter the name\t-")
#     subject = input("\nEnter the subject\t-")
#     marks = input("\nEnter the marks\t-")
#     tp = (name, (subject), int(marks))
#     lt.append(tp)


lt = []
tp1 = ('John', ('Physics', 80))
tp2 = ('Daniel', ('Science', 90))
tp3 = ('John', ('Chemistry', 60))
tp4 = ('Mark',('Maths',100))
tp5 = ('Daniel',('History',75))
tp6 = ('Mark',('Social', 95))


lt1 = [tp1,tp2,tp3,tp4,tp5,tp6]

print("Tuple Form - {lt1}")

dictionary = {}
dict1 = Convert(lt1,dictionary)