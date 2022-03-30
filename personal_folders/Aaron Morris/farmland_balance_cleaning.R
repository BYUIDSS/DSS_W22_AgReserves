library(tidyverse)
library(lubridate)

#file_path = str_c(getwd(), "personal_folders", "Aaron Morris", "farmland_balance_sheet.csv", sep = "/")
dat <- read_csv("/Users/aaronmorris/Desktop/DSS_W22_AgReserves/personal_folders/Aaron Morris/farmland_balance_sheet.csv")

year1 <- year(mdy(colnames(dat)[4]))
year2 <- year(mdy(colnames(dat)[3]))

assets <- dat[2:23,] %>%
  mutate(category = "assets") %>%
  rename("item" = "Consolidated Balance Sheets - USD ($) $ in Thousands",
         !!as.character(year1) := ends_with(as.character(year1)),
         !!as.character(year2) := ends_with(as.character(year2))) %>%
  select(-X1) %>%
  pivot_longer(cols = c(`2021`, `2020`), names_to = "year", values_to = "amount_usd") %>%
  mutate(amount_usd = as.numeric(str_replace_all(amount_usd, "[:punct:]|\\$", "")))

liabilities <- dat[26:37,] %>%
  mutate(category = "liabilities") %>%
  rename("item" = "Consolidated Balance Sheets - USD ($) $ in Thousands",
         !!as.character(year1) := ends_with(as.character(year1)),
         !!as.character(year2) := ends_with(as.character(year2))) %>%
  select(-X1) %>%
  pivot_longer(cols = c(`2021`, `2020`), names_to = "year", values_to = "amount_usd") %>%
  mutate(amount_usd = as.numeric(str_replace_all(amount_usd, "[:punct:]|\\$", "")))

equity <- dat[39:44,] %>%
  mutate(category = "equity") %>%
  rename("item" = "Consolidated Balance Sheets - USD ($) $ in Thousands",
         !!as.character(year1) := ends_with(as.character(year1)),
         !!as.character(year2) := ends_with(as.character(year2))) %>%
  select(-X1) %>%
  pivot_longer(cols = c(`2021`, `2020`), names_to = "year", values_to = "amount_usd") %>%
  mutate(amount_usd = as.numeric(str_replace_all(amount_usd, "[:punct:]|\\$", "")))

clean_farmland_balance <- bind_rows(assets, liabilities, equity)

write_csv(clean_farmland_balance, "clean_farmland_balance.csv")