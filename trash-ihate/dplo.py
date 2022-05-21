def solve(total_people , cost , bus_pol , car_pol , obj ):
	if total_people <= 0:
		return cost
	if total_people in obj:
	    return obj[total_people]
	print(obj)
	b = min( solve(total_people-100 , cost+bus_pol , bus_pol , car_pol , obj) , solve(total_people-4 , cost+car_pol , bus_pol , car_pol , obj) )

	obj[total_peple] = b
	return b


try:
    t = input()
    obj = {}
    for _ in range(int(t)):
        total_peple , bus_cost , car_cost = map(int , input().split())
        r = solve(total_peple , 0 , bus_cost , car_cost, {} )
        print(r)
    
except Exception:
    pass
t = input()
for _ in range(int(t)):
    total_peple , bus_cost , car_cost = map(int , input().split())
    arr2 = [0]
    arr3 = [0]
    res = []
    total_bus_cost = bus_cost
    total_car_cost = car_cost
    for i in range(1 , total_peple+1):
        if i%100 == 0:
            total_bus_cost += bus_cost
        arr2.append(total_bus_cost)
    
    for i in range(1 , total_peple+1):
        if i%4 == 0:
            total_car_cost += car_cost
        arr3.append(total_car_cost)
    print(arr2)
    print(arr3)