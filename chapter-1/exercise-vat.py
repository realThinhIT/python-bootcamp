VAT = 25
calculatedVAT = 1 + (VAT / 100)
orderProcessingFee = 10000

# Assigning multiple variables with different values at once
netPriceOfMacBookPro, netPriceOfTheNewMacBookPro = 25000000, 26000000

grossPriceOfMacBookPro = netPriceOfMacBookPro * calculatedVAT
grossPriceOfMacBookPro += orderProcessingFee;

grossPriceOfTheNewMacBookPro = netPriceOfTheNewMacBookPro * calculatedVAT
grossPriceOfTheNewMacBookPro += orderProcessingFee;

print('grossPriceOfMacBookPro = ', grossPriceOfMacBookPro)
print('grossPriceOfTheNewMacBookPro', grossPriceOfTheNewMacBookPro);