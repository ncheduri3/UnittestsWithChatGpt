def pascal_triangle(n):
    triangle = []
    
    for i in range(n):
        row = []
        
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                prev_row = triangle[i - 1]
                num = prev_row[j - 1] + prev_row[j]
                row.append(num)
        
        triangle.append(row)
    
    return triangle
