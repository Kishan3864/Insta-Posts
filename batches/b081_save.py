import sys; sys.path.insert(0, "tools"); from save_post import save
S = dict
print(save(421, "SINGLE", "India", "GheeMaker", "Desi ghee maker (small dairy, jars and tins)", ["p421_ghee"],
"""Order app for desi ghee makers: log each batch from butter to jars, put the batch number on every label, give every order from that batch, and let regular customers order again from their phone.
Know exactly what is left after orders.
Make ghee? DM us.""", 1,
["#desighee", "#gheemaker", "#homemadeghee", "#dairybusiness"],
["Cream, gold and brown design with the headline 'Ghee orders in a diary? Every jar, batch and order.' Today's batch B-118, sample: 20 kg butter in, 16 kg ghee out, 28 jars and tins. Three drawn jars with B-118 labels: 10 of 1 kg with 2 left after orders, 8 of 500 g with 3 left, 10 of 200 g with 0 left. A teal strip: every label shows batch B-118, packed Mon 23 Nov 2026. Orders from B-118: Sample Sweet Shop 6 of 1 kg picked up today, online 4 orders of 500 g by courier Tue 24 Nov, Sample Store 10 of 200 g on the van round Tuesday, Sample Home 2 of 1 kg and 1 of 500 g for Wed 25 Nov. A phone shows Sample Home's order again screen with the same items, delivery Wed 25 Nov evening, address, UPI on delivery, a note to leave it with the guard, and a Place order button."],
 S(scroll=8, save=8, send=9, clarity=9, finish=9, original=9)))
print(save(422, "CAROUSEL", "India", "PuffedRice", "Puffed rice (murmura) maker supplying shops and carts", [f"p422_puff_s{i}" for i in range(1, 6)],
"""Order app for murmura and puffed rice makers: a standing order book for every shop and day, a roast plan that works out rice and batches for tomorrow, and a van round with paid or weekly bill for each stop.
Make the right number of bags every night.
Make murmura or poha? DM us.""", 3,
["#murmura", "#puffedrice", "#foodmanufacturing", "#smallbusinessindia"],
["White, yellow and indigo design with the headline 'Murmura orders by memory? Bags and rounds, on record.' Four clear plastic bags of puffed rice with 5 kg labels, sample, for tomorrow's 20 bags. Three things shops say with the missing detail: 'Same as last week' (how many bags?), 'Send 2 extra on Friday' (big bags or small?), 'The last bag was soft' (which batch was it?). A strip: 5 shops times 6 days equals 30 standing orders, all kept in one person's head.",
 "Step 1, order book, sample: a table of five shops by Monday to Saturday with 5 kg bag counts and week totals of 40, 28, 16, 31 and 14. Tuesday is highlighted. Bags a day: 20, 20, 17, 20, 25, 27, total 129. A shop calls: no murmura on Wednesday, so Snack Shop C's Wednesday is set to zero. Tomorrow, Tue 24 Nov: 20 bags, 100 kg to make tonight.",
 "Step 2, roast plan: 20 bags for Tuesday, 100 kg of murmura at 5 kg a bag, 112 kg of rice using a sample rule of 10 kg rice for 9 kg murmura, 5 batches of up to 25 kg rice. A time ribbon from 4 AM to 8 AM with batches B1 to B5 and packing. Batch list: B1 to B4 with 25 kg rice each, about 22.5 kg murmura, 45 minutes each from 4:00 AM; B5 with 12 kg rice from 7:00 to 7:22 AM, about 10.8 kg.",
 "Step 3, delivery round: a dotted route timeline. The van leaves at 8:30 with 20 bags; 8:50 Sample Kirana A 6 bags paid by UPI; 9:10 Sample Snack Shop C 3 bags on the weekly bill Saturday; 9:25 Sample Bhel Cart B 4 bags paid; 9:45 Sample Kirana D 5 bags paid; 10:05 Sample Hotel E 2 bags on the weekly bill. Totals: 20 bags delivered, 3 paid on the spot, 2 on the Saturday bill.",
 "Closing slide with the headline 'Make murmura or poha? Let's build your order app.' Four tiles with icons: order book, roast plan, van round, paid or bill, and the question: how do you remember which shop wants how many bags on which day? Tell us in the comments."],
 S(scroll=8, save=9, send=8, clarity=9, finish=8, original=9)))
