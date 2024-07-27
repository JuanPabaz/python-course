numbers = {1:"uno",2:"dos",3:"tres"}
print(numbers)
print(numbers.get(1))
information = {"nombre":"Juan pablo", "apellido":"Giraldo", "edad":20}
print(information)
print(information.get("nombre"))
keys = information.keys()
print(keys)
print(type(keys))
values = information.values()
print(values)
pairs = information.items()
print(pairs)
contacts = {"Juan pablo":
            {"apellido":"Giraldo", "edad":20},
            "Carolina:":{
                "apellido":"Hernandez","edad":19
            }}
print(contacts)