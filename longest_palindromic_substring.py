def longestPalindrome(s: str) -> str:

        if len(s) < 2:
            return s

        s = "|" + "|".join(list(s)) + "|"
        longest = ''
        radiuses = [0 for _ in range(len(s))]
        center = 0
        longest_center = longest_radius = 0

        while center < len(s):
            radius = 0
            while (center - radius - 1 >= 0 and
                    center + radius + 1 < len(s) and
                    s[center - radius - 1] == s[center + radius + 1]):
                radius += 1
            radiuses[center] = radius

            # sub_string = s[center - radius: center + radius + 1]
            # res = "".join(sub_string.split(sep="|"))
            # if len(res) > len(longest):
            #     longest = res
            if radius > longest_radius:
                longest_radius = radius
                longest_center = center

            old_center = center
            old_radius = radius
            center += 1

            max_index = old_center + old_radius
            while center <= max_index:
                mirror_center = old_center * 2 - center
                mirror_radius = radiuses[mirror_center]
                if center + mirror_radius < max_index:
                    radiuses[center] = radiuses[mirror_center]
                    center += 1
                elif center + mirror_radius > max_index:
                    radiuses[center] = max_index - center
                    center += 1
                else:
                    radius = max_index - center
                    break

        # longest_radius = radiuses[0]
        # sub_string = ""
        # for i in range(len(radiuses)):
        #     if  radiuses[i] > longest_radius:
        #         longest_radius = radiuses[i]
        #         sub_string = s[i - radiuses[i]: i + radiuses[i] + 1]

        # print(radiuses)
        sub_string = s[longest_center - longest_radius: longest_center + longest_radius + 1]
        longest = "".join(sub_string.split(sep="|"))
        return longest


s1 = "babad"
s2 = "cbbd"
s3= "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee"
s4 = "aaabaaaa"

print(longestPalindrome(s1))
print(longestPalindrome(s2))
print(longestPalindrome(s3))
print(longestPalindrome(s4))
