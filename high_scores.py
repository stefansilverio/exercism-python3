#!/usr/bin/python3
# create high score component for frogger

def latest(scores):
    return scores.pop()

def personal_best(scores):
    return max(scores)

def personal_top_three(scores):
    if len(scores) >= 3:
        return [scores.pop(scores.index(max(scores))) for i in range(3)]
    else:
        return [scores.pop(scores.index(max(scores))) for i in range(len(scores))]
