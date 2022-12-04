#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 14:23:03 2022

@author: nacim-
"""

#!/usr/bin/env python
# coding: utf-8


# In[1]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r'/Users/nacim-/Downloads/hdvaaa.csv', sep = ",")

# In[2]:


data_discri = data[data["DISCRI1C1"]>0]

# In[3]:
 
    

CSP = ["Subis des moqueries, des insultes","mis à l'écart","traité(é) injustement", "refusé un droit"]
 
data = round((data_discri.groupby(["DISCRI1C1"]).sum()["POIDSFN148"]/sum(data_discri["POIDSFN148"])*100),1)


# In[2]:
 
    
couleur = sns.color_palette("Paired")

CSP = ["Subis des moqueries, des insultes","mis à l'écart","traité(é) injustement", "refusé un droit"]
 
data = round((data_discri.groupby(["DISCRI1C1"]).sum()["POIDSFN148"]/sum(data_discri["POIDSFN148"])*100),1)




# Wedge properties
wp = { 'edgecolor' : "black" }
# 'linewidth' : 1,
# Creating autocpt arguments
def func(pct, allvalues):
    absolute = int(pct / 100.*np.sum(allvalues))
    return "{:.1f}%\n({:d} g)".format(pct, absolute)
 
# Creating plot
fig, ax = plt.subplots(figsize =(10, 7))
wedges, texts, autotexts = ax.pie(data,
                                  autopct = lambda pct: func(pct, data),
                                  shadow = True,
                                  colors = couleur,
                                  startangle = 90,
                                  wedgeprops = wp)
#,                                  textprops = dict(color ="magenta"))
 
# Adding legend
ax.legend(wedges, CSP,
          title ="CSP",
          loc ="center left",
          bbox_to_anchor =(1, 0, 0.5, 1))
 
plt.setp(autotexts, size = 8, weight ="bold")
ax.set_title("Discrimination subis par rapport à l'age selon en 2003")
 
# show plot
plt.show()
-------------------------------------------------------------------------------
#code 2

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 17:09:27 2022

@author: nacim-
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 14:23:03 2022

@author: nacim-
"""

#!/usr/bin/env python
# coding: utf-8


# In[1]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r'/Users/nacim-/Downloads/hdvaaa.csv', sep = ",")

# In[2]:


data_discri = data[data["DFREQ1C1"]>0]

# In[3]:
 
    

CSP = ["Une seule fois","Plusieurs fois","Continuellement"]
 
data = round((data_discri.groupby(["DFREQ1C1"]).sum()["POIDSFN148"]/sum(data_discri["POIDSFN148"])*100),1)


# In[2]:
 
    
couleur = sns.color_palette("Paired")

CSP = ["Une seule fois","Plusieurs fois","Continuellement"] 

data = round((data_discri.groupby(["DFREQ1C1"]).sum()["POIDSFN148"]/sum(data_discri["POIDSFN148"])*100),1)




# Wedge properties
wp = { 'edgecolor' : "black" }
# 'linewidth' : 1,
# Creating autocpt arguments
def func(pct, allvalues):
    absolute = int(pct / 100.*np.sum(allvalues))
    return "{:.1f}%\n({:d} g)".format(pct, absolute)
 
# Creating plot
fig, ax = plt.subplots(figsize =(10, 7))
wedges, texts, autotexts = ax.pie(data,
                                  autopct = lambda pct: func(pct, data),
                                  shadow = True,
                                  colors = couleur,
                                  startangle = 90,
                                  wedgeprops = wp)
#,                                  textprops = dict(color ="magenta"))
 
# Adding legend
ax.legend(wedges, CSP,
          title ="CSP",
          loc ="center left",
          bbox_to_anchor =(1, 0, 0.5, 1))
 
plt.setp(autotexts, size = 8, weight ="bold")
ax.set_title("Fréquence discrimination subis par rapport à l'age en 2003")
 
# show plot
plt.show()

-------------------------------------------------------------------------------
#code 3

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 17:09:27 2022

@author: nacim-
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 14:23:03 2022

