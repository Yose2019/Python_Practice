# this craft teaches to use the zip function 

names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

for name, score in zip(names, scores, strict = True):
    print(f"{name} scored {score}")