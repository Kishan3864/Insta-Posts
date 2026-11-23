import sys; sys.path.insert(0, "tools"); from save_post import save
S = dict
print(save(376,"SINGLE","India","ReadyMixConcrete","Ready-mix concrete (RMC) plant",["p376_rmc"],
"""Dispatch app for ready-mix concrete plants: each site sends 5 ready photos before the pour, and mixers leave the plant only for sites that are ready.
No mixer waiting at a site that is not ready.
Run an RMC plant or batching plant? DM us.""", 3,
["#readymixconcrete","#rmcplant","#concretework","#constructionsite"],
["Concrete grey and orange design with the headline 'Mixer stuck at the site? Send it only when ready.' A dark panel shows a site ready check for order RO-41 at Site A with five photo tiles, all ticked: shuttering done, steel checked, pump on site, labour ready, water and power, and a green label: all 5 OK, load now. Below, today's pours, sample, with one drawn mixer truck per 7 cubic metres: RO-41 roof slab 21 cubic metres loading now; RO-42 footing 14 cubic metres on hold, needs pump on site; RO-43 road PCC 28 cubic metres with trip 2 of 4 on the road; RO-44 columns 7 cubic metres on hold, needs shuttering done, water and power. An auto message to Site B says RO-42 is on hold until the pump photo is sent."],
 S(scroll=8,save=8,send=9,clarity=9,finish=9,original=9)))
print(save(377,"CAROUSEL","India","CottonGinning","Cotton ginning factory",[f"p377_gin_s{i}" for i in range(1,6)],
"""Gate and weighbridge app for cotton ginning factories: farmers get a token by phone, every trolley gets a weigh slip with net weight, and every lot is tracked until it becomes bales.
Shorter lines at the gate in peak season, and clear slips for every farmer.
It is all in one place for the owner too, with a day summary on the phone each evening.
Run a ginning or pressing factory? DM us.""", 5,
["#cottonginning","#ginningfactory","#cottonfarmers","#kapas","#agribusinessindia"],
["Cream and green design with the headline 'Tractor line outside the gin? Give every farmer a token.' A drawn gate sign for a sample ginning factory with two rows of tractors pulling cotton trolleys, tokens T-14 to T-20, and an amber board: now weighing T-14, next T-15 and T-16. Three problems: farmers wait all day with no idea when, paper slips get mixed up at the kanta, and the owner asks the press floor every hour. Three steps: token on arrival, weigh slip in seconds, lots to bales.",
 "Step 1, token on arrival: today's tokens at 20 minutes each, sample: T-14 weighing now, T-15 and T-16 at the gate, T-17 to T-20 with times from about 11:10 AM to 12:10 PM. A message to token T-18 says the turn is about 11:30 AM and a second message at 10:50 AM says leave now. What the farmer sends: name and village, trolley number, phone, and a photo of the cotton.",
 "Step 2, weigh slip in seconds: token T-14 on the kanta, full trolley 7,840 kg and empty trolley 3,260 kg, and an amber board showing net cotton 4,580 kg sent at 10:02 AM. A printed weigh slip WS-0482 for a sample farmer from Sample Village A with full and empty weights, net cotton 4,580 kg, moisture 8 percent as a sample, and lot L-07.",
 "Step 3, lots to bales: a press board with lint at 34 percent of cotton and 170 kg per bale, sample, with drawn bales per lot: L-07 4,580 kg gives 9 bales, L-08 6,200 kg gives 12, L-09 3,900 kg gives 7, L-10 5,100 kg gives 10. Totals: 19,780 kg cotton in 4 lots, 38 bales pressed, and a 6 PM owner message.",
 "Closing slide with the headline 'Run a ginning factory? Let's build your gate app.' A drawn tractor with a cotton trolley and stacked bales, four tiles: tokens, weigh slips, lot board and day summary, and the question: how long is the tractor line at your gate in peak season? Tell us in the comments."],
 S(scroll=8,save=9,send=8,clarity=9,finish=9,original=9)))
