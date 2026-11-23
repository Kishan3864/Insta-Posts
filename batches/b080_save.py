import sys; sys.path.insert(0, "tools"); from save_post import save
S = dict
print(save(416, "CAROUSEL", "India", "SilkReeling", "Silk reeling unit (buys cocoon lots, reels raw silk)", [f"p416_silk_s{i}" for i in range(1, 6)],
"""Lot tracking app for silk reeling units: a card for every cocoon lot, a basin board that shows which lot is in which basin, and raw silk per lot so you know which farmer's cocoons to buy again.
No more mixed-up lots.
Run a reeling unit? DM us.""", 2,
["#silkreeling", "#rawsilk", "#sericulture", "#silkcocoons"],
["Ivory, green and gold design with the headline 'Cocoon lots mixed up? Track every lot to the skein.' Three woven trays of cocoons, sample: lot L-21 from farmer F-03 with 60 kg, L-22 from F-08 with 62 kg, L-23 from F-11 with 55 kg, each bought Mon 23 Nov and kept on racks 1 to 3, each with question chips for basin and silk. A register line reads: L-21 plus L-22 in basins 1 to 4, or 1 to 3, silk weighed together. Three questions: which lot is in which basin today, how much silk did each lot give, which farmer to buy from again.",
 "Step 1, lot card, sample: a tray of cocoons and a card for lot L-22: farmer F-08, Sample Village, bought Mon 23 Nov at 9:10 AM, 62 kg, white bivoltine, stored on rack 2 shelf B. Sorted: 58 kg good, 3 kg double, 1 kg flimsy. 58 kg ready for reeling from Tue 24 Nov.",
 "Step 2, basin board for Tue 24 Nov, sample: six reeling basins drawn from the top. Basins 1 to 3 on lot L-22 with 10, 10 and 9.5 kg of cocoons and 1.3, 1.4 and 1.2 kg of silk so far; basin 4 on L-21; basin 5 on L-23; basin 6 free at 2 PM. L-22 has 29.5 of 58 kg in basins and 3.9 kg of silk so far. Next: give basin 6 lot L-23, 47 kg left.",
 "Step 3, silk per lot, sample: lots finished this week shown as rows of silk hanks, one hank for 1 kg of raw silk. L-18 from farmer F-08: 60 kg of cocoons gave 8.6 kg of silk, 7 kg of cocoons per kg. L-19 from F-03: 55 kg gave 6.5 kg, 8.5 kg per kg. L-20 from F-11: 48 kg gave 6 kg, 8 kg per kg. L-22 is reeling now with 3.9 kg so far. Note: L-18 from F-08 gave the most silk, so buy from F-08 again.",
 "Closing slide with the headline 'Run a reeling unit? Let's build your lot tracker.' Four numbered tiles: lot cards, basin board, silk per lot and farmer ledger, a row of silk hanks, and the question: how do you know which basin has which lot today, chalk on the wall, a register, or you just remember? Tell us in the comments."],
 S(scroll=8, save=9, send=8, clarity=8, finish=9, original=10)))
print(save(417, "SINGLE", "India", "SilageBales", "Silage bale maker (maize silage for dairy farms)", ["p417_silage"],
"""Stock and booking app for silage bale makers: see every bale in the yard as booked or free, keep dairy farm orders by day, plan trolley trips, and answer a new call in seconds.
Never promise bales you don't have.
Make silage bales? DM us.""", 5,
["#silage", "#maizesilage", "#silagebales", "#dairyfarmingindia"],
["Cream, black and blue design with the headline 'Silage bookings on calls? Stock and orders, one board.' A yard board for Tue 24 Nov, sample, with 120 round wrapped bale icons, one icon for 5 bales: 76 blue icons booked and 44 black icons free. Totals: 600 bales in the yard, 380 booked, 220 free to sell. Trolley trips at 40 bales a trip: Wed 25 Nov 120 bales in 3 trips, Thu 26 Nov 80 in 2, Fri 27 Nov 100 in 3, Sat 28 Nov 80 in 2. Orders this week from five sample dairies adding up to 380 bales. A new call from Sample Dairy F wants 250 bales on Saturday; free stock is 220, so offer 220 now and 30 from the next batch."],
 S(scroll=8, save=8, send=9, clarity=9, finish=8, original=9)))
