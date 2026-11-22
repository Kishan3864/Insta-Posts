import sys; sys.path.insert(0, "tools"); from save_post import save
S = dict
print(save(296,"SINGLE","India","WatchRepair","Watch repair shop",["p296_watch"],
"""Job tray and message app for watch repair shops: every watch gets a job number, a promised ready time and a status, and the customer gets a message when it is ready.
Fewer "is it done yet?" calls.
Repair watches or clocks? DM us.""", 1,
["#watchrepair","#watchservice","#watchshop","#smallbusinessindia"],
["Ivory and deep green design with the headline 'Is my watch done? The hands show when.' A dark green job tray with six drawn watches, each with its hands pointing to the ready time and a coloured ring: W-31 battery change, ready 12:30 PM; W-32 strap change, ready 4 PM; W-33 glass change, ready Tuesday 5 PM; W-34 full service, ready Saturday 11 AM; W-35 crown repair, part ordered, waiting; W-36 battery change, ready 1 PM. A message, sample: your watch W-31 (battery change) is ready, please collect it before 8 PM. A legend: ready, in work, booked, waiting for part."],
 S(scroll=9,save=8,send=8,clarity=9,finish=9,original=9)))
print(save(297,"CAROUSEL","India","PapadUnit","Papad and snacks home unit",[f"p297_papad_s{i}" for i in range(1,6)],
"""Order and batch app for papad and snack home units: shops order by packet on one link, you see the totals, turn packets into dough with your own rule, and dispatch by shop with a message.
No more orders lost in long voice notes.
Swipe for the 3 steps.
Make papad, chips or namkeen at home for shops? DM us.""", 3,
["#papad","#homemadesnacks","#homebusinessindia","#womenentrepreneurs"],
["Beige design with the headline 'Orders on voice notes? Put them in one sheet.' Drying mats with rows of drawn papads: plain, masala and moong. A dark voice note bubble, 0:48: send 10 masala, 6 plain, no wait, 8 plain, and the moong one also.",
 "Step 1, one order sheet for all shops, sample: shop S-01 8 plain, 10 masala, 4 moong; S-02 12, 6, none; S-03 6, 6, 6; S-04 10, none, 8; S-05 4, 8, 2. Packets: 40 plain, 30 masala, 20 moong. Note: orders close every Wednesday at 6 PM, so Thursday's batch is planned.",
 "Step 2, packets to dough by a rule: headline '40 packets of plain? Know the dough first.' Plain: 40 packets, 800 papads, 20 kg dough. Masala: 30 packets, 600 papads, 15 kg dough. Moong: 20 packets, 400 papads, 10 kg dough. Note: sample rule, 1 packet is 20 papads and 1 kg dough makes 40 papads, change it to your own.",
 "Step 3, packed and dispatched by shop, with one small packet icon for each packet: Friday 27 November, S-01 and S-02, 40 packets; Saturday 28 November, S-03 and S-04, 36 packets; Saturday 28 November, S-05, 14 packets. Note: the shop gets a message when its packets leave, 90 packets this week, sample.",
 "Closing slide with the headline 'Make papad or snacks at home? Let's build your order sheet.' Rows of drawn papads, four tiles: order link, batch plan, packing list and dispatch, and the question: how do shops send you orders today? Tell us in the comments."],
 S(scroll=8,save=9,send=9,clarity=9,finish=8,original=9)))
print(save(298,"SINGLE","USA","HotTubService","Hot tub service",["p298_hottub"],
"""Visit log and report app for hot tub service companies: every weekly visit records pH, sanitizer and filter work, and the owner gets a visit report with a photo and the next visit time.
Clients see the work, even when they are not home.
Service hot tubs or spas? DM us.""", 5,
["#hottubservice","#spaservice","#hottubcare","#backyardliving"],
["Light aqua design with the headline 'Every visit logged, every reading shared.' Left: a top view of a sample client hot tub with a cedar frame, four seats with jets and a filter in the middle, and a visit log: Tuesday 3 November pH 7.4, sanitizer 3 ppm, filter rinsed; Tuesday 10 November pH 7.6, 2 ppm; Tuesday 17 November pH 7.5, 3 ppm, filter rinsed. Right: a phone with a sample visit report for Tuesday 17 November: a photo of clear water, pH 7.5, sanitizer 3 ppm, filter rinsed, cover clips OK, next visit Tuesday 24 November AM, tech note: one cover strap is loose, new strap next visit, and a change my visit button."],
 S(scroll=8,save=8,send=8,clarity=9,finish=8,original=9)))
print(save(299,"SINGLE","India","DTPCentre","Typing and DTP centre",["p299_dtp"],
"""Token and job queue app for typing and DTP centres: each customer gets a token with a ready time on a screen, sends files on a link, and gets a message when it is their turn.
No crowd at the counter, no lost pen drives.
Run a typing, DTP or print centre? DM us.""", 2,
["#dtpcentre","#typingcentre","#printingshop","#localbusinessindia"],
["Light cyan design with the headline 'A crowd at the counter? Give them a token.' A dark LED token board, sample: T-14 resume typing, now; T-15 shop bill book design, 11:40 AM; T-16 form filling, 3 pages, 12:10 PM; T-17 wedding card proof, 12:45 PM. Bottom left: files received on the link: T-15 logo and rates, 2 files, got it; T-16 ID page photo, 1 file, got it; T-17 card text, proof sent. Bottom right: messages, sample: your bill book design is ready at 11:40 AM, you are next; T-16, your forms will be ready at 12:10 PM, please bring the original ID. In queue 4, done today 13."],
 S(scroll=8,save=8,send=8,clarity=9,finish=8,original=9)))
print(save(300,"SINGLE","India","SteelUtensilsBulk","Steel utensils shop (bulk for caterers)",["p300_utensils"],
"""Bulk order app for steel utensil shops that supply caterers: the guest count and a simple rule turn into plates, bowls and glasses, with a ready time, delivery and one-tap repeat orders.
Count by guests, not by guesswork.
Sell steel utensils to caterers or event teams? DM us.""", 4,
["#steelutensils","#cateringsupplies","#utensilshop","#wholesaleindia"],
["Light grey design with the headline '300 guests on Saturday? Count it in stacks.' Three white cards with drawn steel stacks: 300 full plates, 600 katori bowls and 300 glasses, each with a sample note of how many pieces one layer shows. A dark order card, caterer order C-300, sample: event Saturday 28 November, 300 guests; rule 1 plate, 2 bowls and 1 glass a guest; ready Friday 27 November 6 PM; delivery by tempo Saturday 7 AM. A white card: repeat order, one tap next time, the same list comes back and updates when you change the guest count."],
 S(scroll=8,save=8,send=8,clarity=9,finish=8,original=8)))
