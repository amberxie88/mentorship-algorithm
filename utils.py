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
			if ((not pd.isnull(df.iloc[i][j])) & (df.iloc[i][j] not in mentees)):	# no duplicates
				mentees.append(df.iloc[i][j])
		mentor_preferences[df.iloc[i][0]] = mentees
	return mentor_preferences

def parse_num_mentees(csv_path):
	df = pd.read_csv(csv_path, sep=',')

	mentees_per_mentor = {}

	for i in range(len(df)):
		mentees_per_mentor[df.iloc[i][0]] = df.iloc[i][1]
	return mentees_per_mentor

#NEW
def parse_attributes(csv_path):
	df = pd.read_csv(csv_path, sep=',')
	allpeople = {}

	columns = list(df.columns)
	#iterate through rows
	for i in range(len(df)):
		individual_data = {}
		#iterate through columns(attributes)
		for j in range(1, len(df.columns)):
			attribute = columns[j]
			individual_data[attribute] = df.iloc[i][j]
		allpeople[df.iloc[i][0]] = individual_data
	print(allpeople)
	return allpeople



def check_mentors_mentees(mentor_preferences, mentee_preferences):
	mentors = list(mentor_preferences.keys())
	mentees_in_mentor_preferences = list(mentor_preferences.values())
	#flattening the mentees_in_mentor_preferences into one list, not  a list of lists
	mentees_to_check = []
	for sublist in mentees_in_mentor_preferences:
		for item in sublist:
			mentees_to_check.append(item)


	mentees = list(mentee_preferences.keys())
	mentors_in_mentee_preferences = list(mentee_preferences.values())
	#flattening the mentorss_in_mentee_preferences into one list, not  a list of lists
	mentors_to_check = []
	for sublist in mentors_in_mentee_preferences:
		for item in sublist:
			mentors_to_check.append(item)

	for mentee in mentees_to_check:
		assert mentee in mentees, "Mentee" + mentee + " is not a mentee"
	for mentor in mentors_to_check:
		assert mentor in mentors, "Mentor" + mentor + " is not a mentor" 
