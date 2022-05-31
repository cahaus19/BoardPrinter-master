class Action:

    def get_user_action(self) -> str:
        print('Select your action from the list below.')
        print('1. Fill Spot')
        print('2. Erase Spot')
        print('3. Switch Board')
        print('4. Create Board')
        print('5. Quit')
        print()
        action = input('Enter the number of the action you would like to do: ')
        return action


