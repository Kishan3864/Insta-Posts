import sys; sys.path.insert(0, "tools"); from save_post import save
S = dict
print(save(146,"CAROUSEL","India","TourOperator","Tour operator (group trips)",[f"p146_tour_s{i}" for i in range(1,6)],
"""Trip booking website for tour operators: a live seat map, a trip page with the plan, payment status for every traveller and a pickup list for departure day.
No more seat lists on WhatsApp. Travellers pick their own seat, the 3 on hold get a reminder to pay, and on the day you can see who has boarded at each stop.
Swipe through all 3 parts.
Run weekend trips or group tours? DM us.""", 3,
["#touroperator","#grouptours","#weekendtrips","#travelbusinessindia"],
["Sand slide with the headline 'Seats on a WhatsApp list? Show a live seat map.' A top-down drawing of a 20-seat tempo traveller with numbered seats: 14 booked in teal, seats 9, 13 and 18 on hold in orange, seats 6, 16 and 20 free. Cards for a sample hill trip, Friday 18 to Sunday 20 December: 14 booked, 3 on hold (pay by Tuesday 24 November), 3 free. Note: travellers pick their own seat.",
 "Part 1, trip page: a browser page for a sample hill trip with a drawn mountain banner, a three-day plan (pickup 5:30 AM, sightseeing, drop back by 9 PM), what is included (van both ways, 2 nights stay, breakfast and dinner, sightseeing), '3 seats left' and a 'Book a seat' button.",
 "Part 2, payments: a table of sample travellers with seat number, pickup point and status: full paid, advance paid or on hold, due Tuesday. Totals: 9 full paid, 5 advance paid, 3 on hold, and a reminder sent to the 3 on hold to pay by Tuesday 24 November.",
 "Part 3, departure day: a phone pickup list for Friday 18 December: Point A 6 of 6 boarded, Point B 5 of 6 boarded, Point C next stop with 5, a late traveller with a call button and 'Message all 17'. Cards: stops in order, tick as they board, call who is late, message everyone.",
 "Closing slide with the headline 'Run group trips? Let's build your trip booking site.' A seat strip of 20 seats and a boarding pass card listing seat map, trip page, payments and pickup list for tour operators."],
 S(scroll=9,save=9,send=9,clarity=9,finish=9,original=9)))
print(save(147,"SINGLE","USA","SaaSFounder","SaaS founder (landing page + waitlist)",["p147_saas"],
"""Landing page and waitlist site for SaaS founders: the 5 parts every one-page site needs before you build the full product.
One clear promise, one email field, three key features, a short survey and an FAQ. Save this for your next idea.
Have a SaaS idea you want to test? DM us.""", 2,
["#saasfounder","#indiehackers","#landingpagedesign","#startupideas"],
["Dark violet design with the headline 'Testing a SaaS idea? Start with a one-page waitlist site. The 5 parts every landing page needs.' A sample landing page in a browser for an invoice app, with numbered pins on each part, and a matching list: 1 one clear promise, 2 one email field, 3 three key features, 4 a short survey, 5 FAQ."],
 S(scroll=8,save=9,send=8,clarity=9,finish=9,original=9)))
print(save(148,"SINGLE","India","SwimmingPool","Swimming pool (memberships + batches)",["p148_pool"],
"""Batch booking app for swimming pools: every batch shown as a lane with free spots, and a membership pass on each member's phone.
Members see which batch has space before they come, full batches close on their own, and the renewal reminder goes out 7 days before the pass ends.
Run a swimming pool or a pool club? DM us.""", 4,
["#swimmingpool","#swimmingclasses","#poolmembership","#swimmingindia"],
["Light blue tiled design with the headline 'Which batch has space? Show it lane by lane.' A top-down pool where each lane is a batch with dots for members: 6 AM adult beginners 2 left, 7 AM lap swim full, 8 AM ladies batch 4 left, 5 PM adult beginners 1 left, 6 PM lap swim 5 left, 7 PM ladies batch full. A phone shows a sample pool pass with batch, validity till 31 January 2027, a QR code, 18 of 24 visits used, a renewal reminder note and a 'Book a batch' button."],
 S(scroll=9,save=8,send=8,clarity=9,finish=9,original=9)))
print(save(149,"SINGLE","India","GSTPractitioner","GST practitioner (small office)",["p149_gst"],
"""Client document tracker for GST practitioners and small tax offices: see which client has sent sales bills, purchase bills and bank statements before each due date.
The app sends the reminder for you, so you stop chasing 20 clients on calls every month.
Run a GST or tax practice? DM us.""", 1,
["#gstpractitioner","#gstfiling","#taxconsultant","#accountingoffice"],
["Off-white design with the headline 'Chasing clients for bills before every due date? Let the app ask for them.' A spiral wall calendar for December 2026 with the 11th (GSTR-1) and 20th (GSTR-3B) circled for monthly filers, with a note to always check the portal. Next to it, a tracker of five sample clients with ticks and crosses for sales, purchase and bank documents, and an auto reminder sent to 3 clients asking for pending November bills by 5 December."],
 S(scroll=8,save=9,send=9,clarity=9,finish=9,original=8)))
print(save(150,"CAROUSEL","Canada","MartialArtsSchool","Martial arts school (adult classes)",[f"p150_ma_s{i}" for i in range(1,6)],
"""Member app for martial arts schools: a belt tracker, class booking, skill checklists and test day reminders for adult classes.
See who is ready for the next belt test without opening the binder, let members book spots, and send test day reminders on their own.
Swipe through all 3 parts.
Run a martial arts school or dojo? DM us.""", 5,
["#martialartsschool","#dojolife","#beltpromotion","#gymownerscanada"],
["Cream slide with the headline 'Who's ready for the next belt test? Know without the binder.' Drawn belts from white to brown with sample member counts and how many are ready: white 14 members 5 ready, yellow 11 and 4, orange 9 and 3, green 8 and 2, blue 6 and 1, brown 3 and 0. Totals: 51 adult members, 15 ready for the test on Saturday, December 12.",
 "Part 1, class booking: a browser week schedule from Monday to Saturday with adult beginners, sparring, forms, early class and open mat, each with spots left or 'Full'.",
 "Part 2, member progress: a sample green belt member with a ring showing 22 of 24 classes, 2 more classes to be ready for the blue belt test, and a skills list with four skills done and a board break next class.",
 "Part 3, test day: the belt test list for Saturday, December 12 with 15 members ready by belt (5, 4, 3, 2 and 1), and three automatic messages: a confirm request on Monday, November 30, an arrival reminder on Thursday, December 10 and results on test day.",
 "Closing slide with the headline 'Run a martial arts school? Let's build your member app.' Four belt tiles: belt tracker, class booking, skill checklists and auto reminders."],
 S(scroll=8,save=8,send=9,clarity=9,finish=9,original=9)))
