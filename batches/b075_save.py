import sys; sys.path.insert(0, "tools"); from save_post import save
S = dict
print(save(391,"SINGLE","India","CashewProcessing","Cashew processing unit",["p391_cashew"],
"""Stock and order app for cashew processing units: see kilos in stock for every grade, book them against buyer orders by delivery date, and get an alert before a grade runs short.
No more guessing when a buyer asks "Is W240 ready?"
Process or pack cashews? DM us.""", 4,
["#cashewprocessing","#cashewnuts","#dryfruitsbusiness","#foodprocessingindia"],
["Cream, amber and olive design with the headline 'Is W240 ready for Monday? See stock by grade, not by guess.' Five grade cards, each with a drawn cashew sized by grade and tins for stock (1 tin = 10 kg, sample), booked tins filled amber: W180 40 kg with 20 kg free, W240 90 kg with 0 kg free (in red), W320 120 kg with 50 kg free, W450 60 kg all free, Splits 50 kg with 0 kg free. Orders filled by delivery date: O-52 Sample Sweet Maker Splits 50 kg Wed 25 Nov ready; O-53 Sample Wholesaler W320 70 kg Thu 26 Nov ready; O-51 Sample Dry Fruit Store W240 60 kg Fri 27 Nov ready; O-54 Sample Gift Box Maker W180 20 kg Sat 28 Nov ready; O-55 Sample Bakery W240 40 kg Mon 30 Nov, 30 ready and 10 short. An owner alert: W240 is 10 kg short for O-55, grade the next batch before then."],
 S(scroll=8,save=8,send=8,clarity=9,finish=9,original=9)))
print(save(392,"CAROUSEL","India","StudyLibrary","Self-study library (paid reading room)",[f"p392_library_s{i}" for i in range(1,6)],
"""Seat and member app for self-study libraries: a live seat map for morning and evening shifts, a quick join form, renewal reminders and a waitlist for full shifts.
Answer "Is any seat free?" in one look.
Run a study library or reading room? DM us.""", 1,
["#studylibrary","#selfstudylibrary","#readingroom","#libraryowner"],
["Cream and green design with the headline 'Seats tracked in a register? See every seat, every shift.' A seat map of 40 seats in 5 rows, each seat split into a morning half and an evening half, coloured full day, morning 6 AM to 2 PM, evening 2 to 10 PM or free, sample with 59 members. Counts: 14 full-day seats, 0 morning seats free, 7 evening seats free. Three problems: is any evening seat free, who has not paid, morning seat for my friend.",
 "Step 1, new member in two minutes: a walk-in at 6:40 PM asks for an evening seat. The seat map highlights the 7 free evening seats: 2, 3, 4, 6, 15, 23 and 36, with seat 2 picked. A phone join form for a sample member: evening shift 2 to 10 PM, seat 2, locker L-12, starts Tue 24 Nov, renews Thu 24 Dec, ID photo checked and a confirm button. A welcome message is sent on save.",
 "Step 2, renewals without chasing: a week strip from Mon 23 to Sun 29 Nov with the number of renewals due each day. A member list with no amounts shown: seat 5 paid by UPI today, seat 24 due today, seat 4 due Tuesday, seat 14 due Wednesday, seat 33 two days late, seat 21 due Friday. An auto reminder one day before for seat 4, and a second reminder note for the late seat 33.",
 "Step 3, waitlist for full shifts: a waitlist of three sample members since 18, 20 and 22 Nov. Morning seats ending 30 Nov: seat 27 renewed, seat 7 renewed, seat 10 not renewing, seat 13 no reply yet. Flow: seat 10 morning is free from Tue 1 Dec and is offered to W-1 first, with an auto offer message asking to reply YES by Wednesday 6 PM.",
 "Closing slide with the headline 'Run a study library? Let's build your seat app.' Four tiles: seat map, join form, renewal reminders and waitlist, and the question: how do you track seats today, a register, a sheet or chat groups? Tell us in the comments."],
 S(scroll=9,save=8,send=9,clarity=9,finish=8,original=9)))
