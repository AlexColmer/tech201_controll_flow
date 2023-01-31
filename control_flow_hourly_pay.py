hours_worked = input("What is your hours worked a week?")
hourly_pay = input("what is your hourly pay?")

if int(hours_worked) <= 40:
    print("Your gross pay is", int(hourly_pay) * int(hours_worked), "Pounds")
elif int(hours_worked) > 40:
    print("Your gross pay is", (int(hours_worked) - 40) * (int(hourly_pay) * 1.5) + 40 * int(hourly_pay))