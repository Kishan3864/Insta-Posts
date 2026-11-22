import sys; sys.path.insert(0, "tools"); from save_post import save
S = dict
print(save(141,"SINGLE","India","AutoPartsDealer","Auto parts dealer",["p141_parts"],
"""Stock app for auto parts dealers: search a part number and see the godown, rack and bin it sits in, with the count in each place.
Mechanics get an answer in seconds, your staff stop searching every rack, and a reorder alert comes up before a fast part runs out.
Run an auto parts or spare parts shop? DM us.""", 3,
["#autoparts","#spareparts","#autopartsdealer","#bikeparts"],
["Grey design with the headline 'Mechanic needs part BP-210. Find it in 5 seconds, not 15 minutes.' A dark wall of 15 parts bins with labels like OF-118 oil filter and SP-44 spark plug; bin BP-210 brake pad glows red. Next to it, a search for BP-210 and a 'part found' card: brake pad set, front, fits sample bike models A, B and C, with 18 pieces in Godown 1 rack C bin 4, 6 in Godown 2 rack A bin 9 and 2 at the shop counter. Note: 26 pieces in all, reorder alert set at 10."],
 S(scroll=8,save=8,send=9,clarity=9,finish=9,original=9)))
print(save(142,"CAROUSEL","India","BuilderProject","Small real estate builder (project website + buyer app)",[f"p142_bl_s{i}" for i in range(1,6)],
"""Project website and buyer app for small builders: live flat availability, a page for every free flat, buyer stages and monthly site updates.
Buyers see which flats are sold, booked or free without calling you, open the plan of any free flat, and follow their flat's stages with photos every month.
Swipe through all 3 parts.
Building flats or a housing project? DM us.""", 1,
["#builders","#realestateindia","#flatsforsale","#constructionindia"],
["Grey slide with the headline 'Buyers keep asking “Which flats are free?” Show live availability on your project site.' A sample building drawn as a grid of 10 floors with flats A to D: dark for sold, terracotta for booked, white with a green border for available. Cards: 40 flats, 26 sold, 5 booked, 9 available.",
 "Part 1, flat page: every free flat with its plan, floor and facing. A browser page for available flat 7B, 2 BHK, with a simple floor plan of the living room, kitchen, two bedrooms, bath and balcony with room sizes, and details: 7th of 10 floors, 1,050 sq ft carpet area, east facing, 1 covered parking, and a 'Book a site visit' button.",
 "Part 2, buyer stages: each buyer sees which stage is done and what is next. A buyer page for flat 5A: booking, agreement, plinth and slabs 1 to 5 done, slabs 6 to 10 in progress with slab 9 of 10 cast, then brickwork, plaster and tiles, and possession. A note says the demand letter and site photos go to buyers on WhatsApp when a stage is done.",
 "Part 3, monthly update: buyers see the building grow without visiting the site. Four drawings of the building from August to November with slabs 4, 6, 8 and 9 cast, and an overall progress bar at slab 9 of 10.",
 "Closing slide with the headline 'Building flats? Let's build your project website and buyer app.' The building availability grid and four tiles: live availability, flat pages, buyer stages, monthly updates."],
 S(scroll=8,save=9,send=9,clarity=9,finish=9,original=9)))
print(save(143,"SINGLE","USA","CakeShop","Cake shop (custom cake order form)",["p143_cake"],
"""Custom cake order form for cake shops: size, flavor, filling, finish, topper text and pickup time in one form, with a cake preview that changes as they pick.
No more 40 DMs and voice notes per order. You get every detail in one place, and the customer gets a confirmation within a day.
Own a bakery or cake shop? DM us.""", 5,
["#cakeshop","#customcakes","#bakerybusiness","#cakeorders"],
["Cream design with the headline 'Cake orders over 40 DMs and voice notes? Send one custom cake order form.' A drawing of a three-tier vanilla cake with a raspberry drip and a '30' topper, labelled '3 tiers, vanilla, raspberry, drip' and 'Preview updates as they pick'. Next to it, a sample order form with choices for size, flavor, filling and finish, pickup Saturday, December 5 at 11 AM, topper text “30”, and a 'Send order' button."],
 S(scroll=8,save=8,send=9,clarity=9,finish=9,original=8)))
print(save(144,"SINGLE","India","PetGroomingHome","Pet grooming at home",["p144_petgroom"],
"""Booking app for home pet groomers: a profile for every pet with services and notes, visit stamps, reminders and a day plan for each groomer.
Pet parents don't have to repeat the same things every visit, you remember which pet is scared of the dryer, and the next visit reminder goes out on its own.
Groom pets at home? DM us.""", 2,
["#petgrooming","#doggrooming","#petgroomingathome","#petparentsindia"],
["Aqua design with the headline 'Pet parents ask the same questions every visit? Keep a profile for every pet.' Two pet profile cards with drawn faces: sample dog Bruno, Labrador, bath and nail trim, note 'scared of dryer noise', next visit Saturday 5 December; sample cat Mishti, Persian, brush, bath and ear clean, note 'calm if held on the lap', next visit Wednesday 9 December. Each has stamps for past visits. A phone shows Groomer 1's day with four home visits and a 'Send on my way message' button."],
 S(scroll=8,save=8,send=9,clarity=9,finish=8,original=9)))
print(save(145,"SINGLE","India","OilMill","Oil mill",["p145_oil"],
"""Stock and order app for oil mills: live level of every tank, dealer orders against that stock and an alert when a tank can't cover an order.
Know how much mustard, groundnut or sesame oil is left before you promise a dealer, and plan the next pressing batch in time.
Run an oil mill? DM us.""", 4,
["#oilmill","#mustardoil","#woodpressedoil","#edibleoil"],
["Cream design with the headline 'How much oil is left in each tank? Know before you take the order.' Three drawn storage tanks with sample levels: mustard at 72% of 8,000 L, groundnut at 38% of 6,000 L and sesame at 15% of 4,000 L. Below, dealer orders this week: Sample Dealer 1 mustard 120 tins packed, Sample Dealer 2 groundnut 80 tins filling today, Sample Dealer 3 sesame 60 tins needs pressing, and an alert: sesame tank at 15%, 600 L left, the order needs 900 L, plan a pressing batch."],
 S(scroll=8,save=8,send=8,clarity=9,finish=9,original=9)))
