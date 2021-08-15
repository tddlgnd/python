invitations = ["Kim", "Lee", "Park", "Choi"]
persons = [1, 3, 0, 6]

# 총인원을 확인
print(sum(persons))

# 파티에 한 사람이라도 오는 지를 확인
print(any(persons))

# 모든 초대받은 그룹이 전부 오는 지는 확인
print(all(persons))

# 가장 많이 오는 그룹에는 몇 사람이나 있는지 확인
print(max(persons))

# 이름과 사람수를 묶어서 출력
for name, person in zip(invitations, persons):
     print(name, person)

