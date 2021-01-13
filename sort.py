# TODO: Create parsing algorithm that will return this information

# Assume the total number of mentees matches up this
mentees_per_mentor = {
	"A1": 2, 
	"A2": 1, 
	"A3": 4, 
	"A4": 2
}

# Mentors and mentees rank their top 3 preferences
# Assume that every mentor or mentee is part of someone's top 3
TOP_X = 3
mentor_preferences = {
	"A1": ["Z3", "Z1", "Z4"], 
	"A2": ["Z8", "Z9", "Z2"], 
	"A3": ["Z3", "Z2", "Z4"], 
	"A4": ["Z5", "Z7", "Z6"]
}

mentee_preferences = {
	"Z1": ["A1", "A2", "A3"], 
	"Z2": ["A2", "A1", "A3"], 
	"Z3": ["A4", "A2", "A1"], 
	"Z4": ["A3", "A2", "A1"],
	"Z5": ["A1", "A2", "A4"],
	"Z6": ["A1", "A3", "A2"],
	"Z7": ["A1", "A4", "A3"],
	"Z8": ["A1", "A2", "A3"],
	"Z9": ["A1", "A3", "A4"]
}

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

		if (proposal_index >= TOP_X):
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

			# Mentees that didn't make the cut will propose again
			for extra_mentee in proposed_mentees.difference(mentees_to_keep):
				rejected_mentees.add(extra_mentee)
			mentor_mentee_list[mentor] = mentees_to_keep

for mentor in mentors:
	print(mentor, mentor_mentee_list[mentor])
print(lingering_mentees)
