def linear_search(ar, target):
  for i in range(len(ar)):
    element = ar[i]
    if element == target:
      return i
  return None

print(linear_search([10, 40, 93, -5, 7, 32], -5))
print(linear_search([40, 93, 82], 100))
