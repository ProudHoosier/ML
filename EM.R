data <- scan("/home/ds/Downloads/project/data1.txt")
mixtures <- c(3)
x <- list()
iterations <- 250
x <- EM(data, mixtures, iterations)
x

#Covergence condition
delta <- 10^(-5)

EM <- function(data, mixtures, iterations){
      
      prior <- rep(1/mixtures, mixtures)
      mu <- runif(mixtures, min = 0, max=1)
      sd <- runif(mixtures, min = 0, max=1)
      
      counter = 1
      columns <- list()
      L <- list()
      L2 <- vector()
      
      while(counter < iterations){
        
        #Expectation
          for(i in 1:mixtures){
            columns[[i]] <- c(prior[i] * dnorm(data, mu[i], sd[i]))
          }
          output <- matrix(unlist(columns), nrow = mixtures, byrow = TRUE)
          output <- t(t(output)/rowSums(t(output)))
          N = rowSums(output)
        
        #Maximization
        for (i in 1:mixtures){
          mu[i]<- sum(output[i,]*data)/N[i]
          sd[i]<- sqrt(((sum(output[i,]*(data^2)))/N[i]) - ((mu[i])^2))
          
        }
        
        prior = N/sum(N)
        
        # Calculate log-likelihood.
        for (i in 1:mixtures) {
          L[[i]]<- c(prior[i] * dnorm(data,mu[i], sd[i]))
        }

        L1 <- matrix(unlist(L), nrow = mixtures, byrow = TRUE)
        L2[counter] <- sum(log(colSums(L1)))
        counter = counter + 1
        
      }
    return(list("prior" = c(prior), "mu" = c(mu), "sd" = c(sd), "Log likelihood" = c(L2)))
}
