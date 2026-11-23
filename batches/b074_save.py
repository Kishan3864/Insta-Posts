import sys; sys.path.insert(0, "tools"); from save_post import save
S = dict
print(save(386,"SINGLE","India","Vermicompost","Vermicompost unit",["p386_vermi"],
"""Bed and order tracking app for vermicompost units: see the week of every compost bed, know when it will be ready, and fill buyer orders from the beds that are ready first.
Buyers get a clear date, not a guess.
Make vermicompost or organic manure? DM us.""", 2,
["#vermicompost","#organicmanure","#organicfarmingindia","#compostbusiness"],
["Cream, brown and green design with the headline 'Buyer asks: Is it ready? Track every bed by week.' Six drawn compost beds on an 8-week cycle with 25 kg bags, sample: Bed 1 week 8 ready now about 40 bags, Bed 2 week 7 ready next week about 38 bags, Bed 3 week 5 ready in 3 weeks, Bed 4 week 3 ready in 5 weeks, Bed 5 week 1 ready in 7 weeks, Bed 6 empty for refill. Orders filled from the beds that are ready first: O-11 Sample Nursery 30 bags this week from Bed 1; O-12 Sample Farmer Group 45 bags next week from Bed 1 and Bed 2; O-13 Sample Garden Shop 12 bags in 3 weeks from Bed 2 and Bed 3. An auto message: O-12, 45 bags ready next week from Bed 1 and Bed 2."],
 S(scroll=8,save=8,send=8,clarity=9,finish=9,original=9)))
print(save(387,"CAROUSEL","India","TractorRepair","Tractor repair workshop",[f"p387_tractor_s{i}" for i in range(1,6)],
"""Workshop app for tractor repair garages: a job card at the gate with photos and problem, one status board for every tractor, parts ordered with arrival days, a ready message and full repair history.
Fewer calls asking "is it done?", even in harvest season.
Repair tractors or farm machines? DM us.""", 4,
["#tractorrepair","#tractormechanic","#farmmachinery","#tractorworkshop","#agricultureindia"],
["Cream, black and orange design with the headline '8 tractors in the yard? Give each one a job card.' A top-down drawing of a workshop yard with eight tractors in bays, each with a job tag J-201 to J-208 and coloured by status: checking, waiting for parts, working or ready. Three problems: is my tractor done, which part did we order, what did you fix last time.",
 "Step 1, job card at the gate: a paper job card J-204 for a sample farmer from a sample village, tractor Sample 45 HP, hour meter 3,420 hours, in at Monday 9:10 AM, problems oil leak, lift slow and check brakes, three photo boxes and promised Wednesday evening. A message to the farmer confirms the job, and a card shows who sees it: mechanic, parts counter and owner.",
 "Step 2, see what is waiting: a board with four columns, two jobs each, sample: checking J-204 and J-207, waiting for parts J-202 and J-206, working J-201 and J-205, ready J-203 and J-208, each with its promised day. Parts ordered: hydraulic pump seal kit arrives Thursday, radiator core arrives Wednesday, clutch plate in stock, gear lever bush check first.",
 "Step 3, ready message and history: a message on Wednesday at 5:40 PM saying the Sample 45 HP is ready with the work done, bill attached and old parts kept. A repair history for the tractor from March 2025 to November 2026 with hours and work done, and the next service due at about 3,670 hours with a reminder by message.",
 "Closing slide with the headline 'Repair tractors? Let's build your workshop app.' The yard drawing with counts of 2 checking, 2 waiting for parts, 2 working and 2 ready, four tiles: job cards, status board, parts list and history, and the question: how do farmers ask about their tractor today, calls or visits? Tell us in the comments."],
 S(scroll=8,save=9,send=8,clarity=9,finish=9,original=9)))
print(save(388,"SINGLE","USA","MobileMechanic","Mobile mechanic (driveway repairs)",["p388_mobilemech"],
"""Booking and parts app for mobile mechanics: customers enter year, model, engine and the problem, parts are picked before you drive, and the van is loaded one bin per stop.
The right part on the van, the first time.
Fix cars at the customer's home? DM us.""", 3,
["#mobilemechanic","#mobilecarrepair","#automechanic","#smallbusinessusa"],
["Grey, navy and yellow design with the headline 'Wrong part on the van? Get the car details first.' A booking form M-41: 2017 sample sedan, 2.0 L 4 cylinder engine, front brakes squeak, photo of the VIN sticker added, driveway at ZIP 00011, with an arrow to a dark card of parts picked: front pads, front rotors x2 and brake cleaner. A drawing of a cargo van seen from the side with two shelves of coloured bins, one per job: M-41 brake parts, M-42 battery and terminal kit, M-43 oil filter, oil and drain plug gasket, M-44 serpentine belt and tensioner. Today's route, sample: 8:30 AM M-41, 10:45 AM M-42 battery dead, 1:15 PM M-43 oil change, 3:30 PM M-44 belt squeal."],
 S(scroll=8,save=8,send=8,clarity=9,finish=9,original=9)))
print(save(389,"SINGLE","India","PetFoodShop","Pet food and supplies shop",["p389_petfood"],
"""Repeat order app for pet food shops: save each customer's bag size and daily grams, see how many days of food are left, and send a reminder before the bag runs out.
Regulars reorder from you, on time.
Run a pet shop? DM us.""", 5,
["#petshop","#petfood","#dogfood","#petsupplies"],
["Cream, orange and blue design with the headline 'Pet food bag ran out? Remind owners first.' Six regular customers, sample, each with a drawn food bag showing how much is left: C-11 dog 10 kg bag at 300 g a day bought 28 days ago, 5 days left; C-12 cat 3 kg, 30 days left; C-13 dog 3 kg, 3 days left; C-14 dog 4 kg, 23 days left; C-15 cat 1.5 kg, 3 days left; C-16 dog 15 kg, 7 days left. A green auto reminder for C-11: your dog's 10 kg food bag will finish in about 5 days, same bag again, with buttons yes deliver and pick up at shop. A dark card: due this week, 4 customers, C-13, C-15, C-11 and C-16."],
 S(scroll=8,save=8,send=9,clarity=9,finish=9,original=8)))
print(save(390,"SINGLE","USA","DonutShop","Donut shop (office pre-orders)",["p390_donut"],
"""Pre-order site for donut shops: offices order by the dozen the day before, pick a mix and a pickup time, and you get one bake list for the morning.
Every box ready at pickup time.
Run a donut or bakery shop? DM us.""", 2,
["#donutshop","#donuts","#officebreakfast","#bakerybusiness"],
["Cream, pink and chocolate design with the headline 'Office orders by text at 6 AM? Pre-order by the dozen.' Three open donut boxes with 12 drawn donuts each, sample: D-31 at 7:30 AM for Sample Office A with 4 glazed, 4 chocolate and 4 strawberry; D-32 at 8:00 AM for Sample Clinic Front Desk with 6 glazed, 3 maple and 3 chocolate; D-33 at 8:15 AM for Sample Law Office with 4 strawberry, 4 sprinkle and 4 maple. A dark 5 AM bake list for 36 donuts: glazed 10, chocolate 7, strawberry 8, maple 7, sprinkle 4. A pre-order form: name on the box, 1 dozen, pick 12 or shop's choice, pickup tomorrow at 7:30 AM, and orders close at 6 PM the day before."],
 S(scroll=8,save=8,send=8,clarity=9,finish=9,original=9)))
