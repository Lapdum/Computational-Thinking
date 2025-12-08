def Maximum(a, b):
    if a >= b:
        return a
    else:
        return b
    
def Minimum(a,b):
    if a <= b:
        return a
    else:
        return b
    
def find_max_lengths(tasks):
    if not tasks:
        return 0, 0, 0
    
    max_task_len = 0
    max_deadline_len = 0
    max_status_len = 0
    
    for task_dict in tasks:
        if "task" in task_dict:
            max_task_len = Maximum(max_task_len, length(str(task_dict["task"])))
        if "deadline" in task_dict:
            max_deadline_len = Maximum(max_deadline_len, length(str(task_dict["deadline"])))
        if "status" in task_dict:
            max_status_len = Maximum(max_status_len, length(str(task_dict["status"])))
    #print(max_task_len, max_deadline_len, max_status_len)
    return max_task_len, max_deadline_len, max_status_len
                
def length(str):
    cnt = 0
    for s in str:
        cnt += 1
    return cnt

def number_task(tasks):
    cnt = 0
    for _ in tasks:
        cnt += 1
    return cnt