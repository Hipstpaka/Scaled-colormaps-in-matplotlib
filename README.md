# Scaled-colormaps-in-matplotlib

Assume you have some noisy 2D data

```
import numpy as np

num_columns=50
num_rows=50
data_noise=np.random.normal(0,2*num_rows,(num_rows,num_columns))
data_without_noise= [[i*j-num_columns*num_rows/3 for i in range(num_columns)] for j in range(num_rows)] 
data=data_noise+datat_without_noise
```

which you want to plot. You could use imshow from matplotlib:

```
import matplotlib.pyplot as plt

plt.imshow(data,vmin=vmin,vmax=vmax,cmap='bwr')
plt.colorbar()
```

This results in the following figure:
![No_scaling_no_midpoint](https://user-images.githubusercontent.com/37422619/121489621-8ebe0680-c9d4-11eb-8854-37ba9a33aff3.png)

Now let's assume that the transition region from negative to positive values has a special meaning and we'd like to make this region more visible. The first step is to map the white middle region of our colormap to 0:

```
import matplotlib.colors

norm = matplotlib.colors.TwoSlopeNorm(vcenter=0)
plt.imshow(data,cmap='bwr',norm=norm)
plt.colorbar()
```
This gives the following figure:

![no_scaling_midpoint](https://user-images.githubusercontent.com/37422619/121490771-a47ffb80-c9d5-11eb-8fb2-8fa5ae0c4da9.png)

In this figure it is already much easier to identify the transition region. 