print(save(393,"SINGLE","India","ShutterFabricator","Rolling shutter and grill fabricator",["p393_shutter"],
"""Job app for rolling shutter and grill fabricators: site measurements with photos in one form, every job's stage from cutting to fitting, and a message to the customer before fitting day.
Right size, right day.
Make shutters, grills or gates? DM us.""", 3,
["#rollingshutter","#shuttermanufacturer","#fabricationwork","#weldingworkshop"],
["Off-white, red oxide and grey design with the headline 'Shutter size on a scrap of paper? Measure the site in the app.' A front-view drawing of a rolling shutter for job J-14 with its box on top, side channels and centre lock, marked 10 ft 6 in wide and 9 ft high. A dark site measure form, sample: Sample Shop, Main Road, width 10 ft 6 in, height 9 ft, plain 18 gauge slats, opened by hand with centre lock, grey colour, three photos. A jobs table with stage dots for measured, cut, welded, primer, painted and fitted: J-11 fitting today, J-12 paint Wednesday, J-14 fitting Thursday 26 Nov, J-15 window grills primer Wednesday, J-16 safety door cutting Tuesday. An auto message: your shutter J-14 is in primer now, fitting on Thursday 26 Nov at 10 AM."],
 S(scroll=8,save=8,send=8,clarity=9,finish=9,original=9)))
print(save(394,"CAROUSEL","India","CorrugatedBox","Corrugated box maker",[f"p394_box_s{i}" for i in range(1,6)],
"""Order app for corrugated box makers: one spec card per box with size, ply, print and approved proof, sheet size and cuts worked out from the box size, every order's station on the factory line, and a dispatch message with the bill.
Repeat orders in one tap.
Make corrugated boxes or cartons? DM us.""", 5,
["#corrugatedboxes","#cartonbox","#packagingindia","#boxmanufacturer","#corrugatedpackaging"],
["Tan, blue and red design with the headline 'Same box as last time. Which size was that?' A flat box layout for B-104 in mm, sample: four panels 300, 200, 300 and 200 with a glue flap and flaps of 100, cut lines in red and fold lines dashed blue. An old diary note with an unsure size, question chips for ply, print colour, joint and last quantity, and the line inside size 300 x 200 x 150 mm, sheet 1,035 x 350 mm. Three problems: same as last time, 3 ply or 5 ply, print in blue right.",
 "Step 1, one spec card per box: B-104 for Sample Snacks Unit, inside size 300 x 200 x 150 mm, regular slotted box, 5 ply, 1 colour print on 2 sides, stitched joint, usual quantity 2,000 boxes, last order Tue 3 Nov, and a repeat button. A side view of 3 ply and 5 ply board with the 5 ply marked for B-104, and an approved print proof.",
 "Step 2, sheet size from the box size: sheet length 2 x (300 + 200) + 35 glue flap = 1,035 mm, sheet width 150 height + 2 flaps of 100 = 350 mm. A drawing of a 1,100 mm reel with 3 sheets across and 50 mm trim. Tiles: 2,000 boxes ordered, 3 ups per cut, 667 cuts on the machine. Note: sizes before trim allowance.",
 "Step 3, every order on the line: a factory line with six stations, corrugation, printing, slotting, stitching, bundled and dispatch, each holding two sample order cartons. A dispatch slip for B-104: 2,000 boxes in 40 bundles of 50, bill attached, sample tempo, leaving today at 4 PM, an auto message to the customer, and a dispatch plan with two orders today and two tomorrow.",
 "Closing slide with the headline 'Make corrugated boxes? Let's build your order app.' The flat box layout, four tiles: spec cards, sheet sizes, order line and dispatch messages, and the question: how do your regular buyers reorder today, a call, a chat or a visit? Tell us in the comments."],
 S(scroll=8,save=9,send=8,clarity=9,finish=8,original=9)))
print(save(395,"SINGLE","USA","EpoxyFloors","Epoxy garage floor installer",["p395_epoxy"],
"""Quote request form for epoxy garage floor installers: customers enter ZIP code, garage size, floor condition, cracks and photos, pick a flake color, and get a clear install plan with the quote.
Quote right the first time, without a wasted visit.
Install epoxy or flake floors? DM us.""", 2,
["#epoxyflooring","#garagefloor","#flakeflooring","#garagemakeover"],
["Light grey, slate and teal design with the headline 'Quoting a garage floor blind? Get size and photos first.' A top-down drawing of a 22 by 24 foot garage floor with grey flake speckles, two marked cracks, a center drain and the garage door at the bottom, sample. A quote request Q-208: ZIP 00012 in service area, 22 x 24 ft = 528 sq ft, old paint peeling in spots, 2 cracks marked, 3 photos, best week of Dec 7, and three flake color swatches with Sample Granite picked. A dark install plan sent with the quote: Day 1 morning grind floor and fill cracks, Day 1 afternoon base coat and flakes, Day 2 scrape and top coat, after that we text you when to park; dry times depend on the product."],
 S(scroll=8,save=8,send=8,clarity=9,finish=9,original=9)))