@author: nacim-
"""

#!/usr/bin/env python
# coding: utf-8


# In[1]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r'/Users/nacim-/Downloads/hdvaaa.csv', sep = ",")

# In[2]:


data_discri = data[data["DISCRI3C1"]>0]

# In[3]:
 
    

CSP = ["Subis des moqueries, des insultes","mis à l'écart","traité(é) injustement", "refusé un droit"]
 
data = round((data_discri.groupby(["DISCRI3C1"]).sum()["POIDSFN148"]/sum(data_discri["POIDSFN148"])*100),1)


# In[2]:
 
    
couleur = sns.color_palette("Paired")

CSP = ["Subis des moqueries, des insultes","mis à l'écart","traité(é) injustement", "refusé un droit"] 

data = round((data_discri.groupby(["DISCRI3C1"]).sum()["POIDSFN148"]/sum(data_discri["POIDSFN148"])*100),1)




# Wedge properties
wp = { 'edgecolor' : "black" }
# 'linewidth' : 1,
# Creating autocpt arguments
def func(pct, allvalues):
    absolute = int(pct / 100.*np.sum(allvalues))
    return "{:.1f}%\n({:d} g)".format(pct, absolute)
 
# Creating plot
fig, ax = plt.subplots(figsize =(10, 7))
wedges, texts, autotexts = ax.pie(data,
                                  autopct = lambda pct: func(pct, data),
                                  shadow = True,
                                  colors = couleur,
                                  startangle = 90,
                                  wedgeprops = wp)
#,                                  textprops = dict(color ="magenta"))
 
# Adding legend
ax.legend(wedges, CSP,
          title ="CSP",
          loc ="center left",
          bbox_to_anchor =(1, 0, 0.5, 1))
 
plt.setp(autotexts, size = 8, weight ="bold")
ax.set_title("Discrimination subis sur des personne en situation d'handicap en 2003")
 
# show plot
plt.show()

-------------------------------------------------------------------------------
#code 4

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 17:09:27 2022

@author: nacim-
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 14:23:03 2022

@author: nacim-
"""

#!/usr/bin/env python
# coding: utf-8


# In[1]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r'/Users/nacim-/Downloads/hdvaaa.csv', sep = ",")

# In[2]:


data_discri = data[data["DFREQ3C1"]>0]

# In[3]:
 
    

CSP = ["Une seule fois","Plusieurs fois","Continuellement"]
 
data = round((data_discri.groupby(["DFREQ3C1"]).sum()["POIDSFN148"]/sum(data_discri["POIDSFN148"])*100),1)


# In[2]:
 
    
couleur = sns.color_palette("Paired")

CSP = ["Une seule fois","Plusieurs fois","Continuellement"]

data = round((data_discri.groupby(["DFREQ3C1"]).sum()["POIDSFN148"]/sum(data_discri["POIDSFN148"])*100),1)




# Wedge properties
wp = { 'edgecolor' : "black" }
# 'linewidth' : 1,
# Creating autocpt arguments
def func(pct, allvalues):
    absolute = int(pct / 100.*np.sum(allvalues))
    return "{:.1f}%\n({:d} g)".format(pct, absolute)
 
# Creating plot
fig, ax = plt.subplots(figsize =(10, 7))
wedges, texts, autotexts = ax.pie(data,
                                  autopct = lambda pct: func(pct, data),
                                  shadow = True,
                                  colors = couleur,
                                  startangle = 90,
                                  wedgeprops = wp)
#,                                  textprops = dict(color ="magenta"))
 
# Adding legend
ax.legend(wedges, CSP,
          title ="CSP",
          loc ="center left",
          bbox_to_anchor =(1, 0, 0.5, 1))
 
plt.setp(autotexts, size = 8, weight ="bold")
ax.set_title("Fréquence discrimination subis sur des personnes en situation d'handicap en 2003")
 
# show plot
plt.show()

-------------------------------------------------------------------------------
#code 5

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 19:10:31 2022

@author: nacim-
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 17:09:27 2022

