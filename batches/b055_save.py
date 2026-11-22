import sys; sys.path.insert(0, "tools"); from save_post import save
S = dict
print(save(291,"SINGLE","India","MandiCommissionAgent","Fruit commission agent (mandi)",["p291_mandi"],
"""Crate tracking app for fruit commission agents in the mandi: every crate given to a grower and every crate returned is logged, so you always know who still has your crates.
A reminder goes out before the next load.
Work as a commission agent or fruit trader? DM us.""", 1,
["#fruitmandi","#commissionagent","#fruitwholesale","#agribusinessindia"],
["Light mango design with the headline '120 crates went out. Who still has them?' A ledger for this week, sample, with one small green crate drawn for each crate: grower G-11, mango, 30 given, all back, 0 still out; G-14, banana, 40 given, 12 still out shown as dashed red crates; G-19, papaya, 20 given, 8 still out; G-23, guava, 30 given, 0 still out. A legend: faded crate came back, dashed crate still with the grower. A dark reminder to G-14, sample: you have 12 crates with you, please send them with your next load."],
 S(scroll=8,save=8,send=9,clarity=9,finish=8,original=9)))
print(save(292,"SINGLE","Canada","MobileBikeRepair","Mobile bike repair",["p292_bikerepair"],
"""Booking app for mobile bike repair: riders book a home visit with bike type, problem, tire size and photos, and your van load list for the day is built from the bookings.
No more driving out without the right tube.
Fix bikes at people's homes? DM us.""", 4,
["#mobilebikerepair","#bikerepair","#cyclingcanada","#bikemechanic"],
["Off-white design with the headline 'Drove there, no tube? Bookings fill the van.' Left: a phone with a sample mobile bike repair booking page: book a home visit, bike type hybrid, what needs fixing flat tire and brakes, tire size 700 by 35c, where driveway, postal code A1A 1A1, 2 photos added, visit Saturday PM, and a book visit button. Right: a green van with wheels and a shelf of bins, load for Saturday 28 November from 6 bookings: 4 tubes 700c, 2 tubes 26 in, 6 brake pads, 1 chain, 3 cables, 2 tire levers. Below: today, sample: flat tires 4 visits, brakes 3 visits, gears and chain 1 visit."],
 S(scroll=8,save=8,send=8,clarity=9,finish=8,original=9)))
print(save(293,"CAROUSEL","India","SeedlingNursery","Vegetable seedling nursery",[f"p293_seedling_s{i}" for i in range(1,6)],
"""Tray booking app for vegetable seedling nurseries: farmers see free trays by crop, book by tray, follow their batch from sowing to ready with weekly photos, and get a fixed pickup slot.
Swipe for the 3 steps.
Grow chilli, tomato or other vegetable seedlings for farmers? DM us.""", 2,
["#seedlingnursery","#vegetableseedlings","#nurserybusiness","#farmingindia"],
["Light design with the headline '2,000 chilli plants? Book trays, not calls.' A large drawn plug tray with 98 cells and green seedlings: 1 tray equals 98 seedlings, sample. Tiles: order 2,000 chilli seedlings, 21 trays of 98 cells, ready Monday 7 December, sample date.",
 "Step 1, trays available by crop: chilli, ready in about 5 weeks, 34 trays free; tomato, about 4 weeks, 18 trays free; brinjal, about 5 weeks, 9 trays free; cauliflower, about 4 weeks, sowing Monday 23 November. Each row has a small tray drawing.",
 "Step 2, every batch on a timeline: batch C-41, chilli, sample, 21 trays for order O-293. Stages with small trays: sow Monday 2 November, sprout Monday 9 November, grow Monday 16 to 30 November, harden Wednesday 2 December, ready Monday 7 December; sow and sprout done, grow in progress. Note: a tray photo goes to the farmer every week, so no one has to visit to check.",
 "Step 3, pickup slot and tray return: order O-293, sample: farmer F-118, crop chilli batch C-41, 2,000 seedlings in 21 trays, pickup Monday 7 December 7 AM, pickup van in 2 trips. A dark card: 21 trays to return, marked back when the van returns. A message on Sunday 6 December: your 21 trays are ready for 7 AM tomorrow.",
 "Closing slide with the headline 'Grow seedlings for farmers? Let's build your tray booking.' Three drawn plug trays, four tiles: trays by crop, batch timeline, weekly photos, pickup slots and tray returns, and the question: how do farmers book seedlings with you today? Tell us in the comments."],
 S(scroll=8,save=9,send=8,clarity=9,finish=8,original=9)))
print(save(294,"SINGLE","India","KeyShop","Key duplicate and lock shop",["p294_keyshop"],
"""Job and message app for key duplicate and lock shops: every key in a job is listed with its copies and ready time, the customer gets a ready message, and home visits for lock changes are booked with a photo of the lock.
No more waiting at the counter.
Run a key cutting or lock repair shop? DM us.""", 5,
["#keyduplicate","#keymaker","#locksmithindia","#localshop"],
["Cream design with the headline 'Come back in an hour? Send a ready message.' A white card for job K-294, the customer's key ring, sample, with four drawn keys with coloured caps: main door, 2 copies, ready 12:30 PM; bedroom, 1 copy, ready 12:30 PM; bike, 1 copy, ready 1 PM; cupboard, 2 copies, ready 1 PM. A dark card: 6 copies in this job, the ready message goes out when the last key is cut. A home visit card, sample: lock change, flat 3B, Saturday 28 November at 5 PM, photo of the lock received."],
 S(scroll=8,save=8,send=8,clarity=9,finish=8,original=8)))
print(save(295,"SINGLE","USA","SprinklerBlowout","Sprinkler blowout (winterizing)",["p295_sprinkler"],
"""Booking page for sprinkler blowout and winterizing companies: homeowners enter their zones, valve box, backflow and water shutoff, and you group bookings street by street.
Fewer surprises on site, shorter drives in a short season.
Do sprinkler blowouts or irrigation service? DM us.""", 3,
["#sprinklerblowout","#irrigationservice","#winterizing","#lawncarebusiness"],
["Pale blue design with the headline 'Blowout season is short. Book by zones and street.' Left: a top-down sample yard with 5 zones and 20 heads: a back fence, a patio with no heads, zones Z1 and Z2 behind the house, Z3, Z4 and Z5 in front, a valve box on the left side and the backflow on the right, and Sample Street at the bottom. Right: a booking form, sample: zones 5, valve box on the left side of the house, backflow on the right side outside, water shutoff found in the basement, day Saturday 5 December, morning. A dark card: same street route for Saturday 5 December: 8:00 AM house 12, 8:40 AM house 18, 9:20 AM your home, 10:00 AM house 31."],
 S(scroll=8,save=8,send=8,clarity=9,finish=8,original=9)))
