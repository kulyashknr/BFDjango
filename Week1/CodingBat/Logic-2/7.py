def make_chocolate(small, big, goal):
    if goal/5 <= big:
    	goal = goal - (goal/5)*5
    else:
    	goal = goal - big*5
    	
    if goal <= small:
    	return goal
    	
    return -1;
