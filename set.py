#set

students = {"cap","iron","thor","black","ant","spider"}
print(students)

#set default function
#check is there or not
print ("panther" in students)

#add()
students.add("marvel")
print(students)

#update
students.update(["groot","wanda"])
print(students)

#len
print(len(students))

#remove #discard #pop
students.remove("groot")
print(students)

#clear
students.clear()
print(students)

#union
teach = {"Marvel studio","Stann Lee"}
students = {"cap","iron","thor","black","ant","spider"}

movie = students.union(teach)
print(movie)