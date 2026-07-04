import matplotlib.pyplot as plt 
import seaborn as sns
import matplotlib.pyplot as plt

x=[0,2,4,8,10]
y=[0,4,8,16,36]
Values=[0,4,8,16,36]
Labels=['Cows','Goats','Sheep','Pigs','Chickens']
fig, ax=plt.subplots(2,2,figsize=(10,5))
ax[0,0].plot(x,y,marker='o',label='data points',color='green',linestyle='--')
ax[0,0].set_title('basic line graph')
ax[0,0].set_xlabel('x-axis')
ax[0,0].set_ylabel('y-axis')
ax[0,0].legend()

ax[0,1].bar(x=Labels, height=Values, color='blue', label='Animals')
ax[0,1].set_title('basic bar graph')
ax[0,1].set_xlabel('Animals')
ax[0,1].set_ylabel('Values')
ax[0,1].legend()
ax[1,0].boxplot(Values, patch_artist=True, notch=True, vert=True, meanline=True)
ax[1,0].set_title('basic box plot')
ax[1,0].set_xlabel('Animals')
ax[1,0].set_ylabel('Values')
plt.show()

data = [
    [100,200,350],
    [50,180,250],
    [300,320,400]
]

sns.heatmap(
    data,
    annot=True,
    xticklabels=["Jan","Feb","Mar"],
    yticklabels=["Rice","Beans","Sugar"]
)

plt.show()
