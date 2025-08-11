### convert the time entered in hh, min and sec into seconds.

hh=int(input("enter hours :"))
min=int(input("enter minutes :"))
sec=int(input("enter seconds :"))

total_sec=(hh * 3600) + (min * 60) + sec

print(f"total seconds is {total_sec}.")