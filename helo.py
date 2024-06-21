from timeit import default_timer
lst=list(range(0,15))
print(lst)
r=1
start=default_timer()
for num in lst:
    print(num,end=" ")
    r=r+num
print(r)
stop=default_timer()
join_time= stop-start
print("start time",start)
print("stop time",stop)
print("join::",join_time)