print(save(378,"SINGLE","USA","LawnAeration","Lawn aeration (spring sign-up list)",["p378_aeration"],
"""Sign-up site for lawn aeration crews: homeowners join a spring list by street, and a street gets its route day once enough neighbors sign up.
Full streets, short drives.
Run a lawn care crew? DM us.""", 2,
["#lawnaeration","#coreaeration","#lawncarebusiness","#springlawncare"],
["Mint and green design with the headline 'One yard per street? Fill the street first.' A top-down drawing of a sample neighborhood with three streets, Maple St, Oak Ave and Cedar Ln, ten houses each; 12 yards that signed up are shown with aeration plug dots and pink sprinkler flags. Below, a 1-minute sign-up form with address 14 Oak Ave, lawn size medium, sprinkler heads we'll flag them, and gate and pets: side gate open, dog inside. A dark card of route days that open at 5 yards, sample: Maple St 6 of 10 yards with a route day on Sat, Apr 11; Oak Ave 4 of 10, 1 more yard to open; Cedar Ln 2 of 10, 3 more yards to open."],
 S(scroll=8,save=8,send=8,clarity=9,finish=8,original=9)))
print(save(379,"SINGLE","India","HosieryWholesaler","Hosiery wholesaler (leggings, socks, vests)",["p379_hosiery"],
"""Order app for hosiery wholesalers: each retailer fills one colour and size sheet in dozens, stock is checked before packing, and cartons are planned per shop.
No more orders spread over chats and voice notes.
Sell hosiery wholesale? DM us.""", 4,
["#hosierywholesale","#leggingswholesale","#garmentwholesaler","#textilebusiness"],
["Light grey, navy and coral design with the headline 'Orders lost in 40 chats? One size sheet per shop.' Three chat messages marked before: leggings black 3 dozen XL and L mix, same as last time but less maroon, send navy XXL how many left. A big order sheet for R-12 Your Shop, leggings in dozens, sample: colours black, navy, maroon, beige and bottle green against sizes M, L, XL and XXL, with row totals 19, 12, 11, 5 and 5, size totals 9, 17, 17 and 9, and 52 dozen in all; maroon XXL is marked in red. A packing card at 10 dozen per carton with drawn cartons: R-12 52 dozen in 6 cartons, R-09 18 dozen in 2, R-15 25 dozen in 3, R-21 9 dozen in 1. A stock check: maroon XXL 3 dozen asked, 1 in stock, and the shop gets a message before packing."],
 S(scroll=8,save=8,send=8,clarity=9,finish=9,original=8)))
print(save(380,"SINGLE","India","GarmentTrimsShop","Button, zip and lace shop (garment trims)",["p380_trims"],
"""Order app for button, zip and lace shops: tailors pick the exact shade number from your card, choose length and quantity, and pick up a packed order.
The right zip, packed the first time.
Run a trims or tailoring material shop? DM us.""", 1,
["#tailoringmaterial","#buttonsandzips","#lacework","#tailorshop","#boutiqueindia"],
["Ivory and teal design with the headline 'Which zip matches? Send the shade number.' A phone shows the Sample Trims Store shade card with twelve drawn zips, Z-101 to Z-135, with Z-114 selected, length 9 inches, 12 zips, matching buttons B-27 15 mm 48, matching lace L-08 cotton lace 5 metres, pickup today 4 PM, and an add to order button. Beside it, three packed orders, sample: Sample Tailors A ready for pickup at 4 PM with the same items; Sample Boutique B packing for 5 PM with Z-108 7 inch zips, B-12 buttons and net lace; Sample Tailors C new for delivery tomorrow with Z-111 12 inch zips, B-03 buttons and gota lace. A dark note: tailors pick from the same shade numbers printed on your card."],
 S(scroll=8,save=8,send=9,clarity=9,finish=9,original=9)))
