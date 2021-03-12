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

def parse_extra_preferences(csv_path):
	""" 
	Takes in path to csv file
	Returns dictionary of mentor / mentee to their top 3 preferences
	With non-top 3 preferences, 
	"""	
	df = pd.read_csv(csv_path, sep=',')

	mentor_preferences = {}
	extra_mentor_preferences = {}

	for i in range(len(df)):
		mentees = []
		for j in range(1, 4):		# only go thru top 3 preferences
			if (not pd.isnull(df.iloc[i][j])):
				mentees.append(df.iloc[i][j])
		mentor_preferences[df.iloc[i][0]] = mentees
		for k in range(4, len(df.columns)):		# go thru the extra preferences
			if (not pd.isnull(df.iloc[i][k])):
				mentees.append(df.iloc[i][k])
		extra_mentor_preferences[df.iloc[i][0]] = mentees
	return mentor_preferences, extra_mentor_preferences	

def parse_num_mentees(csv_path):
	df = pd.read_csv(csv_path, sep=',')

	mentees_per_mentor = {}

	for i in range(len(df)):
		mentees_per_mentor[df.iloc[i][0]] = df.iloc[i][1]
	return mentees_per_mentor