print(save(418, "SINGLE", "USA", "StumpGrinding", "Stump grinding service", ["p418_stump"],
"""Site visit app for stump grinding companies: mark every stump on a yard map, measure it once, note the gate width and options, and send a clear quote from one job card.
No more second trips to measure.
Grind stumps? DM us.""", 3,
["#stumpgrinding", "#stumpremoval", "#treeservice", "#yardwork"],
["Tan, brown and green design with the headline 'Stump quotes by guesswork? Measure each stump once.' A top view of a sample backyard with the house, back door, patio, flower bed, shed and a 36 inch gate, with four stumps drawn to scale as tree-ring circles and a dashed grinder path from the gate. The stump list: 1 is 18 inches by the side fence, 2 is 26 inches with surface roots, 3 is 10 inches in the flower bed, 4 is 32 inches near the patio, total 86 inches. Options: grind 6 inches below grade, haul chips away, lines marked. A dark job card for Sample Home, ZIP 12345: visit Fri 27 Nov at 9 AM, small grinder that fits the 36 inch gate, 6 photos added by the owner, and a Send quote button."],
 S(scroll=8, save=8, send=8, clarity=9, finish=9, original=9)))
print(save(419, "SINGLE", "India", "PalletMaker", "Wooden pallet maker (factory orders)", ["p419_pallet"],
"""Order app for wooden pallet makers: factory buyers pick size, entry, wood, heat treated stamp and quantity on one form, you see it drawn to size, and every order in the yard shows how many are made.
No more confusion over phone calls.
Make pallets? DM us.""", 1,
["#woodenpallets", "#palletmanufacturer", "#industrialpackaging", "#msmeindia"],
["Cream, black and blue design with the headline 'Pallet orders by phone call? Buyers fill one order form.' A 3D drawing of a wooden pallet for order PL-58, sample, marked 1200 mm by 1000 mm, with tags for 4-way entry, pine, load 1,000 kg and HT stamp. In the yard today: PL-55 Sample Auto Parts 120 of 120 ready, PL-56 Sample Foods 48 of 80 nailing, PL-57 Sample Textiles 0 of 50 wood cut, PL-58 Sample Engineering 0 of 100 new. A phone shows the buyer's order form for Sample Engineering: size 1200 by 1000, 4-way, pine, heat treated stamp yes, quantity 100, load 1,000 kg per pallet, deliver by Thu 3 Dec, unload at gate 3 loading dock, a note to stack in 10s, strapped and labelled, and a Send order button."],
 S(scroll=8, save=8, send=8, clarity=9, finish=9, original=9)))
print(save(420, "CAROUSEL", "Canada", "MobileWelder", "Mobile welder (farm, trailer and gate repairs)", [f"p420_weld_s{i}" for i in range(1, 6)],
"""Job app for mobile welders: a request form that asks for photos, metal, thickness, power and truck access up front, a day route by area, and job cards with before and after photos and a signature on site.
Load the right gear the first time.
Do mobile welding? DM us.""", 4,
["#mobilewelding", "#weldingrepair", "#farmrepair", "#canadasmallbusiness"],
["Grey, blue and orange design with the headline 'Weld jobs from blurry texts? Ask the right things first.' Three texts from sample customers with blurry photos: trailer hitch cracked, can you come today; gate hinge snapped off; loader bucket edge is worn out. Each has orange chips for what is missing, such as where is the crack, steel or aluminum, can a truck reach it, how wide is the gate, power on site, which machine. Note: every unclear text means calls back and forth, the wrong rods in the truck, or a second trip.",
 "Step 1, request form in a browser, sample job J-31: job type trailer, three clear photos of the hitch, the trailer and a tape measure, damage on the hitch coupler with a crack on the left weld, steel, about a quarter inch thick, no power on site so the welder brings a generator, truck can park within 50 ft, Sample Township 22 km away, best day Wed 25 Nov morning, and a Send request button.",
 "Step 2, day route for Wed 25 Nov, sample: a map with the shop and three numbered job pins on a dashed route. A day ribbon from 7 AM to 5 PM with drive time hatched: J-31 from 8 to 9:30 AM, J-32 from 10:15 to 11:15 AM, J-33 from 12:30 to 2:30 PM. Job cards: J-31 trailer hitch at Sample Farm A, 22 km; J-32 gate hinge at Sample Ranch B, 14 km; J-33 stair railing at Sample Home C, 9 km.",
 "Step 3, job card on site: before photo at 8:05 AM with the cracked hitch and after photo at 9:20 AM with a new weld bead. J-31 at Sample Farm A: ground out the crack, welded both sides, added a gusset; steel plate a quarter inch, 4 by 6 inches; flux-core wire about half a pound; on site 8 to 9:30 AM, 1 hour 30 minutes. Customer sign-off with a signature, signed 9:28 AM, and a Send job card button.",
 "Closing slide with the headline 'Weld on the road? Let's build your job app.' Four tiles with icons: request form, day route, job cards and sign-off, and the question: when a weld job comes in by text, what is the first thing you ask? Tell us in the comments."],
 S(scroll=8, save=8, send=9, clarity=9, finish=8, original=9)))
