#################### R script that generates plots for Figs. 2a and 2b, written by John Sproul  #####################
library (ggplot2)

##Fig 2a
#reads input file
in_data<-read.table("Fig2a_data.txt", header = TRUE)
#sets sample order
in_data$name <- factor(in_data$name, levels =unique(in_data$name))
#makes plot for Fig. 2a
ggplot(data = in_data, aes(x = name, y = length)) +
  geom_bar(stat='identity') + coord_flip() + theme_bw()#+ scale_fill_viridis() + theme_bw()


##Fig2b
#reads input file
df<-read.table("busco_plot_final.txt", header = TRUE)
#set color scheme
bar_cols3=c("#D66C03", "#F9EE8A", "#3A6199", "#50A9CC")
#sets the order of species in plot to match order in input file
df$name <- factor(df$name, levels =unique(df$name))
#makes plot for Fig 2b
ggplot(data = df, aes(x = name, y = value, fill = category)) +
  geom_bar(stat='identity') + coord_flip() + scale_fill_manual(values=bar_cols3)+
  theme_bw()

#end
