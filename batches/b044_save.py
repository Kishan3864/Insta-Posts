import sys; sys.path.insert(0, "tools"); from save_post import save
S = dict
print(save(236,"SINGLE","India","WaterTankCleaning","Water tank cleaning service",["p236_tank"],
"""Service app for water tank cleaning: every society's tanks are listed with the last cleaning date, due tanks are flagged, and the secretary gets a message with days to pick.
When someone asks "when was our tank cleaned?", the answer is one tap away.
Clean water tanks for societies or buildings? DM us.""", 3,
["#watertankcleaning","#tankcleaning","#housingsociety","#homeservicesindia"],
["Light grey design with the headline 'When was our tank cleaned? Show it, tank by tank.' A drawn sample society with three wings, each with an overhead tank on the roof, and an underground sump joined by a pump line. Each tank shows its water and a brown sediment layer, with a status dot: Tank A clean, Tank B due, Tank C overdue, sump clean. Below: a list with Tank A, Wing A roof, cleaned 12 September, next in December; Tank B, Wing B roof, cleaned 14 June, due now; Tank C, Wing C roof, cleaned 2 March, overdue; sump, underground, cleaned 12 September. A message to the secretary says Tank B and Tank C are due, with days Saturday 28 November and Sunday 29 November, and before and after photos."],
 S(scroll=8,save=8,send=9,clarity=9,finish=9,original=9)))
print(save(237,"SINGLE","USA","FenceInstaller","Fence installer",["p237_fence"],
"""Quote request page for fence installers: the customer draws the fence on a map of their yard, marks the gates and picks a style, and you get the total length before any site visit.
You set the price per foot, so the quote is ready from the drawing.
Install wood, vinyl or chain link fences? DM us.""", 5,
["#fenceinstallation","#fencecompany","#fencing","#backyardfence"],
["Pale sage design with the headline 'How much for a fence? Let them draw it first.' A top-down sample backyard drawn by the customer, with a house, a pool, two trees and an orange fence line: 110 feet at the back, 135 feet on each side and 28 feet on each side of the house, with gate 1 and gate 2. Right: a dark quote request card: total length 436 feet, 2 walk gates, height 6 feet, no old fence to remove, and the style wood privacy picked from picket, vinyl and chain link. A note says you set the price per foot and the quote is ready from the drawing, before any site visit."],
 S(scroll=8,save=8,send=8,clarity=9,finish=9,original=9)))
print(save(238,"CAROUSEL","India","HomeSalon","Home salon at doorstep (women)",[f"p238_salon_s{i}" for i in range(1,6)],
"""Booking app for home salon services: customers pick slots by area, each stylist gets one clean route for the day, and the kit bag is packed from the bookings.
Less time on the road and no missing towels at the last booking.
Swipe for the 3 steps.
Run a home salon or beauty service at doorstep? DM us.""", 2,
["#homesalon","#salonathome","#beautyservices","#beautybusinessindia"],
["Sand design with the headline 'Bookings across the city? Plan the route, not just the time.' A day ribbon for stylist 1 on Tuesday, booked by calls: 10:00 facial and threading in area A, 35 minutes of travel, a gap, 12:00 hair spa in area B, 50 minutes of travel, 14:05 manicure and pedicure in area D, ending at 3:35 PM. Cards below: 85 minutes on the road in one day, 3 areas booked far apart, 1 kit bag packed for three services.",
 "Step 1, slots by area: four area cards with time slots, some already taken: area A, area B, area C and area D. A phone shows a sample booking page for a hair spa in area B on Tuesday 24 November with 1 PM picked, stylist 1, a chair and plug point needed, advance paid by UPI, and a button to confirm 1 PM.",
 "Step 2, the day's route for stylist 1 on Wednesday 25 November: a drawn map with areas A, B and C and four numbered stops on a dotted route. The list: 10:00 AM area A, facial and threading, 60 minutes; 11:20 AM area A, waxing, 45 minutes; 1:00 PM area B, hair spa, 75 minutes; 3:00 PM area C, manicure, 45 minutes. 4 bookings and about 40 minutes on the road.",
 "Step 3, kit checklist from bookings: an open coral kit bag with six compartments: facial kit and threading set for booking 1, wax heater and strips for booking 2, hair spa cream and steamer for booking 3, nail kit for booking 4, all checked, and fresh towels times 4 for all bookings, not packed yet. Note: 5 of 6 packed, towels are still missing, and the app reminds the stylist before leaving home.",
 "Closing slide with the headline 'Run a home salon service? Let's build your booking app.' Four tiles: slots by area, day route, kit checklist and advance by UPI, and the question: how do you plan your stylists' day today? Tell us in the comments."],
 S(scroll=8,save=9,send=8,clarity=9,finish=9,original=9)))
print(save(239,"SINGLE","India","DoorstepBikeService","Bike servicing at doorstep",["p239_bike"],
"""Service record app for doorstep bike servicing: every visit is saved with date, km reading and work done, parts used are listed, and the owner gets a reminder before the next service.
No more lost service books or guessing the last oil change.
Service bikes and scooters at home? DM us.""", 4,
["#bikeservice","#doorstepservice","#twowheelerservice","#bikeservicing"],
["Cream design with the headline 'Service book lost again? Keep every visit online.' Left: a sample service book for a 125 cc bike with three stamped visits: 12 January 2026 at 8,150 km, oil and chain; 18 May 2026 at 11,020 km, oil and brakes; 2 September 2026 at 13,940 km, oil and air filter. The next service is at 16,900 km: oil change, chain clean and brake check. Right: a dark card on the owner's phone showing today's reading of 15,780 km on a bar from 13,940 to 16,900, and parts used last visit: engine oil 1 litre, air filter replaced, chain cleaned and oiled. A reminder says about 1,100 km to go and offers a home visit this Sunday."],
 S(scroll=8,save=8,send=8,clarity=9,finish=9,original=8)))
print(save(240,"SINGLE","Canada","WoodStoveInstaller","Wood stove installer",["p240_stove"],
"""Site survey form for wood stove installers: the same five checks at every site, with measurements and photos saved, so the crew knows the job before install day.
No more second trips because a number was missing.
Install wood stoves or fireplace inserts? DM us.""", 1,
["#woodstove","#woodstoveinstallation","#hearth","#canadianbusiness"],
["Light grey design with the headline 'Same 5 checks at every site? Do them in one form.' Left: a drawn cutaway of a sample cabin living room with a wood stove on a floor pad and a pipe going up through the roof, with five numbered points. Right: a survey form for a sample cabin, lot 12: 1 wall distance, measured with a photo; 2 side distance, measured with a photo; 3 floor pad, stone, size noted; 4 pipe through roof, roof type and pitch noted; 5 room size, for the stove size you suggest. Below: install day Thursday 10 December, and the crew sees all 5 points before they arrive."],
 S(scroll=8,save=8,send=8,clarity=9,finish=9,original=9)))
