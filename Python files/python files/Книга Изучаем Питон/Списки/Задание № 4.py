People = ['Abraham Linkoln','Papich','Nikola Tesla']
will_not_come = People.pop(1)
People.insert(1,'Stalin')
will_come = People[1]
print(f"Unfortunatally {will_not_come} can't visit my party, but {will_come} will come instead of him")
print ("Finally i wait:\t\n",People[0],People[1],People[2])

