people = [
  {"Name":"harry" , "House":"Grifinoria" },
  {"Name":"pera" , "House":"Grifinoria" },
  {"Name":"Ablubleh" , "House":"zluezao" }
]

def f(person):
  return person["Name"]


people.sort(key=f)

print(people)

def d(casa):
  return casa["House"]

people.sort(key=d)

print(people)

people.sort(key = lambda person: person["Name"])

print(people)