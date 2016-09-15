def div():
        print("======================================================")
div()
print("========== PyConverter / Currency Converter ==========")
div()

rates = {'SE': 1.18, 'ES': 0.85, 'DS': 0.76, 'SD': 1.32, 'DE': 0.89, 'ED': 1.12}

print()
print("Commands: ")
print("'SE' for Sterling Pound to Euro;")
print("'ES' for Euro to Pound;")
print("'DS' for United States Dollar to Pound;")
print("'SD' for Pound to Dollar;")
print("'DE' for United States Dollar to Euro;")
print("'ED' for Euro to United State Dollar;")
print()
div()
i = input("Exchange: ")
div()

def SE():
	print("Sterling to Euro Rate: 1.18")
	y = float(input("Sterling: £"))
	print("£", y, "-> €", '%.2f' % (y*rates['SE']))
	
def ES():
	print("Euro to Sterling Rate: 0.85")
	y = float(input("Euro: €"))
	print("€", y, "-> £", '%.2f' % (y*rates['ES']))

def DS():
	print("USD to Sterling Rate: 0.76")
	y = float(input("USD: $"))
	print("$", y, "-> £", '%.2f' % (y*rates['DS']))

def SD():
        print("Sterling to USD Rate: 1.32")
        y = float(input("Sterling: £"))
        print("£", y, "-> $", '%.2f' % (y*rates['SD']))

def DE():
        print("USD to Euro Rate: 0.89")
        y = float(input("USD: $"))
        print("$", y, "-> €", '%.2f' % (y*rates['DE']))
def ED():
        print("Euro to USD Rate: 1.12")
        y = float(input("Euro: €"))
        print("€", y, "-> $", '%.2f' % (y*rates['ED']))

if i == 'SE':
        SE()
if i == 'ES':
        ES()
if i == 'DS':
        DS()
if i == 'SD':
        SD()
if i == 'DE':
        DE()
if i == 'ED':
        ED()
