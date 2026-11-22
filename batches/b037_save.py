import sys; sys.path.insert(0, "tools"); from save_post import save
S = dict
print(save(201,"SINGLE","India","IceFactory","Ice factory: morning delivery round",["p201_ice"],
"""Delivery round app for ice factories: every shop's morning slot, block count and delivery status on one clock, with bills due shown the same day.
Your tempo drivers know the order, and no shop waits for its ice.
Run an ice factory or ice supply business? DM us.""", 2,
["#icefactory","#iceblocks","#icesupplier","#smallbusinessindia"],
["Deep blue design with the headline 'Every shop wants ice before 8 AM? Plan it on one clock.' Left: a clock dial with four coloured delivery slots between 4:30 and 7:45 AM, numbered 1 to 4, and the hands at 5:40. Right: the sample round: 1 Sample Fish Market, 4:30 AM, 40 blocks, delivered; 2 Sample Hotel, 5:30 AM, 20 blocks, on the way; 3 juice stall row, 6:15 AM, 12 blocks, next; 4 Sample Caterer, 7:00 AM, 24 blocks, next. Below: 96 blocks today, 2 tempos on the road, 1 bill due today from Sample Hotel."],
 S(scroll=9,save=8,send=8,clarity=9,finish=9,original=9)))
print(save(202,"CAROUSEL","India","CurtainBlinds","Curtain and blinds shop",[f"p202_curtain_s{i}" for i in range(1,6)],
"""Measure-to-fit app for curtain and blinds shops: save every window with its size, type and photo on site, pick a fabric and let the app work out the metres, then track each job from fabric cut to fitted.
No more lost paper slips or wrong cuts at the counter.
Swipe to see all 3 parts.
Sell curtains, blinds or home furnishing? DM us.""", 4,
["#curtainshop","#blindsandcurtains","#homefurnishing","#curtainstitching","#interiorsindia"],
["Linen coloured slide with the headline 'Window sizes on a torn paper slip? Measure once, fit right.' Left: a torn paper slip with handwritten sizes: Hall 6.5 by question mark, Bedroom 5 by 4 and a half, Kitchen 3 by 3 blind with a question mark, Balcony 4 by 7 door, Fabric question marks. Right: three problem cards: which room was 6.5 ft, eyelet or pleated, and how many metres to cut.",
 "Part 1, measure on site: four drawn windows with size lines: Hall 7 by 5 ft with an eyelet curtain, Bedroom 1 5 by 4 and a half ft with a pleated curtain, Kitchen 3 by 3 ft with a roller blind, and a balcony door 4 by 7 ft with an eyelet curtain. A note says a site photo is saved with each window.",
 "Part 2, fabric and metres: four fabric swatches (natural linen selected, stripe, plain sage, blackout) and a table: Hall 4 panels of 2.4 m, 9.6 m; Bedroom 1 3 panels of 2.2 m, 6.6 m; Balcony door 2 panels of 2.7 m, 5.4 m; total 21.6 m of natural linen for 3 rooms, plus 1 olive roller blind for the kitchen.",
 "Part 3, stitching and fitting: a grid of items against stages fabric cut, stitching, ready and fitted. Hall is in stitching; Bedroom 1, balcony and kitchen are ready. A fitting card for Saturday 28 Nov at 11 AM says Hall stitching ends Thursday, and a team list: 3 curtain rods with brackets, 9 stitched panels, 1 roller blind, drill and spirit level.",
 "Closing slide with the headline 'Sell curtains and blinds? Let's build your measure-to-fit app.' A large drawn window with terracotta curtains and four tiles: site measure, fabric picker, job tracker, fitting day."],
 S(scroll=8,save=9,send=8,clarity=9,finish=9,original=9)))
print(save(203,"SINGLE","USA","ChimneySweep","Chimney sweep company",["p203_chimney"],
"""Online booking for chimney sweeps: customers check your service area by ZIP code, pick sweep and inspection or inspection only, and choose an open day and time.
After the visit, they get a report with flue photos and the next sweep date.
Run a chimney sweep or fireplace service? DM us.""", 3,
["#chimneysweep","#chimneycleaning","#fireplaceservice","#smallbusinessusa"],
["Cream design with the headline 'Every fireplace wants a sweep this month? Let them book online.' Left: a drawn house with a brick chimney and a fire in the fireplace, with a tag: soot in the flue, book a sweep before the first fire. Right: a browser booking page: ZIP 12345, we serve this area; sweep and inspection selected; open days Tuesday 24 to Monday 30 November; 9 AM selected; a button to book Tuesday, Nov 24 at 9 AM. Below, a dark bar: after the visit, they get a report with flue photos, cap checked, damper checked and next sweep in November 2027."],
 S(scroll=8,save=8,send=8,clarity=9,finish=9,original=9)))
print(save(204,"SINGLE","India","LiftAMC","Lift AMC and service company",["p204_lift"],
"""Service app for lift AMC companies: every lift in every building with its last visit, next due date and open breakdown calls, and each technician's list for the day.
No more wall charts, and no missed monthly visits.
Run a lift or elevator service company? DM us.""", 5,
["#liftamc","#liftservice","#elevatormaintenance","#facilitymanagement"],
["Light grey design with the headline 'Lift visits on a wall chart? See every lift's status at once.' Six drawn lifts, each with an amber floor display above steel doors: Sample Tower A, visit done 3 Nov; Sample Plaza, due today with Tech 1; Sample Heights B highlighted in dark with the doors open, a stuck call with Tech 2 on the way; Sample Residency, due 28 Nov; Sample Mall lift 2, due today with Tech 1; Sample Apartments, visit done 9 Nov. Below: Tech 1 has 2 visits, Sample Plaza then Sample Mall; Tech 2 has 1 stuck call at Sample Heights B, floor 4."],
 S(scroll=9,save=8,send=8,clarity=9,finish=9,original=9)))
print(save(205,"SINGLE","India","AquariumShop","Aquarium shop with tank care visits",["p205_aquarium"],
"""Tank care app for aquarium shops: every customer tank with its size, visit cycle and what was done last time, and a reminder goes out before the next visit.
Your team never misses a tank, and customers know when you are coming.
Run an aquarium shop? DM us.""", 1,
["#aquariumshop","#aquariumcare","#fishtank","#aquariumindia"],
["Sand coloured design with the headline 'Tank cleaning every 2 weeks? Never miss a customer's visit.' A drawn aquarium with fish, plants, gravel and bubbles, tagged Tank T-12, 3 ft, Sample home, Sector 4. Below it a strip of days from 10 to 24 November: visit on 10 Nov, today 22 Nov, next visit 24 Nov. Bottom left: last visit on 10 Nov: 30% water change, filter sponge cleaned, glass cleaned inside, fish food refilled. Bottom right: reminder sent today, visit on Tuesday, 24 Nov at 11 AM at Sample home, tech brings filter wool."],
 S(scroll=8,save=8,send=8,clarity=9,finish=9,original=9)))
