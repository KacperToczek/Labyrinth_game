from time import perf_counter
from labyrinth import Labyrinth


def game():
    t0 = perf_counter()
    print("Give me your name:")
    pl_name = input("\n>>>")
    lab = Labyrinth("The labyrinth", pl_name)
    print(lab.get_description())
    while True:
        if lab.player.current_chamber.final:
            print("This is the end !!! You found the exit from labyrinth !!! \n")
            t1 = perf_counter()
            print(lab.player.get_info())
            print(lab.player.get_items())
            print("Your game lasted: {} s.".format(t1 - t0))
            print("Possible moves:")
            print("exit")
            print("play again")
            while True:
                choice = input(">>>")
                if choice == "play again":
                    return game()
                elif choice == "exit":
                    break
                else:
                    print("Sorry, I don't understand you. Choose possible move.")
            break
        if lab.player.current_chamber.monster is not None:
            print("In this chamber is monster. You have to fight with him. Good luck! \n")
            print(lab.player.current_chamber.duel.ask_question())
            answer = input("\n>>>")
            print(lab.player.current_chamber.duel.check_answer(answer))
            print(lab.player.current_chamber.duel.give_prize())
        print("Possible moves:")
        print("look around")
        print("map")
        print("info")
        print("check backpack")
        possible_move = ["look around", "map", "info", "check backpack"]
        if not lab.player.current_chamber.items == []:
            print("take item")
            possible_move.append("take item")
        if not lab.player.items == []:
            print("drop item")
            possible_move.append("drop item")
        if not lab.player.current_chamber.doors == []:
            print("check doors")
            print("change chamber")
            possible_move.append("check doors")
            possible_move.append("change chamber")

        while True:
            choice = input("\n>>>")
            if choice in possible_move:

                if choice == "look around":
                    print(lab.player.look_around())
                    break

                elif choice == "map":
                    print(lab.map)
                    break

                elif choice == "info":
                    print(lab.player.get_info())
                    break

                elif choice == "check backpack":
                    print(lab.player.get_items())
                    break

                elif choice == "take item":
                    print("Choose item:")
                    print(lab.player.current_chamber.get_items())
                    while True:
                        choice_item = input(">>>")
                        if choice_item in [str(i) for i in range(len(lab.player.current_chamber.items))]:
                            lab.player.take_item(lab.player.current_chamber.items[int(choice_item)])
                            break
                        else:
                            print("Sorry, I don't understand you. Choose possible item.")
                    break

                elif choice == "drop item":
                    print("Choose item:")
                    print(lab.player.get_items())
                    while True:
                        choice_item = input("\n>>>")
                        if choice_item in [str(i) for i in range(len(lab.player.items))]:
                            lab.player.drop_item(lab.player.items[int(choice_item)])
                            break
                        else:
                            print("Sorry, I don't understand you. Choose possible item.")
                    break

                elif choice == "check doors":
                    print(lab.player.check_doors())
                    break

                elif choice == "change chamber":
                    print("Choose door:")
                    print(lab.player.current_chamber.get_doors())
                    while True:
                        choice_door = input("\n>>>")
                        if choice_door in [str(i) for i in range(len(lab.player.current_chamber.doors))]:
                            print("Possible moves:")
                            print("open")
                            while True:
                                choice_move = input("\n>>>")
                                if choice_move == "open":
                                    print(lab.player.open_door(lab.player.current_chamber.doors[int(choice_door)]))
                                    if lab.player.current_chamber.doors[int(choice_door)].status == "open":
                                        print("Possible moves:")
                                        print("go through the door")
                                        print("go back")
                                        while True:
                                            choice_next_move = input("\n>>>")
                                            if choice_next_move == "go through the door":
                                                print(lab.player.change_chamber(lab.player.current_chamber.doors[int(choice_door)]))
                                                break
                                            elif choice_next_move == "go back":
                                                break
                                            else:
                                                print("Sorry, I don't understand you. Choose possible move.")
                                        break
                                    break
                                else:
                                    print("Sorry, I don't understand you. Choose possible move.")
                            break
                        else:
                            print("Sorry, I don't understand you. Choose possible item.")
                    break
            else:
                print("Sorry, I don't understand you. Choose possible move.")


if __name__ == "__main__":
    game()
