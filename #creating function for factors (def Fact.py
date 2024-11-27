#creating function for factors (def Factors)
def Factors(n):
  factors = []
  for i in range(2,(n//2)+1):
    if n%i == 0:
      factors.append(i)
  factors.append(n) # we have done this because number is factor of itself
  return factors

# know create function where we check if the factore is square free or not
def IsSquareFree(n):
  SquareFree = True
  for i in Factors(n):
    if (i**0.5).is_integer():
      SquareFree = False
      break
  return SquareFree

n = int(input("Enter a number : "))
factors = Factors(n)

# count loop is created to count how many square free factors are there
count = 0
for k in factors:
  if IsSquareFree(k):
    count+=1

print(count)