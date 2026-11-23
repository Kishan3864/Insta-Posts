import sys; sys.path.insert(0, "tools"); from save_post import save
S = dict
print(save(366,"SINGLE","India","LaserCutting","CNC laser cutting job shop",["p366_laser"],
"""Job queue app for CNC laser cutting and sheet metal job shops: every job on its machine with a ready time, sheet changes planned, and a message to the customer when the parts are cut.
Fewer "is my job ready?" calls.
Run a laser cutting or fabrication shop? DM us.""", 3,
["#lasercutting","#cnclaser","#sheetmetal","#jobwork","#makeinindia"],
["Steel grey and orange design with the headline 'When will my job be cut? Show every machine's queue.' A queue board for today with three machines from 10:00 to 1:00 and a red line at now, 11:45, sample: Laser 1 for MS sheet 2 to 6 mm at 6 sheets an hour with jobs J-41, J-42 and J-44 done, J-47 on the machine and J-50 waiting; Laser 2 for SS sheet 1 to 2 mm at 8 sheets an hour with J-43, J-45 and J-48 done, J-51 on the machine and J-54 waiting; Bending on a press brake at 60 parts an hour with J-46, J-49, J-52 and J-55 done and J-56 waiting; striped blocks mark sheet or tool changes. Below: a job slip for J-50, MS 3 mm, 3 sheets, Laser 1, ready 12:55; a dark card with 15 jobs today, 32 sheets today and 10 ready to pick up; and a green auto message: Job J-44, your 4 sheets of MS 5 mm are cut, please pick them up today."],
 S(scroll=8,save=8,send=8,clarity=9,finish=9,original=9)))
print(save(367,"CAROUSEL","India","BatteryDealer","Battery dealer (car, bike, inverter)",[f"p367_battery_s{i}" for i in range(1,7)],
"""Sales and warranty app for battery dealers: every car, bike and inverter battery saved by serial number, warranty checked in one search, old batteries counted, and check-up reminders sent for you.
No more searching old bill books.
Sell or service batteries? DM us.""", 5,
["#batterydealer","#inverterbattery","#carbattery","#shopsoftware","#retailindia"],
["Grey and lime design with the headline 'Battery died, bill is lost. Find it by serial number.' A drawn battery with a lime label showing serial SN-24A-0187, a customer bubble saying he bought it here last year and the bill is lost, the shop asking which month and which model while three bill books for 2024, 2025 and 2026 pile up. Four steps: every sale saved, warranty in one search, old batteries counted, check-up reminders.",
 "Step 1, every sale saved: a browser with a new sale form, serial SN-31C-0518 scanned, inverter 200 Ah tubular, customer mobile masked, 48 months warranty, above a sales table with six sample sales showing serial, type, model, masked mobile, sale date and warranty months.",
 "Step 2, warranty in one search: a search box with SN-24A-0187. Result one: car battery 35 Ah, sold 14 Jan 2026, 24 months warranty, in warranty with 13 months left, a green timeline bar with a today marker. Result two: car battery 45 Ah, sold 9 Mar 2024, warranty ended on 9 Mar 2026, a red bar. Note: no bill book search, the customer gets a clear answer at the counter.",
 "Step 3, old batteries counted: blocks for old batteries taken in during November, sample: car 14, inverter 9, bike 22. An exchange slip for new battery SN-31C-0518 with an old inverter 150 Ah battery taken in on 2 Oct 2026, and a dark card: 45 old batteries in the store room for the recycler pickup.",
 "Step 4, check-up reminders: a phone chat from Your Battery Shop telling a customer the inverter battery was last checked 6 months ago and it is time for a water level check, reply 1 to book a home visit; the customer replies 1 and the visit is booked for Tuesday 11 AM to 1 PM. Beside it, five check-up visits this week by day and area.",
 "Closing slide with the headline 'Sell batteries? Let's build your shop app.' Three drawn batteries for car, inverter and bike with customer questions, four tiles: sale by serial, warranty search, exchange log and check-up reminders, and the question: how do you check warranty at your shop today? Tell us in the comments."],
 S(scroll=8,save=9,send=8,clarity=9,finish=8,original=8)))
