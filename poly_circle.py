import turtle
bob = turtle.Turtle()
print(bob)

for i in range(10000000):
    bob.fd(100/(i+1))
    bob.lt(90/(i+1))

turtle.mainloop()
