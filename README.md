# Multi-Criteria Decision Making (MCDM) - TOPSIS Method

This project implements the **TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution)** method for decision making. The project uses a decision matrix with multiple criteria to rank options based on their proximity to the ideal solution.

## Project Overview

The TOPSIS method is used in decision-making scenarios where several alternatives are evaluated against multiple criteria. In this project, the criteria matrix is provided, and the goal is to determine the ranking of alternatives based on their performance across the given criteria.

### Key Components:
1. **Criteria Matrix**: A matrix where each row represents an alternative, and each column represents a criterion.
2. **Criteria Weights**: The relative importance of each criterion.
3. **Criteria Preferences**: Whether higher values for a criterion are preferred (`+1`) or lower values are preferred (`-1`).

### Example Matrix:
The decision matrix used in the script is as follows:

```python
criteria_matrix = [
    [2500, 1500, 3, 1.2, 15],
    [2000, 1300, 2, 0.5, 20],
    [3000, 2000, 5, 2, 10],
    [2200, 1700, 4, 1, 12]
]
criteria_weight = [0.2, 0.2, 0.2, 0.2, 0.2]
criteria_preference = [-1, 1, -1, -1, 1]
```

## Key Steps

1. **Normalization of the Decision Matrix**:
   The decision matrix is normalized by dividing each element by the square root of the sum of squares for that column.

2. **Weighted Normalization**:
   The normalized matrix is then weighted according to the criteria weights.

3. **Ideal and Negative-Ideal Solutions**:
   The ideal solution maximizes the benefit criteria and minimizes the cost criteria, while the negative-ideal solution does the opposite.

4. **Distance Calculation**:
   The Euclidean distance of each alternative from the ideal and negative-ideal solutions is computed.

5. **Rank Calculation**:
   Finally, the alternatives are ranked based on their closeness to the ideal solution.

## Project Structure

- `porto1_case_study_ice.py`: Python script implementing the TOPSIS method for decision making.
- `README.md`: This file, providing an overview of the project.

## Installation

To run the project, ensure you have Python 3 installed.

## Usage

You can execute the script by running:

```bash
python porto1_case_study_ice.py
```

This will output:
- The normalized decision matrix.
- The ranking of alternatives based on the TOPSIS method.

## Example Output

Upon running the script, you will see the normalized matrix and the ranking of the alternatives based on their closeness to the ideal solution.

## Future Improvements

- Add user input functionality to dynamically update the decision matrix and weights.
- Enhance the script with visualization options for better understanding of the ranking process.
- Implement other MCDM techniques for comparison.
