p1 = password [28:32]
p2 = password [36:38]
p3 = password [113:118]
p4 = password [66:69]     #뒤집어서 출력해야한다
p5 = password [322:326]   #뒤집어서 출력해야한다
p6 = password [365:371]    #'python' 임

print(f'{p1} {p2} {p3} {p4[::-1]} {p5[::-1]} "{p6}".')