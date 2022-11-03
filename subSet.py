def subSet(arr):
      # [1,2,3] -> [], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1,2,3]

      if len(arr) == 0:
            return [[]]

      if len(arr) == 1:
            return [[], arr]

      last = arr.pop()
      rest_subset = subSet(arr)
      subset_with_last = []
      for ele in rest_subset:
            new_set = [*ele]
            new_set.append(last)
            subset_with_last.append(new_set)

      return rest_subset + subset_with_last

print(subSet([1,2,3,4]))
