import sys
from argparse import ArgumentParser
import pandas as pd

df = pd.read_csv('exercise_data.csv')
df.drop('Unnamed: 0', inplace=True, axis=1)

class Program:
    def __init__(self, difficulty, split):
        """Initalize difficuly, split, and number of exercises/sets"""
        self.difficulty = difficulty
        self.split = split

        if self.difficulty == 'a':
            self.exercise_nums = (2, 2, 2, "5x10-6", "4x8", "3x10")
        elif self.difficulty == 'i':
            self.exercise_nums = (2, 2, 2, "4x10-8", "3x10", "3x10")
        elif self.difficulty == 'b':
            self.exercise_nums = (1, 1, 2, "4x10", "3x10", "3x12")
    
    def write_program(self):
        """Formats a program given a user's split"""
        if self.split == 'legs':
            user_program = self.legs()
        elif self.split == 'push':
            user_program = self.push()
        elif self.split == 'pull':
            user_program = self.pull()
        self.export_program(user_program)
    
    def legs(self):
        """Formats a leg day program"""
        self.leg_day = pd.DataFrame

        main_legs = main_lift[main_lift['primaryMuscleGroups'].apply(lambda x: 'legs' in x)]
        less_back = main_legs[main_legs['primaryMuscles'].apply(lambda x: 'quadriceps' in x)]
        select_from_main = less_back.sample(n=self.exercise_nums[0])

        sec_legs = secondary_lift[secondary_lift['primaryMuscleGroups'].apply(lambda x: 'legs' in x)]
        select_from_sec = sec_legs.sample(n=self.exercise_nums[1])

        iso_legs = isolation[isolation['primaryMuscleGroups'].apply(lambda x: 'legs' in x)]
        select_from_iso = iso_legs.sample(n=2)

        self.leg_day = pd.concat([select_from_main, select_from_sec, select_from_iso], ignore_index=True)
        return self.leg_day
    
    def push(self):
        """Formats a push day program"""
        self.push_day= pd.DataFrame

        main1 = main_lift[main_lift['primaryMuscleGroups'].apply(lambda x: 'chest' in x)]
        selectmain1 = main1.sample()
        if self.difficulty != 'b':
            main2 = main_lift[main_lift['primaryMuscleGroups'].apply(lambda x: 'shoulders' in x)]
            selectmain2 = main2.sample()

        sec1 = secondary_lift[secondary_lift['primaryMuscleGroups'].apply(lambda x: 'shoulders' in x)]
        selectsec1 = sec1.sample()
        if self.difficulty != 'b':
            sec2 = secondary_lift[secondary_lift['primaryMuscleGroups'].apply(lambda x: 'chest' in x)]
            selectsec2 = sec2.sample()

        iso1 = isolation[isolation['primaryMuscles'].apply(lambda x: 'triceps' in x)]
        selectiso1 = iso1.sample()

        iso2 = isolation[isolation['primaryMuscleGroups'].apply(lambda x: 'chest' in x)]
        selectiso2 = iso2.sample()

        if self.difficulty != 'b':
            self.push_day = pd.concat([selectmain1, selectmain2, selectsec1, selectsec2, selectiso1, selectiso2], ignore_index=True)
        else:
            self.push_day = pd.concat([selectmain1, selectsec1, selectiso1, selectiso2], ignore_index=True)
        return self.push_day
    
    def pull(self):
        """Formats a pull day program"""
        self.pull_day = pd.DataFrame()

        main_pull = main_lift[main_lift['primaryMuscleGroups'].apply(lambda x: 'back' in x)]
        no_legs = main_pull[main_pull['primaryMuscleGroups'].apply(lambda x: 'legs' not in x)]
        select_from_main = no_legs.sample(n = self.exercise_nums[0])

        sec_pull = secondary_lift[secondary_lift['primaryMuscleGroups'].apply(lambda x: 'back' in x)]
        select_from_sec = sec_pull.sample(n = self.exercise_nums[1])

        iso1 = isolation[isolation['primaryMuscles'].apply(lambda x: 'biceps' in x)]
        selectiso1 = iso1.sample()

        iso2 = isolation[isolation['primaryMuscleGroups'].apply(lambda x: 'back' in x)]
        selectiso2 = iso2.sample()

        self.pull_day = pd.concat([select_from_main, select_from_sec, selectiso1, selectiso2], ignore_index = True)
        return self.pull_day
    
    def export_program(self, program):
        """writes program to a text file"""
        self.program = program
        filepath = 'workout_program.txt'
        with open(filepath, "w") as file:
            file.write(f"Here is your workout program for {self.split} day:\n")
            for index, row in self.program.iterrows():
                file.write(f"{row['name']}:\n")
                file.write(f"\t{row['instructions']}\n")
                if row['equipment'] == 'barbell' and row['type'] == 'compound':
                    file.write(f"\tPerform this exercise {self.exercise_nums[3]} times\n")
                elif row['equipment'] == 'dumbbells' and row['type'] == 'compound':
                    file.write(f"\tPerform this exercise {self.exercise_nums[4]} times\n")
                elif row['type'] == 'isolation':
                    file.write(f"\tPerform this exercise {self.exercise_nums[5]} times\n")

def parse_args(args_list):
    """parse command-line arguments"""
    parser = ArgumentParser() 
    parser.add_argument("difficulty", choices=['b','i','a'], help= "what is the user's desired difficulty level? (b - beginner, i - intermediate, a - advanced)")
    parser.add_argument("split", choices = ['push', 'pull', 'legs'], help = "what muscle group does the user wish to work? (push, pull, or legs)") 
    return parser.parse_args(args_list)

if __name__ == "__main__":
    main_lift = df.loc[df['equipment']=='barbell'].loc[df['type']=='compound']
    secondary_lift = df.loc[df['equipment'] == 'dumbbells'].loc[df['type'] == 'compound']
    isolation = df.loc[df['type'] == 'isolation']

    args = parse_args(sys.argv[1:])
    user_choice = Program(args.difficulty, args.split)
    user_choice.write_program()