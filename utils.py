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

def parse_mentee_do_nots(csv_path):
	df = pd.read_csv(csv_path, sep=',')

	mentees_do_not_per_mentor = {}

	for i in range(len(df)):
		mentees = []
		for j in range(1, len(df.columns)):
			if (not pd.isnull(df.iloc[i][j])):
				mentees.append(df.iloc[i][j])
		mentees_do_not_per_mentor[df.iloc[i][0]] = mentees
	return mentees_do_not_per_mentor

