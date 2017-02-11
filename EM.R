data<- scan("C:/Users/prathameshj/Desktop/ML/data1.txt")
clusters<- c(4)
x<-list()
x<-Expectation_Maximization(data, 200,clusters)
x

Expectation_Maximization<- function(data, iterations, clusters){
      cluster_probability<-rep(1/clusters,clusters)
      cluster_mean<-runif(clusters, min = 0, max=1)
      cluster_sd<- runif(clusters, min=0, max=1)
      iter=1
      cols<- list()
      L<-list()
      L2<-vector()
      
      while( iter < iterations){
        #Expectation Step
          for(i in 1:clusters){
            cols[[i]]<- c(cluster_probability[i]*dnorm(data, cluster_mean[i],cluster_sd[i]))
          }
          output <- matrix(unlist(cols), nrow = clusters, byrow = TRUE)
          output<-t(t(output)/rowSums(t(output)))
          N=rowSums(output)
        
        
        #Maximization Step
        for (i in 1:clusters){
          cluster_mean[i]<- sum(output[i,]*data)/N[i]
          cluster_sd[i]<- sqrt(((sum(output[i,]*(data^2)))/N[i]) - ((cluster_mean[i])^2))
          
        }
        cluster_probability = N/sum(N)
        #Log likelihood.
        for (i in 1:clusters) {
          L[[i]]<- c(cluster_probability[i]*dnorm(data,cluster_mean[i],cluster_sd[i]))
        }
        L1<-matrix(unlist(L), nrow = clusters, byrow = TRUE)
        L2[iter]<-sum(log(colSums(L1)))
        iter=iter+1
        
      }
    return(list("cluster_probability" = c(cluster_probability), "cluster_mean" = c(cluster_mean), "cluster_sd" = c(cluster_sd), "Log likelihood" = c(L2)))
}
