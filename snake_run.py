from snake_agent import train, test


def menu():

    print("=" * 40)

    print("      SNAKE RL")

    print("=" * 40)

    print("1 Train Agent")

    print("2 Test Agent")

    print("3 Exit")

    print("=" * 40)

    choice = input("Choice: ")

    if choice == "1":

        episodes = int(

            input(

                "Episodes (1000 recommended): "

            )

        )

        train(

            render=True,

            episodes=episodes

        )

    elif choice == "2":

        test()

    else:

        print("Bye!")


if __name__ == "__main__":

    menu()