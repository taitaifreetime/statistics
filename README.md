# python implementation to learn statistics

## Visualize Distribution
- binominal distribution
```
python3 prob_distribution/binominal_distribution.py --n 30 --probability 0.5
```
![binominal distribution](./results/Binominal%20Distribution%20(n%20=%2030,%20p%20=%200.5).png)
- normal distribution
```
python3 prob_distribution/normal_distribution.py --mean 0.0 --variance 10.0
python3 prob_distribution/normal_distribution_animation.py --mean 5.0 # animation that variance will be changing
python3 prob_distribution/normal_distribution_animation.py --variance 10.0 # animation that mean will be changing
```
![normal distribution](./results/Normal%20Distribution%20(mean%20=%200.0,%20variance%20=%2010.0).png)
![animation that variance will be changing](./results/normal_distribution_variance.gif)
![animation that mean will be changing](./results/normal_distribution_mean.gif)