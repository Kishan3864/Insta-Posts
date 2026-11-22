import sys; sys.path.insert(0, "tools"); from save_post import save
S = dict
print(save(96,"SINGLE","India","ROWaterPurifier","RO water purifier dealer",["p96_ro"],
"""RO water purifier dealer software: every installation with its filter change dates and an automatic reminder text.
See which customers are due this week, remind them before the water tastes bad, and let them reply to book a service visit. AMC visits sit in the same list.
Sell and service RO purifiers? DM us.""", 2,
["#rowaterpurifier","#roservice","#waterpurifierdealer","#amcservice"],
["Aqua design with the headline 'Customers call only when the water tastes bad? Remind them before the filter is due.' A drawing of an RO purifier opened up to show three filters labelled sediment, carbon and membrane. Next to it, a 'coming up' list of four sample customers with filter life bars: sediment due Tuesday, carbon due Thursday, a service visit due Saturday and a membrane due next month. Below, a sample reminder text: 'Your RO sediment filter is due for a change on Tuesday. Reply 1 to book a visit.'"],
 S(scroll=8,save=8,send=9,clarity=9,finish=9,original=9)))
print(save(97,"CAROUSEL","USA","TowingCompany","Towing company",[f"p97_towing_s{i}" for i in range(1,6)],
"""Towing dispatch software: a quick call form, a dispatch board for every truck and a live tracking link for the customer.
Every call becomes a job while the caller is still on the line. Move jobs from waiting to done on one board, and the customer gets a text with a live link, so fewer "where is the truck?" calls.
Swipe through the 3 steps.
Run a towing or roadside company? DM us.""", 4,
["#towingcompany","#towtruck","#roadsideassistance","#towingservice"],
["Dark slide with the headline 'Tow calls on sticky notes? Turn every call into a job on one board.' A drawing of a white flatbed tow truck with an amber light bar carrying a gray sedan. Below, a sample new call card: sedan won't start, pickup Hwy 80 exit 12, drop-off Sample Auto Shop.",
 "Step 1, call form: one short form while they talk. A browser form with five filled sample fields: caller phone, pickup location, vehicle, problem and drop-off, a tow type choice with flatbed selected, and a 'Create job and send a truck' button.",
 "Step 2, dispatch board: every truck and every job on one screen. Five lanes, waiting, en route, on scene, towing and done, each with sample job cards like Job 40, Truck 3, 12 min away, lockout. A note: drag a job to the next lane and the customer gets a text at each step.",
 "Step 3, customer text: no more 'where is the truck?' calls, send a live link. A phone shows a text saying Truck 3 is on the way with a tracking link, a small map with the truck's route, about 12 min away. Three cards: sent on its own, live location, replies come to you.",
 "Closing amber slide with the headline 'Want a dispatch board for your towing company?' The tow truck drawing and a list: call form in 5 fields, dispatch board, live link for the customer, photos and payment per job."],
 S(scroll=8,save=8,send=9,clarity=9,finish=9,original=9)))
print(save(98,"SINGLE","India","LatheWorkshop","Engineering workshop / lathe and CNC",["p98_lathe"],
"""Job card software for lathe, CNC and engineering workshops: every job with its drawing, machine, quantity done and delivery date.
When a party calls asking "when will my job be ready?", you answer in seconds. A machine load board shows which machine is busy and when it is free, so you promise dates you can keep.
Run an engineering workshop? DM us.""", 1,
["#engineeringworkshop","#latheworkshop","#cncmachining","#jobwork","#msmeindia"],
["Dark green design with the headline '“When will my job be ready?” Every job card, with its delivery date.' A technical drawing of a stepped shaft on grid paper with dimensions 480, 200, diameter 110 and diameter 80, and a sample job card J-318 shaft for sample party B, EN8 steel, Lathe 2, delivery 28 Nov, 24 of 40 done. Below, a sample machine load board: Lathe 1 free at 4 pm, Lathe 2 free tomorrow, CNC 1 free Wednesday, milling free now."],
 S(scroll=8,save=8,send=9,clarity=9,finish=9,original=9)))
print(save(99,"CAROUSEL","India","PowerloomUnit","Powerloom / weaving unit",[f"p99_loom_s{i}" for i in range(1,6)],
"""Powerloom and weaving unit software: live loom status, metres per loom per shift and beam finish dates.
See all your looms on one screen, compare day and night shift output, and know which beam finishes tonight before the loom stops. Thread breaks get logged so you can see where time is lost.
Swipe to see all 3 parts.
Own a powerloom or weaving unit? DM us.""", 3,
["#powerloom","#weavingunit","#textilemanufacturing","#surattextile"],
["Cotton white slide with the headline 'Which loom made how many metres? Know every loom, every shift.' On a dark panel, a drawing of a warp beam roll with red, blue and white threads, and a card: beam B-12, 860 of 1,200 m woven. Three small cards: 24 looms on one screen, 2 shifts compared, live thread break alerts.",
 "Part 1, loom floor: all 24 looms on one screen. A grid of looms L-01 to L-24 in sample status colours: 20 running in green, 2 thread breaks in red, 1 beam change in blue and 1 idle in grey.",
 "Part 2, shifts: day shift vs night shift, metres per loom. Paired bars for looms L-01 to L-06 with sample metres, and a red note: L-05 night shift made 180 m because it stopped 4 hours for a thread break.",
 "Part 3, beams: know when each beam will run out. Three sample beam cards with progress bars: B-12 on L-07 about 2 days left, next beam ready; B-15 on L-11 finishes tonight, next beam not ready; B-09 on L-02 about 6 days left.",
 "Closing slide with the headline 'Run a powerloom or weaving unit? Let's build your loom app.' A card with coloured thread stripes on the left and a list: loom status live, metres per loom per shift, beam finish dates, thread break log."],
 S(scroll=8,save=9,send=9,clarity=9,finish=9,original=9)))
print(save(100,"SINGLE","Canada","FarmersMarket","Farmers market vendor",["p100_market"],
"""Pre-order website for farmers market vendors: customers reserve before market day and pick up at your stall.
Pack only what's ordered. Set a pickup time window, close pre-orders the day before, and items show sold out on their own when the reserved count is full.
Sell at a farmers market? DM us.""", 5,
["#farmersmarket","#farmersmarketvendor","#shoplocalcanada","#winterfarmersmarket"],
["Beige design with the headline 'Sold out by 10 am, or stuck with extra? Take pre-orders before market day.' A drawing of a market stall with a purple striped awning, a chalkboard sign saying 'Pre-ordered? Pick up here', and crates of red apples and squash. A dark card: pre-orders close Friday 6 pm, you pack only what's ordered. On the right, a sample pre-order page for a Saturday winter market with pickup times and a stall number, items with quantity buttons and reserved bars: apples 32 of 40, butternut squash 18 of 25, potatoes 21 of 30, farm eggs sold out, honey 9 of 20, and a 'Reserve for pickup' button."],
 S(scroll=9,save=8,send=9,clarity=9,finish=9,original=9)))
