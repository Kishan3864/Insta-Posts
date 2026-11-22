import sys; sys.path.insert(0, "tools"); from save_post import save
S = dict
print(save(111,"SINGLE","India","Dhaba","Dhaba / highway restaurant",["p111_dhaba"],
"""Pre-order link for dhabas and highway restaurants: bus operators send the group's order before the bus arrives.
When 40 people walk in at once, the kitchen already knows how much dal, roti and rice to make. Table orders, truck groups and bus pre-orders all show on one kitchen board.
Run a dhaba or highway restaurant? DM us.""", 2,
["#dhaba","#highwayrestaurant","#restaurantownerindia","#kitchenmanagement"],
["Mustard yellow design with the headline 'A bus of 40 stops at your dhaba at once? Take their order before they arrive.' On the left, a drawing of a red and white highway milestone reading 'Your Dhaba 2 km' with a road below and a note: bus operators order with your link. On the right, a sample bus pre-order for Bus BS-12 with 40 guests arriving at 1:30 pm: dal tadka 40, tandoori roti 160, paneer curry 20, jeera rice 40, tea 40. Below, a kitchen ticket rail with four sample tickets: Table 4 cooking, truck group ready, Bus BS-12 starts 1:00 pm, Table 9 new."],
 S(scroll=9,save=8,send=9,clarity=9,finish=9,original=9)))
print(save(112,"CAROUSEL","India","GroceryWholesaler","Grocery wholesaler",[f"p112_grocery_s{i}" for i in range(1,6)],
"""Order app for grocery and FMCG wholesalers: kirana shops order from their phone, you check credit limits and get a loading list per route.
No more 30 calls every morning. Shops repeat their last order in one tap, the app warns you when a shop is at its credit limit, and each van gets one list in drop order.
Swipe to see how it works.
Supply kirana shops? DM us.""", 4,
["#grocerywholesale","#fmcgdistributor","#kiranastore","#wholesalebusiness"],
["Jute beige slide with the headline 'Shop orders on 30 calls every morning? Let shops order from their own phone.' A drawing of five stacked jute sacks labelled sugar 50 kg, atta 50 kg, rice 25 kg, dal 30 kg and salt 25 kg on a green panel. Three cards: order app, credit check, loading list.",
 "Step 1, order app: the shop orders, you get a clear list. A phone shows a sample order for Sample Store 3 with sugar, atta, toor dal, salt and rice, each with pack size and quantity buttons, and a 'Send order, deliver tomorrow' button. Side cards: last order in one tap, packs and bag sizes, cut-off time.",
 "Step 2, credit check: know who is at their credit limit. Five sample shops with bars showing credit used: 35%, 62%, 88% (load and remind), 100% (hold, limit reached) and 20%. A note: the app tells you before the goods leave.",
 "Step 3, loading list: one list to load the van, in drop order. A sample list for van 2, route east: sugar 12 bags, atta 40 bags, toor dal 5 bags, rice 14 bags, salt 9 bundles. Next to it, the drop order for four shops and a red row: Sample Mart 4 on hold.",
 "Closing slide with the headline 'Grocery wholesaler? Let's build your order app.' The sack drawing and four tiles: shops order from their phone, credit limit per shop, loading list per route, bills and payments in one place."],
 S(scroll=8,save=8,send=9,clarity=9,finish=9,original=8)))
print(save(113,"SINGLE","USA","RealEstatePhotographer","Real estate photographer",["p113_rephoto"],
"""Booking and delivery portal for real estate photographers: agents book shoots online and download every photo from one link.
No more "are the photos ready?" texts. Agents pick the package and time, and when you upload, they get listing-size and print-size photos plus the floor plan in one place.
Shoot real estate? DM us.""", 1,
["#realestatephotography","#realestatephotographer","#listingphotos","#photographybusiness"],
["Dark slate design with the headline '“Are the photos ready?” Book shoots and deliver in one link.' A drawing of a living room with a sofa, a window and a floor lamp, seen through a camera viewfinder with corner brackets, a rule-of-thirds grid, a focus box, a tag 'Living room, 12 of 32' and settings 'ISO 200, f/8, 1/60, HDR'. Below, two sample cards: a shoot booking for 14 Sample Pine St, photos and floor plan, Thursday, November 26 at 10 am; and a delivery card: 32 photos ready in listing and print size, floor plan PDF, with 'Download all' and 'Share link' buttons."],
 S(scroll=9,save=8,send=8,clarity=9,finish=9,original=9)))
print(save(114,"CAROUSEL","India","PlasticMoulding","Plastic moulding unit",[f"p114_mould_s{i}" for i in range(1,6)],
"""Shop-floor software for plastic injection moulding units: a live machine board, shot count per mould, service reminders and job cards.
See which mould is on which machine, how far each job has reached and when each mould needs service, from shot counts, not guesswork. Rejects and packed boxes are logged per job.
Swipe through all 3 parts.
Run a plastic moulding unit? DM us.""", 3,
["#plasticmoulding","#injectionmoulding","#plasticindustry","#msmemanufacturing"],
["Dark graphite slide with the headline 'Which mould is on which machine? Every job, mould and shot count on one screen.' A drawing of an injection moulding machine with a hopper of pink granules, a barrel, a pink mould and a clamp, with a counter reading shots 18,240. Cards below: machine M-3 150 ton, mould cap 28 mm with 8 cavities, job J-77 for 50,000 pieces, 18,240 shots today, 12 second cycle, next service in 18,000 shots.",
 "Part 1, machines: six machines, one live board. Sample cards for M-1 to M-6: four running with progress bars, M-4 in a mould change and back by 2 pm, M-6 idle. A note: shots come from the machine counter, no paper log.",
 "Part 2, mould care: service the mould before it breaks. Four ring gauges of shots used: cap 28 mm 82% with service in 18,000 shots, bucket 10 L 40%, crate lid 96% with service due this week, container 500 ml 25%.",
 "Part 3, job and dispatch: 'How many are ready?' Answer in one look. A sample job card J-77, cap 28 mm on M-3 for Sample Packaging Co.: 50,000 white pieces ordered, 32,000 made, 420 rejects logged as short shot, delivery Saturday 28 November, 64% done. Next to it, ten boxes: 6 sent, 2 packed, 2 to go.",
 "Closing slide with the headline 'Run a plastic moulding unit? Let's build your shop-floor app.' The machine drawing and four tiles: live machine board, shot count per mould, service reminders, job cards and dispatch."],
 S(scroll=8,save=8,send=9,clarity=9,finish=9,original=9)))
print(save(115,"SINGLE","India","ContentCreator","Content creator / influencer",["p115_creator"],
"""Brand deal tracker app for content creators: every deal, every post date and every payment in one place.
See what is due this week, which brand has your draft, what is live and which payment is still pending, instead of digging through DMs and notes.
Create content for brands? DM us.""", 5,
["#contentcreatorindia","#influencerindia","#creatoreconomy","#branddeals"],
["Lavender design with the headline 'Brand deals lost in DMs and notes? Track every post, date and payment.' On the left, a ring-bound planner page for December week 2 with sample entries: reel draft for Brand 1 on Monday, three stories for Brand 2 on Tuesday, no posts on Wednesday, reel live on Thursday, send report on Friday, shoot for Brand 3 on Saturday, rest day on Sunday. On the right, a dark deal tracker with five sample brands and statuses: draft sent, live, brief received, payment pending and paid."],
 S(scroll=8,save=8,send=9,clarity=9,finish=9,original=9)))
