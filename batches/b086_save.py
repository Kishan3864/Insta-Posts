import sys; sys.path.insert(0, "tools"); from save_post import save
S = dict
print(save(446, "SINGLE", "India", "FuelStation", "Fuel station (shift closing)", ["p446_fuel"],
"""Shift closing app for fuel stations: enter the opening and closing reading of every nozzle, see litres sold by fuel, and match them with the tank dip for the same shift.
No calculator, no long register at 2 PM.
Run a fuel station? DM us.""", 4,
["#petrolpump", "#fuelstation", "#petrolpumpindia", "#fuelbusiness"],
["Light grey, navy, amber, blue and green design with the headline 'Shift closing on a calculator? Every nozzle matched to a tank.' Two drawn fuel dispensers, each with two nozzle screens showing open and close readings, sample: N1 petrol 482,310.5 to 483,126.0, sold 815.5 L; N2 diesel 610,442.0 to 611,708.5, sold 1,266.5 L; N3 petrol 377,905.0 to 378,520.5, sold 615.5 L; N4 diesel 291,118.5 to 292,010.0, sold 891.5 L. A dark bar: Shift A, Mon 23 Nov, 6 AM to 2 PM, closed at 2:05 PM and handed to Shift B; petrol sold 1,431.0 L, diesel sold 2,158.0 L. Two tank cards with level gauges: petrol tank T1 dip 9,840 L at the start and 8,415 L at the end, 1,425 L out of the tank against 1,431.0 L sold, difference 6 L, within your limit; diesel tank T2 14,200 L to 12,046 L, 2,154 L out against 2,158.0 L sold, difference 4 L; no water found in either tank."],
 S(scroll=8, save=9, send=9, clarity=8, finish=8, original=9)))
print(save(447, "SINGLE", "USA", "CabinetRefacing", "Cabinet refacing", ["p447_cab"],
"""Quote app for cabinet refacing companies: draw the kitchen wall to scale, size every door and drawer front on the drawing, and get the door order grouped by size in one click.
Let the homeowner pick the style and finish on the same screen.
Do cabinet refacing? DM us.""", 2,
["#cabinetrefacing", "#kitchencabinets", "#kitchenremodel", "#cabinetmaker"],
["Cream and olive green design with the headline 'Doors ordered from a tape list? Size every door on one drawing.' A to-scale drawing of a sample 96 inch kitchen wall with olive shaker doors: six upper doors U1 to U6 (15 by 30 and 18 by 30 inches) and base cabinets B1 to B6 with doors and drawer fronts, each labelled with its size; 11 doors and 5 drawer fronts. A door order grouped by size: doors 18 by 30 times 4, 15 by 30 times 4, 12 by 30 times 1, 15 by 24 times 2; drawer fronts 18 by 15, 18 by 9 and 18 by 6 times 1 each, 15 by 6 times 2; 16 pieces in all. Style and finish picked by the homeowner: Shaker chosen over Slab and Raised, finishes olive, white and oak. Job for a sample homeowner: measured Mon 23 Nov, quote sent Tue 24 Nov, install when the doors arrive."],
 S(scroll=8, save=9, send=8, clarity=9, finish=8, original=9)))
