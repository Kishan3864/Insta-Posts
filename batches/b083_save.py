import sys; sys.path.insert(0, "tools"); from save_post import save
S = dict
print(save(431, "CAROUSEL", "India", "MakhanaProcessor", "Makhana (fox nut) processor and grader", [f"p431_makhana_s{i}" for i in range(1, 6)],
"""Lot app for makhana processors: a lot card for every farmer's lot, the grade split after sieving, stock by grade in kg, and buyer orders matched to the grade they asked for.
Know how much 6+ sutta is really left.
Process makhana? DM us.""", 5,
["#makhana", "#foxnuts", "#makhanaprocessing", "#agribusinessindia"],
["Cream, pond green and pink design with the headline 'Makhana by guesswork? Every lot graded, every kg known.' Four round sieve trays of drawn makhana pops for one sample lot: 6+ sutta 120 kg, 5 sutta 160 kg, 4 sutta 88 kg and broken 32 kg, with bars under each. A strip: lot L-21, Sample Farmer A, 400 kg of popped makhana in, Mon 16 Nov. Three questions: 'Which farmer's lot was this?', 'How much 6+ is left?', 'Send the same grade as last time.'",
 "Step 1, lot card, sample: L-21 from Sample Farmer A, came in Mon 16 Nov, 400 kg of popped makhana in 40 sacks of 10 kg. A grade split bar for L-21: 30% 6+ sutta 120 kg, 40% 5 sutta 160 kg, 22% 4 sutta 88 kg, 8% broken 32 kg. A table of all lots this week: L-21, L-22 and L-23 with kg per grade.",
 "Step 2, grade stock: sack icons of 25 kg per grade from lots L-21, L-22 and L-23: 6+ sutta 299 kg, 5 sutta 398 kg, 4 sutta 223 kg, broken 80 kg. Stock against orders: 6+ sutta 299 kg in stock and 350 kg ordered, short 51 kg; 5 sutta 398 and 280, 118 kg free; 4 sutta 223 and 120, 103 kg free.",
 "Step 3, buyer orders filled in order of booking: Sample Snack Brand A 150 kg of 6+ packed, Sample Wholesaler B 220 kg of 5 sutta packed, Sample Retail Chain C 120 kg of 4 sutta packed, Sample Exporter D 200 kg of 6+ with 149 kg now, Sample Shop E 60 kg of 5 sutta packed. A message to Sample Exporter D: 149 kg packed today, the other 51 kg from the next lot by Sat 28 Nov. Left after orders: 0, 118, 103 and 80 kg.",
 "Closing slide with the headline 'Process makhana? Let's build your lot app.' Four tiles: lot cards, grade split, grade stock and buyer orders, and the question: how do you keep track of which lot each grade came from? Tell us in the comments."],
 S(scroll=8, save=9, send=8, clarity=9, finish=8, original=9)))
print(save(432, "SINGLE", "India", "WireHarness", "Wire harness job work unit", ["p432_harness"],
"""Job app for wire harness makers: keep every harness drawing with its wire lengths, get the cut list for the whole order in metres, track cut, crimp, assemble and test counts, and log test bench results.
Make wire harnesses? DM us.""", 2,
["#wireharness", "#cableharness", "#jobworkindia", "#autocomponents"],
["Light grey, black, copper and blue design with the headline 'Harness orders on paper? Every wire cut, crimped, tested.' A harness board drawing for H-12, sample, with wires drawn to scale from connector A: red and black 450 mm to connector C, blue and yellow 620 mm to connector B, green and white 380 mm to connector D, taped at the branch. A cut list for an order of 500 harnesses: W1 red 1.0 sq mm 450 mm 225 m, W2 black 225 m, W3 blue 0.5 sq mm 620 mm 310 m, W4 yellow 310 m, W5 green 380 mm 190 m, W6 white 190 m, total 1,450 m. A dark stage board for H-12, due Sat 28 Nov: cut 500, crimp 420, assemble 260, test 180 of 500. Test bench today: continuity checked on each harness, 3 failed and the crimp on W4 was redone."],
 S(scroll=8, save=9, send=8, clarity=9, finish=9, original=9)))
