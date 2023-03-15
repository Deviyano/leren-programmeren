import time
from termcolor import colored
from data import JOURNEY_IN_DAYS
from data import COST_FOOD_HUMAN_COPPER_PER_DAY
from data import COST_FOOD_HORSE_COPPER_PER_DAY
from data import COST_TENT_GOLD_PER_WEEK
from data import COST_HORSE_SILVER_PER_DAY
from data import COST_INN_HUMAN_SILVER_PER_NIGHT
from data import COST_INN_HORSE_COPPER_PER_NIGHT
import math
##################### M04.D02.O2 #####################
def copper2silver(amount:int) -> float:
    #deze code berekent het aantal copper naar zilver
    return amount / 10

def silver2gold(amount:int) -> float:
    #deze code berekent het aantal zilver naar goud
    return amount / 5

def copper2gold(amount:int) -> float:
    #deze code berekent het aantal copper naar goud
    return amount / 50


def platinum2gold(amount:int) -> float:
    #deze code berekent het aantal platinum naar goud
    return amount * 25

def getPersonCashInGold(personCash:dict) -> float:
    #deze code bereknt het aantal goeu dat je hebt door alles naar goud te veranderen
    return copper2gold(personCash['copper']) + silver2gold(personCash['silver']) + personCash['gold'] + platinum2gold(personCash['platinum'])
##################### M04.D02.O4 #####################

def getJourneyFoodCostsInGold(people:int, horses:int) -> float:
    #deze code berekent het aantal goud dat het kost om eten te kopen
    human=copper2gold(COST_FOOD_HUMAN_COPPER_PER_DAY * people) * JOURNEY_IN_DAYS 
    horse = copper2gold(COST_FOOD_HORSE_COPPER_PER_DAY * horses) * JOURNEY_IN_DAYS 
    return round(human+horse,2)
##################### M04.D02.O5 #####################

def getFromListByKeyIs(list:list, key:str, value:any) -> list:
    #deze code geeft een lijst terug met de waardes die je gebruikt 
    # dus als je key = "adventuring" en value = True dan krijg je een lijst terug met alle mensen die avontuurlijk zijn
    lijst = []
    for x in range(len(list)):
        if list[x][key] == value:
            lijst.append(list[x])
    return lijst

def getAdventuringPeople(people:list) -> list:
    #deze code geeft een lijst terug met alle mensen die avontuurlijk zijn
    return getFromListByKeyIs(people, "adventuring", True)

def getShareWithFriends(friends:list) -> list:
    #deze code geeft een lijst terug met alle mensen die je wilt delen
    return getFromListByKeyIs(friends, "shareWith", True)

def getAdventuringFriends(friends:list) -> list:
    #deze code geeft een lijst terug met alle mensen die je wilt delen en avontuurlijk zijn
    adventurefriends = []
    adventure = getAdventuringPeople(friends)
    share = getShareWithFriends(friends)

    for x in range(len(adventure)):

        if share[x] in adventure:
            adventurefriends.append(share[x])
    return adventurefriends
##################### M04.D02.O6 #####################

def getNumberOfHorsesNeeded(people:int) -> int:
    #deze code berekent het aantal paarden dat je nodig hebt
    return math.ceil(people / 2)

def getNumberOfTentsNeeded(people:int) -> int:
    #deze code berekent het aantal tenten dat je nodig hebt
    return math.ceil(people / 3) 

def getTotalRentalCost(horses:int, tents:int) -> float:
    #deze code berekent het totaal aantal goud dat je nodig hebt voor de huur van de paarden en de tenten
    costHorses = JOURNEY_IN_DAYS * horses * silver2gold(COST_HORSE_SILVER_PER_DAY)
    costTents = math.ceil(JOURNEY_IN_DAYS / 7) * tents * COST_TENT_GOLD_PER_WEEK    
    return round(costHorses + costTents, 2)
##################### M04.D02.O7 #####################

def getItemsAsText(items:list) -> str:
    #deze code geeft een lijst terug met alle items die je hebt
    text = ""
    space = ""
    for item in items:
        text += f"{space}{item['amount']}{item['unit']} {item['name']}"
        space = ", "

    return text
