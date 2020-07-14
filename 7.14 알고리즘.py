## 공원공간 x = 0~100, y = 0~100
## 공사장 (x,y) 소음반경 R
## 그늘의 존재 N개

## 기본 값 입력 0 = x좌표, 1 = y좌표, 2 = 소음반경

x = input("")
x_split = x.split(" ")
x_split_int = list(map(int, x_split))
print("공사장 정보", x_split_int)

y = int(input("그늘의 갯수 :"))
print("그늘의 갯수 :" , y)

a = []

for i in range(y):
    s = input("그늘의 위치")
    s_split = s.split(" ")
    s_split_int = list(map(int, s_split))
    a.append(s_split_int)


    x_range = (( x_split_int[0] - a[i][0] ) ** 2)
    y_range = (( x_split_int[1] - a[i][1] ) ** 2)
    R_range = ( x_split_int[2] ** 2)

    if x_range + y_range >= R_range:
        print('silent')
    else:
        print('noisy')





# for i in range(y):
#     y_map = input("그늘의 위치")
#     y_map.split(" ")
#     a.append(y_map) 