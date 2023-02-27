from collections import deque
def solution(book_time):
    time = []
    for t in book_time:
        sh, sm = map(int, t[0].split(':'))
        eh, em = map(int, t[1].split(':'))
        time.append([sh * 60 + sm, eh * 60 + em + 10])
    
    # dq
    dq = deque(sorted(time))
    first_s, first_e = dq.popleft()
    room = [
        # first room
        [
            # first book
            [first_s, first_e]
        ]
    ]
    while dq:
        
        s, e = dq.popleft()
        room_check = 0
        n = len(room)
        for i in range(n):
            
            cnt = 0
            for j in range(len(room[i])):
                
                bs, be = room[i][j][0], room[i][j][1]
                
                # 겹친다는 조건: booked 안에 new가 들어가거나 new 안에 booked가 들어감
                if bs <= s < be or bs <= e < be or s < bs <= e or s < be <= e:
                    break
                # 안 겹치면
                else:
                    cnt += 1
            
            # 이 방에 겹치는 시간이 없다면
            if cnt == len(room[i]):
                room[i].append([s, e]) # 이 방에 추가
                break
            
            # 겹치는 시간대가 있다면 다음방 확인
            else:
                room_check += 1
        
        # 모든 방이 다 시간대가 겹치면
        if room_check == len(room):
            room.append([[s, e]])
            
    return len(room)