print(save(423, "SINGLE", "India", "BiogasInstaller", "Biogas plant installer (farm units)", ["p423_biogas"],
"""Job app for biogas plant installers: survey each site, size the plant from your own chart, track install stages part by part, and plan service visits for every plant you built.
Every site on record, from survey to service.
Install biogas plants? DM us.""", 5,
["#biogas", "#biogasplant", "#farmindia", "#gobargas"],
["Cream, green and brown design with the headline 'Biogas jobs on loose paper? Survey to service, one app.' An underground cross-section of a fixed dome biogas plant at site S-27, sample, with parts coloured by stage and numbered: 1 pit dug and 2 base and walls are done in green, 3 dome is working in orange, 4 inlet tank, 5 outlet tank and 6 gas pipe to the kitchen are next, shown dashed. A stage list matches the numbers, with 7 first gas check on Sat 5 Dec. Survey for S-27 at Sample Farm: 6 cattle, space 4 by 4 metres, kitchen 15 metres away, size from your chart 3 cubic metres. Service visits this week: S-11 slurry check Sat 28 Nov, S-19 pipe leak check Mon 30 Nov, S-22 gas valve check Wed 2 Dec."],
 S(scroll=8, save=8, send=8, clarity=8, finish=8, original=9)))
print(save(424, "SINGLE", "India", "TrolleyMaker", "Tractor trolley maker (fabrication)", ["p424_trolley"],
"""Build tracker for tractor trolley makers: every order with its size and type, each part marked done, working or next, a board of all trolleys in the shop, and an update with photos sent to the farmer.
Fewer calls asking when it will be ready.
Build trolleys? DM us.""", 2,
["#tractortrolley", "#trolleymanufacturer", "#fabricationwork", "#farmequipment"],
["Grey, red and yellow design with the headline 'Customers calling for updates? Show the build, part by part.' A side view of tipping trolley T-14, sample, on Tue 24 Nov with each part coloured by stage: chassis, drawbar and tyres done, body working in yellow, hydraulic ram next as a dashed outline. Order T-14 for Sample Farmer C: body 10 by 6 ft with 2 ft sides, hydraulic tipping, tandem axle with 4 tyres, red with a yellow strip, ready Sat 28 Nov. A board of four orders with stage dots for cut, chassis, body, ram, paint and ready: T-12 ready, T-13 in paint, T-14 on body, T-15 being cut. An update sent to Sample Farmer C: T-14 body welding today, 3 photos attached, ram and paint on Thu 26 Nov, ready Sat 28 Nov."],
 S(scroll=8, save=8, send=9, clarity=9, finish=8, original=9)))
print(save(425, "SINGLE", "USA", "GroutCleaning", "Tile and grout cleaning service", ["p425_grout"],
"""Quote app for tile and grout cleaning companies: draw the floor plan on site, measure each room, pick clean, clear seal or color seal per room, and send the quote with the booking window in one go.
No more guessing square feet over the phone.
Clean tile and grout? DM us.""", 4,
["#groutcleaning", "#tilecleaning", "#groutsealing", "#homeservicebusiness"],
["Light aqua and navy design with the headline 'Grout quotes over the phone? Plan every room first.' A floor plan of a sample home drawn to scale with tiled rooms filled by service: kitchen 12 by 14 ft, 168 sq ft, clean and clear seal; entry 6 by 10 ft, 60 sq ft, color seal; hall bath 6 by 8 ft, 48 sq ft, clean and clear seal; laundry 7 by 8 ft, 56 sq ft, clean only; a hatched carpet area not included. A tile close-up split on a diagonal: before with dark stained grout, after with clean light grout. Rooms measured on site add up to 332 sq ft of tile to clean. A booking card for Sample Home, ZIP 12345: Tue 1 Dec, 8 to 10 AM arrival window, we move the furniture, and a Send quote button."],
 S(scroll=8, save=8, send=8, clarity=9, finish=9, original=9)))
