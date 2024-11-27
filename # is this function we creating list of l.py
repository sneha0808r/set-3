# is this function we creating list of lists which length is equal to k.
def sublists(arr, k):
    result = []
    for i in range(len(arr) - k + 1):
        sublist = arr[i:i+k]
        result.append(sublist)
    return result
# here in this function we are finding the max value from an list(array).
def FindMax(l):
  Max=l[0]
  for i in range(len(l)):
    if Max<l[i]:
      Max = l[i]
  return Max

arr = [1, 2, 3, 4, 5, 6, 7, 8]
k = int(input("Enter K : "))
print(sublists(arr, k))
data = sublists(arr, k)

# when we use this for loop it means that i will take [1,2,3].... as an element from data
Maximums = []
for i in data:
  max = FindMax(i)
  Maximums.append(max)
print(f"Maximums From each list of kth length : {Maximums}")