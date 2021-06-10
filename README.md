# Scaled-colormaps-in-matplotlib

Assume you have some noisy 2D data

```
import numpy as np

num_columns=50
num_rows=50
data_noise=np.random.normal(0,2*num_rows,(num_rows,num_columns))
data_without_noise= [[i*j-num_columns*num_rows/3 for i in range(num_columns)] for j in range(num_rows)] 
data=data_noise+data_without_noise
```

which you want to plot. You could use imshow from matplotlib:

```
import matplotlib.pyplot as plt

plt.imshow(data, cmap = 'bwr')
plt.colorbar()
```
This results in the following figure:

![No_scaling_no_midpoint](https://user-images.githubusercontent.com/37422619/121489621-8ebe0680-c9d4-11eb-8854-37ba9a33aff3.png)

Now let's assume that the transition region from negative to positive values has a special meaning and we'd like to make this region more visible. The first step is to map the white middle region of our colormap to 0:

```
import matplotlib.colors

norm = matplotlib.colors.TwoSlopeNorm(vcenter = 0)
plt.imshow(data, cmap = 'bwr', norm = norm)
plt.colorbar()
```
This gives the following figure:

![no_scaling_midpoint](https://user-images.githubusercontent.com/37422619/121490771-a47ffb80-c9d5-11eb-8fb2-8fa5ae0c4da9.png)

In this figure it is already much easier to identify the transition region. 

Now, under certain circumstances it might be advantageous to make the transition from blue to red happen more 'slowly'. This is what the function 

```
scaled_cmap(colormap: str, exponent: float, x_max = 10000) -> ListedColormap
```
from the file colormap_scaling.py in this repository achieves. Assume you want to 'rescale' a given colormap, e.g. bwr:

![bwr](https://user-images.githubusercontent.com/37422619/121492123-e493ae00-c9d6-11eb-9553-809d06a990b6.png)

Then, to 'spread' the white transition region use the scaled_cmap function with an exponent larger than 1:

```
from colormap_scaling import scaled_colormap
rescaled_cmap = scaled_colormap('bwr',2)
```
resulting in:

![rescaled_bwr](https://user-images.githubusercontent.com/37422619/121492655-566bf780-c9d7-11eb-9b48-5cdf0aff115d.png)

Using this rescaled colormap for our data results in:

```
plt.imshow(data, cmap = scaled_colormap('bwr',2), norm = norm)
plt.colorbar()
```

![rescaled_plot](https://user-images.githubusercontent.com/37422619/121493023-b4004400-c9d7-11eb-9870-526d81300458.png)


In this plot the white region is much larger due to the rescaled colormap. By using an exponent smaller than one, we can also make the transition region look 'smaller':

```
plt.imshow(data, cmap = scaled_colormap('bwr',0.5), norm = norm)
plt.colorbar()
```

![small_transition_region](https://user-images.githubusercontent.com/37422619/121493288-f9bd0c80-c9d7-11eb-979a-60f886201cad.png)




