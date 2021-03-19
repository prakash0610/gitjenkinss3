total=0
grade_counter=0
grades=[98,77,54,34,24,87,85,76,87,98]

for grade in grades:
    total += grade
    grade_counter +=1
average =total/grade_counter
print(f"Class average grade is ", average)
