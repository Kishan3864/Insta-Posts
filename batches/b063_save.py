import sys; sys.path.insert(0, "tools"); from save_post import save
S = dict
print(save(331,"SINGLE","India","NewspaperAgency","Newspaper agency with home delivery",["p331_paper"],
"""Billing app for newspaper agencies and paper vendors: a delivery register per building, pause days marked when a customer replies, and a month-end bill per flat with exact copies, sent by message with a UPI link.
No more arguments over 4 missing days.
Run a newspaper agency or delivery line? DM us.""", 2,
["#newspaperagency","#newspaperdelivery","#paperwala","#localbusinessindia"],
["Light grey design with the headline 'Month-end bills by memory? Count every paper.' Left: a sample register for Tower B in November with six flats, each with a strip of 30 day boxes, black for delivered and red outline for paused: B-201 paused 2 days, B-202 3 days, B-304 4 days. Right: a paper receipt with zigzag edges for flat B-304: English daily 30 days, paused 12 to 15 November minus 4 days, 26 copies delivered; weekly magazine on Sundays 5 issues, paused Sunday 15 November minus 1, 4 delivered; to pay for 30 papers. A small calendar with 12 to 15 marked, a note that the bill is sent by message on 1 December, and a Pay by UPI button."],
 S(scroll=8,save=8,send=9,clarity=9,finish=9,original=9)))
print(save(332,"SINGLE","India","HydroponicFarm","Hydroponic farm",["p332_hydro"],
"""Grow and order app for hydroponic farms: every channel with its crop, week and harvest date, buyer orders matched to what is ready, and a message to buyers when a crop comes later.
Sell what is ready, not what you hope is ready.
Grow hydroponic greens or microgreens? DM us.""", 5,
["#hydroponics","#hydroponicfarming","#urbanfarmingindia","#freshgreens"],
["Light green design with the headline 'Which channel is ready? Know before buyers call.' A dark grow room card with six drawn white grow pipes, C1 to C6, nine plants each, plants bigger as they get older, sample: C1 lettuce week 5 harvest Saturday 28 November, C2 lettuce week 3, C3 basil week 4 harvest Friday 4 December, C4 spinach week 5 harvest Saturday 28 November, C5 pak choi week 2, C6 basil week 1. Below, buyer orders for Saturday 28 November in kg: Café 1 lettuce 6, Restaurant 2 basil 2, Salad bar 3 spinach 4, Hotel 4 lettuce 5. A green note: C1 and C4 ready on Saturday; basil for Restaurant 2 comes from C3 next Friday, so they get a message today."],
 S(scroll=8,save=8,send=8,clarity=9,finish=9,original=9)))
print(save(333,"CAROUSEL","India","LaptopRental","Laptop rental for offices and events",[f"p333_laptops_s{i}" for i in range(1,6)],
"""Rental app for laptop and IT equipment rental businesses: every rental lists its exact tag numbers, returns show on a calendar, each unit is checked for charger, bag and keys, and clients get the list by message.
Swipe for the 3 steps.
Rent laptops, desktops or event IT gear? DM us.""", 3,
["#laptoprental","#itrental","#eventtech","#rentalbusinessindia"],
["Light grey design with the headline '40 laptops out on rent. Who has L-33?' A card for Training C, laptops L-26 to L-40, sample: 15 drawn laptops with yellow tag stickers, three of them in red with L-question mark. A dark note from Training C at 11:20 AM: we returned all 15 laptops, your sheet says 14.",
 "Step 1, every tag has a client: three cards, sample: Company A, office project, 15 units L-01 to L-15, out Monday 2 November, back Monday 30 November; Event B, 3-day event, 10 units L-16 to L-25, out Tuesday 24 November, back Friday 27 November; Training C, staff class, 15 units L-26 to L-40, out Monday 16 November, back Monday 30 November. Note: 40 laptops out, 3 clients, search any tag and see who has it.",
 "Step 2, returns on a calendar: a bar chart of laptops out per day out of 40, from Monday 23 November to Monday 30 November: 30, then 40 from Tuesday to Friday, then 30. Two cards: Friday 27 November, Event B returns 10; Monday 30 November, A and C return 30, pickup van booked and check sheet ready.",
 "Step 3, check every unit on return: a table for Event B on Friday 27 November with tags L-16 to L-22 and ticks for screen, charger, bag and keys; L-19 is missing its charger and L-21 its bag, 5 of 7 shown complete. Note: Event B gets a message with the list.",
 "Closing slide with the headline 'Rent laptops or IT gear? Let's build your rental app.' Nine tagged laptops, four tiles: tag search, return calendar, return check and client messages, and the question: how do you track laptops out on rent today? Tell us in the comments."],
 S(scroll=8,save=8,send=8,clarity=9,finish=9,original=9)))
print(save(334,"SINGLE","India","SolarPanelCleaning","Rooftop solar panel cleaning service",["p334_solar"],
"""Visit planner for solar panel cleaning services: rooftops by area with panel counts, live progress on each roof, and an app where customers see before and after photos and their next visit.
Twice-a-month plans that run on time.
Clean rooftop solar panels? DM us.""", 4,
["#solarpanelcleaning","#rooftopsolar","#solarindia","#solarmaintenance"],
["Warm beige design with the headline 'Dusty panels on 40 rooftops? Plan every visit.' Left: a top-down drawing of rooftop R-12 on Tuesday 24 November, sample, with a water tank, a stair room and 16 solar panels, 10 cleaned in shiny navy and 6 still dusty. Below, today's list: R-10 Sector 4, 12 panels, done 7:50 AM; R-12 Sector 4, 16 panels, now 10 of 16; R-15 Sector 6, 24 panels, next 11 AM. Right: a phone showing your rooftop R-12, 16 panels, twice a month, cleaning now 10 of 16 done, before and after pictures, last visit Monday 9 November, next visit Tuesday 8 December 7 AM, team 2 with 2 cleaners, water from your tank tap on the roof, and a change visit time button."],
 S(scroll=8,save=8,send=8,clarity=9,finish=9,original=9)))
print(save(335,"SINGLE","USA","DumpsterRental","Roll-off dumpster rental",["p335_dumpster"],
"""Booking and dispatch board for roll-off dumpster rental companies: every unit by size, drop-off and pickup dates for each job, and online booking with a driveway photo and pin for the driver.
Know which dumpster is where, every morning.
Rent roll-off dumpsters? DM us.""", 1,
["#dumpsterrental","#rolloffdumpster","#junkhauling","#localbusinessusa"],
["Light grey-green design with the headline 'Which dumpster is where? See every drop and pickup.' Three drawn green roll-off dumpsters: 10 yard, 2 in yard and 2 out; 20 yard, 2 in yard and 3 out; 30 yard, 2 in yard and 1 out. A table of sample jobs for today, December 1: D-10-1 Oak St on site; D-20-1 Pine Ave on site; D-20-3 Lake Rd and D-30-2 Mill St drop today; D-10-2 Elm Ct and D-20-4 Birch Ln pickup today, with drop and pickup dates. A green note: customers book online and add a driveway photo with a pin, so the driver knows where to drop."],
 S(scroll=8,save=8,send=8,clarity=9,finish=9,original=9)))
