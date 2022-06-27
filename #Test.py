#Test

#if statement
testx = input('go on: ')

print("Not old enough") if ( int(testx) > 1 and int(testx) < 18 ) else print("You're perfect") 
#ternary condition

#loop statement with range
#for index in range(0, 10, 2): #range(start, stop, step) | range(n) =default(increases by 1)
   # print(index)

sum = 10 #Using Python for loop to calculate the sum of a sequence
for tux in range(10):
    sum += tux
print(sum)

fu = 0
max = 10 #while loop
while fu < max:   
    #print('works')
    fu += 1

# while statement to build a simple command prompt program
    command = ''

while command.lower() != 'quit':
    command = input('>')
    #print(f"Echo: {command}")
#breaking a loop
fun = 2 
for fun in range(13):
    pass
    if (fun == 4):
        break
    #When you use the break statement in a nested loop, it’ll terminate the innermost loop. For example:
for x in range(5):
    for y in range(5):
        # terminate the innermost loop
        if y == 1:
            continue #skips the current iteration if conditon is true
        if y > 2:
            break

        # show coordinates on the screen
        pass#print(f"({x},{y})") 
  #Use the Python break statement to terminate a for loop or a while loop prematurely.
        
for index in range(10):
    if index % 3:
        continue
    #print(index)

j = 0
while j < 5: #continue/pass example
    j += 1
    if not j % 2:
        pass #used as placeholder for code that'll be written later
    pass#print(j) tried