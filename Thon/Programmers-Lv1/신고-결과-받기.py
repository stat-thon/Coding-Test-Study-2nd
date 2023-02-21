def solution(id_list, report, k):
    report = list(set(report))
    who_report_whom_dict = {name:[] for name in id_list}
    reported_dict = {name:0 for name in id_list}
    banned = []
    
    for case in report:
        user_a, user_reported = case.split()
        
        reported_dict[user_reported] += 1
        who_report_whom_dict[user_a].append(user_reported)
        
        if reported_dict[user_reported] >= k:
            banned.append(user_reported)
    
    return [len(set(who_report_whom_dict[user]) & set(banned)) for user in id_list] 