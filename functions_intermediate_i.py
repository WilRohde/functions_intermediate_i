x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

print(x[1][0])
x[1][0] = 15
print(x)

print(students[0])
students[0]['last_name'] = "Bryant"
print(students[0])

print(sports_directory['soccer'])
sports_directory['soccer'][0] = "Andres"
print(sports_directory['soccer'])

print(z[0])
z[0]['y']=30
print(z)

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(items):
    for x in range(0,len(items),1):
        outstr = ""
        for key, val in students[x].items():
            #outstr = outstr + key + '-' + val
            outstr = f"{key} - {val}"
            print(outstr)
        # print(outstr)

iterateDictionary(students)

def iterateDictionary2(KeyName, SomeList):
    SomeValue = ""
    print(len(SomeList))
    for x in range(0,len(SomeList),1):
        SomeValue = SomeList[x].get(KeyName)
        print(KeyName + " - " + SomeValue)

iterateDictionary2('first_name',students)

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(someDict):
    listLen = 0
    listName = ""
    aList = []
    for listName, aList in someDict.items():
        print(f"{len(aList)} {listName}")
        for y in range(0,len(aList),1):
            print(aList[y])

printInfo(dojo)
