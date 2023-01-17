dat = read_csv("CO2.csv")
p = ggplot(dat, aes(x = Age, y = CO2)) +
  geom_line() +
  geom_ribbon(aes(ymin = CO2 - Standard_error,
                  ymax = CO2 + Standard_error), alpha = 0.2)

p