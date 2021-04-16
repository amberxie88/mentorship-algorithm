# Mentorship Algorithm
A matching algorithm for mentors and mentees. Runs a variation of stable matching on the provided inputs. Features include (1) Verification / error-processing to make sure that mentors listed as preferences actually exist on the mentor csv, etc. (2) Variable length preferences for mentors / mentees.

## Inputs
```mentor_preferences.csv```: The preference form mentors fill out for ranking their preferred mentees

```mentee_preferences.csv```: The preference form mentees fill out for ranking their prefered mentors

```mentors_per_mentee.csv```: The number of mentees each mentor is willing to take on

## Output
The mentor / mentee families, printed in csv form, and any lingering mentees that remained unmatched

## Next Steps 
1. Take in mentor and mentee do-not-pairs. Some mentors or mentees already know other participants and would prefer to not be paired to them.
2. Generate randomized extra preferences. The current TOP_X framework is not ideal, because it does not guarantee matchings for everyone. 
3. Take in years (freshman, sophomore, junior), as to ensure that a sophomore mentor is not paired to a sophomore mentee
4. Output a csv (instead of just printing it), and / or any extra details that may be relevant, like email, grade, etc.
