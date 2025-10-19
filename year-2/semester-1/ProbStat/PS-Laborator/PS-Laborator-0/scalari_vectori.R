# ex 1

#a
c(1:30)
#b
c(50:1)
#c
c(1:30,29,18:1)
#d
a=c(4,6,3)
a
#e
c(rep(a,10))
#f
c(rep(a,10),4)
#g
rep(a,c(10,15,20))


# ex 2
zile=c(106, 123, 123, 111, 125, 113, 130, 113, 114, 100, 120, 130, 118, 114, 127, 112, 121, 114, 120, 119, 127, 114, 108, 127, 131, 157, 102, 133)

order(zile)[1:3]
rev(order(zile))[1:3]
order(zile)[zile>120]


#ex 3
?seq()
#a
c(0.1)^(seq(3,36,3)) * c(0.2)^(seq(1,34,3))
#b
c(2^(1:25))/c(1:25)
#c
exp(seq(5,7,by=0.1)) * cos(2^(seq(5,7,by=0.1)))



#ex 4
#a
i=seq(10,200)
sum(i^3+5*i^2)
#b
i=seq(1,200)
sum(3^i/i+2^i/i^2)

#c
sum(c(1,cumprod(seq(2,100,by=2))/cumprod(seq(3,101,by=2))))


# ex 5
paste("label",seq(1,30),sep=" ")
paste0("fn",seq(1,30))


#ex 6
set.seed(1234)

x <- sample(0:999, 250, replace = TRUE)
y <- sample(0:999, 250, replace = TRUE)

#a
n=length(x)
y[2:n]-x[1:(n-1)]

#b
sin(y[1:(n-1)])/cos(x[2:n])

#c
x[1:(n-2)]+2*x[2:(n-1)]-x[3:n]

#d



