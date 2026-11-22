import sys; sys.path.insert(0, "tools"); from save_post import save
S = dict
print(save(101,"SINGLE","India","EggSupplier","Poultry / egg supplier",["p101_eggs"],
"""Egg supplier software: trays given, empty trays back and payments for every shop on your route.
Know which shop still has your empty trays, who has not paid for how many days, and what each shop takes every morning. The month-end bill for each shop is ready on its own.
Supply eggs to shops and hotels? DM us.""", 2,
["#eggsupplier","#poultrybusiness","#eggdistributor","#deliveryroute"],
["Cream design with the headline 'Eggs to 40 shops every morning? Track trays, empties and dues per shop.' A top-down drawing of a 30-egg tray with two empty cups, and a dark card with a stack of trays: 12 empty trays still with shops, sample. Below, a sample table for today's route with five shops showing trays given, empties back (for example 10 of 12) and payment status, either Paid or Unpaid for 1, 2 or 5 days."],
 S(scroll=8,save=8,send=9,clarity=9,finish=8,original=9)))
print(save(102,"CAROUSEL","India","TextileWholesaler","Textile wholesaler (Surat)",[f"p102_textile_s{i}" for i in range(1,7)],
"""Textile wholesaler software for Surat and every cloth market: a design catalogue with live stock, broker orders, dispatch slips and credit days.
Brokers open one link to see what is in stock today. Their orders land in one list, stock is held when you confirm, the LR goes to the party in one tap, and you can see which bills are over 30 or 60 days.
Swipe through all 4 parts.
Run a textile wholesale business? DM us.""", 4,
["#surattextile","#textilewholesaler","#fabricwholesale","#textilebusiness","#clothmarket"],
["Cream slide with the headline 'Brokers order on photos and calls? Catalogue, orders and dispatch in one app.' A drawing of five stacked fabric rolls in cream, purple, yellow, rust and teal on a dark teal panel, and four step cards: catalogue, broker orders, dispatch and credit days.",
 "Part 1, catalogue: every design with live stock, one link. Six fabric swatches with sample design numbers and stock: D-401 cotton stripe 42 thans, D-402 yarn-dyed check 18 thans, D-405 rayon polka 6 thans, D-409 printed leaf 30 thans, D-411 ikat print 0 and on order, D-415 plain dyed 55 thans.",
 "Part 2, broker orders: every broker order in one list. Four sample orders from brokers A, B and C for parties in Jaipur, Pune, Indore and Kolkata, with design quantities and a status of New, Confirmed or Packing. Two notes: stock is held when an order is confirmed, brokers see status without calling you.",
 "Part 3, dispatch: 'Has my parcel left?' Send the LR in one tap. A sample dispatch slip for Sample Fabrics, Pune: 2 bales, 8 thans, Sample Transport, a sample LR number, sent Monday 23 November, with a barcode. Next to it, four steps: packed, bale made and given to transport are done; LR sent to party is next.",
 "Part 4, credit days: who is due, and for how many days? Three rows of sample bills: 0 to 30 days with four bills, 31 to 60 days with two bills, and over 60 days with one bill and a note that a reminder was sent on Friday. A note says bills move to the next row on their own.",
 "Closing dark teal slide with the headline 'Textile wholesaler? Let's build your order app.' The fabric roll drawing and a list: catalogue with live stock, broker orders in one list, dispatch slip and LR, credit days board."],
 S(scroll=8,save=9,send=9,clarity=9,finish=9,original=9)))
print(save(103,"SINGLE","USA","ThriftStore","Thrift / resale shop",["p103_thrift"],
"""Inventory website for thrift and resale shops: one list for your store and your site.
Tag an item, snap a photo, and it's online. When it sells at the register, it comes off your website on its own, so nobody drives over for something that's already gone.
Own a thrift or resale shop? DM us.""", 1,
["#thriftstore","#resaleshop","#secondhandshop","#thriftshopowner"],
["Mustard yellow design with the headline 'Sold in the shop, still on your website? One list for both.' Four manila hang tags on strings from a rail, each with an item code, item name, size and barcode: denim jacket, wool coat and table lamp say 'On your site', leather boots say 'Sold in store'. Below, a sample browser page 'New in this week' with six items: denim jacket, wool coat, leather boots marked sold in store and off the site, table lamp, canvas bag and side chair."],
 S(scroll=8,save=8,send=8,clarity=9,finish=9,original=9)))
print(save(104,"CAROUSEL","India","CarGarage","Four-wheeler garage",[f"p104_garage_s{i}" for i in range(1,6)],
"""Garage software for four-wheeler workshops: job cards at the gate, photo approvals before work and service reminders.
Every car gets a job card with reading, fuel level, complaints and photos. The customer gets the list of work on their phone and taps yes, and "can wait" items come back later as reminders.
Swipe to see the 3 steps.
Own a car garage or service centre? DM us.""", 3,
["#cargarage","#carservicecentre","#automobileworkshop","#garagebusiness"],
["Grey slide with the headline '“Why is the bill so high?” Show photos and get a yes before the work.' A top-down drawing of a car on a blue bay with four numbered red pins, and sample check-in notes: front bumper scratch, front right tyre worn on one side, windscreen small chip, rear left door dent from before.",
 "Step 1, job card: every car gets a job card at the gate. A sample browser job card JC-2231 hatchback in bay 3 with car number, owner, reading 48,210 km, promised Monday 23 November 6 pm, a fuel bar at 3 of 8, what the customer said, what the garage found, and five photo tiles.",
 "Step 2, approval: send the list, the customer taps yes. A phone shows a sample message asking to approve the work: brake pads and AC gas top-up needed now, wiper blades can wait, with 'Approve all' and 'Call me' buttons. Three cards: photo with each item, can-wait items saved, yes is on record.",
 "Step 3, reminders: bring them back before the next problem. Four sample cars with number plates and reminders: wiper blades at next visit, general service due this week, insurance renewal due in 12 days, wheel alignment due next week. A sample text: your car is due for a general service this week, reply 1 to book a slot.",
 "Closing yellow slide with the headline 'Run a car garage? Let's build your garage app.' The car drawing and a list: job card at the gate, photos and a yes before work, reminders that bring cars back, bills and history per car."],
 S(scroll=9,save=8,send=9,clarity=9,finish=9,original=9)))
print(save(105,"SINGLE","India","DryFruitsSeller","Dry fruits seller",["p105_dryfruit"],
"""Online gift box builder for dry fruits sellers: buyers pick the box size, fill each section and add a note card.
Bulk orders from companies come in as one clear form with quantity and delivery date, not 50 calls and voice notes.
Sell dry fruits or gift boxes? DM us.""", 5,
["#dryfruits","#dryfruitsindia","#giftboxes","#corporategiftsindia"],
["Almond cream design with the headline 'Gift box orders on 50 phone calls? Let buyers build the box online.' A top-down drawing of a 4-section gift box with almonds, cashews, pistachios and raisins on a green panel, with a colour legend. On the right, a sample 'Build your box' card for Your Dry Fruits: box size 4 sections, all four fillings chosen, a note card saying 'Thanks for a great year. Sample Co.', 40 boxes for delivery on 12 December, and a 'Send bulk order' button."],
 S(scroll=8,save=8,send=8,clarity=9,finish=9,original=9)))
