import requests
import pandas as pd

"""fetches list of exercises w/ data from API"""
url = "https://advanced-exercise-finder.p.rapidapi.com/"

payload = {"query": "query allExercises {allExercises {name equipment primaryMuscleGroups primaryMuscles secondaryMuscleGroups type tags instructions}}", "variables": {}}

headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "3a544f53c3msh3f23c9e06ff7419p1fb61djsn38bd631c47f3",
	"X-RapidAPI-Host": "advanced-exercise-finder.p.rapidapi.com"
    }

response = requests.post(url, json=payload, headers=headers)

"""makes a copy of the query response"""
exercises = list()

for data in response.json().values():
    for exercise_list in data.values():
        for exercise in exercise_list:
            exercises.append(exercise)

"""creates dataframe"""
df = pd.DataFrame()
exercise_data = list()

for exercise in exercises:
    single_df = pd.DataFrame.from_dict(exercise, orient = 'index')
    single_df = single_df.transpose()
    exercise_data.append(single_df)

df = pd.concat(exercise_data, ignore_index=True)

"""exports dataframe to csv"""
df.to_csv('exercise_data.csv', encoding='utf-8')
