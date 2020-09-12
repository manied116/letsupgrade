#dictionary
car = {
  "brand": "Benz",
  "model": "Mercedez",
  "year": 1970
}
print(car)

#dict default methods

#get
print(car.get("brand"))

#keys
print(car.keys())

#items
print(car.items())

#pop
car.pop("model")
print(car)