
def krill_consumption(feeding, whales):

    total_consumption = 0

    for whale_type, count in whales.items():
        if whale_type in feeding:
            daily_consumption = feeding[whale_type]
            type_consumption = daily_consumption * count
            total_consumption += type_consumption
    
    return total_consumption


if __name__ == '__main__':

    feeding = {'Humpback whale': 2000, 'Gray whale': 1500, 'Bowhead whale':
    2500, 'Blue whale': 3600}
    whales = {'Humpback whale': 8, 'Gray whale': 3}
    

    total_consum = krill_consumption(feeding, whales)
  
    print('Estimate daily consumption: %d kg of krill' % total_consum)
