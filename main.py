import datetime
import os
import time
import random

####################
file_name = "katilimcilar.txt"
rewards_file_name = "oduller.txt"
log_file_name = "cekilis2018.log"
col_count = 6
reward_count = 12
elimination_wait_time = .1 
reward_wait_time = .3
spacing = 25
time_before_starting = .1

def print_header():
	crypttech_string_2 = """
        CCCCCCCCCCCCC RRRRRRRRRRRRRRRR  YYYYYYY       YYYYYYPPPPPPPPPPPPPPPPP  TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTEEEEEEEEEEEEEEEEEEEEEE      CCCCCCCCCCCCHHHHHHHHH     HHHHHHHHH
     CCC::::::::::::C R::::::::::::::::R Y:::::Y       Y:::::P::::::::::::::::P T:::::::::::::::::::::T:::::::::::::::::::::E::::::::::::::::::::E   CCC::::::::::::H:::::::H     H:::::::H
   CC:::::::::::::::C R::::::RRRRRR:::::RY:::::Y       Y:::::P::::::PPPPPP:::::PT:::::::::::::::::::::T:::::::::::::::::::::E::::::::::::::::::::E CC:::::::::::::::H:::::::H     H:::::::H
  C:::::CCCCCCCC::::C RR:::::R     R:::::Y::::::Y     Y::::::PP:::::P     P:::::T:::::TT:::::::TT:::::T:::::TT:::::::TT:::::EE::::::EEEEEEEEE::::EC:::::CCCCCCCC::::HH::::::H     H::::::HH
 C:::::C       CCCCCC  R::::R     R:::::YYY:::::Y   Y:::::YYY P::::P     P:::::TTTTTT  T:::::T  TTTTTTTTTTT  T:::::T  TTTTTT E:::::E       EEEEEC:::::C       CCCCCC H:::::H     H:::::H  
C:::::C                R::::R     R:::::R  Y:::::Y Y:::::Y    P::::P     P:::::P       T:::::T               T:::::T         E:::::E           C:::::C               H:::::H     H:::::H  
C:::::C                R::::RRRRRR:::::R    Y:::::Y:::::Y     P::::PPPPPP:::::P        T:::::T               T:::::T         E::::::EEEEEEEEEE C:::::C               H::::::HHHHH::::::H  
C:::::C                R:::::::::::::RR      Y:::::::::Y      P:::::::::::::PP         T:::::T               T:::::T         E:::::::::::::::E C:::::C               H:::::::::::::::::H  
C:::::C                R::::RRRRRR:::::R      Y:::::::Y       P::::PPPPPPPPP           T:::::T               T:::::T         E:::::::::::::::E C:::::C               H:::::::::::::::::H  
C:::::C                R::::R     R:::::R      Y:::::Y        P::::P                   T:::::T               T:::::T         E::::::EEEEEEEEEE C:::::C               H::::::HHHHH::::::H  
C:::::C                R::::R     R:::::R      Y:::::Y        P::::P                   T:::::T               T:::::T         E:::::E           C:::::C               H:::::H     H:::::H  
 C:::::C       CCCCCC  R::::R     R:::::R      Y:::::Y        P::::P                   T:::::T               T:::::T         E:::::E       EEEEEC:::::C       CCCCCC H:::::H     H:::::H  
  C:::::CCCCCCCC::::C RR:::::R     R:::::R      Y:::::Y      PP::::::PP               TT:::::::TT           TT:::::::TT     EE::::::EEEEEEEE:::::EC:::::CCCCCCCC::::HH::::::H     H::::::HH
   CC:::::::::::::::C R::::::R     R:::::R   YYYY:::::YYYY   P::::::::P               T:::::::::T           T:::::::::T     E::::::::::::::::::::E CC:::::::::::::::H:::::::H     H:::::::H
     CCC::::::::::::C R::::::R     R:::::R   Y:::::::::::Y   P::::::::P               T:::::::::T           T:::::::::T     E::::::::::::::::::::E   CCC::::::::::::H:::::::H     H:::::::H
        CCCCCCCCCCCCC RRRRRRRR     RRRRRRR   YYYYYYYYYYYYY   PPPPPPPPPP               TTTTTTTTTTT           TTTTTTTTTTT     EEEEEEEEEEEEEEEEEEEEEE      CCCCCCCCCCCCHHHHHHHHH     HHHHHHHHH
	 """                                                                                                                                                                                                                              
                                                                                                                                                                                                                                         
	os.system("clear")
	print(crypttech_string_2)
	print("      CYBER SECURITY INTELLIGENCE - 2018 Cekilis\n\n")

def read_attendants(file_name):
	attendants = []
	
	with open(file_name,"r") as f:
		for line in f:
			line = line.replace('\n','')
			attendants.append(line)

	random.shuffle(attendants)
	return attendants

def print_attendants(attendants):
	attendants_list = [attendants[i:i+col_count] for i in range(0, len(attendants), col_count)]        # use xrange in py2k
	col_width = max(len(word) for row in attendants for word in row) + spacing
	for row in attendants_list:
		print(" ".join(word.ljust(col_width) for word in row)) 

def read_rewards(file_name):
	rewards = []
	with open(file_name,"r") as f:
		for line in f:
			line = line.replace('\n','')
			rewards.append(line)
	return rewards

def shuffle_10_times(array):
	for i in range(0,9):
		random.shuffle(array)
	return array

def print_winners(winners,rewards):
	final_list = []
	for i in range(0,len(rewards)):
		write_log(winners[i],rewards[i]+" KAZANDI ")
		final_list.append([rewards[i],winners[i]])
	
	col_width = max(len(word) for row in final_list for word in row) + 15
	for row in final_list:
		time.sleep(reward_wait_time)
		print(" ".join(word.ljust(col_width) for word in row))

def print_spares(spares):
	for i in range(0,len(spares)):
		print(str(i+1)+"    		  "+spares[i])
		input()
		write_log(spares[i],str(i)+".[YEDEK]")

def mask(name):
	masked = name[0:3]
	for i in range(3,len(name)):
		masked += "*"
	return masked

def write_log(name,status):
	ts = time.time()
	time_stamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
	log_text = "Time: "
	log_text += time_stamp
	log_text += " Name: "
	log_text += mask(name)
	log_text += " Status: "
	log_text += status
	log_text += "\n"
	
	with open(log_file_name,"a") as log:
		log.write(log_text)


def main():
	print_header()
	winner_list = []
	print("\n\n         Cekilis 1 dakika icinde baslayacaktir...\n\n")
	time.sleep(time_before_starting)
	initial_list = read_attendants(file_name)
	print_attendants(initial_list)
	winner_list = initial_list

	rewards = read_rewards(rewards_file_name)
	
	for i in range(0,len(winner_list)-reward_count):
		eliminated = random.choice(winner_list)
		winner_list.remove(eliminated)
		write_log(eliminated,"ELENDİ")
		print_header()
		print("Elenen Kisi: ",eliminated,"\n\n")
		print_attendants(initial_list)
		time.sleep(elimination_wait_time)
	
	print_header()
	print("...:::Asil Adaylar:::...")
	print_attendants(winner_list)
	random.shuffle(winner_list),
	
	spare_list = read_attendants(file_name)
	for winner in winner_list:
		spare_list.remove(winner)
	random.shuffle(spare_list)

	print("\n\n\n...:::Asil Kazananlar:::...:")
	print_winners(winner_list,rewards)

	print("\n\n\n...:::Yedek Listesi:::...")
	print_spares(spare_list)

if __name__ == "__main__":
	main()

