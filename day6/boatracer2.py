options = 0
record = 333163512891532
time = 53837288
for i in range(1, time):
    if i * (time - i) > record:
        options += 1

print(options)