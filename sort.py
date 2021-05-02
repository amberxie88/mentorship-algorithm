from utils import parse_preferences, parse_num_mentees, check_mentors_mentees, parse_emails, check_grade, check_matching_email
import csv

def sort(mentee_preferences_csv, mentor_preferences_csv, mentees_per_mentor_csv, mentors_email=None, mentees_email=None):
    # Assume the total number of mentees matches up this
    mentees_per_mentor = parse_num_mentees(mentees_per_mentor_csv)

    # Mentors and mentees rank their top 3 preferences
    # Assume that every mentor or mentee is part of someone's top 3
    mentor_preferences = parse_preferences(mentor_preferences_csv)
    mentee_preferences = parse_preferences(mentee_preferences_csv)
    check_mentors_mentees(mentor_preferences, mentee_preferences)

    #creates lists of email/grade levels
    if (mentors_email):
        mentor_info = parse_emails(mentors_email)
        check_matching_email(mentor_preferences.keys(), mentor_info)
    else:
        print("No mentor emails found")
        mentor_info = None
    
    if (mentees_email):
        mentee_info = parse_emails(mentees_email)
        check_matching_email(mentee_preferences.keys(), mentee_info)
    else:
        print("No mentee emails found")
        mentee_info = None

    mentor_mentee_list, lingering_mentees = run_sort_alg(mentor_preferences, mentee_preferences, mentees_per_mentor, mentor_info, mentee_info)
  
    report_results(mentor_mentee_list, lingering_mentees, mentor_info, mentee_info)

def run_sort_alg(mentor_preferences, mentee_preferences, mentees_per_mentor, mentor_info=None, mentee_info=None):

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
                if (mentor_info and mentee_info):
                    check_grade(mentor_info, mentee_info, mentor_to_propose_to, mentee)
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

    return mentor_mentee_list, lingering_mentees

def report_results(mentor_mentee_list, lingering_mentees, mentor_emails, mentee_emails):
    results = []
    for mentor in mentor_mentee_list:
        result = [mentor]
        result.extend(mentor_mentee_list[mentor])
        results.append(result)
        if mentor_emails:
            result = [mentor_emails[mentor][0]]
            if mentee_emails:
                for mentee in mentor_mentee_list[mentor]:
                    result.extend([mentee_emails[mentee][0]])
            results.append(result)

    with open('sample_data/ashley_results.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(["Mentor", "Mentee 1", "Mentee 2", "Mentee 3"])
        writer.writerows(results)

    with open('sample_data/ashley_lingering.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(["Lingering Mentees"])
        writer.writerows(zip(lingering_mentees))

	# how many mentors were paired with their top 1, 2, 3 choicesmentor_top_choice_counts = [0,0,0]
    for mentor in mentors:
    	if (mentor_preferences[mentor][0] in mentor_mentee_list[mentor]):
        	mentor_top_choice_counts[0] += 1
	    if (mentor_preferences[mentor][1] in mentor_mentee_list[mentor]):
            mentor_top_choice_counts[1] += 1
	    if (mentor_preferences[mentor][2] in mentor_mentee_list[mentor]):
		    mentor_top_choice_counts[2] += 1
	
	    mentee_top_choice_counts = [0,0,0]
	    for mentee in mentees:
			mentor = mentee_preferences[mentee][0]
			if (mentee in mentor_mentee_list[mentor]):
				mentee_top_choice_counts[0] += 1
			mentor = mentee_preferences[mentee][1]
			if (mentee in mentor_mentee_list[mentor]):
				mentee_top_choice_counts[1] += 1
			mentor = mentee_preferences[mentee][2]
			if (mentee in mentor_mentee_list[mentor]):
				mentee_top_choice_counts[2] += 1

	for i in range(3):
		print(str(mentor_top_choice_counts[i]) + " mentors are paired with their rank " + str(i+1) + " choice")
		print(str(mentee_top_choice_counts[i]) + " mentees are paired with their rank " + str(i+1) + " choice")
