import random
import sys

user_input = input("Boas-vindas ao jogo Pedra, Papel e Tesoura. Insira o seu nome para iniciarmos o jogo!: ")
possible_actions = ["Pedra", "Papel", "Tesoura"]
point_u = 0
point_c = 0


while True:
        computer_action = random.choice(possible_actions)
        while point_c == 0 and point_u == 0:
                user_choice = input("Perfeito, " + user_input + "! Agora escolha uma opção (Pedra, Papel ou Tesoura): ")
                if user_choice.capitalize() in possible_actions:
                    print("Você escolheu " + user_choice + "! E o computador escolheu " + computer_action + ".")
                    break
                else:
                    print("Algo deu errado, tente novamente!")
        while point_c == 1 or point_c == 2 or point_u == 1 or point_u == 2:
                winner = print("O placar está " + str(point_u) + " para você e " + str(point_c) + " para o computador. Quem irá vencer o game?")
                user_choice= input("Bora pra próxima partida? Lembre-se que você precisa de três pontos para vencer o game, " + user_input + "! Escolha uma opção novamente (Pedra, Papel ou Tesoura): ")
                if user_choice.capitalize() in possible_actions:
                    print("Você escolheu " + user_choice + "! E o computador escolheu " + computer_action + ".")
                    break
                else:
                    print("Algo deu errado, tente novamente!")


        match (user_choice.capitalize(), computer_action):            
            case ("Papel", "Pedra"):
                print("Você ganhou!"),
                point_u = point_u + 1 
                        
            case ("Papel", "Tesoura"):
                print("Você perdeu!")
                point_c = point_c + 1
                        
            case ("Pedra", "Papel"):
                print("Você perdeu!")
                point_c = point_c + 1
                        
            case ("Pedra", "Tesoura"):
                print("Você ganhou!")
                point_u = point_u + 1
                        
            case ("Tesoura", "Papel"):
                print("Você ganhou!")
                point_u = point_u + 1
                        
            case ("Tesoura", "Pedra"):
                print("Você perdeu!")
                point_c = point_c + 1

        if user_choice.capitalize() == computer_action:
            print("Deu empate!")
            

        while point_c == 3 or point_u == 3:
                    if point_c == 3:
                        print("O computador venceu o jogo! Que a revolução das máquinas comece :)")
                        break
                    if point_u == 3:
                        print("Você venceu o jogo! Os humanos seguem vencendo as máquinas, mas por quanto tempo?")
                        break
                    else:
                        print("Como assim ninguém venceu? Algo deu errado! Quem programou esse jogo? >:(")    
        
        
        while point_c == 3 or point_u == 3:
            again = input("Você quer jogar novamente? Digite Sim ou Não.") 
            if again.capitalize() == "Sim":
                point_c = 0 
                point_u = 0 
                continue
            elif again.capitalize() in ['Não', 'Nao']:
                sys.exit()
            else: 
                print("Por favor, escolha entre Sim ou Não.")
                continue
        

            
            
        

            
    
    




    




