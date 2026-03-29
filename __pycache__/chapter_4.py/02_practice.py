marks = []
for i in range(6):
    a = int(input(f"enter marks of student {i+1}:"))
    marks.append(a)
print(f"marks of student: {marks}")
marks.sort()
print(f"sorted marks: {marks}")