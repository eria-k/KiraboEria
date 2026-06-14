"""
WORLD CUP 2026 SIMULATION
Uses while loop, break, continue, and pass.
"""

import random

# Initial team stats
team_strength = 70
team_morale = 75
injuries = 0
matches_played = 0

group_matches = 3
group_wins_needed = 2
group_wins = 0
current_stage = "Preparation"

print("\n🏆 WORLD CUP 2026 SIMULATION 🏆")
print("You are the team manager. Make choices to lead your team to glory!\n")

# Main tournament loop
tournament_active = True
while tournament_active:

    # ----- PREPARATION PHASE -----
    if current_stage == "Preparation":
        print("\n=== PRE-TOURNAMENT PREPARATION ===")
        print(f"Team strength: {team_strength} | Morale: {team_morale} | Injuries: {injuries}")
        print("Choose an action:")
        print("1. Hard training (+strength, risk of injury)")
        print("2. Light training (small boost, no injury)")
        print("3. Team bonding (+morale)")
        print("4. Rest players (recover from injuries)")

        choice = input("Your choice (1-4): ")

        if choice == "1":
            team_strength += random.randint(5, 10)
            if random.random() < 0.3:
                injuries += 1
                print("⚠️ A player got injured during hard training!")
            print(f"✅ Strength increased to {team_strength}. Injuries: {injuries}")

        elif choice == "2":
            team_strength += random.randint(1, 5)
            print(f"✅ Strength increased to {team_strength}. No injuries.")

        elif choice == "3":
            team_morale += random.randint(5, 15)
            if team_morale > 100:
                team_morale = 100
            print(f"✅ Morale improved to {team_morale}")

        elif choice == "4":
            # pass as placeholder for future detailed recovery menu
            pass
            if injuries > 0:
                injuries -= 1
                print(f"🩹 One player recovered. Injuries now: {injuries}")
            else:
                print("No injuries to recover.")
        else:
            print("Invalid choice. Try again.")
            continue   # skip rest of iteration, stay in preparation

        ready = input("\nStart group stage? (yes/no): ").lower()
        if ready == "yes":
            current_stage = "Group Stage"
            print("\n⚽ Moving to GROUP STAGE ⚽")
        else:
            continue   # more preparation days

    # ----- GROUP STAGE (3 matches) -----
    elif current_stage == "Group Stage":
        print("\n=== GROUP STAGE ===")
        for match in range(1, group_matches + 1):
            print(f"\n--- Match {match} of {group_matches} ---")

            # continue: skip match if morale too low
            if team_morale < 20:
                print("Team morale is critically low! The team forfeits the match.")
                print("😞 FORFEIT → LOSS")
                # Recorded as loss (no win, no draw)
                # group_wins unchanged, no extra win
                # No strength/morale changes from simulation
                continue

            # Simulate match result
            win_chance = (team_strength / 100) - (injuries * 0.05)
            win_chance = max(0.1, min(0.95, win_chance))
            result = random.choices(["win", "lose", "draw"], weights=[win_chance, 0.2, 0.2])[0]

            if result == "win":
                print("🎉 WIN! Great performance!")
                group_wins += 1
                team_morale += 10
                team_strength += random.randint(1, 5)
            elif result == "lose":
                print("😞 LOSS. Need to regroup.")
                team_morale -= 10
                if random.random() < 0.2:
                    injuries += 1
                    print("⚠️ A player got injured!")
            else:
                print("🤝 DRAW. Could be worse.")
                team_morale += 2

            team_strength = max(0, min(100, team_strength))
            team_morale = max(0, min(100, team_morale))
            injuries = max(0, min(5, injuries))

            print(f"Strength: {team_strength}, Morale: {team_morale}, Injuries: {injuries}")

            # pass placeholder for injury recovery menu
            if injuries >= 3:
                pass   # future: show injured players and allow treatment

        # After group stage, check qualification
        if group_wins >= group_wins_needed:
            print(f"\n✅ Qualified for knockout stage! (Wins: {group_wins})")
            current_stage = "Knockout"
            group_wins = 0
        else:
            print(f"\n❌ Eliminated in group stage. (Wins: {group_wins} needed {group_wins_needed})")
            tournament_active = False   # break out of main loop
            break   # exit while loop

    # KNOCKOUT STAGES (4 rounds: R16, QF, SF, Final) 
    elif current_stage == "Knockout":
        rounds = ["Round of 16", "Quarter-final", "Semi-final", "Final"]
        round_index = 0

        while round_index < len(rounds):
            current_round = rounds[round_index]
            print(f"\n=== {current_round} ===")

            # continue example: if morale too low, forfeit (actually breaks)
            if team_morale < 30:
                print("Team morale is too low to compete! You forfeit the match.")
                print(f"❌ Eliminated in {current_round} due to low morale.")
                tournament_active = False
                break

            win_chance = (team_strength / 100) - (injuries * 0.05)
            win_chance = max(0.1, min(0.95, win_chance))
            result = random.choices(["win", "lose"], weights=[win_chance, 1-win_chance])[0]

            if result == "win":
                print(f"✅ VICTORY! You advance to the next round.")
                team_morale += 15
                team_strength += random.randint(2, 8)
                team_strength = min(100, team_strength)
                team_morale = min(100, team_morale)
                round_index += 1
                if current_round == "Final":
                    print("\n🏆🏆🏆 YOU HAVE WON THE WORLD CUP 2026! 🏆🏆🏆")
                    tournament_active = False
                    break
                else:
                    continue   # go to next round
            else:
                print(f"❌ DEFEAT in {current_round}. Your journey ends here.")
                tournament_active = False
                break

# End of simulation
print("\n=== TOURNAMENT SIMULATION ENDED ===")
if not tournament_active:
    # check for championship
    if current_stage == "Knockout" and "Final" in locals() and result == "win":
        print("🏆 Congratulations! World Champions! 🏆")
    else:
        print("Better luck next time. Keep improving your team!")