def getItemsValueInGold(items:list) -> float: 
    #deze code berekent het totaal aantal goud dat je nodig hebt voor de items
    totalPriceInGold = 0

    for item in items:
        priceInGold = item['price']['amount']
        if item['price']['type'] == 'silver':
            priceInGold = silver2gold(priceInGold)
        elif item['price']['type'] == 'copper':
            priceInGold = copper2gold(priceInGold)
        elif item['price']['type'] == 'platinum':
            priceInGold = platinum2gold(priceInGold)

        totalPriceInGold += priceInGold * item['amount']

    return round(totalPriceInGold,2)

##################### M04.D02.O8 #####################

def getCashInGoldFromPeople(people:list) -> float: 
    #deze code berekent het totaal aantal goud dat je nodig hebt voor de mensen
    total = 0
    for person in people:
        total += getPersonCashInGold(person['cash'])
    return round(total,2)

##################### M04.D02.O9 #####################

def getInterestingInvestors(investors:list) -> list:
    #deze code geeft een lijst terug met alle investeerders die minder dan 10% winst hebben
    investlijst = []
    for x in range(len(investors)):
        if investors[x]['profitReturn'] <=10:
            investlijst.append(investors[x])
    return investlijst
 
def getAdventuringInvestors(investors:list) -> list: 
    #deze code geeft een lijst terug met alle investeerders die minder dan 10% winst hebben en avontuurlijk zijn
    investlijst = getInterestingInvestors(investors)
    goedelijst=[]
    for x in range(len(investlijst)):
        if investlijst[x]['adventuring'] == True:
            goedelijst.append(investlijst[x])
    return goedelijst
    
def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    #deze code berekent het totaal aantal goud dat je nodig hebt voor de investeerders
    adventuringInvestors = getAdventuringInvestors(investors)
    countInvestors = len(adventuringInvestors)
    gearkosten = getItemsValueInGold(gear)*countInvestors
    rentalkosten = getTotalRentalCost(countInvestors, countInvestors)
    foodkosten = getJourneyFoodCostsInGold(countInvestors, countInvestors)
    return round(rentalkosten + gearkosten + foodkosten,2)
##################### M04.D02.O10 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    #deze code berekent het aantal nachten dat je in de herberg kan blijven
    people_per_night_gold = silver2gold(COST_INN_HUMAN_SILVER_PER_NIGHT) * people
    horses_per_night_gold = copper2gold(COST_INN_HORSE_COPPER_PER_NIGHT) * horses
    return int(leftoverGold / (people_per_night_gold + horses_per_night_gold))

def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    #deze code berekent het aantal goud dat je nodig hebt voor de herberg
    gold_per_night = silver2gold(COST_INN_HUMAN_SILVER_PER_NIGHT)
    horses_gold_per_night = copper2gold(COST_INN_HORSE_COPPER_PER_NIGHT)
    human_per_night_Gold =  gold_per_night * people 
    horses_per_night_Gold = horses_gold_per_night * horses 
    return round((human_per_night_Gold + horses_per_night_Gold) * nightsInInn,2)

##################### M04.D02.O12 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    #deze code berekent het aantal goud dat je nodig hebt voor de investeerders
    investorlist = []
    for x in investors:
        if x['profitReturn'] < 10:
            investorlist.append(round(x['profitReturn'] / 100 * profitGold,2) )
    return investorlist

def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:list) -> float:
    #deze code berekent het aantal goud dat je nodig hebt voor de avonturiers
    investor_cuts = 0
    for x in investorsCuts:
        investor_cuts += x
    return round((profitGold - investor_cuts) / fellowship,2)

##################### M04.D02.O13 #####################

def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    pass

##################### view functions #####################
def print_colorvars(txt:str='{}', vars:list=[], color:str='yellow') -> None:
    vars = map(lambda string, color=color: colored(str(string), color, attrs=['bold']) ,vars)
    print(txt.format(*vars))

def print_title(name:str) -> None:
    print_colorvars(vars=['=== [ {} ] ==='.format(name)], color='green')

def print_chapter(number:int, name:str) -> None:
    nextStep(2)
    print_colorvars(vars=['- CHAPTER {}: {} -'.format(number, name)], color='magenta')

def nextStep(secwait:int=1) -> None:
    print('')
    time.sleep(secwait)

def ifOne(amount:int, yes:str, no:str, single='een') -> str:
    text = yes if amount == 1 else no
    amount = single if amount == 1 else amount
    return '{} {}'.format(amount, text).lstrip()