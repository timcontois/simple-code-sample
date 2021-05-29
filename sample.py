def min_absolute_diff_naive(x, y):
  min_absolute_diff = float('inf')
  for x_elem in x:
    for y_elem in y:
      absolute_diff = abs(x_elem - y_elem)
      if absolute_diff < min_absolute_diff:
        min_absolute_diff = absolute_diff
  return min_absolute_diff

def min_absolute_diff_improved(x, y):
  min_absolute_diff = float('inf')
  x.sort() # [0, 5, 8, 1000]
  y.sort() # [7, 10, 40, 80]
  i = 0
  j = 0
  while i < len(x) and j < len(y):
    absolute_diff = abs(x[i] - y[j])
    if absolute_diff < min_absolute_diff:
      min_absolute_diff = absolute_diff
    if min_absolute_diff == 0:
      break # min_absolute_diff can't be less than 0, no need to keep checking
    if x[i] > y[j]:
      # x is sorted, so if x[i] > y[j] checking x[i+1] with y[j] is unnecessary
      j += 1
    else:
      i += 1
  return min_absolute_diff

if __name__ == '__main__':
  x = [5, 0, 1000, 8] 
  y = [40, 7, 10, 80]
  print(min_absolute_diff_naive(x, y))
  print(min_absolute_diff_improved(x, y))