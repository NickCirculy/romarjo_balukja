dataInput = [
    {
        "L": 3,
        "P": 2,
        "C": [
            2,
            1,
            1,
            0,
            1
        ]
    },
    {
        "L": 2,
        "P": 2,
        "C": [
            2,
            0,
            2,
            0
        ]
    }
]

case0 = 0
case1 = 1
case2 = 2

completeMatrices = []

for el in dataInput:
    matrix = el['C']
    L = el['L']
    P = el['P']
    convertedMatrix1 = []
    convertedMatrix2 = []
    sum1 = 0
    sum2 = 0

    for el1 in matrix:
        if el1 == 2:
            convertedMatrix1.append(1)
            convertedMatrix2.append(1)
            sum1 += 1
            sum2 += 1
        elif el1 == 1:
            if sum1 <= sum2:
                convertedMatrix1.append(1)
                convertedMatrix2.append(0)
                sum1 += 1
                sum2 += 0
            else:
                convertedMatrix1.append(0)
                convertedMatrix2.append(1)
                sum1 += 0
                sum2 += 1
        else:
            convertedMatrix1.append(0)
            convertedMatrix2.append(0)
            sum1 += 0
            sum2 += 0

    isValid = sum1 == L | sum2 == P
    if isValid:
        completeMatrices.append([convertedMatrix1, convertedMatrix2])
    else:
        completeMatrices.append('E PAMUNDUR')

print(completeMatrices)
