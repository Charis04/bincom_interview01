from collections import defaultdict

def calculate_total_scores(data):
  """Calculates the total score for each student in the given list of dictionaries.

  Args:
    data: A list of dictionaries, each containing information about a test.

  Returns:
    A list of dictionaries, each containing the student's name and total score.
  """

  scores = defaultdict(int)
  for item in data:
    scores[item['student']] += item['score']

  return [{'student': student, 'total_score': score} for student, score in scores.items()]

# Example usage:
data = [
  {"test id": 1, "student": "Charis", "test": "test 1", "score": 20},
  {"test id": 1, "student": "Olaoluwa", "test": "test 1", "score": 24},
  {"test id": 1, "student": "Moyin", "test": "test 1", "score": 25},
  {"test id": 2, "student": "Charis", "test": "test 2", "score": 23},
  {"test id": 2, "student": "Olaoluwa", "test": "test 2", "score": 25},
  {"test id": 2, "student": "Moyin", "test": "test 2", "score": 22},
]

result = calculate_total_scores(data)
print(result)