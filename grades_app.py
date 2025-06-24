# from flask import Flask, render_template
# import requests

# app = Flask(__name__)

def calc_final_grade(assignment):
     for section, values in assignment.items():
         weight = values[0]
         score = values[1]
         grade = (weight * score) / 100
         values.append(round(grade, 2))


if __name__ == "__main__":
    assignment_sect = []

    cont = True
    while(cont):
        name = input("Enter the assignment name! Type 'stop' to once done: ").lower()
        if name != "stop":
            assignment_sect.append(name)
        else:
            cont = False

    assignment = {}
    for i in range(len(assignment_sect)):
        weight, score = input(f"Enter the {assignment_sect[i]} weight% and score% seperated by a space: ").split()
        values = [float(weight), float(score)]
        assignment.update({assignment_sect[i]: values})


    calc_final_grade(assignment)
    print(assignment)