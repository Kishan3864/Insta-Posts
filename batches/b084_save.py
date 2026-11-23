import sys; sys.path.insert(0, "tools"); from save_post import save
S = dict
print(save(436, "CAROUSEL", "India", "MilkCollectionCentre", "Village milk collection centre", [f"p436_milk_s{i}" for i in range(1, 6)],
"""Collection app for village milk centres: log litres, fat and SNF for every can in both shifts, see each farmer's 10-day cycle, send slips to farmers' phones, and know what's in the cooler before the tanker comes.
No more adding up the register by hand.
Run a milk collection centre? DM us.""", 2,
["#milkcollection", "#dairyfarmers", "#dairyindia", "#villagebusiness"],
["Cream, steel grey, green and blue design with the headline 'Milk register by hand? Every can, both shifts, logged.' Eight drawn milk cans for the morning shift on Mon 23 Nov, sample, filled to their litres: F-01 12 L, F-02 8.5 L, F-03 15 L, F-04 6 L, F-05 10.5 L, F-06 12 L, F-07 7.5 L, F-08 9 L. Three farmer questions: 'How many litres did I give on the 18th?', 'My fat was higher last time.', 'Is my slip ready?'",
 "Step 1, shift log: a table of eight sample farmers with litres, fat % and SNF %. Morning total 80.5 L from 8 farmers, average fat 4.19% weighted by litres. Each farmer gets a message right after testing, for example F-06, Mon 23 Nov morning: 12 L, fat 4.8%, SNF 8.8%.",
 "Step 2, 10-day cycle for Sample Farmer F, 16 to 25 Nov: morning and evening litre bars for each day, no milk on Fri 20 Nov, today the 23rd with the evening still to come. 144 L so far this cycle. The slip on Thu 26 Nov shows litres and fat for every shift, worked out with your own rate chart and sent to the farmer's phone.",
 "Step 3, cooler and tanker: a 250 L bulk cooler, sample, filled to 173 L. Morning shift 80.5 L, evening shift 92.5 L, in the cooler now 173 L, space left 77 L. Tanker pickup Tue 24 Nov at 7 AM: the driver sees the litres and the average fat before he leaves the plant, and both sides sign on the app.",
 "Closing slide with the headline 'Run a milk centre? Let's build your app.' Four tiles: shift log, 10-day cycle, farmer slips and cooler and tanker, and the question: how long does it take you to make the slips at the end of every cycle? Tell us in the comments."],
 S(scroll=8, save=8, send=9, clarity=9, finish=9, original=9)))
print(save(437, "CAROUSEL", "India", "ShopFitOut", "Shop interior fit-out contractor (racks, counters)", [f"p437_fit_s{i}" for i in range(1, 6)],
"""Job app for shop fit-out contractors: turn your measurements into a 3D shop view and a to-scale plan, check every walkway, get the item list signed by the owner, and send photo updates day by day.
Show the shop before you cut a single board.
Do shop fit-outs? DM us.""", 4,
["#shopinterior", "#shopfitout", "#retaildesign", "#shopdesignindia"],
["Beige, teal and charcoal design with the headline 'Shop fit-out on a rough sketch? Show the whole shop first.' An isometric drawing of a sample 12 by 20 ft shop with a back rack, a left wall rack, a right low rack, a centre display and a counter near the shop door. Three owner questions: 'Will the counter block the door?', 'Can two people pass here?', 'How high is the top shelf?'",
 "Step 1, measure and plan: a top view to scale where one square is one foot, with the racks, centre display and counter, and 3 ft walkways marked on both sides of the display. A list of the five items with sizes and heights, and a walkway check: left rack to display 3 ft, display to right rack 3 ft, door clear of the counter.",
 "Step 2, item list the owner signs: left wall rack 1.5 by 14 ft, 7 ft high, 4 shelves; right low rack 1.5 by 14 ft, 4 ft high, 2 shelves; back rack 8 by 1.5 ft, 7 ft high, 4 shelves; centre display 3 by 6 ft; counter 4 by 2.5 ft with a glass top; 36 ft of LED strip; teal and light oak laminate. Approved by the owner on Wed 25 Nov with the 3D view attached, and four laminate swatches.",
 "Step 3, job plan: an 8-day bar chart from Mon 23 Nov to Tue 1 Dec: measure and 3D view, owner approval, racks made in the workshop, fitting at the shop, lights, cleaning and handover; Sun 29 Nov is a day off. A photo update on Fri 27 Nov: wall racks are ready in the workshop, fitting at your shop on Mon 30 Nov at 9 AM, and the shop can stay open.",
 "Closing slide with the headline 'Do shop fit-outs? Let's build your job app.' Four tiles: 3D shop view, walkway check, item list and photo updates, and the question: how do you show a shop owner what the racks will look like before you build them? Tell us in the comments."],
 S(scroll=9, save=9, send=8, clarity=8, finish=8, original=9)))
