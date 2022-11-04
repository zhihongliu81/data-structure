def findMedianSortedArrays(nums1, nums2):
        mid = (len(nums1) + len(nums2) - 1) // 2
        if len(nums1) == 0 and len(nums2) == 0:
            return 0
        if len(nums1) == 0:
            if len(nums2) % 2 == 0:
                return (nums2[mid + 1] + nums2[mid]) / 2
            else:
                return nums2[mid]
        if len(nums2) == 0:
            if len(nums1) % 2 == 0:
                return (nums1[mid + 1] + nums1[mid]) / 2
            else:
                return nums1[mid]

        left_part_num = mid + 1     # when len(nums1) + len(nums2) is odd, left part has one more number

        if len(nums1) > len(nums2):
            temp = nums2
            nums2 = nums1
            nums1 = temp

        low, high = 0, len(nums1)
        middle = (low + high) // 2
        while high >= low:

            left_part1 = nums1[0:middle]
            left_part2 = nums2[0:left_part_num - len(left_part1)]
            right_part1 = nums1[middle:]
            right_part2 = nums2[left_part_num - len(left_part1):]

            left1 = left_part1[-1] if len(left_part1) > 0 else float('-inf')
            right1 = right_part1[0] if len(right_part1) > 0 else float('inf')
            left2 = left_part2[-1] if len(left_part2) > 0 else float('-inf')
            right2 = right_part2[0] if len(right_part2) > 0 else float('inf')

            if right1 >= left2 and right2 >= left1:
                if (len(nums1) + len(nums2)) % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2
                else:
                    return max(left1, left2)

            elif left1 > right2:
                high = middle - 1
                middle = (low + high) // 2

            elif right1 < left2:
                low = middle + 1
                middle = (low + high) // 2