@author: nacim-
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 14:23:03 2022

@author: nacim-
"""

#!/usr/bin/env python
# coding: utf-8


# In[1]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r'/Users/nacim-/Downloads/hdvaaa.csv', sep = ",")

# In[2]:


data_discri = data[data["DISCRI2C1"]>0]

# In[3]:
 
    

CSP = ["Subis des moqueries, des insultes","mis à l'écart","traité(é) injustement", "refusé un droit"]

data = round((data_discri.groupby(["DISCRI2C1"]).sum()["POIDSFN148"]/sum(data_discri["POIDSFN148"])*100),1)


# In[2]:
 
    
couleur = sns.color_palette("Paired")

CSP = ["Subis des moqueries, des insultes","mis à l'écart","traité(é) injustement", "refusé un droit"]

data = round((data_discri.groupby(["DISCRI2C1"]).sum()["POIDSFN148"]/sum(data_discri["POIDSFN148"])*100),1)




# Wedge properties
wp = { 'edgecolor' : "black" }
# 'linewidth' : 1,
# Creating autocpt arguments
def func(pct, allvalues):
    absolute = int(pct / 100.*np.sum(allvalues))
    return "{:.1f}%\n({:d} g)".format(pct, absolute)
 
# Creating plot
fig, ax = plt.subplots(figsize =(10, 7))
wedges, texts, autotexts = ax.pie(data,
                                  autopct = lambda pct: func(pct, data),
                                  shadow = True,
                                  colors = couleur,
                                  startangle = 90,
                                  wedgeprops = wp)
#,                                  textprops = dict(color ="magenta"))
 
# Adding legend
ax.legend(wedges, CSP,
          title ="CSP",
          loc ="center left",
          bbox_to_anchor =(1, 0, 0.5, 1))
 
plt.setp(autotexts, size = 8, weight ="bold")
ax.set_title("Discrimination à cause du sexe en 2003")
 
# show plot
plt.show()

-------------------------------------------------------------------------------
#code 6

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 19:11:09 2022

@author: nacim-
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 17:09:27 2022

@author: nacim-
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 14:23:03 2022

@author: nacim-
"""

#!/usr/bin/env python
# coding: utf-8


# In[1]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r'/Users/nacim-/Downloads/hdvaaa.csv', sep = ",")

# In[2]:


data_discri = data[data["DISCRI4C1"]>0]

# In[3]:
 
    
CSP = ["Subis des moqueries, des insultes","mis à l'écart","traité(é) injustement", "refusé un droit"]

 
data = round((data_discri.groupby(["DISCRI4C1"]).sum()["POIDSFN148"]/sum(data_discri["POIDSFN148"])*100),1)


# In[2]:
 
    
couleur = sns.color_palette("Paired")

CSP = ["Subis des moqueries, des insultes","mis à l'écart","traité(é) injustement", "refusé un droit"]

data = round((data_discri.groupby(["DISCRI4C1"]).sum()["POIDSFN148"]/sum(data_discri["POIDSFN148"])*100),1)




# Wedge properties
wp = { 'edgecolor' : "black" }
# 'linewidth' : 1,
# Creating autocpt arguments
def func(pct, allvalues):
    absolute = int(pct / 100.*np.sum(allvalues))
    return "{:.1f}%\n({:d} g)".format(pct, absolute)
 
# Creating plot
fig, ax = plt.subplots(figsize =(10, 7))
wedges, texts, autotexts = ax.pie(data,
                                  autopct = lambda pct: func(pct, data),
                                  shadow = True,
                                  colors = couleur,
                                  startangle = 90,
                                  wedgeprops = wp)
#,                                  textprops = dict(color ="magenta"))
 
# Adding legend
ax.legend(wedges, CSP,
          title ="CSP",
          loc ="center left",
          bbox_to_anchor =(1, 0, 0.5, 1))
 
plt.setp(autotexts, size = 8, weight ="bold")
ax.set_title("discrimination à cause de la couleurs de peau en 2003")
 
# show plot
plt.show()

