def detect(process, allocation, request, available):
    """ TODO: Implement a selected deadlock detection algorithm, 
        detect: receives processes, allocations, requests, and work 
        and returns true if a deadlock is detected otherwise false.   """
    PN = len(process)
    RN = len(available)
    r, p = 0, 0

    finished = [0] * PN

    has_changed = True
    while has_changed:
        has_changed = False

        for p in range(PN):
            if finished[p] == 0:
                    for r in range(RN):
                        if request[p][r] > available[r]:
                                break
                    if r+1 == RN:
                        has_changed = True
                        finished[p] = 1
                        for r in range(RN):
                                available[r] += allocation[p][r]

    for p in range(PN):
        if finished[p] == 0:
            return False
    return True

if __name__=='__main__':
    '''
    n=int(input('Enter number of processes: '))
    process=list(range(n))

    r=int(input('Enter number of resources: '))

    allocation=input('Enter allocation: ').split()
    request=input('Enter request: ').split()
    available=input('Enter available resources: ')
    '''

    process=[0, 1, 2, 3, 4]
    allocation=[[0, 1, 0], [2, 0, 0], [3, 0, 3], [2, 1, 1], [0, 0, 2]]
    request=[[0, 0, 0], [2, 0, 2], [0, 0, 0], [1, 0, 0], [0, 0, 2]]
    available=[0, 0, 0]

    print( "No Deadlock Exist" if detect(process, allocation, request, available) else "Deadlock Found!")
