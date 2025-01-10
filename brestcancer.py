data = read.csv("breastcancer.csv")

plot(data, col = "diagnosis", pch = 19, cex = 2)

dev.copy(jpeg, "plot.jpg")
dev.off()