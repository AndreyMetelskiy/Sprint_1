
time_string = '1h 45m,360s,25m,30m 120s,2h 60s'
time_string = time_string.replace(",", "  ").split()
total_minutes=0

for item in time_string:
     units_of_time = int(item[:-1]) 
   
     if 'h' in item and units_of_time > 0 and units_of_time % 1 == 0:
             total_minutes += units_of_time*60
     elif 'm' in item and units_of_time > 0 and units_of_time % 1 == 0: 
             total_minutes += units_of_time
     elif 's' in item and units_of_time > 0 and units_of_time % 60 == 0:
             total_minutes += units_of_time / 60
print('Общее количество минут:',int(total_minutes))