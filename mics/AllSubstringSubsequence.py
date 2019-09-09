def AllSubstring(s):
  result = []
  temp = ''
  for start in range(len(s)):
    for end in range(start, len(s)):
      for i in range(start, end + 1):
        temp = temp + s[i]
      result.append(temp)
      temp = ''
  return result

def AllSubsequence(s):
  result = set()
  for start in range(len(s)):
    for end in range(start, len(s)):
      for i in range(start, end + 1):
        # exclude the ith char
        left = s[start:i]
        right = s[i+1:end+1]
        temp = left + right
        result.add(temp)
  result.add(s)
  return result

print(AllSubstring('abcd'))
print(AllSubsequence('abcd'))