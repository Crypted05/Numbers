fibonacci = [1, 1]
end = int(input("How manny times will we run the fibonacci sequence?: "))

for i in range(end):
    new = fibonacci[i] + fibonacci[i + 1]
    fibonacci.append(new)

print(fibonacci)
