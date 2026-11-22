import sys, json; sys.path.insert(0, "tools"); from save_post import save
S = dict
out = []
out.append((21,"CAROUSEL","India","Kirana", save(21,"CAROUSEL","India","Kirana","Kirana / general store",
 [f"p21_kirana_s{i}" for i in range(1,6)],
"""Kirana store app for udhaar khata, monthly lists and payment reminders.
Your udhaar diary works hard, but it gets messy: cut amounts, arrows, lists on the back page. A simple kirana app keeps every customer's khata in one list, repeats monthly orders in one tap and sends a polite reminder on the 1st.
Swipe through all 5 slides. Then tell us in the comments: diary, register or app, how do you keep udhaar today?
Want one for your shop? DM us and we will plan it around how your counter works.""", 4,
["#kiranastore","#udhaar","#kiranashop","#retailindia","#shopowners"],
["Beige paper-style slide with an open notebook full of handwritten udhaar entries, crossed-out amounts and red notes saying 'Who paid?' and 'Which list?'. Headline: Udhaar diary full of cuts and arrows?",
 "A clean sample customer khata list showing each customer's last payment date and amount due or clear, next to three navy cards: find anyone fast, add udhaar in 2 taps, mark paid.",
 "A sample monthly grocery list for Flat 3B with items like atta, rice, dal and oil, a red button 'Repeat this list for December', and an order status panel from list received to delivered.",
 "A sample reminder message from 'Your Kirana Store' showing a November balance with a 'View bill and pay' button, a green 'Paid, khata updated' card, and reminder days: 1st, 5th and 10th.",
 "A hand-drawn shopkeeper pointing up next to a list of app features: customer khata, monthly lists, payment reminders, packing and delivery, daily sales view. Headline: Want a khata and order app for your kirana?"],
 S(scroll=9,save=9,send=9,clarity=9,finish=8,original=9))))
out.append((22,"SINGLE","India","DairyMilk", save(22,"SINGLE","India","DairyMilk","Dairy / milk delivery",["p22_dairy"],
"""Milk delivery app for dairies: month-end bills in one tap.
Every house, every day: litres delivered, skipped days and extra milk are counted on their own. At month end, each customer gets a bill with the full daily list.
DM us if you want this for your dairy.""", 1,
["#dairybusiness","#milkdelivery","#doodhwala","#dairyfarmindia"],
["Milk white and cobalt blue design with the headline 'Month-end milk bill? Ready in one tap.' A sample November calendar for Flat 204 shows 1 L on most days, 2 L extra on some days and skipped days in red. Below: total 30 L, 3 days skipped, and a button to send bills to every house."],
 S(scroll=9,save=8,send=9,clarity=10,finish=9,original=9))))
out.append((23,"SINGLE","India","TiffinService", save(23,"SINGLE","India","TiffinService","Tiffin / dabba service",["p23_tiffin"],
"""Tiffin service app: know tomorrow's meal count by 9 PM.
Customers skip lunch or dinner from their phone before the cut-off. Your kitchen gets the exact count in the morning, riders get their routes, and month-end bills only count the meals people ate.
Running a tiffin or dabba service? Send us a message and we'll show you how it can work for your kitchen.""", 3,
["#tiffinservice","#homemadefood","#dabbaservice","#cloudkitchenindia","#mealsubscription"],
["Deep green design with a yellow sun shape and the headline 'Who eats tomorrow? Know by 9 PM.' A dotted timeline shows a sample day: 9 PM skips close, 7 AM kitchen gets the count, 11 AM riders get routes, month end bills by meals eaten. A phone shows a sample screen with lunch and dinner toggles and a 'Save for tomorrow' button."],
 S(scroll=9,save=8,send=9,clarity=9,finish=9,original=9))))
out.append((24,"CAROUSEL","USA","Plumber", save(24,"CAROUSEL","USA","Plumber","Plumbing business",
 [f"p24_plumber_s{i}" for i in range(1,7)],
"""Plumbing website ideas: 4 things it should do after hours.
Let customers book a time window, flag a leak as urgent, send a photo of the problem and check your service area by ZIP code, all while your office is closed.
Swipe through all 6 slides to see each one.
We build websites and booking systems for plumbing companies in the US and Canada. DM us to talk it through.""", 5,
["#plumbingbusiness","#plumbersofinstagram","#plumbingcompany","#homeservicesbusiness","#contractorlife"],
["Blueprint-style navy slide with copper pipes, a dripping tap, a 'Closed now' office hours sign and a sample list of missed calls at night. Headline: Missed a burst-pipe call at 11 PM?",
 "A browser showing a sample 'Book a plumber' page with service chips, a day picker, time windows marked open or taken, contact fields and a confirm button.",
 "A sample urgent request form asking if water is leaking now, where the problem is, and whether the main valve is closed, with an orange tip card: Find the main shut-off valve and turn it off.",
 "A sample photo upload form with simple drawings of a pipe under a sink, a water heater label and a floor drain, plus a customer note about a dripping pipe joint.",
 "A ZIP code checker with a simple map showing service area rings around a pin and a green message: Yes, we serve your area.",
 "A hand-drawn smiling man next to four feature cards: time window booking, urgent requests, photo upload, ZIP code check. Headline: Want a website that books jobs after hours?"],
 S(scroll=9,save=9,send=8,clarity=9,finish=9,original=9))))
out.append((25,"SINGLE","India","SweetShop", save(25,"SINGLE","India","SweetShop","Sweet shop (mithai) bulk box orders",["p25_sweetshop"],
"""Sweet shop order board for bulk box orders.
Box size, quantity, pickup time and advance on one card. Move each order from New to Packing to Ready, and the customer gets a message when it is ready.
Want a board like this for your mithai shop? DM us.""", 2,
["#sweetshop","#mithaishop","#indiansweets","#bulkorders"],
["Pistachio green design with the headline 'Bulk box orders, from order to pickup.' A sample order board has three columns, New, Packing and Ready, each with order cards showing number of boxes, box size, sweet name, pickup time and a status tag. Three brown cards below: boxes needed per size, ready message to the customer, advance and balance noted."],
 S(scroll=8,save=8,send=8,clarity=9,finish=9,original=9))))
json.dump(out, open("work/saved.json","w"))
for o in out: print(o)
