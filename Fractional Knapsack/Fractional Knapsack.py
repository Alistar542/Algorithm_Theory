
from math import inf

# P is the array that contains the points for diff problems in a question paper
# t is the time taken to solve diff problems in a question paper
# T is the total time available to solve the questions
def fractional_knapsack(p,t,T):
    points_scored = 0
    questions_solved = []
    time_left = T
    sorted_ques_ratio = find_sorted_question_ratio(p,t)
    print(sorted_ques_ratio)
    for question_num in sorted_ques_ratio:
        if time_left > 0:
            questions_solved.append(question_num+1)
            if t[question_num] > time_left:
                points_scored += (p[question_num]/t[question_num]) * time_left
                time_left = 0
            else:
                points_scored += p[question_num]
                time_left -= t[question_num]
    
    print(questions_solved)
    print(points_scored)


# Method to find the sorted question ratio in the decreasing order
def find_sorted_question_ratio(p,t):
    question_ratio = {}
    for index,points in enumerate(p):
        question_ratio[index] = (points/t[index])
    sorted_ques_ratio = dict(sorted(question_ratio.items(), key=lambda item:item[1],reverse=True))
    return sorted_ques_ratio

p = [25, 10,5,10,25,5,20]
t = [70,20,inf,24,80,16,48]
total_time = 4*60
fractional_knapsack(p,t,total_time)
