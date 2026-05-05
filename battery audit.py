# Project: solar bank auditor 2.0
# Lead Developer: djw_wire
battery_reading = [12.6, 13.8, 11.2, 12.1, 14.2]
#1. we create 'bucket' to count our results
healthy_count = 0
error_count= 0

print("–––DJW_WIRE SITE SYSTEM: ONLINE–––")

for volts in battery_reading:
    if 11.5<= volts <=14.0:
        print(f"Checking {volts} V .... [OK]")
        healthy_count +=1
    else:
        print(f"Checking {volts} V .... [SYSTEM ALERT]")
        error_count += 1
        
# final summary 
print("-" * 30)
print("FINAL REPORT for taofeek olamilekan:")
print(f"Total Healthy Batteries: {healthy_count}")
print(f"Total Faulty batteries: {error_count}")
print("-" * 30)