print(save(368,"SINGLE","USA","LeafCleanup","Fall leaf cleanup crew",["p368_leaves"],
"""Booking site for fall leaf cleanup and yard crews: customers pick yard size, trees and bagging online, and you get each day's route street by street.
Fewer phone calls, shorter drives.
Run a lawn or yard crew? DM us.""", 2,
["#leafcleanup","#fallcleanup","#yardcrew","#lawncarebusiness"],
["Kraft and maple orange design with the headline 'Leaf cleanup calls piling up? Book by yard, route by street.' A top-down drawing of Sample Maple Ave with eight yards, each with a house, trees and fallen leaves. Booked yards have a green outline for Tuesday or an orange outline for Thursday, sample: 12, 18 and 21 on Tuesday, 17, 22 and 27 on Thursday, 14 and 13 not booked. Below: a quote form in a browser with yard size small, medium or large, trees on the lot 1 to 2, 3 to 4 or 5 plus, bag and haul or mulch in, and a button 'Send my yard details'; a Tuesday route card with 3 yards on one street and a Thursday route card with 3 yards on one street; note: we text each customer a quote and their day, 6 of 8 yards on Maple Ave are booked."],
 S(scroll=9,save=8,send=8,clarity=9,finish=9,original=9)))
print(save(369,"SINGLE","India","FridgeRepair","Fridge and washing machine repair service",["p369_fridge"],
"""Job card app for fridge and washing machine repair services: customers send the model, problem and photos when they book, and your technician sees the day's jobs and the parts to carry.
Right part, first visit.
Run an appliance repair service? DM us.""", 4,
["#fridgerepair","#washingmachinerepair","#appliancerepair","#servicebusinessindia"],
["Ice blue and copper design with the headline 'Fridge not cooling calls? Get the model and photos first.' A drawn double door fridge with numbered pins on the top door, lower door and model sticker SAMPLE-DD-340. Beside it, a dark job card J-2611 for today 10 to 12 with matching numbered fields: fridge, double door, model SAMPLE-DD-340; problem: not cooling, for 2 days; photos of the model sticker and back panel; area Sector 7 and a masked mobile number. Below: the technician's 5 jobs today with time slots, appliance, area, problem and part, and an orange card with parts to carry today counted from the job cards: thermostat 2, belt 1, door gasket 1, drain pump 1."],
 S(scroll=8,save=8,send=8,clarity=9,finish=9,original=8)))
print(save(370,"SINGLE","India","CarpenterContractor","Carpenter and interior woodwork contractor",["p370_carpenter"],
"""Site progress app for carpenters and interior woodwork contractors: every item in the flat on one plan, its status by room, and a site update the owner can read any day.
"How much is left?" answered in one look.
Do carpentry or interior work? DM us.""", 1,
["#carpenter","#interiorwork","#woodwork","#modularfurniture","#homeinteriorindia"],
["Beige and teak design with the headline 'Owner asks how much is left? Show the flat, room by room.' A 3D top view of a sample 2BHK, flat 302 on day 12, with Living, Kitchen, Bedroom 1 and Bedroom 2 and seven numbered furniture blocks coloured by status: 1 TV unit and 2 shoe rack in dark teak for done; 3 kitchen cabinets, 4 wardrobe and 6 bed with storage in light wood for in progress; 5 bed with storage and 7 study table in dashed grey for not started. Below: a numbered list with each item, its room and its status or start day, and a blue site update sent to the owner: TV unit and shoe rack are done, kitchen, wardrobe and one bed are in progress, with three photos and counts of 2 done, 3 in progress and 2 not started."],
 S(scroll=8,save=8,send=9,clarity=8,finish=9,original=9)))
