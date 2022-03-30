library(tidyverse)

# read in the data

dat <- read_csv('/Users/aaronmorris/Desktop/DSS_W22_AgReserves/personal_folders/Aaron Morris/farmland_acres.csv')

farmland_acres <- dat %>% 
  select(Name, County, `Total Acres`, `Tillable Acres`) %>% 
  separate(County, into = c("county", "state"), sep = ",")

farmland_state_acres <- farmland_acres %>% 
  group_by(state) %>% 
  summarise(acres = sum(`Total Acres`, na.rm = TRUE),
            tillable_acres = sum(`Tillable Acres`, na.rm = TRUE))

write_csv(farmland_acres, "clean_farmland_acres.csv")
write_csv(farmland_state_acres, "farmland_state_acres.csv")