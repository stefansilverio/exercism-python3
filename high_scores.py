#!/usr/bin/python3
# create high score component for frogger

def latest(scores):
    return scores.copy().pop()

def personal_best(scores):
    return max(scores)

def personal_top_three(scores):
    return sorted(scores, reverse=True)[:3]