print(save(433, "SINGLE", "India", "SoilTestingLab", "Soil testing lab for farm samples", ["p433_soil"],
"""Sample tracking app for soil testing labs: code every sample bag with the farmer's phone and field, see each one move from received to drying, testing and report, and send the report straight to the farmer's phone.
No more names in marker on plastic bags.
Run a soil lab? DM us.""", 4,
["#soiltesting", "#soiltestinglab", "#agriculturelab", "#farmingindia"],
["Cream, brown and green design with the headline 'Soil samples in loose bags? Track each one to the report.' A sample rack on Mon 23 Nov, sample, with twelve coded pouches S-101 to S-112 coloured by stage: received 2, drying 3, testing 3, report sent 4. A brown note: before, a marker on the bag said 'Field near the well, wheat, mustard?'; now every bag gets a code, the farmer's phone number and the field. A phone shows a sample soil report for S-107, Sample Farmer G, field 2, 3 acres, tested Sat 21 Nov, with bars and markers: pH 7.8 high, nitrogen 210 kg per hectare low, phosphorus 18 medium, potassium 320 high, organic carbon 0.42% low, bands set by your lab, past tests Nov 2025 and Nov 2024, and a Send report to farmer button."],
 S(scroll=8, save=8, send=9, clarity=9, finish=8, original=9)))
print(save(434, "SINGLE", "India", "SewingClasses", "Sewing and tailoring classes for adults", ["p434_sewing"],
"""App for sewing and tailoring classes: batch timings with seats filled, lessons done for every learner, fee reminders on time, certificates when a course is done, and a waiting list for full batches.
Run sewing classes? DM us.""", 1,
["#sewingclasses", "#tailoringclasses", "#stitchingclass", "#learnsewing"],
["Chalk white, denim blue and yellow design with the headline 'Sewing class in a register? Batches, lessons, reminders.' Three batch cards with seat dots: 10 AM Basic, 10 of 12 seats filled; 2 PM Blouse, 10 of 10; 5 PM Kurti and salwar, 7 of 12. Six sample learners with measuring tape progress bars out of 30 lessons: Learner A 8, B 21, C 27, D 14, E 30, F 3. Fee reminders sent to Learner A for Fri 27 Nov and Learner D for Mon 30 Nov. Certificate ready for Learner E, Basic course done. Waiting list for the 2 PM batch: 3 learners get a message as soon as a seat opens."],
 S(scroll=8, save=8, send=9, clarity=9, finish=9, original=9)))
print(save(435, "SINGLE", "USA", "KnifeSharpening", "Mobile knife sharpening at markets", ["p435_knife"],
"""Drop-off app for mobile knife sharpeners: a numbered claim ticket for every knife roll, each knife logged with its job, texts when it is ready, and your week of market stops with drop-offs and pickups.
Sharpen knives? DM us.""", 3,
["#knifesharpening", "#farmersmarket", "#sharpknives", "#mobilebusiness"],
["Cream, slate and teal design with the headline 'Knife drop-offs on scraps? Ticket every knife, every stop.' A two-part claim ticket #K-0418 with a perforated tear line, sample: Sample Customer, dropped off Tue 24 Nov at Sample Farmers Market, 5 knives in one roll, pick up Sat 28 Nov at Sample Town Square; the dark part stays with the knives and says we text you when they are ready and again the morning of pickup. A leather knife roll with knives drawn to blade length and tags: chef's knife 8 inch sharpened, bread knife 9 inch serrated hand file, paring knife 3.5 inch sharpened, santoku 7 inch chip fixed, kitchen shears sharpened. Three market stops: Tue 24 Nov Sample Farmers Market 14 drop-offs and 9 pickups, Thu 26 Nov Sample Library lot 6 and 11, Sat 28 Nov Sample Town Square 18 and 14."],
 S(scroll=8, save=8, send=8, clarity=9, finish=9, original=9)))
