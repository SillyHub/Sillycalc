# # # # STUPID CALCULATOR PROJECT
# # # # By ME

age = input("How old are you (in years)?\n>")

first_time = input("When was your first sexual experience?\n>")

years_active = float(age - first_time)


if 0< years_active< 11:
	number_of_times = years_active*112

elif 12 < years_active < 21:
	number_of_times = (10*112) + (years_active - 12) * 86
	
elif 22< years_active < 31:
	number_of_times = ((10*112) + (10*86) + (years_active-22) * 69)

else:
	print "I have no idea"
	
time_spent = 10 # minutes, per session

total_time = time_spent * number_of_times

print "Therefore, you have spent %d minutes with a penis inside you. Congratulations!" % total_time

av_length = 15 #cm

number_of_thrusts = 72 # thrusts per minute

length_per_minute = number_of_thrusts * av_length

total_length = length_per_minute*total_time

total_m = total_length/100

total_km = total_m/1000

print "This means exactly %.2f kilometres of penis have penetrated you. Have a nice day!" % total_km
