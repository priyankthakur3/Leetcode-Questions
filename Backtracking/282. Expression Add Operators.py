class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        self.result = []
        self.dfs(num, target, 0, [], 0, 0)
        return self.result

    def dfs(self, num, target, index, path, current_value, last_value):
        if index == len(num):
            if current_value == target:
                self.result.append("".join(path))
            return

        for i in range(index, len(num)):

            if num[index] == '0' and i != index:
                continue
            curr_str = num[index: i + 1]
            curr_num = int(curr_str)
            len_value = len(path)
            if index == 0:
                # action
                path.append(curr_str)
                # recurse
                self.dfs(num, target, i + 1, path, curr_num, curr_num)
                # backtrack
                path = path[:len_value]

            else:
                # action
                path.append('+')
                path.append(curr_str)
                # recurse
                self.dfs(num, target, i + 1, path,
                         current_value + curr_num, + curr_num)
                # backtrack
                path = path[:len_value]

                # action
                path.append('-')
                path.append(curr_str)
                # recurse
                self.dfs(num, target, i + 1, path,
                         current_value - curr_num, - curr_num)
                # backtrack
                path = path[:len_value]

                # action
                path.append('*')
                path.append(curr_str)
                # recurse
                self.dfs(num, target, i + 1, path, current_value -
                         last_value + last_value * curr_num, last_value * curr_num)
                # backtrack
                path = path[:len_value]
