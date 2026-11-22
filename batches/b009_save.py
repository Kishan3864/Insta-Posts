import sys; sys.path.insert(0, "tools"); from save_post import save
S = dict
print(save(61,"SINGLE","India","TyreShop","Tyre shop",["p61_tyre"],
"""Tyre shop software: stock by size across shop and godown, plus alignment bookings.
Type the size, see how many are on the rack and in the godown, and answer the caller before they hang up. Free alignment slots for today sit on the same screen.
Run a tyre shop? DM us.""", 2,
["#tyreshop","#tyredealer","#autopartsindia","#wheelalignment"],
["Grey design with the headline 'Do you have 185/65 R15? Answer before the call ends.' On the left, a black panel shows four tyres stacked side-on with their sizes and stock counts, the 185/65 R15 tyre outlined in red. On the right, a sample search for 185/65 R15 shows four results with location and stock tags, and a red card shows today's wheel alignment slots with free times in white."],
 S(scroll=9,save=8,send=9,clarity=9,finish=9,original=9)))
print(save(62,"CAROUSEL","India","HomeBaker","Home baker",[f"p62_homebaker_s{i}" for i in range(1,7)],
"""Home bakers: 7 things your cake order form must ask.
Flavour and weight, egg or eggless, the exact message, a design photo, date and time, the address with a landmark and the advance. Ask all 7 every time and the "I wanted it different" talks stop.
Save this for your next order.
Bake from home? We build simple order forms. DM us.""", 4,
["#homebaker","#homebakersofinstagram","#cakeorders","#homebakeryindia","#customcakes"],
["Cream slide with the headline '7 things your cake order form must ask.' A top view of a pink cake with 'Happy Birthday Riya' sits on a brown panel next to a numbered list of the seven questions.",
 "Start with what they want. Two cards: 1, flavour and weight, and 2, egg or eggless. Each shows a vague chat message, the clear form answer and a short reason why it matters.",
 "Get the design in writing. Cards 3, message on the cake with exact spelling, and 4, photo of the design they like, each with a vague chat example and the reason.",
 "Then when and where. Cards 5, date and time with pickup or delivery, and 6, address with a landmark, each with a vague chat example and the reason.",
 "Last: the advance. Then it's all in one list. Card 7, advance paid by UPI, above a dark sample order list with three cakes, dates and advance status tags.",
 "A hand-drawn woman reading a paper next to four cards: all 7 questions every time, design photo upload, orders sorted by date, advance status. Headline: Want this as your own order form?"],
 S(scroll=8,save=10,send=9,clarity=9,finish=9,original=9)))
print(save(63,"SINGLE","India","LawyerOffice","Advocate office",["p63_lawyer"],
"""Software for advocates: case dates, client files and hearing reminders.
See every hearing this week on one screen, keep the documents with each case and let clients get a reminder one day before their date.
Are you an advocate or run a law office? DM us.""", 1,
["#advocate","#lawyersofindia","#lawoffice","#legalpractice"],
["Parchment design with the headline 'Hearing dates in a diary? Get reminders instead.' On the left, a navy tear-off desk calendar shows December 14, Monday, next hearing, with a checklist and a sample case card. On the right, a list of this week's sample hearings and meetings from Monday to Friday, and a red card says the client gets a reminder one day before each hearing."],
 S(scroll=8,save=8,send=9,clarity=9,finish=9,original=10)))
print(save(64,"SINGLE","India","TractorRental","Tractor and farm equipment rental",["p64_tractor"],
"""Tractor rental booking app: see which machine is free on any day.
A week view of every tractor and attachment, with hours used, advance and balance for each farmer. No more checking a notebook while the caller waits.
Rent out tractors or farm machines? DM us.""", 3,
["#tractorrental","#farmequipment","#agribusinessindia","#farmmachinery"],
["Light wheat design with the headline 'Which tractor is free on Thursday? See the whole week.' A sample week chart shows three tractors and a seed drill with booking bars for farmers by day, Thursday highlighted. Below, a green card for one farmer lists hours used, advance received and balance pending, and a dark card says Tractors 2 and 3 and the seed drill are free on Thursday."],
 S(scroll=8,save=8,send=9,clarity=9,finish=9,original=10)))
print(save(65,"CAROUSEL","USA","MovingCompany","Moving company",[f"p65_moving_s{i}" for i in range(1,6)],
"""Moving company quote form: customers list rooms, big items and access details first.
You see the full picture before you quote: how many bedrooms, the piano, the third floor with no elevator and where the truck can park.
Swipe through the 3 steps.
Run a moving company? DM us.""", 5,
["#movingcompany","#movers","#movingservices","#localmovers"],
["Cream slide with the headline 'Moving quotes by phone? Let them list it first.' A navy panel shows a stack of cardboard boxes with blue tape and labels like bedroom, books, kitchen and fragile glass, with a tag: full list before you quote.",
 "Step 1: They pick the rooms. Six room cards with icons and plus and minus counters: living room, bedrooms 3, kitchen, garage, home office and patio.",
 "Step 2: They add the big items. A sample list with counts: sofa, queen bed, dresser, fridge, washer and dryer, piano marked as needing special handling, and about 40 boxes.",
 "Step 3: They add the access details. Two cards, moving from and moving to, with ZIP code, floor, elevator and truck parking, plus a moving day bar.",
 "A hand-drawn man with crossed arms next to four cards: rooms, big items, access details, sent to your inbox. Headline: Want a quote form like this?"],
 S(scroll=8,save=8,send=8,clarity=9,finish=9,original=9)))