print(save(438, "SINGLE", "India", "HydraulicHoseShop", "Hydraulic hose shop (crimping for earthmovers and tractors)", ["p438_hose"],
"""Job app for hydraulic hose shops: save every hose by customer and machine with size, length and end fittings, make the same hose again in one tap, and see how many metres are left on each reel.
Run a hose shop? DM us.""", 5,
["#hydraulichose", "#hosecrimping", "#earthmovingequipment", "#sparepartsindia"],
["Light grey, black, brass and red design with the headline 'Old hose in hand, no record? Every hose saved by machine.' A drawing of hose job H-2231 for a backhoe loader bucket line, sample: a black hose with a straight female fitting on one end and a 90 degree elbow female fitting on the other, 1,250 mm long, half inch 2-wire. Hose history by machine: Sample Contractor A backhoe loader bucket line Mon 23 Nov and boom line Sat 3 Oct, Sample Farmer B tractor loader line Fri 20 Nov, Sample Crane C truck crane outrigger Thu 12 Nov, with a 'Same as last time: make it again' button. Hose reels with metres left: quarter inch 34 of 50 m, 3/8 inch 12 of 50 m marked order more, half inch 41 of 50 m, 3/4 inch 4-wire 18 of 40 m."],
 S(scroll=8, save=8, send=9, clarity=9, finish=9, original=9)))
print(save(439, "SINGLE", "India", "FishSeedHatchery", "Fish seed hatchery (carp fry and fingerlings)", ["p439_hatchery"],
"""Booking app for fish seed hatcheries: see every tank's species, size and ready date, let pond farmers book fingerlings from their phone, and know how many oxygen bags to pack for each pickup.
Run a hatchery? DM us.""", 3,
["#fishseed", "#fishhatchery", "#fishfarmingindia", "#aquaculture"],
["Light teal and orange design with the headline 'Seed bookings by phone call? Every tank, every booking.' Six round hatchery tanks seen from above with small fish, Mon 23 Nov, sample: T1 Rohu fingerlings 18,000, T2 Catla 12,000 and T3 Mrigal 15,000 ready now; T4 Rohu fry 40,000 and T5 Catla fry 30,000 ready Fri 4 Dec; T6 Mrigal spawn 90,000 ready Mon 14 Dec. Tiles: 45,000 fingerlings ready now and 20 bags to pack for Thu 26 Nov. A phone shows a booking for Sample Farmer K, pond 1 acre: fingerlings 2 to 3 inch, Rohu 4,000, Catla 3,000, Mrigal 3,000, total 10,000 fish, 20 oxygen bags at 500 a bag, from tanks T1, T2 and T3, pickup Thu 26 Nov at 6 AM, and a Book button."],
 S(scroll=8, save=8, send=9, clarity=9, finish=8, original=9)))
print(save(440, "SINGLE", "USA", "SeniorMoveManager", "Senior move manager (downsizing and moving)", ["p440_senior"],
"""Planning app for senior move managers: sort every room into keep, family, donate and sell, check the keep furniture against the new floor plan, and share the move plan with the family.
Help seniors move? DM us.""", 1,
["#seniormove", "#downsizing", "#movingtips", "#seniorliving"],
["Warm sand, sage and plum design with the headline 'Downsizing a whole house? Every item has a plan.' Items sorted by room in a sample home with stacked bars: living room 22 items, kitchen 40, main bedroom 16, guest room 17, garage 36; totals keep 22, to family 16, donate 64, sell 29. A new apartment plan to scale with the keep items placed: sofa, armchair, table, queen bed and dresser, and a dashed red china cabinet; 5 of 6 big keep items fit, the china cabinet is 1 ft too wide for the dining wall, ask the family first. A plan: Mon 30 Nov sort and pack, Thu 3 Dec move day with movers at 8 AM and the new place by 1 PM, Fri 4 Dec unpack and set up."],
 S(scroll=8, save=8, send=9, clarity=9, finish=8, original=9)))
