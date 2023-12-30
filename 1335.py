def minDifficulty(jobDifficulty, d):
    min_difficulty = float('inf')

    def backtrack(curr_day,task_left, current_difficulty, min_difficulty):
        if curr_day > d:
            return
        if not task_left:
            min_difficulty = min(min_difficulty, current_difficulty)
            return
        
        for task in task_left:
            current_day_tasks.append(task_index)  # Example using a list to track tasks
            current_difficulty = max(current_difficulty, jobDifficulty[task_index])
            

