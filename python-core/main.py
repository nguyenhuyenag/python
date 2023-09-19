A = [1,2,3] # =>    [1,2,3,4] hoặc [1,2,3,""]

B = []

result = A + ([4] if B else [''])

print(result)