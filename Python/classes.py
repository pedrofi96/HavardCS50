class Point():
  def __init__(self, x, y):
    self.x= x
    self.y= y

p = Point(10, 15)

print(p.x)
print(p.y)

class Flight():
  def __init__(self, capacity):
    self.capacity = capacity
    self.passengers = []

  def add_passenger(self, name):
    if not self.open_seats():
      return False
    self.passengers.append(name)
    return True
  
  def open_seats(self):
    return self.capacity - len(self.passengers)

flight = Flight(3)

people = ["gringo Viado", "Arthur", "Pedro", "Pera"]
for person in people:
  sucess = flight.add_passenger(person)
  if sucess:
    print(f"Added {person} to flight sucessfully.")
  else:
    print(f"No availeble seats for {person}")
