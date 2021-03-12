import pandas as pd


def parse_preferences(csv_path):
	""" 
	Takes in path to csv file
	Returns dictionary of mentor / mentee to their preferences
	"""	
	df = pd.read_csv(csv_path, sep=',')

	mentor_preferences = {}

	for i in range(len(df)):
		mentees = []
		for j in range(1, len(df.columns)):
			if (not pd.isnull(df.iloc[i][j])):
				mentees.append(df.iloc[i][j])
		mentor_preferences[df.iloc[i][0]] = mentees
	return mentor_preferences

def parse_num_mentees(csv_path):
	df = pd.read_csv(csv_path, sep=',')

	mentees_per_mentor = {}

	for i in range(len(df)):
		mentees_per_mentor[df.iloc[i][0]] = df.iloc[i][1]
	return mentees_per_mentor

def check_mentors_mentees(mentor_preferences, mentee_preferences):
	mentors = list(mentor_preferences.keys())
	mentor_preferences_list = list(mentor_preferences.values())
	mentees = list(mentee_preferences.keys())
	mentee_preferences_list = list(mentee_preferences.values())
	for mentee in mentor_preferences_list:
		if mentee not in mentees:
			print("error")
	for mentor in mentee_preferences_list:
		if mentor not in mentors:
			print("error")