print(save(448, "CAROUSEL", "India", "IndustrialGasCylinders", "Industrial gas cylinder supplier (welding gases)", [f"p448_gas_s{i}" for i in range(1, 6)],
"""Cylinder tracking app for industrial gas suppliers: scan every cylinder in and out at the gate, see which customer holds which cylinder and for how many days, get a red alert after 60 days, and plan the refill round.
Built for oxygen, argon, CO2 and acetylene suppliers to fabricators and workshops.
Supply gas cylinders? DM us.""", 5,
["#industrialgas", "#weldinggas", "#gascylinders", "#fabricationindia"],
["Grey, dark blue, brass and red design with the headline 'Where are my 40 cylinders? Every cylinder, every customer.' Six cards with drawn cylinders coloured by gas: 12 full and 8 empty in the yard, Sample Fabricator A 6, Sample Workshop B 5, Sample Garage C 4 and Sample Factory D 5, where three cylinders have a red band for over 60 days. A legend for oxygen, argon, CO2, acetylene and over 60 days. Three questions: 'Who has my argon cylinder?', 'How many empties to send?', 'That one is out for months.'",
 "Step 1, cylinder register: a table of sample cylinders with number, gas, where it is and days out; C-136, C-137 and C-138 at Factory D are highlighted at 91, 74 and 68 days. A gate scan on Mon 23 Nov at 10:20 AM: C-128, CO2, out to Sample Workshop B, full and sealed. Totals for all 40 cylinders: 12 full and 8 empty in the yard, 20 with customers, 3 over 60 days, and a bar by gas: 16 oxygen, 8 argon, 8 CO2, 8 acetylene.",
 "Step 2, who holds what: for each of the four customers, a bar per cylinder showing days held with a red 60-day line; the three cylinders at Sample Factory D over 60 days are red. A reminder to Factory D lists C-136 (91 days), C-137 (74 days) and C-138 (68 days); the customer replies that two are empty and will go back on Tuesday and they still use C-138, and the supplier notes it. The rule: over 60 days with a customer means red on the board and a reminder on the next round.",
 "Step 3, refill round: a truck carrying the 8 empty cylinders from the yard to the refill plant on Tue 24 Nov at 9 AM, with their numbers. Orders this week, sample: Fabricator A 3 oxygen on Wed 25 Nov, Workshop B 2 argon and Garage C 2 CO2 on Thu 26 Nov, Factory D 2 acetylene on Fri 27 Nov. Tiles: 12 full in the yard now, 9 needed for orders, 20 full on Wednesday after the refill.",
 "Closing slide with the headline 'Supply gas cylinders? Let's build your app.' Four tiles: gate scan, who holds what, old cylinder alert and refill round, and the question: how many of your cylinders are with customers right now, and do you know without calling? Tell us in the comments."],
 S(scroll=8, save=9, send=9, clarity=8, finish=8, original=9)))
print(save(449, "SINGLE", "India", "LandSurveyor", "Land surveyor (plot survey)", ["p449_survey"],
"""Survey app for land surveyors: enter the boundary points from the field, get the plot drawing, side lengths and area in square metres, square feet and acres, and send the PDF to your client's phone the same day.
Do land surveys? DM us.""", 3,
["#landsurvey", "#landsurveyor", "#surveyingindia", "#plotsurvey"],
["Cream, blueprint blue and red design with the headline 'Field book to drawing in days? Points in, plot area out.' A plot drawn on graph paper with six red boundary points P1 to P6, side lengths 38.3 m, 25.9 m, 19.5 m, 21.1 m, 17.6 m and 14.6 m, a north arrow, a 10 m scale bar and the area 1,272 square metres in the middle of sample plot 112. A table of the points in metres east and north, from P1 at 0, 0 to P6 at minus 1.8, 14.5. A blue area card: 1,272 square metres, 13,693 square feet, 0.31 acres, boundary 136.9 m. Job steps: field visit with 6 points taken and drawing and area worked out on Mon 23 Nov, PDF sent to the client's phone on Tue 24 Nov, boundary stones fixed on Fri 27 Nov."],
 S(scroll=8, save=9, send=8, clarity=9, finish=8, original=9)))
print(save(450, "SINGLE", "Canada", "Campground", "Campground (site booking)", ["p450_camp"],
"""Booking website for campgrounds: show every site on a map, let campers pick a free tent or RV site for their dates, and close booked sites on their own.
Run a campground? Send us a DM.""", 1,
["#campground", "#rvcamping", "#campingcanada", "#campsitebooking"],
["Birch white, forest green and red design with the headline 'Site requests by email? Campers pick a site on the map.' A map of a sample campground for Fri 16 to Sun 18 Jul 2027: a lake at the top, a loop road with washrooms in the middle, a gate and the road to the highway, and 24 numbered sites around the loop, white when free, grey when booked, dashed for tent sites, and site 14 in red as the camper's pick. Counts: 13 free, 10 booked, your pick site 14, 8 tent sites. A booking page: site 14, RV 30 amp, fits up to 32 ft; Fri 16 Jul to Sun 18 Jul 2027, 2 nights, 4 campers, RV length 28 ft, 1 dog on a leash, arrive after 2 PM, 1 RV and 1 car, fire pit at the site; booked sites close on their own, no double booking; a button 'Book site 14'."],
 S(scroll=8, save=8, send=8, clarity=9, finish=8, original=9)))
