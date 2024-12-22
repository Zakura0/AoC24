def regularPath():
    node = s
    steps = 0
    path = {s:0}
    while node != e:
          row, col = node
          for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
              new_row, new_col = row + x, col + y
              if (new_row, new_col) not in path:
                  if 0 <= new_row < height and 0 <= new_col < width:
                      if grid[new_row][new_col] == '.':
                          steps += 1
                          node = (new_row, new_col)
                          path[node] = steps
                          break
    return path, steps
                     

def searchCheat(node, path, regular_time, max_time, max_cheat_time):
    global total_steps
    found_cheats = 0
    start_time = path[node]
    queue = OrderedDict()
    visited = set()
    queue[node] = start_time
    while queue:
        node, time = queue.popitem(last=False)
        visited.add(node)
        if (time - start_time) > max_cheat_time:
            break
        if node in path:
            if regular_time - path[node] + time <= max_time:
                found_cheats += 1
                steps = regular_time - path[node] + time
                if steps in total_steps:
                    total_steps[steps] += 1
                else:
                    total_steps[steps] = 1
        row, col = node
        for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_row, new_col = row + x, col + y
            if (new_row, new_col) not in queue and (new_row, new_col) not in visited:
                if 0 <= new_row < height and 0 <= new_col < width:
                    queue[(new_row, new_col)] = time + 1
    
    return found_cheats


regular_path, regular_time = regularPath()
max_time = regular_time - 100
total_cheats = 0
total_steps = {}
for node in regular_path:
    total_cheats += searchCheat(node, regular_path, regular_time, max_time, 20)

sorted_steps2 = dict(sorted(total_steps.items(), key=lambda item: item[0], reverse=True))
# test = sorted_steps.keys() - sorted_steps2.keys()
# print(test)
#print(sorted_steps2)
print(total_cheats)