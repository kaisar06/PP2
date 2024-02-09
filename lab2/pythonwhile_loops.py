#it will print i until i less 6
i = 1
while i < 6:
  print(i)
  i += 1

#break will stop iterating even if if is true
  i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#With the continue statement we can stop the current iteration, and continue with the next:
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

