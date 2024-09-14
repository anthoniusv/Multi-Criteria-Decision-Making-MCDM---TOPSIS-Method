criteria_matrix = [
    [2500,1500,3,1.2,15],
    [2000,1300,2,0.5,20],
    [3000,2000,5,2,10],
    [2200,1700,4,1,12]
]

criteria_weight= [0.2,0.2,0.2,0.2,0.2]
criteria_preference = [-1,1,-1,-1,1]

def normalize_decision_matrix(criteria_matrix):
    criteria_rows = len(criteria_matrix)
    criteria_columns = len(criteria_matrix[0])
    column_sums= [0] * criteria_columns

    for j in range(criteria_columns):
        for i in range(criteria_rows):
            column_sums[j] += criteria_matrix[i][j] ** 2
    column_sums = [value ** 0.5 for value in column_sums]

    normalized_matrix = []
    for i in range(criteria_rows):
        normalized_matrix_rows = []
        for j in range(criteria_columns):
            normalized_matrix_rows.append(criteria_matrix [i][j]/column_sums[j])
        normalized_matrix.append(normalized_matrix_rows)
    
    print('\nNormalized matrix from criteria matrix: ')
    for i in normalized_matrix:
        for j in i:
            print(f'{j:.4f}',end=' ')
        print()
    return normalized_matrix

def weighted_matrix(criteria_weight, normalized_matrix):
    normalized_rows = len(normalized_matrix)
    normalized_columns = len(normalized_matrix[0])
    
    weighted_matrix = []
    for i in range(normalized_rows):
        weighted_matrix_rows = []
        for j in range(normalized_columns):
            weighted_matrix_rows.append(normalized_matrix [i][j]* criteria_weight[j])
        weighted_matrix.append(weighted_matrix_rows)
    
    print('\nWeighted matrix from normalized matrix: ')
    for i in weighted_matrix:
        for j in i:
            print(f'{j:.4f}',end=' ')
        print()
    return weighted_matrix

def ideal_best_worst(weighted_matrix,criteria_preferences):
    weighted_column = len(weighted_matrix[0])
    positive_ideal= [] 
    negative_ideal = [] 

    for j in range(weighted_column):
        max_value = weighted_matrix[0][j]
        min_value = weighted_matrix[0][j]

        for i in range(len(weighted_matrix)):
            if weighted_matrix[i][j] > max_value:
                max_value = weighted_matrix [i][j]
            if weighted_matrix[i][j] < min_value:
                min_value = weighted_matrix [i][j]
        if criteria_preferences[j] == 1:  
            positive_ideal.append(max_value)
            negative_ideal.append(min_value)
        else:  
            positive_ideal.append(min_value)
            negative_ideal.append(max_value)
    
    print('\nPositive ideal point for each column: ')
    for i in positive_ideal:
        print(f'{i:.4f}',end=' ')
    print()
    print('\nNegative ideal point for each column: ')
    for i in negative_ideal:
        print(f'{i:.4f}',end=' ')
    print()

    return positive_ideal, negative_ideal

def separation_from_ideal_point(weighted_matrix,positive_ideal,negative_ideal):
    weighted_rows = len(weighted_matrix)
    positive_separation = []
    negative_separation = []

    for i in range(weighted_rows):
        pos_sep = 0
        neg_sep = 0
        for j in range(len(positive_ideal)):
            pos_sep += (weighted_matrix[i][j] - positive_ideal[j]) ** 2
            neg_sep += (weighted_matrix[i][j] - negative_ideal[j]) ** 2
        positive_separation.append(pos_sep ** 0.5)
        negative_separation.append(neg_sep ** 0.5)

    print('\nPositive separation: ')
    for i in (positive_separation):
        print(f'{i:.4f}')
    print('\nNegative separation: ')
    for i in (negative_separation):
        print(f'{i:.4f}')
    return positive_separation,negative_separation

def similarities_to_PIS(positive_separation,negative_separation):
    num_rows = len(positive_separation)
    relative_similarity = []

    for i in range(num_rows):
        pos_sep = positive_separation[i]
        neg_sep = negative_separation[i]
        similarity = neg_sep/(pos_sep + neg_sep)
        relative_similarity.append(similarity)
    
    print('\nOrder: ')
    for i in (relative_similarity):
        print(f'{i:.4f}')
    return relative_similarity



normalize_matrix = normalize_decision_matrix(criteria_matrix)
weighted_matrix = weighted_matrix(criteria_weight,normalize_matrix)
positive_ideal, negative_ideal = ideal_best_worst(weighted_matrix,criteria_preference)
positive_separation,negative_separation = separation_from_ideal_point(weighted_matrix,positive_ideal,negative_ideal)
relative_similarity = similarities_to_PIS(positive_separation,negative_separation)
    

