import moment

x = moment.now()
print(x)

# x = moment.now().strftime("%H-%M-%S_%d-%m-%Y")
x = moment.now().strftime("%Y-%m-%d - %H:%M:%S")
print(x)