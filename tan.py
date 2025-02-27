#목적구(내가 쳐야하는공 1 내가 치는공 흰공 0)
import math
diff_y = balls[1][0] - balls[0][0] # 둘 y 좌표를 구하는 밑변
diff_x = balls[1][1] - balls[0][1]  # 둘 x 좌표를 구하는 높이
math.degrees(math.atan2(diff_y, diff_x))

# 각 타겟 공에 대한 각도를 구해서 출력
for i, target in enumerate(target_balls):
    diff_y = target[0] - balls[0]  # 타겟 공과 흰공의 y 좌표 차이
    diff_x = target[1] - balls[1]  # 타겟 공과 흰공의 x 좌표 차이
    angle_deg = math.degrees(math.atan2(diff_y, diff_x))  # 각도 계산
    #목적구(내가 쳐야하는공 1 내가 치는공 흰공 0)
import math
diff_y = balls[1][0] - balls[0][0] # 둘 y 좌표를 구하는 밑변
diff_x = balls[1][1] - balls[0][1]  # 둘 x 좌표를 구하는 높이
math.degrees(math.atan2(diff_y, diff_x))

# 각 타겟 공에 대한 각도를 구해서 출력
for i, target in enumerate(target_balls):
    diff_y = target[0] - balls[0]  # 타겟 공과 흰공의 y 좌표 차이
    diff_x = target[1] - balls[1]  # 타겟 공과 흰공의 x 좌표 차이
    angle_deg = math.degrees(math.atan2(diff_y, diff_x))  # 각도 계산

    #목적구(내가 쳐야하는공 1 내가 치는공 흰공 0)
import math
diff_y = balls[1][0] - balls[0][0] # 둘 y 좌표를 구하는 밑변
diff_x = balls[1][1] - balls[0][1]  # 둘 x 좌표를 구하는 높이
math.degrees(math.atan2(diff_y, diff_x))

# 각 타겟 공에 대한 각도를 구해서 출력
for i, target in enumerate(target_balls):
    diff_y = target[0] - balls[0]  # 타겟 공과 흰공의 y 좌표 차이
    diff_x = target[1] - balls[1]  # 타겟 공과 흰공의 x 좌표 차이
    angle_deg = math.degrees(math.atan2(diff_y, diff_x))  # 각도 계산