#杨辉三角
def generate(num_rows):
    triangle = []
    for i in range(num_rows):
        row = [None for _ in range(i+1)]
        row[0], row[-1] = 1, 1
        for j in range(1, len(row) - 1):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    return triangle

print(generate(5))
