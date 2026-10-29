def solution(video_len, pos, op_start, op_end, commands):
    video_len = list(map(int, list(video_len.split(':'))))
    video_sec = video_len[0] * 60 + video_len[1]
    pos = list(map(int, pos.split(':')))
    pos_sec = pos[0] * 60 + pos[1]
    op_start, op_end = list(map(int, op_start.split(':'))), list(map(int, op_end.split(':')))
    op_start_sec = op_start[0] * 60 + op_start[1]
    op_end_sec = op_end[0] * 60 + op_end[1]
    if op_start_sec <= pos_sec <= op_end_sec:
            pos_sec = op_end_sec
            
    for command in commands:
        if command == 'next':
            pos_sec += 10
            if pos_sec > video_sec:
                pos_sec = video_sec
        elif command == 'prev':
            pos_sec -= 10
            if pos_sec < 0:
                pos_sec = 0
        if op_start_sec <= pos_sec <= op_end_sec:
            pos_sec = op_end_sec
    
    minute, sec = str(pos_sec // 60), str(pos_sec % 60)
    if int(minute) < 10:
        minute = '0' + minute
    if int(sec) < 10:
        sec = '0' + sec
    return minute + ':' + sec