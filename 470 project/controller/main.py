import getpass
import string
import os

users = ['user1', 'user2', 'user3']
pins = ['6428', '2580', '7878']
amounts = [50000, 25262, 90000]
count = 0

while True:
	user = input('\nENTER USER NAME: ')
	user = user.lower()
	if user in users:
		if user == users[0]:
			n = 0
		elif user == users[1]:
			n = 1
		else:
			n = 2
		break
	else:

		print('INVALID USERNAME')



while count < 3:

	pin = input('PLEASE ENTER PIN: ')

	if pin.isdigit():
		if user == 'user1':
			if pin == pins[0]:
				break
			else:
				count += 1

				print('INVALID PIN')

				print()

		if user == 'user2':
			if pin == pins[1]:
				break
			else:
				count += 1

				print('INVALID PIN')

				print()
				
		if user == 'user3':
			if pin == pins[2]:
				break
			else:
				count += 1

				print('INVALID PIN')

				print()
	else:

		print('PIN CONSISTS OF 4 DIGITS')

		count += 1
	

if count == 3:

	print('3 UNSUCCESSFUL PIN ATTEMPTS, EXITING')
	print('YOUR CARD HAS BEEN LOCKED')

	exit()


print('LOGIN SUCCESSFUL, CONTINUE')
print()
print(str.capitalize(users[n]), 'welcome to ATM')

print('----------ATM SYSTEM-----------')
# Main menu
while True:

	response = input('SELECT FROM FOLLOWING OPTIONS: \nStatement__(S) \nWithdraw___(W) \nLodgement__(L)  \nChange PIN_(P)  \nQuit_______(Q) \nType The Letter Of Your Choices: ').lower()

	valid_responses = ['s', 'w', 'l', 'p', 'q']
	response = response.lower()
	if response == 's':

		print(str.capitalize(users[n]), 'YOU HAVE ', amounts[n],'TAKA ON YOUR ACCOUNT.')

		
	elif response == 'w':

		cash_out = int(input('ENTER AMOUNT YOU WOULD LIKE TO WITHDRAW: '))

		if cash_out%10 != 0:

			print('AMOUNT YOU WANT TO WITHDRAW MUST TO MATCH 10 EURO NOTES')

		elif cash_out > amounts[n]:

			print('YOU HAVE INSUFFICIENT BALANCE')

		else:
			amounts[n] = amounts[n] - cash_out

			print('YOUR NEW BALANCE IS: ', amounts[n], 'EURO')

			
	elif response == 'l':
		print()

		cash_in = int(input('ENTER AMOUNT YOU WANT TO LODGE: '))

		print()
		if cash_in%10 != 0:

			print('AMOUNT YOU WANT TO LODGE MUST TO MATCH 10 EURO NOTES')

		else:
			amounts[n] = amounts[n] + cash_in

			print('YOUR NEW BALANCE IS: ', amounts[n], 'EURO')

	elif response == 'p':

		new_pin = str(getpass.getpass('ENTER A NEW PIN: '))

		if new_pin.isdigit() and new_pin != pins[n] and len(new_pin) == 4:

			new_ppin = str(getpass.getpass('CONFIRM NEW PIN: '))

			if new_ppin != new_pin:

				print('PIN MISMATCH')

			else:
				pins[n] = new_pin
				print('NEW PIN SAVED')
		else:

			print('   NEW PIN MUST CONSIST OF 4 DIGITS \nAND MUST BE DIFFERENT TO PREVIOUS PIN')

	elif response == 'q':
		exit()
	else:

		print('RESPONSE NOT VALID')
