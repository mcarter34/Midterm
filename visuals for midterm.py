#pie chart of payment type
import matplotlib.pyplot as plt
import numpy as np
y=np.array ([2,7,3])
mylabels=['Gift Card','Credit Card','Visa']
mycolors=['pink','purple','blue']
plt.pie(y, labels=mylabels, colors=mycolors)
plt.title ('Types of Payment')
plt.show()

#bar graph of category of item
import matplotlib.pyplot as plt
import numpy as np
x=np.array (['Decor','Tech','Cosmetics','Miscellaneous','Food'])
y=np.array ([5,2,2,2,1])
plt.bar(x,y, color= 'pink')
plt.title('Types of Purchases')
plt.show()

#line graph of spending comparing 2021 and 2022
import matplotlib.pyplot as plt
import numpy as np
y1=np.array([15,19,19])
y2=np.array ([11,40,6])
plt.ylabel ('Spending by Year')
plt.plot(y1)
plt.plot(y2)
plt.show()