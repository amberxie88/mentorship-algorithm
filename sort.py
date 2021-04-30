from utils import parse_preferences, parse_num_mentees, check_mentors_mentees, parse_attributes
import csv

def sort(mentee_preferences_csv, mentor_preferences_csv, mentees_per_mentor_csv):
	#NEW
	#info = parse_attributes(info_csv)

	# Assume the total number of mentees matches up this
	mentees_per_mentor = parse_num_mentees(mentees_per_mentor_csv)

	# Mentors and mentees rank their top 3 preferences
	# Assume that every mentor or mentee is part of someone's top 3
	mentor_preferences = parse_preferences(mentor_preferences_csv)
	mentee_preferences = parse_preferences(mentee_preferences_csv)
	check_mentors_mentees(mentor_preferences, mentee_preferences)

	mentor_mentee_list, lingering_mentees = run_sort_alg(mentor_preferences, mentee_preferences, mentees_per_mentor)
	mentor_mentee_list = pair_lingering_mentees(mentor_mentee_list, lingering_mentees, mentees_per_mentor_csv)

	report_results(mentor_preferences.keys(), mentor_mentee_list, lingering_mentees)

def run_sort_alg(mentor_preferences, mentee_preferences, mentees_per_mentor):

	# Some useful information
	mentors = mentor_preferences.keys()
	mentees = mentee_preferences.keys()

	num_mentors = len(mentors)
	num_mentees = len(mentees)


	# Useful data structures for sorting algorithm
	mentee_proposal_index = {}
	for mentee in mentees:
		mentee_proposal_index[mentee] = 0

	rejected_mentees = set()
	for mentee in mentees:
		rejected_mentees.add(mentee)

	mentor_mentee_list = {}
	for mentor in mentors:
		mentor_mentee_list[mentor] = set()

	lingering_mentees = set()

	i = 0
	while True: 
		i += 1
		if i == 10:
			break
		# Iterate through mentee proposals
		for mentee in rejected_mentees:
			# Find next mentor to propose to
			proposal_index = mentee_proposal_index[mentee]
			if (proposal_index >= len(mentee_preferences[mentee])):
				lingering_mentees.add(mentee)
			else:
				# Propose to said mentor
				mentor_to_propose_to = mentee_preferences[mentee][proposal_index]

				mentor_mentee_list[mentor_to_propose_to].add(mentee)
				mentee_proposal_index[mentee] += 1

		# No more rejected mentees, so reset
		rejected_mentees = set()

		# Mentors go through their choices
		for mentor in mentors:
			proposed_mentees = mentor_mentee_list[mentor]
			desired_num_mentees = mentees_per_mentor[mentor]
			num_extra_mentees = len(proposed_mentees) - desired_num_mentees

			# Proposed mentees is more than desired
			if (num_extra_mentees > 0):
				# Create a new set of mentees no more than the desired number
				mentees_to_keep = set()
				for desired_mentee in mentor_preferences[mentor]:
					if (desired_mentee in proposed_mentees):
						mentees_to_keep.add(desired_mentee)
					if (len(mentees_to_keep) == desired_num_mentees):
						break

				add_back = desired_num_mentees - len(mentees_to_keep)
				for extra_mentee in proposed_mentees.difference(mentees_to_keep):
					if (add_back > 0):
						# Add back some mentees semi-randomly
						mentees_to_keep.add(extra_mentee)
						add_back -= 1
					else:
						# Mentees that didn't make the cut will propose again
						rejected_mentees.add(extra_mentee)
				mentor_mentee_list[mentor] = mentees_to_keep
		print("Mentor mentee list")
		print(mentor_mentee_list)
		print("mentees per mentor")
		print(mentees_per_mentor)

	return mentor_mentee_list, lingering_mentees

def pair_lingering_mentees(mentor_mentee_list, lingering_mentees, mentees_per_mentor_csv):
	mentees_per_mentor = parse_num_mentees(mentees_per_mentor_csv)
	while (len(lingering_mentees) > 0):
		for m in mentees_per_mentor:
			while (mentees_per_mentor[m] <= len(mentor_mentee_list[m])):
					mentor_mentee_list[m].append(lingering_mentees.pop(0))
	return mentor_mentee_list

def report_results(mentors, mentor_mentee_list, lingering_mentees):
	#for mentor in mentors:
	#	print("Mentor: ", mentor, "\tMentees: ", mentor_mentee_list[mentor])
	#print("Lingering mentees: ", lingering_mentees)

	for mentor in mentors:
		print(mentor,end=',')
		for mentee in mentor_mentee_list[mentor]:
			print(mentee, end=',')
		print()
	print("Lingering mentees: ", lingering_mentees)


