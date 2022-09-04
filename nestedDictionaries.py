# Problem 1
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

x[1] = [15, 8, 9] # 1a. 
students[0]['lastname'] = 'Bryant' #1b.
sports_directory['soccer'][0] = 'Andres' #1c.
z[0]['y'] = 30 #1d.

print(x)
print(students[0])
print(sports_directory['soccer'])
print(z)

#Problem 2
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(list):
    for studentList in range(0, len(list)):
        output = ''
        for key, val in list[studentList].items():
            output += f" {key} - {val}"
        print(output)

iterateDictionary(students)

#Problem 3
def iterateDictionary2(name, students):
    for studentList in range(0, len(students)):
        for key, val in students[studentList].items():
            if key == name:
                print(val)

iterateDictionary2('first_name' , students)
iterateDictionary2('last_name', students)

#Problem 4
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(places):
    for key, val in places.items():
        print("----------")
        print(f"{len(val)} {key}")
        for g in range(0, len(val)):
            print(val[g])

printInfo(dojo)
