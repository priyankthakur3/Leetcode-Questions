class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        processRun = [0] * n
        stack = []
        prevTime = 0
        for l in logs:
            proc_id, state, p_time = l.split(':')
            proc_id = int(proc_id)
            p_time = int(p_time)
            if state == 'start':
                if stack:    
                    processRun[stack[-1]] += p_time - prevTime
                stack.append(proc_id)
                prevTime = p_time
            else:
                processRun[stack.pop()] += p_time - prevTime + 1
                prevTime = p_time + 1
        return processRun