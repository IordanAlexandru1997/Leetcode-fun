import heapq


def tasks(tasks_list):
    heapq.heapify(tasks_list)
    machine_no = 0
    machines_available = []
    while tasks_list:
        task = heapq.heappop(tasks_list)
        if machines_available and task[0] >= machines_available[0][0]:
            machine_in_use = heapq.heappop(machines_available)
            machine_in_use = (task[1], machine_in_use[1])
        else:
            machine_no += 1
            machine_in_use = (task[1], machine_no)
        heapq.heappush(machines_available, machine_in_use)
    return machine_no


#    # to count the total number of machines for "optimal_machines" tasks
#     optimal_machines = 0
#     # empty list to store tasks finish time
#     machines_available = []
#     # converting list of set "optimal_machines" to a heap
#     heapq.heapify(tasks_list)

#     while tasks_list:  # looping through the tasks list
#         # remove from "tasks_list" the task i with earliest start time
#         task = heapq.heappop(tasks_list)

#         if machines_available and task[0] >= machines_available[0][0]:
#             # top element is deleted from "machines_available"
#             machine_in_use = heapq.heappop(machines_available)

#             # schedule task on the current machine
#             machine_in_use = (task[1], machine_in_use[1])

#         else:
#             # if there's a conflicting task, increment the
#             # counter for machines and store this task's
#             # end time on heap "machines_available"
#             optimal_machines += 1
#             machine_in_use = (task[1], optimal_machines)

#         heapq.heappush(machines_available, machine_in_use)

#     # return the total number of machines used by "tasks_list" tasks
#     return optimal_machines


taskss = [[1, 1], [5, 5], [8, 8], [4, 4], [6, 6], [10, 10], [7, 7]]
taskss = [[1, 7], [8, 13], [5, 6], [10, 14], [6, 7]]
print(tasks(taskss))
