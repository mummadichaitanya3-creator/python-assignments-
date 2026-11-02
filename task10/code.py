def evaluate_exam(answer_key, student_responses, positive_marks=4, negative_marks=1):
    results = {}
    for student_id, response in student_responses.items():
        correct = 0
        incorrect = 0
        unanswered = 0
        score = 0
        
        for student_ans, key_ans in zip(response, answer_key):
            if student_ans == "-":
                unanswered += 1
            elif student_ans == key_ans:
                correct += 1
                score += positive_marks
            else:
                incorrect += 1
                score -= negative_marks
                
        results[student_id] = {
            "correct": correct,
            "incorrect": incorrect,
            "unanswered": unanswered,
            "score": score
        }
        
    return results

