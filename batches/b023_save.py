import sys; sys.path.insert(0, "tools"); from save_post import save
S = dict
print(save(131,"SINGLE","India","CabOperator","Cab / taxi operator",["p131_cab"],
"""Duty board app for cab and taxi operators: which car, which driver, which trip, and its status, all on one screen.
Every trip gets a log with km at start and end, fuel entries come with a photo of the bill, and you can see duty hours for each driver.
Run a cab or taxi service? DM us.""", 5,
["#cabservice","#taxiservice","#fleetowner","#travelsbusiness"],
["Off-white design with the headline '“Who took Car 4 today?” See every duty on one board.' A black split-flap style board titled Today's duties, 7 cars, 6 drivers, sample, with columns for time, car, driver, trip and status: 06:30 Car 4 Driver 2 airport done, 08:00 Car 1 city 8 hours on trip, 09:15 Car 7 outstation on trip, then station, hotel and airport trips marked next. Three cards below: trip log per car, fuel entries with a bill photo, duty hours per driver."],
 S(scroll=9,save=8,send=8,clarity=9,finish=9,original=9)))
print(save(132,"CAROUSEL","India","Homestay","Homestay owner (direct booking website)",[f"p132_hs_s{i}" for i in range(1,7)],
"""Booking website for homestays: your own rooms page, a live calendar, online booking with advance, and a guest guide link.
Guests see which rooms are free before they call, pay the advance directly to you and get the route and house rules in one link. You keep every guest's contact for next time.
Swipe through all 4 parts.
Run a homestay? DM us.""", 3,
["#homestay","#homestayindia","#hillstay","#directbooking"],
["Misty green slide with the headline 'Guests book your homestay through agents? Get your own booking website.' A drawing of a hill cottage with lit windows among pine trees and mountains at sunrise, with a card: Sample Homestay, 4 rooms, hill view, rooms free this weekend, Book direct. Three chips: your own photos, live calendar, advance online.",
 "Part 1, rooms page: your own photos and rooms, not a listing among hundreds. A browser shows four room cards with drawings: Valley View Room, Pine Room and Attic Room free on the guest's dates of 18 to 20 December, and Family Room booked.",
 "Part 2, live calendar: guests see free rooms before they call you. A December 2026 calendar showing rooms left out of 4 for each day in green, peach or grey, with 24 to 26 and 29 to 31 December full and the guest's dates, 18 and 19 December, outlined.",
 "Part 3, booking and advance: done while you sleep. A phone shows a sample booking for Valley View Room, check-in Friday 18 December, check-out Sunday 20 December, 2 guests, with 'Pay advance by UPI' and 'Advance paid, booking confirmed'. Side cards show the WhatsApp confirmation to the guest, the message to the owner, and 'No agent in the middle'.",
 "Part 4, guest guide: send one guide link instead of 20 messages. A folded guide card with check-in and check-out times, how to get there with a pickup from the main road, Wi-Fi, house rules and nearby spots.",
 "Closing slide with the headline 'Run a homestay? Let's build your own booking website.' The cottage scene and four tiles: rooms page, live calendar, book and advance, guest guide."],
 S(scroll=8,save=9,send=9,clarity=9,finish=9,original=8)))
print(save(133,"SINGLE","USA","DeliveryStartup","Courier / delivery startup (tracking page)",["p133_courier"],
"""Tracking page for delivery startups: every package gets a link with live steps, a delivery time window and a text at each step.
Fewer "where's my package?" calls for your team, and customers know when to be home.
Run a delivery or courier business? DM us.""", 1,
["#deliverybusiness","#courierservice","#lastmiledelivery","#smallbusinessusa"],
["Cream design with the headline '“Where's my package?” Give every customer a tracking page.' On the left, an isometric stack of cardboard parcels and a card: 1 link per package, sent by text the moment you pick it up. On the right, a browser tracking page for sample order SA-20417: expected today 2:30 to 3:00 PM, steps picked up at 9:12 AM, at our hub at 11:40 AM, out for delivery at 1:05 PM with Driver 3, and delivered still to come, plus the text that was sent."],
 S(scroll=8,save=8,send=8,clarity=9,finish=8,original=8)))
print(save(134,"SINGLE","India","FlourMill","Flour mill (atta chakki)",["p134_mill"],
"""Token and queue app for flour mills (atta chakki): a token for every bag, a live queue and a WhatsApp message when the flour is ready.
No lost paper slips, no mixed-up bags, and customers come only when their flour is ready.
Run a flour mill or grinding shop? DM us.""", 4,
["#flourmill","#attachakki","#chakki","#smallbusinessindia"],
["Wheat-coloured design with the headline 'Grain bags piling up with paper slips? Give a token, send a “ready” message.' A drawing of a flour mill with a hopper, motor and a sack marked T-42. A paper token: T-42, bajra 5 kg coarse, ready by 6:00 PM. Today's sample queue: token 41 wheat 10 kg ready and message sent, 42 bajra grinding now, 43 jowar next in line, 44 rice and 45 wheat in queue. A WhatsApp message: your wheat flour (token 41) is ready, please pick it up before 8 PM."],
 S(scroll=8,save=8,send=9,clarity=9,finish=9,original=9)))
print(save(135,"SINGLE","India","ExpenseTracker","Personal expense tracker (personal app)",["p135_expense"],
"""Personal expense tracker app: your monthly limits as envelopes, every expense added in seconds, and a clear view of where the money went.
Set a limit for groceries, travel, eating out, bills and shopping, and see right away when one goes over. A personal app made just for the way you spend.
Want an app built for your own use? DM us.""", 2,
["#expensetracker","#budgetplanner","#moneymanagement","#personalapp"],
["Manila design with the headline 'Where did this month's money go? Get an app made just for your spending.' Five sample envelopes with bars showing spent of limit: groceries ₹8,200 of ₹10,000, travel ₹2,100 of ₹3,000, eating out ₹3,900 of ₹3,000 marked over in red, bills ₹4,600 of ₹5,000, shopping ₹1,200 of ₹4,000. A phone shows today: ₹559 spent on chai, auto, vegetables and a phone recharge, and an add expense box for ₹450 under eating out."],
 S(scroll=8,save=8,send=8,clarity=9,finish=9,original=8)))
