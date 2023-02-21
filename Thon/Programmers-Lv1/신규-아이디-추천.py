import re
def solution(new_id):
    # step 1
    new_id = new_id.lower()
    
    # step 2, step 3
    id_rec = ''
    for s in new_id:
        if s.isalnum() or s in ['.', '-', '_']:
            if len(id_rec) != 0 and id_rec[-1] == '.' and s == '.':
                pass
            else:
                id_rec += str(s)
    
    # step 4
    if id_rec != '' and id_rec[0] == '.':
        id_rec = id_rec[1:]
    if id_rec != '' and id_rec[-1] == '.':
        id_rec = id_rec[:-1]
    
    # step 5
    if id_rec == '':
        id_rec = 'a'
    
    # step 6
    if len(id_rec) >= 16:
        id_rec = id_rec[:15]
    
    if id_rec[-1] == '.':
        id_rec = id_rec[:-1]
        
    # step 7
    if len(id_rec) <= 2:
        id_rec += id_rec[-1] * (3 - len(id_rec))
    
    return id_rec