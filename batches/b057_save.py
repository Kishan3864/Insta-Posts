import sys; sys.path.insert(0, "tools"); from save_post import save
S = dict
print(save(301,"SINGLE","India","ERickshawFleet","E-rickshaw fleet owner",["p301_erick"],
"""Battery and shift app for e-rickshaw fleet owners: see the charge of every battery in the shed, which rickshaw is on the road, who paid today's rent, and message the next driver when his battery is full.
No more calls asking "is my battery ready?"
Own a few e-rickshaws or more? DM us.""", 2,
["#erickshaw","#electricrickshaw","#evindia","#fleetowner"],
["Light grey and lime design with the headline 'Which battery is full? See all 8 at a glance.' A dark charging shed board, today 1:15 PM, sample, with eight drawn batteries: ER-01 100%, ready now; ER-02 85%, charging, full by 2:10 PM; ER-03 on the road; ER-04 55%, full by 3:30 PM; ER-05 95%, full by 1:40 PM; ER-06 30%, full by 5 PM; ER-07 on the road; ER-08 100%, ready now. Below, driver shifts and daily rent, sample: ER-03 morning 6 AM to 2 PM, paid; ER-07 morning, due; ER-05 evening 2 PM to 10 PM, next. A green message card: ER-05 will be full by 1:40 PM, pick it up at the shed for your 2 PM shift."],
 S(scroll=9,save=8,send=8,clarity=9,finish=9,original=9)))
print(save(302,"CAROUSEL","India","HandloomWeaver","Handloom weaving cluster (weavers at home)",[f"p302_loom_s{i}" for i in range(1,6)],
"""Yarn and loom tracking app for handloom saree businesses: write down every kg of yarn given to each weaver, see metres woven on each loom, get ready dates, and know how much yarn is still with each weaver.
No more guessing who has what.
Swipe for the 3 steps.
Give yarn to weavers who work at home? DM us.""", 4,
["#handloom","#handloomsaree","#weaversofindia","#handwoven"],
["Cream design with the headline 'Yarn with 6 weavers? Know where each saree is.' A drawn handloom with warp threads and a red saree with a teal border being woven: loom L-03, sample, 4.1 m of a 6.3 m saree woven, ready about Friday 27 November. A dark message bubble: How much yarn did I give loom 4? Was it 2 kg or 3? And when is the teal one ready?",
 "Step 1, every kg of yarn written once. A table, sample: L-01 turmeric 3 kg, Monday 9 November; L-02 peacock teal 2 kg, Tuesday 10 November; L-03 madder red 2.5 kg, Wednesday 11 November; L-04 turmeric 2 kg, Friday 13 November; L-05 indigo 3 kg, Monday 16 November; L-06 peacock teal 1.5 kg, Wednesday 18 November. Total 14 kg, 6 looms. Note: the weaver gets a message with the kg and colour, so nobody has to remember.",
 "Step 2, weavers send metres. Woven bars out of 6.3 m for each loom: L-01 6.3 m, ready to collect; L-02 5.2 m, Wednesday 25 November; L-03 4.1 m, Friday 27 November; L-04 2.6 m, Tuesday 1 December; L-05 1.4 m, Friday 4 December; L-06 0.5 m, Tuesday 8 December. Note: each evening the weaver taps the metres done, and ready dates update by themselves.",
 "Step 3, sarees in, yarn balance out. Three cards with saree icons: L-01 yarn given 3 kg, sarees back so far 2, yarn used 1 kg, still with weaver 2 kg; L-02 given 2 kg, 1 back, used 0.5 kg, 1.5 kg still with weaver; L-04 given 2 kg, 1 back, used 0.5 kg, 1.5 kg still with weaver. Note: sample rule, 1 saree uses 0.5 kg yarn, change it to your own design.",
 "Closing slide with the headline 'Give yarn to weavers? Let's build your loom book.' Three drawn looms at 5.2 m, 4.1 m and 2.6 m, four tiles: yarn book, metres woven, sarees back and messages, and the question: how do you keep track of yarn today? Tell us in the comments."],
 S(scroll=8,save=9,send=9,clarity=9,finish=9,original=9)))
print(save(303,"SINGLE","USA","MealPrep","Meal prep company",["p303_mealprep"],
"""Order page and cook list for meal prep companies: customers pick their meals for the week before the cutoff, and you get one cook list and a delivery route by ZIP code.
Close orders on time without chasing texts.
Run a meal prep business? DM us.""", 1,
["#mealprepbusiness","#mealprepdelivery","#foodbusiness","#smallbusinessusa"],
["Oat cream design with the headline 'Orders in 40 texts? Close them on one page.' Left: a browser order page, sample, week of Monday 7 December, with quantity buttons for lemon chicken and rice 2, beef chili bowl 1, veggie pasta 0, turkey meatballs 2; delivery Sunday 6 December 8 AM to 12 PM, ZIP 12345, orders close Thursday 3 December 8 PM, drop-off note, repeat next week, 5 meals, and a place my order button. Right: a dark kitchen cook list with drawn meal containers: lemon chicken and rice 46, beef chili bowl 38, veggie pasta 29, turkey meatballs 33, total meals to cook 146. Below: Sunday delivery route by ZIP, zone A 8 to 10 AM 14 bags, zone B 10 AM to 12 PM 11 bags."],
 S(scroll=8,save=8,send=8,clarity=9,finish=8,original=9)))
print(save(304,"SINGLE","India","MessService","Mess (meals for working people)",["p304_mess"],
"""Meal card app for mess owners: every member has one card for the month, each lunch and dinner is marked, skips are told in time, and you know how many meals to cook today.
No lost paper coupons, no food wasted on empty plates.
Run a mess or a meal service? DM us.""", 5,
["#messservice","#messfood","#homestylefood","#foodbusinessindia"],
["Navy design with the headline 'Paper coupons lost again? One card counts every meal.' A manila punch card for member M-12, November, sample: 30 day boxes, each with a lunch hole and a dinner hole; punched dark holes are meals eaten, red crossed holes are skips told in time, open holes are meals left; eaten 38, skip told 6, left 16, today the 22nd is marked. Right: today's lunch, Sunday 22 November: 42 members, 5 skips told by 10 AM, cook for 37. Tonight's dinner: 42 members, 3 skips so far. A red member app card: not coming for dinner? Tap before 4 PM, the meal stays on your card; a skip tonight's dinner button; card M-12 has 16 meals left, renew by Monday 30 November."],
 S(scroll=9,save=8,send=9,clarity=9,finish=9,original=9)))
print(save(305,"SINGLE","Canada","BoatStorage","Boat winter storage (marina)",["p305_boat"],
"""Storage yard and launch booking app for marinas: every boat has a spot, a winter status and a spring launch date that owners book from their phone.
Spring launch day without the phone ringing all week.
Store boats for the winter? DM us.""", 3,
["#boatstorage","#winterstorage","#marinalife","#boatingcanada"],
["Light blue design with the headline 'Boats wrapped for winter. Spring launch, booked now.' Left: a top view of a sample storage yard with ten boats under white shrink-wrap in two rows beside a lane, numbered B-01 to B-10; navy outline wrapped and stored 6, green launch booked 2, orange dashed wrap this week 2. Right: a phone with book spring launch for boat B-07, spot 7, row 4: launch week Saturday 8 May picked from 24 April, 1 May, 8 May and 15 May; before launch, remove shrink-wrap and wash and wax ticked, battery check not ticked; launch time 9 AM; we text you the day before launch; note for the yard, trailer pickup right after launch; and a book Saturday 8 May button."],
 S(scroll=8,save=8,send=8,clarity=9,finish=8,original=9)))
