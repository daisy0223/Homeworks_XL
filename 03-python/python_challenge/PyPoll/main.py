import os
import csv
#Set the path for the file
csvpath = os.path.join('/', 'Users', 'xllz', 'Desktop', 'GTbootcamp', 'Homeworks_XL', '03-python','PyPoll','Resources','election_data.csv')
print(csvpath)
#Open csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",") 
#Skip the header
    next(csvreader) 
#Initialize the total vote
    Total_vote=0
    Candidate_list=[]
    Candidate=[]
    Count_Khan=0
    Count_Correy=0
    Count_Li=0
    Count_OTooley=0
    Winner_rate=[]
#calculate number of total vote, complete list of candidates
    for row in csvreader:
        Total_vote+=1
        Candidate.append(row[2])
        if row[2] not in Candidate_list:
            Candidate_list.append(row[2])
 # count how many votes for each candiate and calculate percentage and formatting the final results   
    for i in Candidate:
        if i==Candidate_list[0]:
            Count_Khan+=1
            Rate_Khan=round(Count_Khan/Total_vote,3)
            Rate_Khan_format= format(Rate_Khan, ".3%")
        elif i==Candidate_list[1]:
            Count_Correy+=1
            Rate_Correy=round(Count_Correy/Total_vote,3)
            Rate_Correy_format= format(Rate_Correy, ".3%")
        elif i==Candidate_list[2]:
            Count_Li+=1
            Rate_Li=round(Count_Li/Total_vote,3)
            Rate_Li_format= format(Rate_Li, ".3%")
        elif i==Candidate_list[3]:
            Count_OTooley+=1
            Rate_OTooley=round(Count_OTooley/Total_vote,3)
            Rate_OTooley_format= format(Rate_OTooley, ".3%")
 # To find the winner, generate a list of voting rates for each candidate   
    Winner_rate= (Rate_Khan, Rate_Correy, Rate_Li, Rate_OTooley)
# find the maximum voting rate
    Winner_maximum=max(Winner_rate)
# find the index for the maximum voting rate in the list
    Winner_index=Winner_rate.index(Winner_maximum)
# the index is the same as the order in the candidate list
    Winner=Candidate_list[Winner_index]     
# Analysis output
    print("Election Results") 
    print("-----------------------------------------") 
    print(f"Total Votes: {Total_vote}")
    print("-----------------------------------------") 
    print(f"{Candidate_list[0]}: {Rate_Khan_format} ({Count_Khan})")
    print(f"{Candidate_list[1]}: {Rate_Correy_format} ({Count_Correy})")
    print(f"{Candidate_list[2]}: {Rate_Li_format} ({Count_Li})")
    print(f"{Candidate_list[3]}: {Rate_OTooley_format} ({Count_OTooley})")
    print("-----------------------------------------") 
    print(f"Winner: {Winner}")
    print("-----------------------------------------") 
# write output in a txt file
    Pypoll_output_file = os.path.join('/', 'Users', 'xllz', 'Desktop', 'GTbootcamp', 'Homeworks_XL', '03-python','python_challenge','PyPoll','Pypoll_output.txt')
    f=open(Pypoll_output_file, 'w')
    f.write("Election Results\n") 
    f.write("-----------------------------------------\n") 
    f.write(f"Total Votes: {Total_vote}\n")
    f.write("-----------------------------------------\n") 
    f.write(f"{Candidate_list[0]}: {Rate_Khan_format} ({Count_Khan})\n")
    f.write(f"{Candidate_list[1]}: {Rate_Correy_format} ({Count_Correy})\n")
    f.write(f"{Candidate_list[2]}: {Rate_Li_format} ({Count_Li})\n")
    f.write(f"{Candidate_list[3]}: {Rate_OTooley_format} ({Count_OTooley})\n")
    f.write("-----------------------------------------\n") 
    f.write(f"Winner: {Winner}\n")
    f.write("-----------------------------------------\n") 